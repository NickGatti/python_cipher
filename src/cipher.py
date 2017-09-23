def readFile(file):
    with open(file, 'r') as myfile:
        data=myfile.read().replace('', '')
        return data
        
def cipherOption(data, key, option):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    output = ''
    if option == 'encipher':
        for i in range(0, len(data)):
            for z in range(0, len(alpha)):
                if data[i] == alpha[z]:
                    output += key[z]
        return output
    
    if option == 'decipher':
        for i in range(0, len(data)):
            for z in range(0, len(alpha)):
                if data[i] == key[z]:
                    output += alpha[z]
        return output
        
fileData = readFile('./cipher.txt')

newCipher = cipherOption(fileData, 'bcdefghijklmnopqrstuvwxyza', 'encipher')
newDeCipher = cipherOption(newCipher, 'bcdefghijklmnopqrstuvwxyza', 'decipher')

print(newCipher)
print(newDeCipher)