import requests
import json


voice_url = "https://api.elevenlabs.io/v1/voices"

response = requests.get(url= voice_url)

json_data = response.content.decode('utf-8')

voice_data = json.loads(json_data)

for voice in voice_data['voices']:
    print(f"Voice ID: {voice['voice_id']}")
    print(f"Name: {voice['name']}")
    print(f"Accent: {voice['labels']['accent']}")
    print(f"Description: {voice['labels']['description']}")
    print(f"Preview URL: {voice['preview_url']}\n")