def apakahTahun_kabisat(tahun) :
    
    habisDibagi_400 = tahun % 400 == 0
    habisDibagi_100 = tahun % 100 == 0
    habisDibagi_4   = tahun % 4   == 0

    return habisDibagi_400 or(habisDibagi_4 and not habisDibagi_400)

tahunAwal  =int(input('Masukan tahun awal ='))
tahunAkhir =int(input('Masukan tahun akhir ='))

tahunKabisat = []

for tahun in range(tahunAwal , tahunAkhir + 1):
    if apakahTahun_kabisat(tahun):
        tahunKabisat.append(tahun)

print(f'{tahunKabisat} \nadalah tahun kabisat')