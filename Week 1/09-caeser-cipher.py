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
        #split into list
        message = list(message)
        #ASCII decimal value list
        ASCII_list = []
        ASCII_shifted_list = []
        ASCII_Char_list = []

        #loop through message list 
        for i in message:
            #convert all i to ASCII and append
            ascii = ord(i)
            ASCII_list.append(ascii)
        #print(ASCII_list)

        #loop through ASCII_list and add shift value to each i value of list
        for i in ASCII_list:
            shifted_ascii = i + shift
            ASCII_shifted_list.append(shifted_ascii)
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

        #split into list
        message = list(message)
        #ASCII decimal value list
        ASCII_list = []
        ASCII_shifted_list = []
        ASCII_Char_list = []

        #loop through message list 
        for i in message:
            #convert all i to ASCII and append
            ascii = ord(i)
            ASCII_list.append(ascii)
        #print(ASCII_list)

        #loop through ASCII_list and add shift value to each i value of list
        for i in ASCII_list:
            shifted_ascii = i - shift
            ASCII_shifted_list.append(shifted_ascii)
        #print(ASCII_shifted_list)

        #loop through shifted_list to convert it back to ASCII character
        for i in ASCII_shifted_list:
            #convert all i to ASCII character and append
            ascii_char = chr(i)
            ASCII_Char_list.append(ascii_char)
        #print(ASCII_Char_list)

        #join list 
        unciphered_text = (''.join(ASCII_Char_list))
        print("The caeser ciphered text is"  , unciphered_text)


decrypt_caesar("bcd", 1)


#assert test


