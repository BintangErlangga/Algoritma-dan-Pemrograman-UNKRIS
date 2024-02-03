## Membuat Modul di python 

import psycopg2 # Module postgres sql
from time import time  # Module tanggal dan waktu 
import time # Module tanggal dan waktu 
import string
import random


# input password untuk masuk ke postgres sql 
password = input("Silahkan Masukan Password Database :")

# membuat fungsi untuk koneks ke Database 
def create_connection():
    ## membuat parameter yang diperlukan untuk Konek ke DB 
    db_params ={
        'dbname': 'dbkaryawan',
        'user': 'postgres',
        'password': password,
        'host': 'localhost',
        'port': '5432'  # Port default PostgreSQL adalah 5432
    }

    ## Menggunakan Exception try dan expect 
    ## untuk memsatikan saat proses running koneksi tidak ada error
    try :
        connection = psycopg2.connect(**db_params) 
        print("Koneksi Berhasil")
        return connection
    except psycopg2.Error as er :
        print("Koneksi Gagal",er)


def random_string(panjang:int) ->str :
    hasil_string = ''.join(random.choice(string.ascii_letters)for i in range(6))
    return hasil_string


def insert_karyawan(connection,no_id,tanggal,nama,jabatan,departemen):
    # Membuat objek cursor
    cursor = connection.cursor()

    try:
        # Mengganti 'nama_tabel' dan 'kolom1, kolom2, kolom3, ...' dengan nama tabel dan kolom di database Anda
        query = "INSERT INTO tblkaryawan (no_id,tanggal,nama,jabatan,departemen) VALUES (%s, %s, %s,%s,%s)"
        
        # Mengganti (nama, posisi, gaji) dengan nilai yang ingin Anda masukkan
        data_to_insert = (no_id,tanggal,nama,jabatan,departemen)
        
        cursor.execute(query, data_to_insert)
        
        # Commit perubahan ke database
        connection.commit()
        print("Data karyawan berhasil dimasukkan ke database!")
    except psycopg2.Error as e:
        # Rollback jika terjadi kesalahan
        connection.rollback()
        print("Kesalahan eksekusi SQL:", e)
    finally:
        # Menutup kursor
        cursor.close()

def main():
    # Membuat koneksi
    connection = create_connection()

    if connection:
        # Memasukkan data karyawan
        no_id = random_string(6)
        tanggal = time.strftime("%Y-%m-%d",time.gmtime())
        nama = input("Masukan Nama Karyawan: ")
        jabatan = input("Masukan jabatan Karyawan: ")
        departemen = input("Masukan debpartemen Karyawan: ")


        insert_karyawan(connection,no_id,tanggal,nama,jabatan,departemen)

        # Menutup koneksi
        connection.close()

if __name__ == "__main__":
    main()