from core.karaoke import run_karaoke
from interface.gui import Verioke
from songs.importer import get_reference

# def main():
#     performance = run_karaoke("assets/songs/buwan")
#     score = performance["score"]
#     print(f"\nFinal Song Score: {score:.2f}")

# if __name__ == "__main__":
#     main()

# get_reference()

app = Verioke()
app.mainloop()