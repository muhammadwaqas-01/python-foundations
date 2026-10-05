def safe_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
    finally:
        print("Done")




def get_number(text):
    try:
        x = int(text)
        return x
    except ValueError:
        return None
    finally:
        print("Done")


def main():
    print(safe_divide(10, 2))
    print(safe_divide(2,0))
    print(get_number("123"))
    print(get_number("Waqas"))

if __name__ == "__main__":
    main()