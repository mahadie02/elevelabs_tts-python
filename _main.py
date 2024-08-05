#import elevenlabs_api as el
#import new_el as el
import elevenlabs_api_new as el

7
#..........Parameters.........#
api_key = 'YOUR_ELEVEN_LABS_API_KEY'

file_path = "_script.txt"
selected_voice = 4

stability = 0.75
similarity_boost = 0.75
style = 0.0

character_limit = 2500
format = '.mp3'
save_dir = 'voices'




el.el_tts(file_path, selected_voice, api_key, stability, similarity_boost, style, character_limit, format, save_dir)

