def digits(n):
    count = 0
    n_string = str(n)
    for i in n_string:
        count +=1
    return count
print(digits(25))
print(digits(144))
print(digits(1000))
print(digits(0))
