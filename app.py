
low_stocks = ['FPH', 'ANZ', 'AFI', 'FSF', 'MEL']

medium_stocks = ['WBC', 'TLS', 'AIR', 'AIA', 'SPK']
  
high_stocks = [ 'CBD', 'FBU', 'SKC', 'KMD', 'GEO' ]

my_portfolio = [ ]

def createList():

  investor_type = ['Agressive' 'Defensive' 'Balanced' 'Concervative' 'Growth']
  money = float(input('How much money would you like to invest? \n $'))

  Time = int(input('How many years are you planning on investing? \n'))
  moneyIn(money, Time)


def moneyIn(money, Time):
  if money > 500 and Time < 30:
    print ("some possible investments for you could be:" + str(high_stocks))
  elif money < 500 and money > 100 and Time > 2 :
    print ("some possible investments for you could be:" + str(medium_stocks))
  else:
      print ("some possible investments for you could be:" + str(low_stocks))

createList()
