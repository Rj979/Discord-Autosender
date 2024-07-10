import requests
import time
from datetime import datetime

# Define your channels, URLs, and cooldowns
channels = [
    {"name": "channel1", "url": "https://discord.com/api/v9/channels/858734007729258526/messages"},
    {"name": "channel2", "url": "https://discord.com/api/v9/channels/546371699076104192/messages"},
    
    # Add more channels as needed
]
# Define the message content (same for all channels)
message_content = # if the content is single line use quotes (" ")
                  # if the content is multi line use docstring (""" """)

# Function to send a message to a channel
def send_message(url, payload, headers):
    try:
        res = requests.post(url, json=payload, headers=headers)
        if res.status_code == 200:
            print(f"Message sent successfully to {url}")
            return True
        elif res.status_code == 429:
            retry_after = res.headers.get('Retry-After')
            if retry_after:
                print(f"Rate limited. Retrying after {retry_after} seconds.")
                return int(retry_after) + 1  # Add 1 second to be safe
            else:
                print(f"Rate limited. No Retry-After header provided. Status code: {res.status_code}")
        else:
            print(f"Failed to send message to {url}. Status code: {res.status_code}")
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
            headers = {"Authorization": "Enter-token-here"}  # Replace with your actual token

            retry_after = send_message(url, payload, headers)
            if retry_after:
                print(f"Channel {channel_name} is rate-limited. Will retry in next cycle.")

            time.sleep(1)  # Add a small delay to avoid hitting rate limits

        print("Waiting for 30 minutes before the next cycle...")
        time.sleep(30 * 60)  # Wait for 30 minutes before sending messages again

if __name__ == "__main__":
    main()
