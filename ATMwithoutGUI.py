
def main():
    print("Welcome to my ATM \n Please enter the details")
    a = int(input("Enter last 4 digits of your Account Number: **** **** **** "))
    b = int(input("Enter your balance Amount: Rs."))
    c = float(input("Enter the rate of Interest: "))
    d = int(input("Select Your Account type: \n1. Savings \n2. Current"))
    print("Thanks For Details; Your account no is: **** **** **** ", a)
    if d == 1:
        e = int(input("Select your transaction: \n1. Withdraw \n2.Deposit \n3. Balance Enquiry \n4. Rate of Interest \nYour choice: "))
        if e == 1:
            sav_with(b)
        elif e == 2:
            sav_dep(b)
        elif e == 3:
            sav_bal(b)
        elif e == 4:
            sav_rate(c, b)
        else:
            print("Invalid Choice... Please do try again...")
    elif d == 2:
        e = int(input("Select your transaction: \n1. Withdraw \n2.Deposit \n3. Balance Enquiry \n4. Rate of Interest \nYour choice: "))
        if e == 1:
            curr_with(b)
        elif e == 2:
            curr_dep(b)
        elif e == 3:
            curr_bal(b)
        elif e == 4:
            curr_rate(c, b)
        else:
            print("Invalid Choice... Please do try again...")
    else:
        print("Invalid Choice... Please do try again...")

def sav_with(b):
    i = int(input("Enter the amount to withdraw: Rs."))
    j = int(input("Amount is withdrawn from your account... \n For checking your balance click 1, else 0"))
    if j == 1:
        print("Your current balance is: Rs. ", b - i)
    elif j == 0:
        print("Thanks for using our ATM")
    else:
        print("Invalid choice")


def sav_dep(b):
    i = int(input("Enter the amount to deposit: Rs. "))
    j = int(input("Amount is deposited to your account... \nFor checking your balance click 1 or else 0"))
    if j == 1:
        print("Your current balance is: Rs. ", b + i)
    elif j == 0:
        print("Thanks for using our ATM")
    else:
        print("Invalid choice")


def sav_bal(b):
    print("Your Balance is: Rs. ", b ,"\nThanks for Using our ATM")


def sav_rate(c, b):
    r = b * c
    print("Your interest on Saving Account is: Rs. ", r)


def curr_with(b):
    i = int(input("Enter the amount to withdraw: Rs."))
    j = int(input("Amount is withdrawn from your account...\n For checking your balance click 1, else 0"))
    if j == 1:
        print("Your current balance is: Rs. ", b - i - 10)
    elif j == 0:
        print("Thanks for using our ATM")
    else:
        print("Invalid choice")


def curr_dep(b):
    i = int(input("Enter the amount to deposit: Rs. "))
    j = int(input("Amount is deposited to your account... \nFor checking your balance click 1 or else 0"))
    if j == 1:
        print("Your current balance is: Rs. ", b + i - 10)
    elif j == 0:
        print("Thanks for using our ATM")
    else:
        print("Invalid choice")


def curr_bal(b):
    print("Your Balance is: Rs. ", b, "\nThanks for Using our ATM")


def curr_rate(c, b):
    r = b * c
    print("Your interest on Saving Account is: Rs. ", r)

