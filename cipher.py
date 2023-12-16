st=input('paste a phrase to decipher: '
alphabet ='abcdefghijklmnopqrstuwxyz'
stl= (list(st))
alist = list(alphabet)
text = []
for i in range(len(stl)):
    if stl[i] == 'z':
        text.append('b')
    elif stl[i] == 'y':
        text.append('a')
    elif stl[i] in alist:
        text.append(alphabet[(alphabet.index(stl[i])+2)])
    else:
        text.append(stl[i])

message = ''.join(text)
print(message)
