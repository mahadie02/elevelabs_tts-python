import requests
import json

def get_elevenlabs_user_info(api_key):
  headers = {
    "xi-api-key": api_key,
    "Content-Type": "application/json"
  }

  url = "https://api.elevenlabs.io/v1/user"

  response = requests.get(url=url, headers=headers)
  json_data = response.content.decode('utf-8')
  user_data = json.loads(json_data)
  subscription_info = user_data.get('subscription', {})
  account_type = subscription_info.get('tier')
  character_count = subscription_info.get('character_count')
  character_limit = subscription_info.get('character_limit')
  return account_type, character_limit-character_count
