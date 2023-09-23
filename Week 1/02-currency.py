currency_dict = {
    'penny': 0.01,
    'nickel': 0.05,
    'dime': 0.10,
    'quarter': 0.25,
    'one_dollar': 1.00,
    'five_dollar': 5.00,
    'ten_dollar': 10.00,
    'twenty_dollar': 20.00,
    'fifty_dollar': 50.00,
    'hundred_dollar': 100.00
}
def float_to_currency(amount):
    
    check_amount = currency_dict.get(amount)
    if check_amount != None:
        return check_amount
    else:
        print("Invalid amount")


    



    
    
  



        
    








float_to_currency(12)
