print("\n","\n","-------++++++++++++..........Welcome to AVK Bank..........++++++++++++-------","\n","\t")
pin= [1234]
amount = [0]
mbl = ["0987654321"]

def pin2():
	print("\n")
	a = int(input("Enter your PIN number :  "))
	for b in pin:
		if a == b:
			home()
		else:
			print("\n","\t","Please enter a valid pin number","\n")
			pin2()

def inp(s):
	
	if s == "1":
		print("\n")
		bi()
	elif s == "2":
		print("\n")
		cw()
	elif s == "3":
		print("\n")
		dm()
	elif s == "4":
		print("\n")
		cp()
	elif s == "5":
		print("\n")
		cmn()
	else:
		print("\n")
		print("Please select a valid option")

def home():
	print("\n","\t","1. Balance Inquiry")
	print("\n","\t","2. Cash Withdrawal")
	print("\n","\t","3. Deposite Money")
	print("\n","\t","4. Change Pin")
	print("\n","\t","5. Change Mobile Number","\n")

	a = input("please select the option : ")
	inp(a)	

def bi():
	print("\n","\t","Account balance is : ",amount[0])
	exit()

def dm():
	a = int(input("Enter the amount to Deposite : "))
	for m in amount:
		m=m+a
	del amount[0]
	amount.append(m)
	for n in amount:
		print("\n","\t","Deposited Money : ",n)
	exit()

def cw():
	a = int(input("Enter the amount to Withdraw : "))
	for b in amount:
		if b > a:
			for m in amount:
				m=m-a
			del amount[0]
			amount.append(m)
			for n in amount:
				print("\n","\t","Current balance : ",n)
		else:
			print("\n","\t","Insufficient Balance")
	exit()

def cp():
	print("\n")
	pi = int(input("Enter new pin to update : "))
	del pin[0]
	pin.append(pi)
	for p in pin:
		print("\n","\t","Your new pin is : ",p,"\n","\t")
	pin2()
	

def cmn():
	print("\n")
	pn = input("Enter mobile number to update : ")
	if len(pn)==10:
		for m in mbl:
			print("\n","\t","Your old mobile number is : ",m)
			del mbl[0]
			mbl.append(pn)
		for n in mbl:
			print("\n","\t","Your updated mobile number is : ",n)
			exit()
	else:
		print("\n")
		print("please enter a valid mobile number..!!")
		cmn()

	
def exit():
	print("\n")
	ex = input("End session ( y / n ) : ")
	if ex == "y":
		print("")
	else:
		print("\n")
		home()


pin2()

