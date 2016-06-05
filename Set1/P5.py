input1 = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

def repkeyxor(text,key):
    newkey = key*len(text)
    pairs = zip(text,newkey)
    xored_text = [chr(ord(i)^ord(j)).encode('hex') for i,j in pairs]
    return ''.join(xored_text)

if __name__=='__main__':
    print repkeyxor(input1,'ICE')
