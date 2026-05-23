## Accept age of five people and also per person ticket amount and then calculate total
## amount to ticket to travel for all of them based on following condition :
## a. Children below 12 = 30% discount
## b. Senior citizen (above 59) = 50% discount
## c. Others need to pay full.

P1 = int(input('enter age : '))
P2 = int(input('enter age : '))
P3 = int(input('enter age : '))
P4 = int(input('enter age : '))
P5 = int(input('enter age : '))

amount = int(input('Ticket price is : '))

total_price = 0

if P1 < 12:
    total_price = total_price + (amount - (amount * 0.3))
elif P1 > 59:
    total_price = total_price + (amount - (amount * 0.5))
else:
    total_price = total_price + amount
    
if P2 < 12:
    total_price = total_price + (amount - (amount * 0.3))
elif P2 > 59:
    total_price = total_price + (amount - (amount * 0.5))
else:
    total_price = total_price + amount

if P3 < 12:
    total_price = total_price + (amount - (amount * 0.3))
elif P3 > 59:
    total_price = total_price + (amount - (amount * 0.5))
else:
    total_price = total_price + amount

if P4 < 12:
    total_price = total_price + (amount - (amount * 0.3))
elif P4 > 59:
    total_price = total_price + (amount - (amount * 0.5))
else:
    total_price = total_price + amount

if P5 < 12:
    total_price = total_price + (amount - (amount * 0.3))
elif  P5 > 59:
    total_price = total_price + (amount - (amount * 0.5))
else:
    total_price = total_price + amount

print(f'total amount is {total_price} rs')    











            
      
      
      
      
            




