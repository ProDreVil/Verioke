from core.karaoke import run_karaoke

def main():
    score = run_karaoke("assets/songs/sample")
    print(f"\nFinal Song Score: {score:.2f}")

if __name__ == "__main__":
    main()