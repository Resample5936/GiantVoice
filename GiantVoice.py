import os
import requests
import json

print("Giant Voice interface initiated")

message = input("Enter the announcement to send to Slack: ")
print("Sending...")
if not message.strip():
	exit("Message cannot be empty, exiting program.")

# Load webhook URLs from JSON file
with open("FILEPATH.json", "r") as f:
    channels = json.load(f).get("channels", {})

# Send the message to each channel
for channel, webhook_url in channels.items():
    try:
        payload = {
            "text": message,
            "channel": channel
        }
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
        print(f"Message sent successfully to {channel}.")
    except Exception as e:
        print(f"Failed to send message to {channel}: {e}")

exit("Thanks for using the Giant Voice service.")
