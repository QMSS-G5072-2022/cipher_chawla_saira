## importing necessary libraries 

def cipher(text, shift, encrypt=True):
    """
    function encrypts or decrypts a string based in the shift value
    takes in 3 parameters: a string that will be encrypted or decrypted, an integer to shift the string by, and a boolean that stands for encrypt or decrypt
    returns a string that has been shifted 
    example 1:
        text = dog
        shift = 2
        encrypt = True 
            returns -> fqi
    example 2:
        text = fqi
        shift = 2
        encrypt = False
            returns -> dog
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text