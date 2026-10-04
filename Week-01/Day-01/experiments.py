x = 5
x = "Waqas"
print(x)

print(7/2)
print(7//2)
print(2**2)

my_list = [1, 2, 3, 4]

def check(numbers):
    numbers.append(45)

print("Before:", my_list)
check(my_list)
print("After:", my_list)


def reset(numbers):
    numbers = [100]

reset(my_list)
print(my_list)

my_list = [1, 2, 3]

def reset(numbers):
    print(id(numbers) == id(my_list))
    numbers = [100]
    print(id(numbers) == id(my_list))

reset(my_list)