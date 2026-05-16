## Write a program to accept an integer amount from user and tell minimum
## number of notes needed for representing that amount.

amount = int(input("Enter the Amount : "))

note_2k = amount // 2000
amount = amount % 2000

note_500 = amount // 500
amount = amount % 500

note_200 = amount // 200
amount = amount % 200

note_100 = amount // 100
amount = amount % 100

note_50 = amount // 50
amount = amount % 50

note_20 = amount // 20
amount = amount % 20

note_10 = amount // 10

print(f'''The required notes are : 
note 2000 : {note_2k}
note 500 : {note_500}
note 200 : {note_200}
note 100 : {note_100}
note 50 : {note_50}
note 20 : {note_20}
note 10 : {note_10}'''  )
