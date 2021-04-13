
# import the library that handles connections to sqlite databases
import sqlite3 

# Create a function
def LowRisk():
	with sqlite3.connect("db/stockmarket.db") as db:
		cursor = db.cursor()
		cursor.execute("select StockName,Description,Cost from stockList where Risk = 'Low' ")
		StockLow = cursor.fetchall()

	# print the entire list of medalists
	print (StockLow)

	# use a loop to print each record
	for RiskLow in StockLow:
		print(RiskLow)

def createList():

  investor_type = [ 'Agressive' 'Defensive' 'Balanced' 'Concervative' 'Growth']
  money = float(input('How much money would you like to invest? \n $'))
  Time = int(input('How many years are you planning on investing? \n'))
  moneyIn(money, Time)


def moneyIn(money, Time):
  if money > 500 and Time < 30:
    print ('Some possible investments for you could be: ' + LowRisk())
  elif money < 500 and money > 100 and Time > 2 :
    print ('middle')
  else:
      print('Some possible investments for you could be: ARB, ASD, ASF,\nAIA & AIR')

createList()

#Run the function
LowRisk()
