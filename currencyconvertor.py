with open('Currency.txt') as f:
    currencies=f.readlines()

dict={}
for currency_data in currencies:
    parsed_data=currency_data.split('\t')
    dict[parsed_data[0]]=parsed_data[1]

print(dict) 

amount=int(input("Enter amount to convert:"))
curr=input("Enter currency to convert:")
print(f"{amount} USD = {amount * float(dict[curr])} {curr}")

