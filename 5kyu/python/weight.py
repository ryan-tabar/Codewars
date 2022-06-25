"""5kyu: Weight for weight"""
# My friend Jogn and I are members of the "Fat to Fit Club(FFC)". John is worried
# because each month a list with the weights of members is published and each
# month he is the last on the list which means he is the heaviest.

# I am the one who establishes the list so I told him: "Don't worry any more, I will"
# modify the order of the list". It was decided to attribute a "weight" to numbers.
# The weight of a number will be from now on the sum of its digits.

# For example 99 will have "weight" 18, 100 will have "weight" 1 so in the list
# 100 will come before 99

def order_weight(string):
    new_num = 0
    new_list1 = [] #list of integers of string
    new_list2 = [] #new list of integers of string
    new_str = ""
    list_num = string.split(" ")

    for i in range(len(list_num)):
        new_list1.append(list_num[i])
        list_num[i] = list(list_num[i])
        for j in range(len(list_num[i])):
            new_num += int(list_num[i][j])
        new_list2.append(new_num)
        new_num = 0

    new_str = " ".join([x for _,x in sorted(zip(new_list2,new_list1))])

    return new_str