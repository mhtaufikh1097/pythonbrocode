
# def validate(hand):
#     if hand < 0 or hand > 2 :
#         return false 
#     return True

# def print_hand(hand, name='Tamu'):
#     hands = ['Batu', 'Kertas', 'Gunting']
#     print(name + ' memilih: ' + hands[hand])
    
# def judge(player, computer):
#     if player == computer:
#         return 'Seri'
#     elif player == 0 and computer == 1:
#         return 'Kalah'
#     elif player == 1 and computer == 2:
#         return 'Kalah'
#     elif player == 2 and computer == 0:
#         return 'Kalah'
#     else:
#         return 'menang'

# from menu_item import MenuItem 

# menu_item1 = MenuItem('Roti Kukus', 5000)
# menu_item2 = MenuItem('Roti Bakar', 7000)
# menu_item3 = MenuItem('Roti Goreng', 10000)

# menu_items = [menu_item1, menu_item2, menu_item3]

# index = 0

# for menu_item in menu_items:
#     print(str(index)+ '. ' + menu_item.info())
#     index += 1
# print("------------------")

# order = int(input('Masukan Nomor menu: '))
# selected_menu_item =  menu_items[order]
# print('Item yang di pilih: ' + selected_menu_item.name)

# count = int(input('Jumlah pesanan (diskon 10% untuk 3 atau lebih) = '))
# result = selected_menu_item.get_total_price(count)
# print('Total harga adalah Rp' + str(result))
