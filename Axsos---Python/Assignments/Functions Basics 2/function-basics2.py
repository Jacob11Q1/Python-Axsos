# 1) CountDown from 5 like this and return [5,4,3,2,1]
def c(n):
    if n < 0:
        return [];
    return list(range(n , 0 , -1));
print(c(5));

# 2) Print And Return
def printNumbers(returnNumber):
    print(returnNumber[0])
    return(returnNumber[1])
result = printNumbers([5,8])
print(result)

# 3) First Plus Length
def first_plus_length(listNum):
    return listNum[0] + len(listNum)
first_list = first_plus_length([1,2,3,4,5])
print(first_list)

# 4) Values Greater Than Second
def values_greater_than_second(numReturn):
    if len(numReturn) < 2:
        return False
    sec = numReturn[1]
    result = []
    
    for i in numReturn:
        if i > sec:
            result.append(i)
    print(len(result))
    return(result)

print(values_greater_than_second([5, 2, 3, 2, 1, 4]))
print(values_greater_than_second([3]))

# 5) This Length , That Value
def length_and_value(size , value):
    return [value] * size
print(length_and_value(4, 7))
print(length_and_value(6, 2))