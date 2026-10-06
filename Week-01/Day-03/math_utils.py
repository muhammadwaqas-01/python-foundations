
def average(numbers):
    if len(numbers) == 0:
        return None
    avg_num = sum(numbers)/len(numbers)
    return avg_num

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
    
def main():
    my_list = [1,2,3,4,5,67,7]
    print("Average of numbers:",average(my_list))
    check_avg_num = int(average(my_list))
    print("Round: ",check_avg_num)
    print("Number is even: ",is_even(check_avg_num))

if __name__ == "__main__":
    main()