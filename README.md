# Twitch Viewer Bot

Twitch Viewer Bot is a Python script that automates the process of increasing the number of viewers for a specific Twitch channel.
This script is intended for educational purposes and should be used responsibly and with the proper authorization.

## Features

- ~~Check for updates: The script checks for updates and notifies the user if a new version is available.~~
- ✅ Assumes you are smart enough to check for updates yourself, rather than violating your privacy.
- ~~Display announcements: Important announcements are displayed to the user.~~
- ✅ Shows a static picture of a Doggosaurus™️, which you may freely change to the ascii art of your choosing.
- ~~Proxy server selection: Choose from a list of proxy servers to access Twitch channels.~~
- ✅ Will rotate between available proxies automatically.
- Specify Twitch channel: Enter the username of the Twitch channel you want to increase viewers for.
- Set viewer count: Define the number of viewers to send to the Twitch channel.
- Browser configuration: Uses a headless Chrome browser for automation.
- Usage instructions: Provides guidance on using the bot and troubleshooting common issues.
- ✅ Now supports a `botrc.py` file, allowing you to set values to be used by default. (See below)

## Prerequisites

- Python 3.x
- Selenium
- Chromedriver (Chrome web driver)
- Colorama

## Chromedriver & Chrome Browser

- Download and install the Chrome browser if it's not already on your system.
- <https://www.google.com/intl/en-en/chrome/>

- Download the appropriate ChromeDriver version that is compatible with the Chrome browser.
- <https://sites.google.com/chromium.org/driver/>

## Installation/Usage

1: Install Python 3.x if you haven't already.
2: Install the required packages by running the following command:

```bash
pip install -r req.txt
```

3: Put the chromedriver.exe into the Script folder.
4: Open chromedriver.exe as administrator
5: Run the main.py script using the following command:

```bash
python main.py
```

6: Follow the prompts to configure the bot.
7: Keep the window open for as long as you want to use the bot.
8: To exit, press the ENTER key or close the window.

## Using the `botrc` File

1: Make a copy of `example.botrc.py` and name it `botrc.py`

  ```bash
  cp example.botrc.py botrc.py
  ```

2: Edit the `botrc.py` file with your desired Twitch username and view total.

## Disclaimer

This script is provided for educational and experimental purposes only. The use of such tools to increase viewers on Twitch without proper authorization is against Twitch's terms of service and can result in account suspension or other penalties. Use this tool responsibly and with permission from the respective platform.

## License

This project is licensed under the MIT License.

~~The distribution of the script is prohibited as it violates the guidelines of the websites where it is applied.~~
*That's not how the MIT License works amigo! 😄*
  *--DJ*

See the LICENSE file for details.

## Special Thanks

Special thanks to fLUIDscripts for the original project design.

## Contributing

Contributions and suggestions are welcome. If you have any ideas or improvements, feel free to open an issue or create a pull request.

Happy streaming!
