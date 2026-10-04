numbers = [10, 20, 30, 40, 50]
def stats_loop(numbers):
    if len(numbers) == 0:
        return None
    minmum = numbers[0]
    maximum = numbers[0]

    total = 0

    for i in numbers:
        if i < minmum:
            minmum = i
        if i > maximum:
            maximum = i
        total += i

    avg = total/len(numbers)
    return minmum,maximum,avg
print('Stats With loop Methos')
print(stats_loop(numbers))
print('Stats With Build-in')

def stats_build(numbers):
    if len(numbers) == 0:
        return None
    minimum = min(numbers)
    maximum = max(numbers)
    avg = sum(numbers)/len(numbers)

    return minimum,maximum,avg

print(stats_build(numbers))