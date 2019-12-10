store1 = ["12.30", "9.90", "10.80", "3.44", "20.00"]
store2 = ["11.90", "10.50", "9.50", "3.50", "20.00"]


def cheap_of_two_stores(price1, price2):
    if float(price1) <= float(price2):
        return float(price1)
    else:
        return float(price2)


print(list(map(cheap_of_two_stores, store1, store2)))