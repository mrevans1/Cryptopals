import urllib2
from P3 import choose_byte

url = 'http://cryptopals.com/static/challenge-data/4.txt'
text = urllib2.urlopen(url).read()

decrypted_strings = []
for line in text.split():
    decrypted_strings.append(choose_byte(line))
    
decrypted_strings.sort(key = lambda x: -x[2])

print decrypted_strings[0]
