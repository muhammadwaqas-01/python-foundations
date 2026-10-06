def main():
    sqr = [num * num for num in range(1,11) ]
    print(sqr)

    even = [num for num in sqr if num%2==0]
    print(even)
    my_list = [3, 8, 12, 5, 20, 7]
    even_num = [num for num in my_list if num%2 == 0]
    print(even_num)
    even_list = []
    for i in my_list:
        if i%2 ==0:
            even_list.append(i)
    print(even_list)

    if even_list == even_num:
        print(True)


    words = ["apple", "banana", "cat", "python", "book"]
    my_dic = {word : len(word) for word in words}
    print(my_dic) 

if __name__ == "__main__":
    main()