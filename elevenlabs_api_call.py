import requests
from get_user_info import get_elevenlabs_user_info
import _voice_list as vl
import split_text as st


def el_tts(file_path, selected_voice, api_key, stability, similarity_boost, style, character_limit, format, save_dir):
    
    #Read Text file 
    print("\nReading Script...")
    title, splitted_texts = st.read_and_split_text(file_path, character_limit)
    title += format 

    

    #........Eleven Labs..........#

    print("\nGenerating Voice...")

    full_audio = bytes()
    count = 0
    tts_url = f"https://api.elevenlabs.io/v1/text-to-speech/{vl.voice_id[selected_voice]}/stream"
    headers = {
        "Accept": "application/json",
        "xi-api-key": api_key,
        "Content-Type": "application/json"
        }
    
    for text in splitted_texts:
        data = {
            "text": text,
            "voice_id": vl.voice_id[selected_voice-1],
            "model_id": "eleven_multilingual_v2",
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
                "use_speaker_boost": True
              }
            }
        response = requests.post(tts_url, headers=headers, json=data, stream=True)
        if response.status_code == 200:
            full_audio += response.content
            count += 1
        else:
            if count ==0:
                
                error_message(response)
                print("\nResult: Audio conversion failed!")
                return 0
            else:
                error_message(response)
                count = -1
                break

        if count > 0:
            #save tthe audio
            with open(f"{save_dir}/{vl.voice_name[selected_voice-1]} - {title}", "wb") as file:
                file.write(full_audio)
        

            # Inform the user of success
            print("\nResult: Audio saved successfully.")

        elif count == -1:
            print("\nResult: Audio saved partially!")

        else:
            print("\nResult: Audio conversion failed!")
        
        print("\nGetting Account Details...")
        account_type, character_left = get_elevenlabs_user_info(api_key)
        print(f'\nAccount Type: {account_type}')
        print(f'\nCharacters Left: {character_left}\n')

        

        

    
def error_message(response):
    error_content = response.json()
    # Extract the message from the nested 'detail' dictionary

    error_message = error_content.get('detail', {}).get('message', 'No error message provided')
        
    # Print the status code and the error message
    print(f"\nError Code: {response.status_code}")
    print(f"\nError Message: {error_message}")