
# import the library that handles connections to sqlite databases
import sqlite3 

# Create a function
def Risk(risk):
  print("select StockName,Description,Cost from stockList where Risk = '{0}' ".format(risk))
  with sqlite3.connect("db/stockmarket.db") as db:
    cursor = db.cursor()
    print("Cursor set")
    cursor.execute("select StockName,Description,Cost from stockList where Risk = '{0}'".format(risk))
    print("select StockName,Description,Cost from stockList where Risk = '{0}'".format(risk))
    StockLow = cursor.fetchall()
    print(StockLow)

	# use a loop to print each record
    for RiskLow in StockLow:
      print(RiskLow)

def createList():

  money = int(input('How much money would you like to invest? \n $'))
  Time = int(input('How many years are you planning on investing? \n'))
  moneyIn(money, Time)


def moneyIn(money, Time):
  print (money)
  #print (Time)
  if money == 2:
    risk='Low'
    print ('Some possible investments for you could be:')
    Risk(risk)
  elif money == 3:
    risk='Med'
    print ('Some possible investments for you could be:')
    Risk(risk)
  elif money == 4:
    risk='High'
    print ('Some possible investments for you could be:')
    Risk(risk)
  elif money == 5:
    risk='Other'
    print('Some possible investments for you could be:')
    Risk(risk)


createList()

