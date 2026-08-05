from songs.reference import load_reference

def get_reference():
    load_reference("assets/songs/") # Add the song folder here (ex. assets/songs/beer)

# Basically, what you need are...
# - vocals.wav
# - instrumental.wav
# - cover.jpg
# - reference.json (can be empty or omitted)

# Take note that the names and extensions should be exactly as above
# The process might take a while, considering the length of the song

# Example format:
# assets/
# └── songs/
#     └── beer/
#         ├── vocals.wav
#         ├── instrumental.wav
#         ├── cover.jpg
#         └── reference.json

# I'll fix you soon