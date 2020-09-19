def remainingwords(str):
    str = str.split(' ')
    str = str[1:]
    out_str = " "
    str = out_str.join(str)
    return str

print(remainingwords("This is an example string."))
