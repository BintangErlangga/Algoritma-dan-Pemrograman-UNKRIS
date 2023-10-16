def cek_tahun_kabisat(tahun):
    if tahun % 400 == 0  or ( tahun % 4 == 0 and tahun % 100 !=0):
        return True
    else :
        return False

def tahun_kabisat_dan_bukan_kabisat_antara(x, y):
    tahun_kabisat =[]
    tahun_bukan_kabisat=[]

    for tahun in range(x, y +1):
        if cek_tahun_kabisat(tahun):
            tahun_kabisat.append(tahun)
        else :
            tahun_bukan_kabisat.append(tahun)

    return tahun_kabisat, tahun_bukan_kabisat

#masukan tahun awal dan tahun akhir 
tahunAwal = int(input('Masukan Tahun Awal ='))
tahunAkhir = int(input('Masukan Tahun Akhir ='))

tahun_kabisat,tahun_bukan_kabisat = tahun_kabisat_dan_bukan_kabisat_antara (tahunAwal,tahunAkhir)

print(f'\ntahun kabisat antara {tahunAwal} dan {tahunAwal} adalah')
print(tahun_kabisat,'\n')

print(f'tahun bukan kabisat antara {tahunAwal} dan {tahunAwal} adalah')
print(tahun_bukan_kabisat)
