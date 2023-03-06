import csv

def main_menu():
    rate = None
    while True:
        print("ACME(tm) US DOLLAR EXCHANGE RATE APP")
        print("1) LOAD currency exchange rate data from a file")
        print("2) USE AVERAGE exchange rate")
        print("3) USE HIGHEST exchange rate")
        print("4) USE LOWEST exchange rate")
        print("5) CONVERT USD TO EUR")
        print("6) CONVERT USD TO AUD")
        print("7) CONVERT USD TO GBP")
        print("0) QUIT program")
        choice = int(input("Choose what to do: "))
        if choice == 1:
            file = input("Give name of the data file: ")
            load_data(file)
        elif choice == 2:
            rate = use_average(file)
            print("Using the average currency exchange rate.\n")
        elif choice == 3:
            rate = use_highest(file)
            print("Using the highest currency exchange rate.\n")
        elif choice == 4:
            rate = use_lowest(file)
            print("Using the lowest currency exchange rate.\n")
        elif choice == 5:
            convert_usd_to_eur(file, rate)
        elif choice == 6:
            convert_usd_to_aud(file, rate)
        elif choice == 7:
            convert_usd_to_gbp(file, rate)
        elif choice == 0:
            quit()
        else:
            print("Invalid choice, please try again.")
            main_menu()

def load_data(file):
    date_list = []
    count = 0
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            date = row["DATE"]
            count = count + 1
            if date != "":
                date_list.append(date)
                fi_date = date_list[0]
                las_date = date_list[-1]
    print("Data loaded successfully!")
    print("Currency exchange data is from", count, "days between", fi_date, "and", las_date + ".\n")

def use_average(file):
    eur = []
    aud = []
    gbp = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if row["USD-EUR"] != "":
                eur.append(float(row["USD-EUR"]))
                average_eur = sum(eur) / len(eur)

            if row["USD-AUD"] != "":
                aud.append(float(row["USD-AUD"]))
                average_aud = sum(aud) / len(aud)

            if row["USD-GBP"] != "":
                gbp.append(float(row["USD-GBP"]))
                average_gbp = sum(gbp) / len(gbp)
    return average_eur, average_aud, average_gbp

def use_highest(file):
    eur = []
    aud = []
    gbp = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if row["USD-EUR"] != "":
                eur.append(float(row["USD-EUR"]))
                highest_eur = max(eur)

            if row["USD-AUD"] != "":
                aud.append(float(row["USD-AUD"]))
                highest_aud = max(aud)

            if row["USD-GBP"] != "":
                gbp.append(float(row["USD-GBP"]))
                highest_gbp = max(gbp)
    return highest_eur, highest_aud, highest_gbp

def use_lowest(file):
    eur = []
    aud = []
    gbp = []
    with open(file, "r") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if row["USD-EUR"] != "":
                eur.append(float(row["USD-EUR"]))
                lowest_eur = min(eur)

            if row["USD-AUD"] != "":
                aud.append(float(row["USD-AUD"]))
                lowest_aud = min(aud)

            if row["USD-GBP"] != "":
                gbp.append(float(row["USD-GBP"]))
                lowest_gbp = min(gbp)
    return lowest_eur, lowest_aud, lowest_gbp

def convert_usd_to_eur(file, rate):
    average_eur, _, _ = use_average(file)
    if rate is None:
        amount = float(input("Give USD to convert: "))
        result = amount * average_eur
        print(amount, "USD in EUR is", round(result, 2), "EUR \n")
        return
    amount = float(input("Give USD to convert: "))
    result = amount * rate[0]
    print(amount, "USD in EUR is", round(result, 2), "EUR \n")

def convert_usd_to_aud(file, rate):
    _, average_aud, _ = use_average(file)
    if rate is None:
        amount = float(input("Give USD to convert: "))
        result = amount * average_aud
        print(amount, "USD in AUD is", round(result, 2), "AUD \n")
        return
    amount = float(input("Give USD to convert: "))
    result = amount * rate[1]
    print(amount, "USD in AUD is", round(result, 2), "AUD \n")

def convert_usd_to_gbp(file, rate):
    _, _, average_gbp = use_average(file)
    if rate is None:
        amount = float(input("Give USD to convert: "))
        result = amount * average_gbp
        print(amount, "USD in GBP is", round(result, 2), "GBP \n")
        return
    amount = float(input("Give USD to convert: "))
    result = amount * rate[2]
    print(amount, "USD in GBP is", round(result, 2), "GBP \n")

if __name__ == "__main__":
    main_menu()

