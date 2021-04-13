
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

#Run the function
LowRisk()
