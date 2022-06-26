vowels=['a','e','i','o','u']
word=input('provide a word to look for vowels :')
found={}
found['a']=0
found['e']=0
found['i']=0
found['o']=0
found['u']=0

for letter in word:
    if letter in vowels:
        found[letter]+=1
for k,v in found.items():
    print(k,'found \t ',v, 'times')
