#Fungsi validasi akan memvalidasi inputan nilai tangan user.
#hanya nilai 0-2 yg diterima. selain nilai tsb akan me-returnkan boolean False.
#nilai 0 = gunting, 1 = batu dan 2 = kertas.
def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True

#Deklarasi list untuk tangan dan cetak pilihan tangan dari list
def print_hand(hand, name='Tamu'):
    hands = ['Gunting', 'Batu', 'Kertas']
    print(name + ' memilih: ' + hands[hand])

#Fungsi judge akan menentukan hasil menang/kalah/seri dari suit.
#gunting menang melawan kertas, namun kalah melawan batu.
#batu menang melawan gunting, namun kalah melawan kertas
#kertas menang melawan batu, namun kalah melawan gunting
def judge(player, computer):
    if player == computer:
        return 'Seri gan!'
    elif player == 0 and computer == 1:
        return 'Kalah KEKW'
    elif player == 1 and computer == 2:
        return 'Kalah KEKW'
    elif player == 2 and computer == 0:
        return 'Kalah KEKW'
    else:
        return 'Menang Slurd!'