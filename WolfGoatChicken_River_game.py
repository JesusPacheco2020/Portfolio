
import random

# The following comments and some changes in the code were provided by Mr. Alexey Pogodin. 
# Code has been changed to follow these guidelines.
# All style recommendations below are based on PEP 8 (Style Guide for Python Code)
# http://www.python.org/dev/peps/pep-0008/
# Python module names should be all-lowercase.
# Global variable names should be lowercase, with words separated by underscores as necessary to improve readability.
# Always surround these binary operators with a single space on either side: assignment, augmented assignment,
# comparisons, Booleans
# whitespace after comma is required

east = ['C', 'F', 'G', 'W']
west = []
forbidden = [['C', 'G', 'W'],['C', 'G'],['G', 'W']]

#Complete the following function so it Prints the objects at East and then the objects at West===========================
def print_contains(east, west):
    print("East:")
    k = 0
    while k < len(east):
        print(east[k])
        k = k + 1

    print("\nWest:")
    k = 0
    while k < len(west):
        print(west[k])
        k = k + 1
    
    return east, west
  
#Go west: Complete this function according to the instructions on HW4
def go_west(east, west):
    if 'F' in east:
        east.remove('F')    #Farmer gets on the boat
        candidate = random.choice(east)     #Candidate is chosen
        east.remove(candidate)  #Candidate is taken across
        west.append(candidate)
        west.sort()
        if east in forbidden:   #If what was left behind is forbidden...
            while east in forbidden:   #while wrong choice is made...
                west.remove(candidate)  #Wrong candidate is taken back
                east.append(candidate)
                east.sort()
                candidate = random.choice(east) #choose another candidate
                east.remove(candidate)  #Take the other candidate across
                west.append(candidate)
                west.sort()
        west.append('F')    #Farmer stops at the West with the correct Candidate
        west.sort()
        

    print_contains(east, west)
    print('-------------------------------------\n')
    return east, west
   
    
#Go East: Complete this function according to the instructions on HW4   
def go_east(east, west):
    if 'F' in  west:
        if west.remove('F') is not forbidden: #If Farmer going east alone is allowed...
            east.append('F')    #Farmer goes east alone
            east.sort()
        else:       #If Farmer can't go back alone
            candidate = random.choice(west) #Choose a candidate
            west.remove(candidate)  #Take candidate across
            east.append(candidate)
            east.sort()
            if west in forbidden: #If what was left behind is forbidden...
                while west in forbidden:   #While wrong choice is made...
                    east.remove(candidate)  #Wrong candidate is taken back
                    west.append(candidate)
                    west.sort()
                    candidate = random.choice(west) #choose another candidate
                    west.remove(candidate)  #Take the other candidate across
                    east.append(candidate)
                    east.sort()
            east.append('F')    #Farmer stops at the East with the correct Candidate
            east.sort()

           
   
   
       
    print_contains(east, west)
    print('-------------------------------------\n')    
    return east, west
    

# Solution: This function returns True if all objects are on the West side otherwise returns False (One line of code)    
def solution():

        return west == ['C', 'F', 'G', 'W']



#DO not change anything in the following lines. Your job is to complete the functions above.
# Main

print_contains(east, west)
print('-------------------------------------')

condition = True
while condition:
    east, west = go_west(east,west)
    if not solution():
       east, west = go_east(east,west)
    else:
       condition = False
