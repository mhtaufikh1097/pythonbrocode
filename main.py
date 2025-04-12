#######this is my first python program
# print("Hello world!")
# print("it's really good")
#########################################Variables#################
#string,intger float,boolean)
#strings
# first_name = 'Muhammad'
# last_name = 'Taufik'
# food = "pizza"
# email = "taufik@gmail.com"
# print(f"Hello {first_name} {last_name}")
# print(f"you like {food}")
# print(f"your email is: {email}")

# #integer
# age = 25
# quantity = 3
# num_of_students = 30

# print(f"You are {age} years old")
# print(f"you are buying {quantity} items")
# print(f"your class has {num_of_students} student")

# #float
# price = 10.99
# gpa = 3.2
# distance = 5.5
# print(f"The price is ${price}")
# print(f"Yuor gpa is {gpa}")
# print(f'your ran {distance}km')

# #boolean
# is_student = False
# for_sale = True
# is_online = False

# if is_online:
#     print("You are online")
# else:
#     print(f"You are offline" )






# =======================================================type casting========================================================
#typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()    type(_)->melihat bentuk data nya
# name = ""
# age = 25
# gpa = 3.2
# is_employee = True


# name = bool(name)

# print(name)



# =======================================================USER INPUT========================================================
#input() =  a function that prompts the user to enter data return the entered data as a string
# name = input("What is your name?: ")
# age = int(input("How old are you?: "))


# age = age + 1

# print(f"Hello my name is {name} !")
# print("Happy birthday")
# print(f"im  {age} years old !")

#### exercise 1 rectangle area Calc

# Length = float(input("enter the length: "))
# width = float(input("enter the width: "))
# area = Length * width

# print (f"The are is: {area}cm2")

#### Excersie 2 rectangle area Calc
# item = input("What item would you like to buy?: ")
# price = float(input("What is price?: "))
# quantity = int(input("How many would you like?: "))
# total = price * quantity

# print(f"you have bought {quantity} x {item}/s")
# print(f"Your totalis {total}")

# =======================================================MALID GAME========================================================
#Madlibs game
#word game where you create a story 
#by filling in blanks with random words
# adjective1 = input("enter an adjective (description): ")
# noun1 = input("Enter a noun (person,place,thing): ")
# adjective2 = input("enter an adjective (description):  ")
# verb1 = input("Enter a verb ending with 'ing ")
# adjective3 = input("Enter an adjective (description): ")


# print(f"Today iI went to a {adjective1} zoo.")
# print(f"in an exhibit, i saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

# =======================================================Arictmath========================================================
# friends = 16

# friends = friends + 1
# friends += 1
# friends = friends - 2
#friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2 
# friends = friends ** 2
# friends **= 2
# remainder = friends % 3

# x = 3.14
# y = 4 
# z = 5

# # result = round(x)
# # result = abs(y)
# # result = pow(2, 3) //pangkat
# # result = min(x,y,z)

# print(result)

# import math
# x = 9.9
# # print(math.pi)
# # print(math.e)
# # result = math.sqrt(x) //untuk akar kuadrat
# # result = math.ceil(x) //membulatkan angka ke atas ke bilangan bulat terdeka
# # result = math.floor(x) //membulatkan angka ke bawah ke bilangan bulat terdekat. 
# print(result)

# import math
# radius = float(input('Enter the radius of a circle: '))
# # //panjang (linier) yang mengelilingi lingkaran tersebut.
# circumference = 2 * math.pi * radius 

# print(f"The circumference is: {round(circumference, 2)}cm")

# import math 
# radius = float(input('Enter the radius of a circle: '))
# area = math.pi * pow(radius, 2)
# print(f"the are of the circle is {round(area, 2)}cm^2")


# import math 
# a = float(input('Enter side A: '))
# b = float(input('Enter side B: '))

# c = math.sqrt(pow(a, 2) + pow(b, 2 ))

# print(f'side c = {c}')



# =======================================================IF Else========================================================
# age = int(input("Enter your age: "))

# if age >= 100:
#     print("You are too old to sign up")
# elif age >= 18:
#     print("You are now signed up!")
# elif age < 0:
#     print("You haven't been born yet")
# else:
#     print("You must be 18+ sign up")

# response = input("Would you like food? (Y/N): ")
# if response == "Y":
#     print("Have some food!")
# else:
#     print("No food for you!")


# name = input("Enter your name: ")

# if name == "":
#     print("YOu did not type in your name")
# else:
#     print(f"Hello {name}")



# online = True

# if online:
#     print("This user is online")
# else:
#     print("This user is NOT online")



# =======================================================Simple Calculator========================================================
# operator = input("Enter an operator (+ - * /): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# if operator == "+":
#     result = num1 + num2
#     print(round(result))
# elif operator == "-":
#     result = num1 - num2
#     print(round(result))
# elif operator == "*":
#     result = num1 * num2
#     print(round(result))
# elif operator == "/":
#     result = num1 / num2
#     print(round(result))
# else:
#     print(f"{operator} is Not valid Operator")




#============================================python weight converter if statement

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs." 
#     print(f"Your weight is: {round(weight)} {unit}")

# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs."
#     print(f"Your weight is: {round(weight)} {unit}")

# else:
#     print(f"{unit} was not valid")
    
    
    
    
#============================================temperature in celcius or fahrenhit ()
# unit = input("Is this temperature in Celcius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))

# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     print(f"The temperature in Fahrenheit is: {temp}°F ")
# elif unit == "F":
#     temp = round((temp - 32) * 5 / 9, 1 )
#     print(f"The temperature in Celcius is: {temp}°C ")
# else:
#     print(f"{unit} is an invalid unit of measurement")





# =========================================logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True 
#                     not = inverts the condition (not False, not True)

# temp = 20 
# is_raining = True

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("the outdoor event is still scheduled")

# temp = int(input("what a temperature: "))
# is_sunny = False 

# if temp >= 28 and is_sunny:
#     print("It is HOT outside 🤬")
#     print("It is SUNNY ☀️")
# elif temp <= 0 and is_sunny:
#     print("It is COLD 📪")
#     print("It is SUNNY ☀️")
# elif temp < 28 and temp > 0 and is_sunny:
#     print("It is WARM outside 😃")
#     print("It is SUNNY ☀️")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside 🤬")
#     print("It is CLOUDY ☁️")
# elif temp <= 0 and not is_sunny:
#     print("It is COLD 📪")
#     print("It is CLOUDY ☁️")
# elif temp < 28 and not temp > 0 and is_sunny:
#     print("It is WARM outside 😃")
#     print("It is CLOUDY ☁️")

# ===============================================================String method=========================================
# name= input("Enter your full name: ")
# phone_number = input("enter your phone number")

# # result = len(name) j// jumlah huruf
# # result = name.find('p') // mencari huruf
# # result = name.rfind('q') // mencari huruf berdasarkan array
# # result = name.capitalize() // huruf awal menjadi besar
# # result = name.upper() // huruf menjadi besar semua
# # result = name.lower() // huruf menjadi kecil semua
# # result = name.isdigit() // menentukan digit angka
# # result = name.isalpha() // menentukan karakter huruf
# # result = phone_number.count("-") // memisahkan number dengan spesial karakter
# # phone_number = phone_number.replace("-", " ")
# print(phone_number)

# print(help(str))

#************validare user input exercise
#1. username is no more than 12 characters
#2. username must not contain spaces
#3. username must not contain digits

# username = input("enter a username: ")

# username.find(" ")
# username.isalpha()

# if len(username) > 12:
#     print("your username cant be more than 12 characters ")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain number")
# else:
#     print(f"Welcome {username}")
    

# ===============================================================String indexing=========================================
#indexing = accessing elements of a sequence using [] (indexing operator)
#           [start : end : step]

# credit_number = "1234-5678-9012-3456"

# # print(credit_number[3])  
# # print(credit_number[:4])
# # print(credit_number[5:9])
# # print(credit_number[5:])
# # print(credit_number[-2])
# # print(credit_number[::3])

# # last_digits = credit_number[-4:]
# # print(f"xxxx-xxxx-xxxx-xxxx-{last_digits}")

# credit_number = credit_number[::-1]
# print(credit_number)


















########################################################################################Traine################################################################33









# +++++++++++++++++++++++menghitung luas segitiga
# n1 = int(input("Masukan nilai alas: "))
# n2 = int(input("Masukan nilai tinggi: "))

# result = 1/2 * n1 * n2

# print(f"Hasilnya adalah = " , result)

#++++++++++++++++++menghitung luas persegi+++++++++++++++++++++++++++++++
# p1 = int(input("masukan panjang persegi = "))
# print(f"sebuah persegi memiliki panjang sisi " , p1 , " Hitunglah luas persegi ? ")
# result = p1 * p1 
# print ('Luas persegi tersebut adalah ', result,'cm2')


# ot = int(input("Masukin jumlah jam lembur anda = "))
# day = int(input("Masukin jumlah hari = "))

# print("Jumlah jam lembur anda adalah " , ot ,'jam')
# result = ot * 25000
# print("Jumlah penghasilan kamu " , result)

# j = int(input("Masukan jarak = "))
# k = int(input("Masukan kecepatan =  "))

# print (f"jika jarak adalah {j} dengan kecepatan {k}" )

# result = j / k * 60

# print(f"maka waktu tempuh adalah {result} mnt")


 
# class MenuItem:
#      def info(self):
#          print('Tampilkan nama dan harga dari menu item')
        
# menu_item1 = MenuItem()
# menu_item1.name = 'Roti kukus'   
# menu_item1.price = 5000
# menu_item1.info()

# menu_item2 = MenuItem()
# menu_item2.name = 'Roti bakar'
# menu_item2.price = 7000
# menu_item2.info()

# menu_item3 = MenuItem()
# menu_item3.name = 'Roti Goreng'
# menu_item3.price = 10000
# menu_item3.info()
  
 
 
###aray
# rokok = ['magnum','Sampoerna Mild','Surya']
# print("Ini adalah list roko", rokok[0])
# rokok.extend(['black','super'])
# print(rokok)


# numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# for number in numbers:
#     if number % 3 != 1:
#         continue
#     print(number)

