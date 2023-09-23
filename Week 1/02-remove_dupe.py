user_input = input("input: ")

def remove_dupe(user_input):
    dupe = []
    non_dupe = []

    for letter in user_input:
        #if letter not in dupe append to non_dupe
        if letter not in dupe:            
            non_dupe.append(letter)
            #to ensure that the letter is not appended again
            dupe.append(letter) 
        elif letter in dupe:
            dupe.append(letter)

    #remove the dupes of dupe list
    for alphabet in dupe:
        if alphabet in non_dupe:
            dupe.remove(alphabet)
            


            

    


    #join the list into a string
    non_dupe = ''.join(non_dupe)
    dupe = ''.join(dupe)
    
    print("expected output: " + non_dupe + " " + dupe) 

   


remove_dupe(user_input)



    