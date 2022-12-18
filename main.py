#Dimitrios Passias 
#No Issues and there is nothing needed to run this
#This program displays a menu to the user and uses recursive functions to attempt the given tasks to the user


#Prints the menu for the choices
def print_menu():
 print('========Please selection from the following:========')
 print("[1] Calculate Compounding interest")
 print("[2] Recursive list reversal")
 print("[3] Recursive Triangle")
 print("====================================================")

#Applies the choice number given to the choice
def process_choice(number):

 if int(number) == 1:
  #asks for the amount, interest rate, and years
  init_amount = int(input("Enter the Initial Amount of Money:"))
  interest_rate = float(input("Enter the Interest Rate:"))
  years = int(input("Enter the Amount of Years:"))
  compounding_interest(init_amount, interest_rate, years)

 #asks the user for the file and opens it to read to recursive list
 if int(number) == 2:
  user_selection = input("Enter the filename of your choice:")
  open_file = open(f"{user_selection}", 'r')
  read_file = open_file.readlines()
  recursive_lists(read_file)

#asks for size of the triangle for recursive triangle
 if int(number) == 3:
  user_selection = int(input("Enter the size of the triangle:"))
  recursive_triangle(user_selection)

 #reprints menu
 else:
  print_menu()
  user_selection = input("Enter the number of your choice:")
  process_choice(user_selection)
  return

def compounding_interest(init_amount, interest_rate, years):
 # Base / prints the total amount of money after the years
 if years == 0:
  print (f"Total Amount of Money: {init_amount}")
  return None
 #Recursive /replaces the previous initial amount with the previous year
 else:
  return(compounding_interest(init_amount+init_amount*interest_rate/100,interest_rate,years-1))

def recursive_triangle(user_selection):
 #If its the last number/no numbers it ends the recursion / base function
 if user_selection == 0:
  return None
 #Prints the amount length the user wants then recalls / recursive function
 if user_selection > 0:
  print("#" * user_selection)
  recursive_triangle(user_selection-1)

def recursive_lists(file):
 #base
 if(len(file)==1):
  return file
 #Recursive
 print[file[-1]] + recursive_lists(file[:-1])


#main function for the print menu and sends the user to the user selection
def main():
 print_menu()
 user_selection = input("Enter the number of your choice:")
 process_choice(user_selection)

main()