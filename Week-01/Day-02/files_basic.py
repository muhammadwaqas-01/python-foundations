

def main():
    with open("Info.txt","w") as f:
        f.write("Hi,I'm Waqas!\n")
        f.write("It's day 2 of learning python!\n")
        f.write("Today the topic is file handling\n")
    with open("Info.txt","a") as f:
        f.write("I learend ,how to read a file.\n")

    with open("Info.txt","r") as f:
        text = f.read()
        print(text)
    with open("Info.txt","r") as f:
        for text in f:
            print(text.strip())
    try:
        with open("sample.txt","r") as f:
            f.read()
    except:
        print("File Not Found!")

if __name__ == "__main__":
    main()