def removeThirdNumber(int_list):
    # list starts with
    # 0 index
    pos = 3 - 1
    index = 0
    len_list = (len(int_list))

    # breaks out once the
    # list becomes empty
    while len_list > 0:
        index = (pos + index) % len_list
        print(index)
        # removes and prints the required
        # element
        print(int_list.pop(index))
        len_list -= 1

#Remove duplicate from list using in place method
def remove_duplicate(int_list):
    int_list.sort()
    len_list = len(int_list)
    for i in range(len_list-1, 0,-1):
        if int_list[i] ==  int_list[i-1]:
            print(int_list.pop(i))
            len_list -=1
    print(int_list)

# Driver code
if __name__ == '__main__':
    nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    #removeThirdNumber(nums)

    nums = [10, 20, 10, 20, 50, 50, 70, 10, 90]
    remove_duplicate(nums)


