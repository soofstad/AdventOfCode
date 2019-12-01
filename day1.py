with open("input-day1") as file:
    print(sum([int((int(mass)/3))-2 for mass in file]))
