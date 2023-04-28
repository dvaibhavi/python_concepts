a = "test"
print(a.lower(), a.upper())

my_dict1 = {"small": "big", "black": "white", "up": "down"}
my_dict2 = {"dark": "light", "fat": "thin", "sky": "land"}

# check if my_dict1 and my_dict2 exists
print(my_dict1)
print(my_dict2)

# delete key-value pair with key "black" from my_dict1
del my_dict1["black"]

# check if the key-value pair with key "black" from my_dict1 is deleted
print(my_dict1)

# delete my_dict2
del my_dict2

# check if my_dict2 exists
# print(my_dict2) NameError: name 'my_dict2' is not defined. Did you mean: 'my_dict1'?

print(" ".join(my_dict1)) # only keys are joined not values.

list1 = [0,9,8,7]

l1 = list1.__iter__()
print(l1.__next__())
#print(l1)
print(l1.__next__())

import datetime
date = datetime.date(2000, 11, 16)
print('Date date is ', date.day, ' day of ', date.month, ' month of the year ', date.year)

from datetime import datetime
print(datetime.strptime('15/11/2000', '%d/%m/%Y'))


from time import gmtime, strftime
s = strftime("%a, %d %b %Y %H:%M:%S + 1010", gmtime())
print(s)


import traceback
try:
    raise Exception('Error Message.')
except:
    with open('error.txt', 'w') as error_file:
        error_file.write(traceback.format_exc())
    print('The traceback info was written to error.txt.')