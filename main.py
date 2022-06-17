item = ""
price = 0
SIZE = 6
VALID_ITEMS = [106,108,307,405,457,688]
VALID_PRICES = [0.59,0.99,4.50,15.99,17.50,39.00]
badItemCount = 0
MSG_YES = "Item available"
MSG_NO = "Item not found"
FINISH = 999

item = input("Enter item number or 999 to quit. ")
item = int(item)

while item != FINISH:
  foundIt = "N"
  sub = 0
  while sub < SIZE and foundIt == "N":
    if item == VALID_ITEMS[sub]:
      foundIt = "Y"
      price = VALID_PRICES[sub]
    sub += 1
  if foundIt == "Y":
    print(MSG_YES)
    print("The price of", str(item),"is",str(price))
  else:
    print(MSG_NO)
    badItemCount += 1
  item = input("Enter next item number or 999 to quit. ")
  item = int(item)
print(str(badItemCount),"items had invalid numbers.")