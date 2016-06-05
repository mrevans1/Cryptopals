a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'

text = ''.join([chr(ord(i)^ord(j)) for i,j in zip(a.decode('hex'),b.decode('hex'))])

print text.encode('hex')