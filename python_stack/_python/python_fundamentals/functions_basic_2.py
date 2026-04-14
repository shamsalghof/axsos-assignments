#1
def coundown(number):
    newList = []
    for i in range(number,-1,-1):
        newList.append(i)
    return newList
print(coundown(3))

#2
def printAndReturn(numbersList):
    print(numbersList[0])
    return numbersList[1]
print(printAndReturn([5,10]))

#3
def first_plus_length(listNumbers):
    return listNumbers[0] + len(listNumbers)
print(first_plus_length([1,2,3,4,5]))


#4
def values_greater_than_second(listNumbers):
    new_list = []
    if len(listNumbers) < 2:
        return False
    for number in listNumbers:
        if number > listNumbers[1]:
            new_list.append(number)
    print(len(new_list))

    return new_list

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5
def length_and_value(size,value):
    newList = []
    for i in range(0,size):
        newList.append(value)
    return newList

print(length_and_value(4,7))
print(length_and_value(6,2))