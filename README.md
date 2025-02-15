# Discord-Autosender

## Overview

This Python script is designed to send a predefined message to different channels in various Discord servers at 30-minute intervals. It gracefully handles rate limits and includes basic error handling and logging to monitor its activity.

## Features

- Sends a predefined message to specified channels in different servers.
- Implements a 30-minute interval between message cycles.
- Graceful error handling for connection and rate limiting issues.
- Logging of activities and errors.
- Configurable server and channel URLs and message content.

## Requirements

- Python 3.7 or higher
- `requests` library

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/Discord-Autosender.git
    cd Discord-Autosender
    ```

2. **Install the required libraries:**
    ```sh
    pip install requests
    ```

3. **Update the script with your Discord bot token:**
    Open `main.py` and replace the placeholder token with your actual Discord bot token in the `headers` dictionary.

## Usage

Run the script using the following command:
```sh
python main.py
```

## Configuration
The script uses a list of channels defined within the script to send messages. You can modify this list to add or remove channels as needed. The message content is also defined within the script and can be customized to fit your needs.

## Example Configuration
Here is an example of how the channels and message content are defined in the script:
```
channels = [
    {"name": "channel1", "url": "https://discord.com/api/v9/channels/123456789012345678/messages"},
    {"name": "channel2", "url": "https://discord.com/api/v9/channels/987654321098765432/messages"},
    # Add more channels as needed
]

message_content = """
:tada: Welcome to Hyperblock! :tada:

Looking for an epic Minecraft server experience? Join Hyperblock today!

:globe_with_meridians: Website: [hyperblock.fun](https://hyperblock.fun/)
:video_game: Discord: [HyperBlock SMP](https://discord.gg/7DJgrFrNPw)

"""
```
# How to Get Your Discord Token From the Developer Console

- Open the developer console with `F12` or `ctrl+shift+i`.
- Go to the network tab
- Filter by Fetch/XHR
- Choose a request that isn't an error
- Under the `request headers` -> `authorization` section, there will be your Discord token. Copy and paste it from there.

![image](https://i.imgur.com/O2F5wzs.png)

# How to Get Channel url From the Developer Console

-- Open the developer console with `F12` or `ctrl+shift+i`.
- Go to the network tab
- Filter by Fetch/XHR
- Choose a request that isn't an error
- - Under the `request headers` -> `Request url`
- point to note a message has to be sent to the channel to get the request as well as token

![image](https://i.imgur.com/jMgKyST.png)


## Discord's Terms of Service
By using this script, you agree to comply with Discord's Terms of Service and Discord's Developer Terms of Service. This includes but is not limited to:

 - Not using the script for spamming or any malicious activities.
 - Respecting rate limits and not bypassing them.
 - Ensuring that your bot abides by the guidelines set forth in the documentation.
 - Failure to comply with these terms may result in your bot being banned and your account being suspended.
