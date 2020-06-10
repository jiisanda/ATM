def savings(Ac_No, Bank_Balance):			# Saving Account
	print("Hello & Welcome Again!")
	operation = int(input("Please input the valid option: \n\t1) Withdraw \n\t2) Deposit \n\t3) Balance Enquiry\n"))
	if operation == 1:
		sav_withdraw(Ac_No, Bank_Balance)
	elif operation == 2:
		sav_deposit(Ac_No, Bank_Balance)
	elif operation == 3:
		sav_bal_enq(Ac_No, Bank_Balance)
	else:
		print("Please select the valid option...")

def current(Ac_No, Bank_Balance):			# Current Account
	print("Hello & Welcome Again! \nPlease Note: You have a current account the ammount will always be Rs. 10 less in Balance as well as Withdraw. And for deposit it will be charged extra Rs. 10...")
	operation = int(input("Please input the valid option: \n\t1) Withdraw \n\t2) Deposit \n\t3) Balance Enquiry\n"))
	if operation == 1:
		curr_withdraw(Ac_No, Bank_Balance)
	elif operation == 2:
		curr_deposit(Ac_No, Bank_Balance)
	elif operation == 3:
		curr_bal_enq(Ac_No, Bank_Balance)
	else:
		print("Please select the valid option...")

def sav_withdraw(Ac_No, Bank_Balance):			# Withdraw --> savings Accout
	with_amount = int(input("Enter the amount to withdraw: "))
	print("The {} has been withdraw form the your account no.(Ending from) {}.\nPlease collect the cash form the slot.".format(with_amount, Ac_No))
	bal_check = input("Enter 'yes' to check the Bank Balance of your account or ' ' to not to...")
	if bal_check == 'yes':
		print("Balance Amount: Rs. ", Bank_Balance - with_amount)
	elif bal_check == ' ':
		pass
	else:
		print("Enter the valid choice...")

def sav_deposit(Ac_No, Bank_Balance):			# Deposit --> Saving Account
	depot_amount = int(input("Enter the amount to deposit: "))
	print("Put the money on the slot... \nThe amount has been deposited to your account...")
	bal_check = input("Enter 'yes' to check the Bank Balance of your account or ' ' to not to...")
	if bal_check == 'yes':
		print("Balance Amount: Rs. ", Bank_Balance + bal_check)
	elif bal_check == ' ':
		pass
	else:
		print("Enter the valid choice...")

def sav_bal_enq(Ac_No, Bank_Balance):			# Balance enquirey --> Savings Account
	print("Bank Balance is. Rs. ", Bank_Balance)

def curr_withdraw(Ac_No, Bank_Balance):			# Withdraw --> Current Account
	with_amount = int(input("Enter the amount to withdraw: "))
	print("The {} has been withdraw form the your account no.(Ending from) {}.\nCollect your cash from the slot below.".format(with_amount, Ac_No))
	bal_check = input("Enter 'yes' to check the Bank Balance of your account or ' ' to not to...")
	if bal_check == 'yes':
		print("Balance Amount: Rs. ", Bank_Balance - with_amount - 10)
	elif bal_check == ' ':
		pass
	else:
		print("Enter the valid choice...")

def curr_deposit(Ac_No, Bank_Balance):			# Deposit --> Current Account
	depot_amount = int(input("Enter the amount to deposit: "))
	print("Put the money on the slot... \nThe amount is deposited to your account....")
	bal_check = input("Enter 'yes' to check the Bank Balance of your account or ' ' to not to...")
	if bal_check == 'yes':
		print("Balance Amount: Rs. ", Bank_Balance + bal_check - 10)
	elif bal_check == ' ':
		pass
	else:
		print("Enter the valid choice...")

def curr_bal_enq(Ac_No, Bank_Balance):			# Balance Enquirey --> Current Account
	print("Bank Balance is. Rs. ", Bank_Balance - 10)

# main body
print("Hello! Welcome to HJ bank...")
Ac_No = int(input("Enter last 4 digits of your ATM card: XXXX XXXX XXXX "))
Bank_Balance = 40000							# Already fixed the Bank_Balance
pin = int(input("Enter you Personal Identification Number (PIN): "))
if pin == 1234:									# Pin is fixed
	account_type = int(input("Select the appropriate option: \n\t1) Savings; \n\t2) Current\n"))
	if account_type == 1:
		savings(Ac_No, Bank_Balance)
	elif account_type == 2: 
		current(Ac_No, Bank_Balance)
	else: 
		print("Please select the valid option...")
else:
	print("Yupps! Please enter a vaild Pin...")
