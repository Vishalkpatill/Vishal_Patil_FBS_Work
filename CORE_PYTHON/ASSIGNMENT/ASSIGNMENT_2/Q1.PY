## Convert the time entered in hh,min and sec into seconds.

hrs = int(input("Enter the time in hrs : "))

min = int(input("Enter the time in min : "))

sec = int(input("Enter the time in sec : "))\

total_second = ((hrs * 3600 ) + (min * 60) + sec)

print(f'Total sec are {total_second}.')