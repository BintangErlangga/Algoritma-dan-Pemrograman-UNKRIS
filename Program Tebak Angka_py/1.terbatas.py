import random

angka_rahasia = random.randint(1,100)
print('=' * 40 )
print(f'Kami telah memiliki angka, silahkan tebak!')
print('=' * 40 )

while True :
    jawaban = int(input('\nMasukan Angka = '))

    if jawaban == angka_rahasia :
        print('Selamat tebakan mu benar!')
        break 
    else :
        print('Tebakanmu teralu kecil!'
               if jawaban < angka_rahasia else 'Tebakanmu terlalu besar!')