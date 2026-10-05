from pathlib import Path
Base = Path(__file__).parent

with open(Base/"Story.txt","w") as f:
    f.write(
        "Waqas went to the park in the morning.\n"
        "The park was quiet, and Waqas enjoyed the fresh air.\n"
        "He sat under a tree and read a small book.\n"
        "The book was interesting, so Waqas read the book again.\n"
        "After reading, Waqas walked around the park and smiled.\n"
        "The morning was peaceful, and the park felt beautiful."
    )

def read_text(path):
    try:
        with open(path,"r") as f:
            return f.read()
    except FileNotFoundError:
        return None
def count_words(text):
    text = text.lower()
    for punctuation in ".!,?":
        text = text.replace(punctuation,"")
    words = text.split()

    counts = {}
    for word in words:
        counts[word] = counts.get(word,0) +1
    return counts

def top_words(counts, n=5):
    return sorted(counts.items(), key= lambda item: item[1], reverse=True)[:n]

def main():
    path = Base/"Story.txt"

    text = read_text(path)
    if text is not None:
        counts = count_words(text)
        words = top_words(counts,5)

        print("Top 5 words")
        for word,count in words:
            print(f"{word}: {count}")
    else:
        print("File not Found!")
    missing = read_text(Base/"Missing.txt")
    if missing is None:
        print("Missing test pass!")

if __name__ == "__main__":
    main()