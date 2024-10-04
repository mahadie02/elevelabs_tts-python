import elevenlabs_api_call as el

#..........Parameters.........#
api_key = 'YOUR_API_KEY'

file_path = "_script.txt"

selected_voice = 6

stability = 0.5
similarity_boost = 0.75
style = 0.0

character_limit = 2500
format = '.mp3'
save_dir = 'voices'




el.el_tts(file_path, selected_voice, api_key, stability, similarity_boost, style, character_limit, format, save_dir)

