# Write code below 💖
PESO_TO_USD = 0.00025    # Colombian peso
SOLE_TO_USD = 0.27       # Peruvian sol
REAL_TO_USD = 0.20       # Brazilian real
pesos = int(input("What do you have left in pesos?"))
soles = int(input("What do you have left in soles?"))
reais = int(input("What do you have left in reais?"))
total_usd = pesos * PESO_TO_USD + soles * SOLE_TO_USD + reais * REAL_TO_USD
print(total_usd,"USD")