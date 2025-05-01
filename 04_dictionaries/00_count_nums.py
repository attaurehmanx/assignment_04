# This program counts the number of times each number appears in a list. It uses a dictionary to keep track of the information.

# An example run of the program looks like this (user input is in blue):

# Enter a number: 3
# Enter a number: 4
# Enter a number: 3
# Enter a number: 6
# Enter a number: 4
# Enter a number: 3
# Enter a number: 12
# Enter a number: 
# 3 appears 3 times.
# 4 appears 2 times.
# 6 appears 1 times.
# 12 appears 1 times.

def get_num():
    user_num = []

    while True:
        enput = input("Enter a num :")
        
        if enput == "":
            break

        nums = int(enput)

        user_num.append(nums)

        
    return user_num

def num_count(user_num_lst):

    dic = {}
    for count in user_num_lst:
        if count not in dic:
            dic[count] = 1
        else:
            dic[count] += 1
    
    return dic

def count_print(dic):

    for num in dic:
        print(f"{num} appear {dic[num]} times.")


def main():
    x= get_num()
    y= num_count(x)
    count_print(y)

if __name__ == '__main__':
    main()