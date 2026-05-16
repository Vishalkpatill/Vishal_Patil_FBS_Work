## WAP to calculate selling price of book based on cost price and discount.

CP = int(input("Enter cost price of book : "))
discount = int(input("Enter discount : "))

dis_per = discount / 100 * CP

SP = CP - dis_per

print(f'Selling price of book is {SP} rs.')