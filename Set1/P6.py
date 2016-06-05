import urllib2
from P3 import choose_byte
from P5 import repkeyxor

url = 'http://cryptopals.com/static/challenge-data/6.txt'
request = urllib2.urlopen(url)
text6 = request.read()
text7 = ''.join(text6.splitlines())
text8 = text7.decode('base64')

def hamming_distance(input1,input2):
    '''This return the number of bits needed to transform input1 into input 2'''
    binary = ''.join([bin(ord(i)^ord(j))[2:] for i,j in zip(input1,input2)])
    return sum([char=='1' for char in binary])

if __name__ == '__main__':
    print hamming_distance('this is a test','wokka wokka!!!')
    #returns 37

    #determines keysize by testing 39 key lengths and 
    sizes = []
    for size in range(1,40):
        sizes.append([size,choose_byte(''.join([text8[i] for i in range(len(text8)) if i%size==0]).encode('hex'))[2]])
    sizes.sort(key = lambda x: x[1])
    keysize = sizes[-1][0]
    #keysize == 29

    key = []
    for k in range(keysize):
        key.append(chr(choose_byte(''.join([text8[i] for i in range(len(text8)) if i%keysize==k]).encode('hex'))[0]))
    key = ''.join(key)
    print key + '\n'

    print repkeyxor(text8,key).decode('hex')
