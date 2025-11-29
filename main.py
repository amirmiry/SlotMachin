MAX_LINES = 3



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




def get_lines_of_bet():
    while True:
        lines = input("Enter the lines would you like to bet on? 1-"+ str(MAX_LINES) + ": ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print("the lines must be between the 1 -"+ str(MAX_LINES) + "!")

        else:
            print("Please enter vallid number!")

    return lines