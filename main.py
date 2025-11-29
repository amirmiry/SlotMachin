



def deposite():
    while True:
        amount  = input("What amonut Would You like to set as your balnace? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("the amount must be gerater than 0")

        else:
            print("Please enter vallid number!")

    return amount