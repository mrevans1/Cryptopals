input = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def score_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    return float(sum([(i in alphabet) for i in text]))/len(text)

def single_byte_xor(text,byte):
    return ''.join([chr(ord(i)^byte) for i in text.decode('hex')])

def choose_byte(text):
    possible_outputs = []
    for i in range(256):
        output = single_byte_xor(text,i)
        possible_outputs.append([i,output,score_text(output)])
    possible_outputs.sort(key = lambda x: -x[2])
    return possible_outputs[0]


if __name__=='__main__':
    print choose_byte(input)
