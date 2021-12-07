array = np.array(list)

## jetzt schauen wieviele Fische haben 7 Tage, 6 Tage -> und 256 + 0,1,2,3 anpassen
#wieviele 5er etc.
## i und j stehen für die anzahl der 7 bzw 9er fische
summe_binom = 0
finale = 0
for u in array:
    i = 0
    #summe_binom = 0
    for j in range(40):
        ## wir schauen wieviele Kombinationen mit fixer 9er Fischen und auf 256 aufgefüllten 7ern es gibt
        ## deswegen i -> das läuft hoch bis 256 voll ist

        while (256 - u+1 - (abs(9*(28 - j)) + 7*i)) >= 7:
            i = i+1 # 
        #print(f'i:{i} and j: {28-j}')
        #print((28-j)*9+i*7)
        #print(binom(i+28-j,i))
        summe_binom = summe_binom + binom(i+28-j,i)
    print(summe_binom)
    finale = finale + summe_binom
    
(26984457539 - finale)
