def first_and_last(message):
    if len(message) == 0:
        output = True
    elif message[0] == message[-1]:
        output = True
    else:
        output = False
    return output

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

