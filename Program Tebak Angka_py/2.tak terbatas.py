import random

angka_rahasia = random.randint(1,100)

print('=' * 40 )
print('Kami telah memiliki angka, silahkan tebak!')
print('=' * 40 )

batas_percobaan = 5
for percobaan in range(batas_percobaan):
    jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukan Angka ='))
    if jawaban == angka_rahasia:
        print("Tebakanmu Benar")
        break
    else:
        print('Tebakanmu terlalu',' kecil' if jawaban < angka_rahasia else 'besar')

else:
    print(f"\nSayang sekali anda telah mencapai batas percobaan sebanyak {batas_percobaan} x")