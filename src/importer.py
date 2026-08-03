from reference import load_reference

reference_notes = load_reference("assets/songs/") # Add the song folder here (ex. assets/songs/beer)

# What you need is an instrumental and vocal wav file of the song
# Also you need a cover.jpg and an empty (or just don't make one) reference.json file
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