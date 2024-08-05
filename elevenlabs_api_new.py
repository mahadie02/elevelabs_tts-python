import requests
import voice_list as vl
import split_text as st


def el_tts(file_path, selected_voice, api_key, stability, similarity_boost, style, character_limit, format, save_dir):
    
    #Read Text file 
    print("Reading Script...")
    title, splitted_texts = st.read_and_split_text(file_path, character_limit)
    title += format 
    

    #........Eleven Labs..........#

    print("Generating Voice...")
    full_audio = bytes()
    
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
        full_audio += requests.post(tts_url, headers=headers, json=data, stream=True).content
        
    

    #save tthe audio
    with open(f"{save_dir}/{vl.voice_name[selected_voice-1]} - {title}", "wb") as file:
        file.write(full_audio)

    # Inform the user of success
    print("Audio stream saved successfully.")

    
        
    
    
    