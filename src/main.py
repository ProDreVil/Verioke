from karaoke import run_karaoke

def main():
    score = run_karaoke("assets/songs/sample", 5)
    print(f"\nFinal Song Score: {score:.2f}")

if __name__ == "__main__":
    main()