import time
numbers = []
def add():
  outcome = 0
  for items in numbers:
    outcome = items + outcome

  return outcome
def Add_Numbers():
  numbers.append(int(input("What number would you like to add: ")))
def Remove_Numbers():
  numbers.remove(int(input("What number would you like to remove: ")))
def Divide():
  return numbers[0] / numbers [1]
def multiply():
  outcome = 1
  for items in numbers:
    outcome = outcome * items
  return outcome
def display():
  for items in numbers:
    print(items)
    time.sleep(1)
while True:
  
  menu = input("Menu:\n1.Add\n2.Divide\n3.Multiply\n4.Add numbers\n5.Remove numbers\n6.display current numbers in list\n7.Exit\n>")
  if menu == "1":
    print(add())
    time.sleep(1)
  elif menu == "2":
    print(Divide())
    time.sleep(1)
  elif menu == "3":
    print(multiply())
    time.sleep(1)
  elif menu == "4":
    Add_Numbers()
  elif menu == "5":
    print(Remove_Numbers())
  elif menu == "6":
    print(display())
  elif menu == "7":
    break