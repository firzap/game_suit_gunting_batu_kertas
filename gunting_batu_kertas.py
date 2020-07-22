"""
Game gunting batu kertas sederhana.
User vs BOT(random).
User akan memasukkan nama dan pilihan tangan(0 = gunting, 1 = batu dan 2 = kertas),
sementara BOT akan memilih tangan secara acak(0-2)
"""
import utils
import random

print('--------------------------------------')
print('Memulai permainan Gunting Batu Kertas!')
player_name = input('Masukkan nama Anda: ')

print('Pilih tangan: (0: Gunting, 1: Batu, 2: Kertas)')
player_hand = int(input('Masukkan nomor (0-2): '))

if utils.validate(player_hand):
    #tetapkan nilai acak 0-2 ke bot dgn fungsi randint dari modul random
    computer_hand = random.randint(0, 2)

    #cetak nama user + pilihan tangan dan bot
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Bot')

    #cetak hasil suit
    result = utils.judge(player_hand, computer_hand)
    print('Hasil: ' + result)
else:
    print('Mohon masukkan nomor yang benar')
print('--------------------------------------')
