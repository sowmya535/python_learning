# generating a random password
import random
string = "abcdefghijk@1234#$%"
n = int(input("Enter a length of password: "))
password =" "
for i in range(n):
    password += random.choice(string)
print(f'your password of length {n} is : {password}')


# stepts for atm tracker
import getpass
balance = 0 
p1 = int(getpass.getpass('Set the pin:  '))
if len(str(p1)) != 4:
    print('Pin should be exactly 4 digits')
    exit()
p2 = int(getpass.getpass('Re enter the pin:  '))
if p1 != p2:
    print('Pins are not matching.')
    exit() 
pin = p2 
while True:
    print('-----------------------------------------------')
    print('1. Balance Enquiry')
    print('2. Deposit Amount')
    print('3. Withdraw Amount')
    print('4. Exit')
    n = int(input('Enter the option:  ')) 
    match n:
        case 1:
            p = int(getpass.getpass('Please enter your pin:  '))
            if p != pin:
                print('Entered pin is incorrect')
                continue 
            print(f'Balance is {balance}') 
        case 2: 
            p = int(getpass.getpass('Please enter your pin:  '))
            if p != pin:
                print('Entered pin is incorrect')
                continue 
            amount = int(input('Please enter the amount to deposit:  '))
            balance += amount 
            print(f'Amount deposited succesfully. Balance is {balance}')
        case 3:
            p = int(getpass.getpass('Please enter your pin:  '))
            if p != pin:
                print('Entered pin is incorrect')
                continue 
            amount = int(input('Please enter the amount to withdraw:  '))
            if amount > balance:
                print('Insufficient balance.')
                continue
            balance -= amount 
            print(f'Amount withdrawn successfully. Balance is {balance}')
        case 4: 
            break
