class Mpesa account:
	def__init__(self,name,number,balance):
		self.name = name
		self.number = number
		self.balance = balance

	def deposit(self,d):
		deposit = d
		self.balance = self.balance + d
		sms1 = "Hello {},confirmed you have deposited {} kshs in your account.Your new Mpesa balance is{},kshs".format(self.name,d,self.balance)
		print(sms1)

	def withdraw(self,e):
		e<self.balance
		self.balance = self.balance - e
		sms2 = "Hello {},confirmed your withdrawal of {}kshs is successful.Your new mpesa balance is {}kshs".format(self.name,e,self.balance)
		print(sms2)

	def balance(self):
			sms3 = "Hello {}, your current balance is{},".format(self.name,self.balance)
			print(sms3)