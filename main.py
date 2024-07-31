import requests
import time
import random
import os

# Define your channels, URLs, and cooldowns
channels = [
    {"name": "channel1", "url": "https://discord.com/api/v9/channels/562296002262859776/messages"},
    {"name": "channel2", "url": "https://discord.com/api/v9/channels/546371699076104192/messages"},
    {"name": "channel3", "url": "https://discord.com/api/v9/channels/546371143699791899/messages"},
    {"name": "channel4", "url": "https://discord.com/api/v9/channels/858734007729258526/messages"},
    {"name": "channel5", "url": "https://discord.com/api/v9/channels/825444045789855783/messages"},
    {"name": "channel6", "url": "https://discord.com/api/v9/channels/825445142789619793/messages"},
    {"name": "channel7", "url": "https://discord.com/api/v9/channels/825445260226199592/messages"},
    {"name": "channel8", "url": "https://discord.com/api/v9/channels/825445315120332850/messages"},
    {"name": "channel9", "url": "https://discord.com/api/v9/channels/825446495368773642/messages"},
    {"name": "channel10", "url": "https://discord.com/api/v9/channels/788501452192350219/messages"},
    {"name": "channel11", "url": "https://discord.com/api/v9/channels/789415490606202890/messages"},
    {"name": "channel12", "url": "https://discord.com/api/v9/channels/789413578511089694/messages"},
    {"name": "channel13", "url": "https://discord.com/api/v9/channels/457855906055454732/messages"},
    {"name": "channel14", "url": "https://discord.com/api/v9/channels/1124757607366799481/messages"},
    {"name": "channel15", "url": "https://discord.com/api/v9/channels/1235897594782158961/messages"},
    {"name": "channel16", "url": "https://discord.com/api/v9/channels/1235903408016457768/messages"},
    {"name": "channel17", "url": "https://discord.com/api/v9/channels/1235899858494423060/messages"},
    {"name": "channel18", "url": "https://discord.com/api/v9/channels/1235901392946987048/messages"},
    {"name": "channel19", "url": "https://discord.com/api/v9/channels/1235902739041619999/messages"},
    {"name": "channel20", "url": "https://discord.com/api/v9/channels/1235649534147956798/messages"},
    {"name": "channel21", "url": "https://discord.com/api/v9/channels/1236351211096113162/messages"},
    {"name": "channel22", "url": "https://discord.com/api/v9/channels/812147552136855552/messages"},
    {"name": "channel23", "url": "https://discord.com/api/v9/channels/1134016946929668096/messages"},
    {"name": "channel24", "url": "https://discord.com/api/v9/channels/1133370512794464318/messages"},
    {"name": "channel25", "url": "https://discord.com/api/v9/channels/1134017570714955837/messages"},
    {"name": "channel26", "url": "https://discord.com/api/v9/channels/549949090872557589/messages"},
    {"name": "channel27", "url": "https://discord.com/api/v9/channels/549952532693385226/messages"},
    {"name": "channel28", "url": "https://discord.com/api/v9/channels/549951891522453542/messages"},
    {"name": "channel29", "url": "https://discord.com/api/v9/channels/566313755278049280/messages"},
    {"name": "channel30", "url": "https://discord.com/api/v9/channels/566335596243714050/messages"},
    {"name": "channel37", "url": "https://discord.com/api/v9/channels/1230157505070633001/messages"},
    {"name": "channel38", "url": "https://discord.com/api/v9/channels/1232394495136501780/messages"},
    {"name": "channel39", "url": "https://discord.com/api/v9/channels/1224758908233715722/messages"},
    {"name": "channel40", "url": "https://discord.com/api/v9/channels/1198708218675875860/messages"},
    {"name": "channel41", "url": "https://discord.com/api/v9/channels/1198708301412696197/messages"},
    {"name": "channel42", "url": "https://discord.com/api/v9/channels/1198708390562627675/messages"},
    {"name": "channel43", "url": "https://discord.com/api/v9/channels/1198708428206510250/messages"},
    {"name": "channel44", "url": "https://discord.com/api/v9/channels/1007974128533377055/messages"},
    {"name": "channel45", "url": "https://discord.com/api/v9/channels/1007924025844060262/messages"},
    {"name": "channel46", "url": "https://discord.com/api/v9/channels/1007924026024398928/messages"},
    {"name": "channel47", "url": "https://discord.com/api/v9/channels/1007924026024398929/messages"},
    {"name": "channel48", "url": "https://discord.com/api/v9/channels/1007924026024398930/messages"},
    {"name": "channel49", "url": "https://discord.com/api/v9/channels/1007924026024398932/messages"},
    {"name": "channel50", "url": "https://discord.com/api/v9/channels/1007924026196377724/messages"},
    {"name": "channel51", "url": "https://discord.com/api/v9/channels/1007924026024398934/messages"},
    {"name": "channel52", "url": "https://discord.com/api/v9/channels/1007924026024398936/messages"},
    {"name": "channel53", "url": "https://discord.com/api/v9/channels/1007924026196377721/messages"},
    {"name": "channel54", "url": "https://discord.com/api/v9/channels/1235909945585569874/messages"}
]

# Define the message content (same for all channels)
message_content =""":tada: Welcome to Hyperblock! :tada:

Looking for an epic lifesteal Minecraft server experience? Join Hyperblock today!

:globe_with_meridians: Website: [hyperblock.fun](https://hyperblock.fun/)
:video_game: Discord: [HyperBlock SMP](https://discord.gg/br46C4NFye)

:shield: Anti-Cheat Protection
:lock: Bid farewell to cheaters! Our robust anti-cheat system ensures fair gameplay by detecting and preventing cheats, safeguarding your experience and letting you focus on creativity and fun.

:sparkles: Custom Mods
:tools: Hyperblock offers a unique set of custom mods that enhance gameplay and keep things fresh. We regularly update and add new mods based on community feedback.

:crossed_swords: Competitive and Cooperative Play
:handshake: Whether you're looking to join a team or compete against others, Hyperblock has a place for you. Our server supports both competitive and cooperative gameplay, with various factions and events.

:earth_africa: Thriving Community
:star2: Join a vibrant and active community where players from all over the world come together to build, compete, and have fun. Our Discord server is bustling with activity, offering support, discussions, and events.

:pencil: Player Suggestions
:bulb: We value our players' input and frequently implement suggestions to improve the server. Your ideas can help shape the future of Hyperblock.

:scroll: Rich History
:european_castle: Since our inception, Hyperblock has built a rich history of epic builds, legendary battles, and unforgettable events. Become a part of our story!

:star2: Main Highlight: Vanilla Minecraft - Lifesteal Mode
We offer the classic Vanilla Minecraft experience enhanced with a variety of plugins, ensuring high performance and 24/7 uptime for uninterrupted play!

Join Hyperblock now and embark on your Minecraft adventure with us!

:globe_with_meridians: Website: [hyperblock.fun](https://hyperblock.fun/)
:video_game: Discord: https://discord.gg/br46C4NFye
"""

# Function to send a message to a channel
def send_message(url, payload, headers):
    try:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200 or res.status_code == 204:
            print(f"Message sent successfully to {url}")
            return True
        elif res.status_code == 429:
            retry_after = res.headers.get('Retry-After')
            if retry_after:
                print(f"Rate limited. Retrying after {retry_after} seconds.")
                return int(retry_after) + 1  # Add 1 second to be safe
            else:
                print(f"Rate limited. No Retry-After header provided. Status code: {res.status_code}")
        elif res.status_code == 403:
            print(f"Forbidden: You don't have permission to send messages to this channel. Status code: {res.status_code}")
        else:
            print(f"Failed to send message to {url}. Status code: {res.status_code}")
            print(f"Response: {res.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    return False

# Main loop to send messages based on cooldowns
def main():
    while True:
        for channel in channels:
            channel_name = channel["name"]
            url = channel["url"]

            payload = {"content": message_content}
            headers = {"Authorization": os.getenv('DISCORD_TOKEN')}  # Ensure your token is stored in environment variable

            retry_after = send_message(url, payload, headers)
            if retry_after:
                print(f"Channel {channel_name} is rate-limited. Will retry in next cycle.")

            time.sleep(2)  # Add a small delay to avoid hitting rate limits

        n = random.choice(list1)
        n = int(n)
        print("Waiting for 30 minutes before the next cycle... and offset is", n)
        time.sleep((30 * 60) + n)  # Wait for 30 minutes before sending messages again

if __name__ == "__main__":
    main()
