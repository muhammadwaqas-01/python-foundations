
def stats_loop(numbers):
    if len(numbers) == 0:
        return None
    minimum = numbers[0]
    maximum = numbers[0]

    total = 0

    for i in numbers:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
        total += i

    avg = total/len(numbers)
    return minimum,maximum,avg

def stats_built(numbers):
    if len(numbers) == 0:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    avg = sum(numbers)/len(numbers)

    return minimum,maximum,avg

def main():
    numbers = [10, 20, 30, 40, 50]
    print('Stats With loop')
    print(stats_loop(numbers))
    print('Stats With Built-in')
    print(stats_built(numbers))

if __name__ =="__main__":
    main()