def linear_search(myItem,myList):
    found = False 	# Set Found variable to False by default
    position = 0 	# the starting point in the list
    while position < len(myList) and not found:
        if myList[position] == myItem:
            found = True
        position = position + 1
    return found


def createList():

  low_stocks = ['FPH' 'ANZ' 'AFI' 'FSF' 'MEL']
  medium_stocks = ['WBC' 'TLS' 'AIR' 'AIA' 'SPK']
  high_stocks = ['CBD' 'FBU' 'SKC' 'KMD' 'GEO']
 
  stocks = [["fph", "low"],["ata", "medium"]]

  print (stocks)

  print (stocks[1])

  item = input("Which item would you like to look for? ")

  item_lower = item.lower() # this variable is used to change the input to lowercase before the search

  isitfound = linear_search(item_lower,stocks)

  if isitfound:
    print("Your item is in the list")
  else:
    print("Your item is not in the list")


  investor_type = ['Agressive' 'Defensive' 'Balanced' 'Concervative' 'Growth']
  money = float(input('How much money would you like to invest? \n $'))

  Time = int(input('How many years are you planning on investing? \n'))
  moneyIn(money, Time)

low_stocks = ['FPH', 'ANZ', 'AFI', 'FSF', 'MEL']

medium_stocks = ['WBC', 'TLS', 'AIR', 'AIA', 'SPK']
  
high_stocks = [ 'CBD', 'FBU', 'SKC', 'KMD', 'GEO' ]

my_portfolio = [ ]

def moneyIn(money, Time):
  if money > 500 and Time < 30:
    print ("some possible investments for you could be:" + str(high_stocks))
  elif money < 500 and money > 100 and Time > 2 :
    print ("some possible investments for you could be:" + str(medium_stocks))
  else:
      print ("some possible investments for you could be:" + str(low_stocks))

createList()


 
