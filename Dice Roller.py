from random import randrange
import time
import os

while True:
  
 print ("Select option:")
 print ("1. Roll Dice")
 print ("2. Exit")

 option = input()

 if option == "1":
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Rolling...")
  time.sleep(0.5)
  os.system('cls' if os.name == 'nt' else 'clear')
  print(randrange(6))
  time.sleep(1)

 elif option == "2":
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Exiting...")
  time.sleep(0.5)
  break

 else:
  os.system('cls' if os.name == 'nt' else 'clear')
  print("Invalid option")  
  time.sleep(0.5)