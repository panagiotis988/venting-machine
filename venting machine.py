#Έδω ξεκινάει το α ερώτημα της 4ς υποεργασίας

drink = ['coffee', 'coffeMilk', 'choco', 'chocoMilk']
drinkPrice = [1.50, 1.80, 2.10, 2.40]
money = [0.1, 0.2, 0.5, 1, 2, 5, 10]
changeValue =['δεκάλεπτα:','εικοσάλεπτα:','πενηντάλεπτα:','μονόευρα:','δίευρα:']
print('Δίνονται οι παρακάτω επολογές:')
print('1. Καφές: ', drinkPrice[0], 'ευρώ')
print('2. Καφές με γάλα: ', drinkPrice[1], 'ευρώ')
print('3. Σοκολάτα: ', drinkPrice[2], 'ευρώ')
print('4. Σοκολάτα με γάλα: ', drinkPrice[3], 'ευρώ')
print('0. Έξοδος')
breaker = True
userPay = 0

sum = 0
change = 0
i=0
while breaker:
    try:
        userInput = int(input('Παρακαλώ εισάγετε την επιλογή σας (1-4) ή πατήστε 0 για έξοδο:'))
        if 0 <= userInput < 5:
            if userInput == 0:
                print('εξοδος')
                break

    #Εδώ ξεκινάει το β ερώτημα

            print(drinkPrice[userInput - 1])
            if userPay < drinkPrice[userInput - 1]:
                while sum < drinkPrice[userInput - 1]:
                    drinkPricerReminder = round(drinkPrice[userInput - 1] - sum,1)
                    try:
                        print('Πρέπει να εισάγετε ', drinkPricerReminder, 'ευρώ συνολικά')
                        userPay = float(input('Πόσα εισάγατε;'))

    #Εδω ξεκινάει το γ ερώτημα και παρακάτω εμφανίζει τα ρέστα

                        if userPay in money:
                            sum = userPay + sum
                            change = round((sum - drinkPrice[userInput - 1]),1)
                            breaker=False
                        else:
                            print('ΣΦΑΛΜΑ: εισαγωγή μη έγκυρου ποσού.')
                            print('Παρακαλώ εισάγετε μια έγκυρη τίμη:', money)
                    except:
                        print('Έγραψες λάθος')
            money.reverse()
            changeValue.reverse()
            sum=0
            print("Επιστροφή:", change)
            print("Παρακαλώ πάρτε:")

    #Εδώ ξεκινάει το δ ερώτημα της υποεργασiας

            for value in money[2:]:
                if change >= value:
                    sum=change//value
                    change = round(change - sum * value, 1)
                    print(changeValue[i],':',int(sum))
                i = i + 1
        else:
            print('Έδωσες λάθος είσοδο')
    except:
        print('Έγραψες λάθος')
