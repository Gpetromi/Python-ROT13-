def rot13(s):
    result = ""

    for v in s:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
                c -= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c > ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result

x = input("Enter text: ")
print(rot13(x))
flag = input("Wanna continue? y/n")
while flag.strip()!='n':
    x = input("Enter text: ")
    print(rot13(x))
    flag = input("Wanna continue? y/n")



