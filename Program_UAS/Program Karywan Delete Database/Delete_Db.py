# Membuat Modul di python 

import psycopg2 # Module postgres sql


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
        print("Koneksi KeDatabase Berhasil")
        return connection
    except psycopg2.Error as er :
        print("Koneksi KeDatabase Gagal",er)

def delete_db(connection,nama):
    cursor = connection.cursor()
    try:
        query ="DELETE FROM tblkaryawan WHERE nama = %s"
        cursor.execute(query,(nama,))

        connection.commit()

        if cursor.rowcount > 0:
            print(f"Data Karaywan atas nama {nama},Berhasil dihapus")
        else:
            print("Data Karyawan tidak ditemukan")

    except psycopg2.Error as e:
        cursor.rollback()
        print("Kesalahan eksekusi SQL ",e)
    finally :
        cursor.close()

def main():
    connection = create_connection()
    if connection :
        nama = input("Masukan Nama Karaywan yang ingin di delete: ")

        delete_db(connection,nama)

        connection.close()

if __name__ == "__main__":
    main()