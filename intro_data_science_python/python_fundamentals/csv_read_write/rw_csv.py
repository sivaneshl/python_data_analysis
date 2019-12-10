import csv
from csv import DictReader

# %precision 2

# use csv.DictReader to read the data from the csv file
# this will give a dict for each row in the csv file
# mpg_dict_list is a list of dicts for each row in the csv file
from typing import Any, Union

with open('C:/python_data_analysis/python_fundamentals/resources/course1_downloads/mpg.csv') as csvfile:
    mpg_dict_list = list(csv.DictReader(csvfile))

# print the list
print(mpg_dict_list)
# nbr of rows
print(len(mpg_dict_list))
# print the column labels
print(mpg_dict_list[0].keys())

# find the average city mpg for all cars in the file
sum_cty_mpg = 0.0
for car in mpg_dict_list:
    sum_cty_mpg = sum_cty_mpg + float(car['cty'])
print(sum_cty_mpg / len(mpg_dict_list))
# round to 2 decimals using %
print('%.2f' % (sum_cty_mpg / len(mpg_dict_list)))
# round to 2 decimals using {}
print("{0:.2f}".format(sum_cty_mpg / len(mpg_dict_list)))

# same can be written simplified as
# also using round
print(round(sum(float(car['hwy']) for car in mpg_dict_list) / len(mpg_dict_list), 2))

# city mpg grouped by the nbr of cylinders a car has
# creating a set will give us the unique cyl values
cylinders = set(car['cyl'] for car in mpg_dict_list)
print(cylinders)
# create an empty list for the final output
city_mpg_by_cyl = []
# loop through the cylinders
for cyl in cylinders:
    sum_city_mpg = 0
    cyl_counter = 0
    # loop through the cars
    for car in mpg_dict_list:
        if car['cyl'] == cyl:
            sum_city_mpg += float(car['cty'])
            cyl_counter += 1
    city_mpg_by_cyl.append((cyl, round((sum_city_mpg / cyl_counter),2)))
print(city_mpg_by_cyl)

# city mpg grouped by the cars class
car_class = set(car['class'] for car in mpg_dict_list)
print(car_class)
city_mpg_by_class = []
for c in car_class:
    sum_city_mpg = 0
    class_counter = 0
    for car in mpg_dict_list:
        if car['class'] == c:
            sum_city_mpg += float(car['cty'])
            class_counter += 1
    city_mpg_by_class.append((c, round(sum_city_mpg / class_counter), 2))
print(city_mpg_by_class)


