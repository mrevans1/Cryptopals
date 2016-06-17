import urllib2
from Crypto.Cipher import AES

url = 'http://cryptopals.com/static/challenge-data/7.txt'
text = urllib2.urlopen(url).read()
text = ''.join(text.split()).decode('base64')
key = "YELLOW SUBMARINE"
cipher = AES.new(key, AES.MODE_ECB)
print cipher.decrypt(text)
