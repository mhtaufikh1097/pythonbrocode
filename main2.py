#++++++++++++++++++++++++++ format specifiers
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34

# print(f"Price 1 is {price1:.3f}")
# print(f"Price 1 is {price2:.1f}")
# print(f"Price 1 is {price3:.3f}")

# temp = int(input("masukan nilai temperatur: "))


# if temp >= 28 :
#     print("sangat panas")
# elif temp <=20 :
#     print("suhu lumayan dingin")
# else : print("suhu cukup")


# ++++++++++++++++++++++++++++ while loop
# name = 'kcic'
# user_input = input("Enter your name: ")

# if user_input.strip() == 'kcic':
#     print(f"Hello {user_input}")
# else:
#     print("You did not enter your name")

# name = input("Enter your name: ")

# while name == "":
#     print("You did not enter your name")
#     name = input("Enter your name: ") //loop akan berhenti disini
# print(f"Hello {name}")



# name = 'kcic'
# while True:
#     user_input = input("Enter your name: ").strip()

#     if user_input.strip() == 'kcic':
#         print(f" {user_input}")
#         break
#     else:
#         print("You did not enter your name")


# age = int(input("enter your age: "))
# while age < 0:
#     print("Age can't be negative")
#     age = int(input("enter your age: "))
# print(f"You are {age} years old")



# food = input("enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"you like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("bye")

#   

#+++++++++++++++++++++++++++++++++++compound interest calculator++++++++++++++++++++++++++++++
# principle = 0
# rate = 0
# time = 0

# while True:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle can't be less than zero")
#     else:
#         break 
       
# while True:
#     rate = float(input("Enter the rate amount: "))
#     if rate < 0:
#         print("rate can't be less than zero")
#     else:
#         break
    
# while True:
#     time = float(input("Enter the time in years: "))
#     if time < 0:
#         print("time can't be less than zero")
#     else:
#         break
# total = principle * pow((1 + rate / 100), time)
# print(f"Balance after {time} year/s: Rp.{total:.2f}")

# Misalnya kamu investasi Rp10.000.000 dengan bunga 5% per tahun selama 3 tahun:

# Komponen:
# principle: jumlah pokok awal (modal awal investasi atau pinjaman)

# rate: suku bunga tahunan dalam persen

# time: jumlah tahun

# pow((1 + rate / 100), time): menghitung pertumbuhan eksponensial karena bunga majemuk

# total: jumlah akhir setelah bunga majemuk selama time tahun
# principle = 10000000
# rate = 5
# time = 3
# total = principle * pow((1 + rate / 100), time)
# Hasilnya:

# total = 10000000 * (1.05)^3 = 11576250
# Jadi, setelah 3 tahun, total uangmu menjadi Rp11.576.250.

# Kalau kamu mau, aku bisa bantu bikinkan fungsi Python-nya juga.


# +++++++++++++++++++++++++++++++++++For loop++++++++++++++++++++++++++++++
# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#         print(x)


# for x in range(1, 21):
#         if x == 15:
#                 continue
#         else:
#                 print(x)

#+++++++++++++++++++++++++++++time up menentukan waktu loading up data
# import time

# my_time = int(input("ENTER with time in seconds: "))

# for x in range(my_time, 0, -1):
#         seconds = x % 60
#         minute = int(x / 60) % 60
#         hours = int(x / 3600) 
#         print(f"{hours:02}:{minute:02}:{seconds:02}")
#         time.sleep(1)

# print("Time'S up!")

#+++++++++++++++++++++++++++++ Nested loop = A loop within another loop (outerminner)

# baris = 10

# for i in range(1, baris + 1):
    
#     for s in range(baris - i):
#         print(" ", end="")
        
#     for b in range(i):
#             print("*", end="")
            
#     print()

# baris = int(input("Masukan nilai: "))
# for i in range(1, baris):
#     print("*" * i)

# rows = int(input("Enter the # of rows: "))
# colums3 = int(input("Enter the # of rows: "))
# symbol = input("enter a symbol to use : ")

# for x in range(rows):
#     for y in range(colums):
#         print(symbol, end="")
#     print()


#+++++++++++++++++++++++++++++ LIST SET TUPLE