from webserver import keep_alive
import requests

channelID = 977766253664010313
headers = {
    "authorization":
    "OTgxODEyMTUzOTI3NDg3NTE4.GonTfA.sGgGHnKXKnAqcu0rhBFXsx1TPJJUQbkVWXynm0"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
