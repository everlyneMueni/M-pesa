class MpesaAccount:
	def __init__(self,name,number,balance):
		self.name = name
		self.number = number 
		self.balance=0
		self.deposits=[]
		self.withdrawals=[]
		self.loan=0


	def deposit(self,amount):
		self.balance = self.balance + amount
		self.deposits.append(amount)
		sms1 = "Hello {},confirmed you have deposited {} kshs in your account.Your new Mpesa balance is{},kshs".format(self.name,d,self.balance)
		print(sms1)

	def withdraw(self,amount):
	if amount<self.balance:
		self.balance = self.balance - amount
		self.withdraws.append(amount)
		sms2 = "Hello {},confirmed your withdrawal of {}kshs is successful.Your new mpesa balance is {}kshs".format(self.name,e,self.balance)
		print(sms2)

	else:
		print("insufficient balance")


	def check_balance(self):
			sms3 = "Hello {}, your current balance is{},".format(self.name,self.balance)
			print(sms3)

	def my_deposit(self):
		for r in self.deposits:
			print(r)


	def my_withdraws(self):
		for e in self.withdraws:
			print(e)


	def give_loans(self,amount):
		if len(self.deposits)>=5 and amount<1/3*sum(self.deposits) and self.loan==0:
			self.loan=self.loan+amount
			print("Hello {},you have got {}".format(self.name,amount))
		else:
			print("Hello {},you cannot get the loan".format(self.name))


	def pay_loan(self,amount):
		if self.loan==0:
			print("you cannot qualify for a loan")
		elif amount<self.loan:
			self.loan=self.loan-amount
			print("Hello {}, you have paid part of your loan,{}.your balance is{}".format(self.name,amount,self.loan))
		elif amount==self.loan:
			self.loan=self.loan-amount
			print("You have paid all your loan")

		elif amount>self.loan:
			more=amount-self.loan
			self.balance=more+self.balance
			self.loan=amount-self.loan-more
			print("Hello {} you have paid more than required amount,your new balance is{}".format(self.name,self.balance))