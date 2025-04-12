
# uang = 3000000
# items = {'Roko Magnum': 28000, 'garpit':30000, 'Sampoerna mild':35000}
# for item_name in items:
#     print('===================================')
#     print('anda memiliki '+ str(uang) + ' rupiah di rekening anda')
#     print('harga setiap ' + item_name + ' ' + str(items[item_name]) + ' Rupiah ')
    
#     input_count = input('Mau berapa bungkus ' + item_name +' ?: ')
#     print('Anda akan membeli ' + input_count + ' '+ item_name)
    
#     count = int(input_count)
#     total_price = items[item_name] * count
#     print('Harga total adalah ' + str(total_price) + 'rupiah')
    
#     if uang >= total_price:
#         print('Anda telah membeli ' + input_count + ' ' + item_name)
#         uang -= total_price
        
#         if uang == 0:
#             print('Dompet anda kosong')
#             break
#     else:
#         print('Uang anda tidak mencukupi')
#         print('Anda tidak dapat membeli ' + item_name + ' sebanyak itu ')
    
#     print('Uang anda tinggal ' + str(uang) + 'rupiah')

# import utils 
# import random
# # import module random


# print('Memulai permainan Batu Kertas Gunting!')
# player_name = input('Masukkan nama Anda: ')

# print('Pilih tangan: (0: Batu, 1: Kertas, 2: Gunting)')
# player_hand = int(input('Masukkan nomor (0-2): '))

# if utils.validate(player_hand):
#     # Tetapkan nomor acak antara 0 dan 2 ke computer_hand menggunakan randint
#     computer_hand = random.randint(0,2)
    
#     utils.print_hand(player_hand, player_name)
#     utils.print_hand(computer_hand, 'Komputer')

#     result = utils.judge(player_hand, computer_hand)
#     print('Hasil: ' + result)
# else:
#     print('Mohon masukkan nomor yang benar')

# from gtts import gTTS

# # language = "id"
# # text = "Betul nama mu adalah ujang"

# # speech = gTTS(text=text, lang=language, slow=False, tld="com.au" )
# # speech.save("ujang.mp3")

import time
from playsound import playsound


# Minta input dari user
nama = input("apa nama ibu kota negara indonesia: ")

time.sleep(1)
# Cek nama
if nama.lower() == "jakarta":
    print("Ya benar!")
    # Ganti dengan path file mp3 kamu jika beda
    playsound("suarabenar.mp3")  
else:
    print("Nama anda bukan ujang.")
    playsound("suarasalah.mp3")



# playsound("suarabenar.mp3")

# import pygame
# from gtts import gTTS

# # Buat suara
# text = input("Masukkan teks: ")
# tts = gTTS(text, lang='id')
# tts.save("suara.mp3")

# # Inisialisasi pygame dan mainkan
# pygame.mixer.init()
# pygame.mixer.music.load("suara.mp3")
# pygame.mixer.music.play()

# # Tunggu sampai suara selesai
# while pygame.mixer.music.get_busy():
#     continue