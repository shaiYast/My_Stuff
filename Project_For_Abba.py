import csv

#For Excel version
# with open("Samples.csv", 'r+', ) as csvfile:
#     accounts = csv.reader(csvfile, delimiter='\t')
#     next(accounts)
#     print(accounts.)
#     # for line in accounts:
#     #     print(line)
#     # csvfile.close()
#     # print(line[1].type())
#     with open("Samples2.csv", 'w', ) as newfile:
#         accounts2 = csv.writer(newfile, delimiter='\t')
#         for line in accounts:
#             accounts2.writerow((line,line[1]))

#new change added

# person = ("John", 100, False, "New_York")
# if person[2]:
#     print(person[1]*.1)
# else:
#     print(person[1]*.05)
def Federaltax(person):
    if person[2]:
        if person[1] <= 19400:
            return person[1] * .1
        elif person[1] <= 78950:
            return (person[1] - 19400) * .12 + 1940
        elif person[1] <= 168400:
            return (person[1] - 78950) * .22 + 9086
        elif person[1] <= 321450:
            return (person[1] - 168400) * .24 + 28765
        elif person[1] <= 408200:
            return (person[1] - 321450) * .32 + 65497
        elif person[1] <= 612350:
            return (person[1] - 408200) * .35 + 93257
        else:
            return (person[1] - 612350) * .37 + 164710
    else:
        if person[1] <= 9700:
            return person[1]  * .1
        elif person[1] <= 39475:
            return (person[1] - 9700) * .12 + 970
        elif person[1] <= 84200:
            return (person[1] - 39475) * .22 + 4543
        elif person[1] <= 160725:
            return (person[1] - 74200) * .24 + 14383
        elif person[1] <= 204100:
            return (person[1] - 160725) * .32 + 32749
        elif person[1] <= 510300:
            return (person[1] - 204100) * .35 + 46629
        else:
            return (person[1] - 510300) * .37 + 153799
def statetax(person):
    if person[3] == "NY":
        if person[2]:
            if person[1] <= 17150:
                return person[1] * .04
            elif person[1] <= 23600:
                return (person[1] - 17150) * .045 +686
            elif person[1] <= 27900:
                return (person[1] - 23600) * .0525 + 976
            elif person[1] <= 43000:
                return (person[1] - 27900) * .059 + 1202
            elif person[1] <= 161550:
                return (person[1] - 43000) * .0621 + 2093
            elif person[1] <= 323200:
                return (person[1] - 161550) * .0649 + 9455
            else:
                return (person[1] - 323200) * .0685 + 19946
        else:
            if person[1] <= 8500:
                return person[1] * .04
            elif person[1] <= 11700:
                return (person[1] - 8500) * .045 + 340
            elif person[1] <= 13900:
                return (person[1] - 11700) * .0525 + 484
            elif person[1] <= 21400:
                return (person[1] - 13900) * .059 + 600
            elif person[1] <= 80650:
                return (person[1] - 21400) * .0621 + 1043
            elif person[1] <= 215400:
                return (person[1] - 80650) * .0649 + 4722
            else:
                return (person[1] - 215400) * .0685 + 13467
    elif person[3] == "NJ":
        if person[2]:
            if person[1] <= 20000:
                return person[1] * .014
            elif person[1] <= 50000:
                return (person[1] - 20000) * .0175 + 280
            elif person[1] <= 70000:
                return (person[1] - 50000) * .0245 + 805
            elif person[1] <= 80000:
                return (person[1] - 70000) * .035 + 1295
            elif person[1] <= 150000:
                return (person[1] - 80000) * .0553 + 1645
            elif person[1] <= 500000:
                return (person[1] - 150000) * .0637 + 5513
            elif person[1] <= 5000000:
                return (person[1] - 500000) * .0897 + 27808
            else:
                return (person[1] - 5000000) * .1075 + 431458
        else:
            if person[1] <= 20000:
                return person[1] * .014
            elif person[1] <= 35000:
                return (person[1] - 20000) * .0175 + 280
            elif person[1] <= 40000:
                return (person[1] - 35000) * .035 + 543
            elif person[1] <= 75000:
                return (person[1] - 40000) * .0553 + 718
            elif person[1] <= 500000:
                return (person[1] - 75000) * .0637 + 2652
            elif person[1] <= 5000000:
                return (person[1] - 500000) * .0897 + 29725
            else:
                return (person[1] - 5000000) * .1075 + 433375
    elif person[3] == "CT":
        if person[2]:
            if person[1] <= 20000:
                return person[1] * .03
            elif person[1] <= 100000:
                return (person[1] - 20000) * .05 + 600
            elif person[1] <= 200000:
                return (person[1] - 100000) * .055 + 4600
            elif person[1] <= 400000:
                return (person[1] - 200000) * .06 + 10100
            elif person[1] <= 500000:
                return (person[1] - 800000) * .065 + 22100
            elif person[1] <= 1000000:
                return (person[1] - 500000) * .069 + 28600
            else:
                return (person[1] - 1000000) * .0699 + 63100
        else:
            if person[1] <= 10000:
                return person[1] * .03
            elif person[1] <= 50000:
                return (person[1] - 10000) * .05 + 300
            elif person[1] <= 100000:
                return (person[1] - 50000) * .055 + 2300
            elif person[1] <= 200000:
                return (person[1] - 100000) * .06 + 5050
            elif person[1] <= 250000:
                return (person[1] - 200000) * .065 + 11050
            elif person[1] <= 500000:
                return (person[1] - 250000) * .069 + 14300
            else:
                return (person[1] - 500000) * .0699 + 31550
    else: return None
def citytax(person):
    if person[4] == "New York":
        if person[2]:
            if person[1] <= 21600:
                return person[1] * .03078
            elif person[1] <=45000:
                return (person[1]-21600) *.03762 + 665
            elif person[1] <=90000:
                return (person[1]-45000) *.03819 + 1545
            else:
                return (person [1]-90000 )*.03876 + 3264
        else:
            if person[1] <=12000:
                return person[1] *.03078
            elif person[1] <=25000:
                return (person[1] - 12000) *.03762 + 369
            elif person[1] <=50000:
                return (person[1] -25000) * .03819 + 858
            else:
                return (person[1] - 1813) * .03876
    else:
        return None

print("Thank you for using this program.\nWe are going to create a CSV file for you clients.")
# numclients = int(input("First, tell me how many clients you would like to enter."))
# with open("Samples2.csv", 'w', ) as newfile:
#     accounts2 = csv.writer(newfile, delimiter='\t')
#     accounts2.writerow(["Name","Income","Federal Tax", "State Tax", "City Tax"])
#     for n in range(0,numclients):
presentperson = (input("Please enter the client's name\n"), int(input("Please enter the client's income\n")), input("Please write 1 if they are married and 0 if they aren't\n"), input("Please write their state's initials\n"), input("Please write their city\n"))
print(presentperson[0] + "'s Federal Income Tax is {}.".format(Federaltax(presentperson)))
print(presentperson[0] + "'s State Income Tax is {}.".format(statetax(presentperson)))
print(presentperson[0] + "'s City Income Tax is {}.".format(citytax(presentperson)))
input("Press enter to exit")


