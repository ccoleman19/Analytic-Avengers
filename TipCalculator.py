def getCost():
    while True:
        try:
            cost = float(input('Cost of meal: '))
            cost = round(cost,2)
            if cost < 0:
                print('Must be greater than 0. Please try again')
            else:
                return cost
        except ValueError:
            print('Must be valid decimal number.  Please try again.')    

def getTipPct():
    while True:
        try:
            tipPct = int(input('Tip Percent: '))
            if tipPct < 0:
                print('Must be greater than 0. Please try again')
            else:
                return tipPct
        except ValueError:
            print('Must be valid integer.  Please try again.') 

def calcTip(cost, tipPct):
    tip = round(cost * (tipPct/100),2)
    return tip

def main():

    print('Tip Calculator\n\n')
    print('INPUT')
    cost = getCost()
    tipPct = getTipPct()
    tip = calcTip(cost,tipPct)
    total = cost + tip
    print('\nOUTPUT\n')
    print(f'Cost of meal:   {cost}')
    print(f'Tip percent:    {tipPct}%')
    print(f'Tip amount:     {tip}')
    print(f'Total amount:   {total}')

if __name__ == '__main__':
    main()