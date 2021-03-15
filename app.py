def createList():

  stocks = [ 'FPH' 'AIA' 'SPK' 'ATM' 'MEl' 'RYM' 'MFT' 'FBU' 'IFT' 'CEN' 'MCY' 'EBO' 'CNU' 'SUM' 'GMT' 'SKC' 'POT' 'KPG' 'GNE' 'FRE' 'PCT' 'PPH' 'ZEL']

  investor_type = [ 'Agressive' 'Defensive' 'Balanced' 'Concervative' 'Growth']
  money = float(input('How much money would you like to invest? \n $'))
  Time = int(input('How many years are you planning on investing? \n'))
  moneyIn(money, Time)


def moneyIn(money, Time):
  if money > 500 and Time < 30:
    print ('Some possible investments for you could be:ANZ, AIR, AKL,\nAPL & ASF')
  elif money < 500 and money > 100 and Time > 2 :
    print ('middle')
  else:
      print('Some possible investments for you could be: ARB, ASD, ASF,\nAIA & AIR')

createList()
