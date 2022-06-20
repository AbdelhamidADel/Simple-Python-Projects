
st = input("enter your text : ")

print("The original string is : " + str(st))

res = ' '.join(format(ord(x), 'b') for x in st)

print("The string after binary conversion : " + str(res))
