def greeting(name, greet = "Hello"):
    print(f"{greet}, {name}!")


def min_max(numbers):
    return min(numbers), max(numbers)

def main():   
    greeting("Waqas")
    greeting("Waqas", "Hi")
    low,high = min_max([1,2,3,4,56])
    print("Low: ",low,"\nHigh: ",high)
    print(min_max([1,2,3,4,56]))
if __name__ == "__main__":
    main()
