import elevenlabs
import voice_list as vl
import split_text as st

def el_tts(file_path, selected_voice, api_key, stability, similarity_boost, character_limit, format, save_dir):
    
    #Read Text file 
    print("Reading Script...")
    title, splitted_texts = st.read_and_split_text(file_path, character_limit)
    title += format 
    

    #........Eleven Labs..........#

    print("Generating Voice...")

    voice = elevenlabs.Voice(
        voice_id= vl.voice_id[selected_voice-1],
        settings= elevenlabs.VoiceSettings(
            stability= stability,
            similarity_boost= similarity_boost,
            )
    )
    audio = bytes()

    for text in splitted_texts:
        audio += elevenlabs.generate(
             text= text,
             voice= voice,
             #api_key= api_key
        )

    print("Saving Audio...")
    
    #Save Audio
    elevenlabs.save(audio, f"{save_dir}/{vl.voice_name[selected_voice-1]} - {title}")

    print("Saved successfully!")
    