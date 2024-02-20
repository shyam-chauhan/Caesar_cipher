
def encrypt(text,key):
	'''
	Encrypts text using caesar cipher method
	:param text: text to encrypt
	:param key: key in integer to be used as shift of characters
	:return enc: encrypted text
	''' 
	flag = 0
	length = len(text) 	
	enc = '' 	
	
	for i in range(0,length):   
		temp = text[i]		
		if(temp.islower()):	
			enc += chr((((ord(temp) - (ord('a')-key))%26)+ord('a')))		
		elif(temp.isupper()):	
			enc += chr((((ord(temp) - (ord('A')-key))%26)+ord('A')))		
		elif(temp == " "):	
			enc += " "      
		else:
			print("Error!!") 	
			flag = 1		
			break			

	if(flag == 0):		
		return enc
	else:	
		pass 

def decrypt(cipher,key):
	'''
	Decrypts cipher using caesar cipher method
	:param cipher: cipher to decrypt
	:param key: key in integer to be used as shift of characters
	:return enc: encrypted text
	''' 		
	flag = 0		
	length = len(cipher)	
	dec = ''		
	for i in range(0,length):	
		temp = cipher[i]		
		if(temp.islower()):		
			dec += chr((((ord(temp) - (ord('a')+key))%26)+ord('a'))) 	
		elif(temp.isupper()):		
			dec += chr((((ord(temp) - (ord('A')+key))%26)+ord('A')))		
		elif(temp == " "):		
			dec += " "		
		else:
			print("Error!!")	
			flag = 1		
			break			
	if(flag == 0):		
		return dec		
	else:			
		pass		
	
def brute_caesar(cipher):
	'''
	Brute force attack on caesar cipher
	:param cipher: cipher to attack
	'''
	for i in range(1,26):
		print(f"With key :{i} Text is :{decrypt(cipher,i)}")


if __name__ == '__main__':	
	'''
	Main method
	'''
	choice = 1	
	while(choice !=4):		
		choice = int(input("1. For encryption \n2. For decryption \n3. For Brute force \n. For exit\n Enter your Choice :"))	
		if(choice == 1):
			text = input("Enter Text you want to encrypt: ") 
			key = int(input("Enter Key you want to use for encryption (default is 3) : ") or 3)  
			print("Encrypted text is : ",encrypt(text,key))
		elif(choice == 2):	
			cipher = input("Enter cipher you want to decrypt: ")	
			key = int(input("Enter Key you want to use for decryption default is 3 : ")or 3)	
			decrypt(cipher,key)	
			print("Decrypted text is : ",decrypt(cipher,key))
		elif(choice == 3):	
			cipher = input("Enter cipher you want to decrypt: ")	
			brute_caesar(cipher)
		elif(choice == 4):	
			print("You choose to exit")	
			exit(0)		
		else:		
			print("Wrong choice !")	