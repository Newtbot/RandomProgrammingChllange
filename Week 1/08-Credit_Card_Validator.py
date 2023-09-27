class CreditCard:
    def __init__(self,card_number , card_type , valid):
        self.card_number = card_number
        self.card_type = card_type # "AMEX"
        self.valid = valid #accepts true or false 
    
#Create and add your method called `determine_card_type` to the CreditCard class here:
    def determine_card_type(self):
        # Visa must start with 4
        #Mastercard must start with 51, 52, 53, 54 or 55    
        #AMEX must start with 34 or 37
        #Discover must start with 6011
        print(self.card_type)
        print(self.card_number)


#Create and add your method called `check_length` to the CreditCard class here:
    def check_length(self):
        pass

#Create and add your method called 'validate' to the CreditCard class here:
    def validate(self):
        reverse_number = []
        even_number_pos = []
        odd_number_pos = []
        #340685143688205
        #sum of all odd number position in String
        for i in self.card_number[::-1]:
            reverse_number.append(int(i))
        #take position of all odd array position like 1 3 5 7 9 11 13 15 
        for i in range(len(reverse_number)):
            if i % 2 == 0:
                odd_number_pos.append(reverse_number[i])
            else: 
                even_number_pos.append(reverse_number[i])

        #but first multiple all of i in even_number by 2
        even_list = [] 
        for i in even_number_pos:
            multi = i * 2
            even_list.append(int(multi))

        #if i in sum_even_list is greater than 10. add them
        smaller10 = []
        bigger10 = []
        for i in even_list:
            if i >= 10:
                #split i and add them
                for digit in str(i):
                    bigger10.append(int(digit))
            elif i < 10:
                smaller10.append(int(i))
        total_even = (sum(smaller10) + sum(bigger10))


        total_odd = sum(odd_number_pos)
        luhn = (total_even + total_odd) % 10 
        if luhn == 1:
            self.valid = True
            return self.valid
        else:
            self.valid = False
            return self.valid

cc = CreditCard(card_number="4847352989263095" , card_type="VISA" , valid="TRUE")
print(cc.validate())
cc.determine_card_type()
print(cc.determine_card_type())

