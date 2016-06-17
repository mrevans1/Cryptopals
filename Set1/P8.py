import urllib2

url = 'http://cryptopals.com/static/challenge-data/8.txt'
text = urllib2.urlopen(url).read()
def count_unique_blocks(line):
    blocks = set()
    for n in range(len(line)/16):
        blocks.add(line[16*n:16*n+16])
    return len(blocks)

dict = {}
for line in text.split():
    dict[count_unique_blocks(line.decode('hex'))] = line

print dict[min(dict.keys())]
