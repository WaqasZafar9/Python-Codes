#task no 1
# a = 10
# b = float(a)
# print(b)


#task no 2

# a = 10.10
# b = int(a)
# print(b)

#task no 3

# string = '123'
# b = int(string)
# print(b)

# #task no 4

# string = "1234"
# floatvalue =  float(string)
# print(floatvalue)

#task no 5

# integer = 10
# sstring = str(integer)
# print(sstring)

# #task no 6

# floatvalue = 20.20
# tostring = str(floatvalue)
# print(tostring)

#task no 7

# string = " waqas"
# intvalue = 38605
# concatinate = str(intvalue) + string
# print(concatinate)

# task no 8

# value1 = 10
# value2 = 20.30
# print (value1 + value2)
# print ( value1 - value2)
# print (value2 / value1)
# print (value1 * value2)

#task no 9

# str1 = input('Enter Your age: ')
# str2 = input('enter your age: ')
# intvalue1 = int(str1)
# intvalue2 = int(str2)
# print  (intvalue1 + intvalue2)

# task 10

# celsius = input('enter temprature  in celsius: ')
# celsius = float(celsius)
# farinheit = (celsius * 9/5) + 32 
# print(farinheit)

#task 11

# string = ['40','20','2003']
# intvalue = [eval(x) for x in string ]
# print(intvalue)

# task 12

# integer = [40 , 20 , 2003]
# string = [str(x) for x in integer]
# print(string)

# task 13

# integer = [40,20,2003]
# string = ['20', '30', '40']
# floatvalue = [float(x) for x in integer]
# print(floatvalue)
# floatvalue2 = [float(x) for x in string]
# print(floatvalue2)

#task 14

dict_values = {"a": "5", "b": 10.5, "c": "3.2"}

converted_dict = {
    key: int(value) if value.isdigit() else float(value) 
    for key, value in dict_values.items() 
    if isinstance(value, str) and (value.isdigit() or (value.replace('.', '', 1).isdigit()))
}

print(converted_dict)

