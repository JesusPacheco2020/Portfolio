#Restaurant Receipt
#Program presents the customer with the menu items and prices.
#The program will return the amount owed before and after taxes.

#Program greeting
print('\n\nWelcome to Elite Foods!')
print('\nType 1 or 0 to choose the dish:')

#Menu Format
print(format('\n ', '-<27'), 'Menu', format('', '-<28'))

#Getting data from user
fries = float(input('\nFrench Fries ($5.00): '))
caviar = float(input('\nCaviar Pizza ($50.00): '))
truffles = float(input('\nBurger with White Truffles ($75.00): '))
puffer_fish = float(input('\nRare dish of Puffer Fish ($50.00): '))
ice_cream = float(input('\nIce Cream with Gold Flakes ($25.00): '))

#Menu Format
print(format('\n ', '-<25'), 'Thank You', format('', '-<25'))

#Calculating total cost of items ordered
total = fries*5.00 +  caviar*50.00 + truffles*75.00 + puffer_fish*50.00 + ice_cream*25.00

#Calculating taxes owed for items
tax = total * 0.08

#Calculating final total
final_total = total + tax

#Display amount owed
print('\nTotal before tax: $', format(total, '.2f'))
print('\nTaxes owed(8%): $', format(tax, '.2f'))
print('\nTotal owed: $', format(final_total, '.2f'))
