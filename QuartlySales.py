def quartlySales():
    allSales = []
    for qNumber in range(4):
        quarter = round(float(input(f'Enter sales for Q{qNumber+1}:  ')),2)
        allSales.append(quarter)
    return allSales

def calcSales():
    calcs = []
    qSales = quartlySales()
    calcs.append(sum(qSales))
    avg = round(sum(qSales)/4,2)
    calcs.append(avg)
    calcs.append(max(qSales))
    calcs.append(min(qSales))
    return calcs

def main():
    print('The Quartly Sales program\n\n')
    total, avg, maxSales, minSales = calcSales()
    print(f"\n\nTotal:               {total}")
    print(f"Average Quarter:     {avg}")
    print(f"Lowest Quarter:      {minSales}")
    print(f"Highest Quarter:     {maxSales}")

if __name__ == '__main__':
    main()