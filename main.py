pin = 1234
balance = 28.07

print("Welcome to the ATM")
userinput = int(input("Type in your PIN: "))
if pin != userinput:
  print("Incorrect PIN, try again!")
  exit()
else:
  print("Correct Pin")

print("Here are your options:")
print("Select 1 to display Balance")
print("Select 2 to Withdraw")
print("Select 3 to deposit")
print("Select 9 to return card")
 
findbalance = 1
withdraw = 2
deposit = 3
returncard = 9
action = int(input("Select your next action: "))
if action == findbalance:
   print("Your balance is £28.07")
elif action == withdraw:
   print("How much would you like do withdraw?\n £10\n £20\n £40\n £60\n £80")
   withdraw = int(input("Your balance is £28.07\n Select the amount to withdraw: "))
   if withdraw == 10:
     print("You have withdrawn £10, Your new balance is £18.07")
   if withdraw == 20:
      print("You have withdrawn £20, Your new balance is £8.07")
   if withdraw == 40:
      print("You don't have enough!")
   if withdraw == 60:
      print("You don't have enough!")
   if withdraw == 80:
      print("You don't have enough!")
   

elif action == deposit:
   print("How much would you like to deposit?")
   print("How much would you like do deposit?\n £10\n £20\n £40\n £60\n £80")
   deposit = int(input("Select the amount you would like to withdraw: "))
   if deposit == 10:
     print("You have deposited £10, Your new balance is £38.07")
   if deposit == 20:
      print("You have deposited £20, Your new balance is £48.07")
   if deposit == 40:
      print("You have deposited £40, Your new balance is £68.07")
   if deposit == 60:
      print("You have deposited £60, Your new balance is £88.07")
   if deposit == 80:
      print("You have deposited £80, Your new balance is £108.07")

elif action == returncard:
   print("Returning Card, Goodbye!")
  
