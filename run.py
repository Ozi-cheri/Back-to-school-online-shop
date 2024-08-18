list = []



print("---Back To School OnLine Shop --- ")
name = input("Please enter your name:")
print("Hello "+name)
print("Welcome To Back To School Online Shop")
print(''"*************************************")


print("1. View list")
print("2. Start shopping")
print("3. Remove item") 
print("4. Add item")
print("5. Quit shopping") 

if not list:
    print("your cart is empty")
else:
    print("list:")

    total_price = 0

choice = input("Enter your choice")
if choice == '1':
    item_name = input("Enter item name:")




list = ['pen 0.80€', 'pencil 0.49€', 'notebook 1.5€', 'backpack 13.99€', 'lunchbox 2.5€', 'calculator 1.30€', 'ruler 0.99','erasers 0.15 ', 'folders 0.10 ', 'glue 1€']

def displayList() :
    print ()
    print ("LIST")
for item in list:
    print ("* " + item)
    


