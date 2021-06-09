
# import the library that handles connections to sqlite databases
import sqlite3 
#global varaibles which are used all over the programme
money = 0 
Time = 0

# Create a function
def Risk(risk):
   with sqlite3.connect("db/stockmarket.db") as db:
    cursor = db.cursor()
    cursor.execute("select StockName,Description,Cost from stockList where Risk = '{0}'".format(risk))
    StockLow = cursor.fetchall()

	# for loop that prints using string formatting 
    for RiskLow in StockLow:
      print("{0:8}{1:30}${2:5.2f}".format(RiskLow[0],RiskLow[1],RiskLow[2]))
      

# this function collects the 
def createList():
  global money
  global Time
  while money == 0:
    try:
      money = float(input('How much money would you like to invest? \n $'))
    except ValueError:
        print ('An error occurred. \nMake sure you didnt accidentally type something that isnt a digit')

  while Time == 0:
    try:
      Time = float(input('How many years are you planning on investing? \n'))
    except ValueError:
        print ('An error occured. \nMake sure you didnt accidentally type something that isnt a digit') 

  moneyIn(money, Time)

# elif statement to print the stock recommendations 
def moneyIn(money, Time):
  if money > 500 and Time < 30 and Time > 6:
    risk='Low'
    print ('Some possible investments for you could be:')
    Risk(risk)
  elif money < 500 and money > 100 and Time > 2:
    risk='Med'
    print ('Some possible investments for you could be:')
    Risk(risk)
  elif money > 500 and Time > 2 and Time < 6:
    risk='High'
    print ('Some possible investments for you could be:')
    Risk(risk)
  else:
    risk='Other'
    print('Some possible investments for you could be:')
    Risk(risk)


createList()

