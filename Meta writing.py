import csv
with open("Tax Rates.xlsx", 'r', ) as csvfile:
    rates = csv.reader(csvfile, delimiter='\t')
    rates.next()

    for line in rates:
        print(line)