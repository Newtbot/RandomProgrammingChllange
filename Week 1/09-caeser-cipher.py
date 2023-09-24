import re
#round 1
def caesar(message, shift):

    #ensure message is clean from digit and special character
    number_checker = (bool(re.search(r'\d' , message)))
    special_checker = (bool(re.search(r'[@_!#$%^&*()<>?/\|}{~:]' , message)))


    if ' ' in message or number_checker or special_checker:
        print("no")
        pass
    else:

        #ASCII decimal value list
        ASCII_list = []
        ASCII_shifted_list = []
        ASCII_Char_list = []

        #>>> def char_shift(char, shift):
        #start = 65 if char.isupper() else 97
        #char = ord(char) - start
        #shift = (char + shift) % 26
        #return chr(shift+start)

        #start of 65 if UPPER_case refer to ascii chart
        if message.isupper():
            start = 65 #dec
        else:
            #not upper
            start = 97 #dec

        #loop through message list 
        for i in message:
            #convert all i to ASCII and append
            ascii = ord(i) - start
            ASCII_list.append(ascii)
        #print(ASCII_list)

        #loop through ASCII_list and add shift value to each i value of list
        for i in ASCII_list:
            #mod the shift to prevent overflow of special symbol
            #shift = (shift) % 26

            shifted_ascii = (i + shift) % 26 
            shifted_ascii = shifted_ascii + start
            ASCII_shifted_list.append(shifted_ascii)

        #print(shift)
        #print(ASCII_shifted_list)

        #loop through shifted_list to convert it back to ASCII character
        for i in ASCII_shifted_list:
            #convert all i to ASCII character and append
            ascii_char = chr(i)
            ASCII_Char_list.append(ascii_char)
        #print(ASCII_Char_list)

        #join list 
        ciphered_text = (''.join(ASCII_Char_list))
        print("The caeser ciphered text is"  , ciphered_text)


caesar("abc", 1)


#round 3
def decrypt_caesar(message, shift):

        #ASCII decimal value list
        ASCII_list = []
        ASCII_shifted_list = []
        ASCII_Char_list = []
        
         #start of 65 if UPPER_case refer to ascii chart
        if message.isupper():
            start = 65 #dec
        else:
            #not upper
            start = 97 #dec


        #loop through message list 
        for i in message:
            #convert all i to ASCII and append and minus start 
            ascii = ord(i) - start
            ASCII_list.append(ascii)
        #print(ASCII_list)

        #loop through ASCII_list and add shift value to each i value of list
        for i in ASCII_list:
            #mod the shift to prevent overflow of special symbol
            shifted_ascii = (i - shift) % 26 
            shifted_ascii = shifted_ascii + start
            ASCII_shifted_list.append(shifted_ascii)

        #print(shifted_ascii)
        #print(shift)
        #print(ASCII_shifted_list)

        #loop through shifted_list to convert it back to ASCII character
        for i in ASCII_shifted_list:
            #convert all i to ASCII character and append
            ascii_char = chr(i)
            ASCII_Char_list.append(ascii_char)
        #print(ASCII_Char_list)

        #join list 
        unciphered_text = (''.join(ASCII_Char_list))
        print("The caeser unciphered text is"  , unciphered_text)


decrypt_caesar("bcd", 1)




