#Base 10 to Binary Program
#Program will convert an integer number between 0 and 31 to its binary format.


#Initialization
bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0
bit5 = 0

#Program greeting
print('\nThis program will translate a number (0-31) to its binary format.')

#Get number from user
num = int(input('\nEnter integer number(0-31): '))

#Calculating the binary format
if (num - 16) >= 0:         #If the number is greater than or equal to 16,
    bit5 = 1                #Then bit5 is activated.
    num = num - 16
    #print('num: ', num)    #Test remaining number for accuracy

if (num - 8) >= 0:          #If the remaining number is greater than or equal to 8,
    bit4 = 1                #Then bit4 is activated.
    num = num - 8
    #print('num: ', num)    #Test remaining number for accuracy
        
if (num - 4) >= 0:          #If the remaining number is greater than or equal to 4,
    bit3 = 1                #Then bit3 is activated.
    num = num - 4
    #print('num: ', num)    #Test remaining number for accuracy

if (num - 2) >= 0:          #If the remaining number is greater than or equal to 2,
    bit2 = 1                #Then bit2 is activated.
    num = num - 2
    #print('num: ', num)    #Test remaining number for accuracy

if (num - 1) >= 0:          #If the remaining number is greater than or equal to 1,
    bit1 = 1                #Then bit1 is activated.
    num = num - 1
    #print('num: ', num)    #Test remaining number for accuracy

#Display binary format of the number entered by user.
print('\nNumber in binary format is:', bit5, bit4, bit3, bit2, bit1)
