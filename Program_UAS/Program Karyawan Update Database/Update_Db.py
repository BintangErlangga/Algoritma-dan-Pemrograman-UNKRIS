## Membuat Modul di python 

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

def update_db (connection,nama,new_jabatan):
    cursor = connection.cursor()

    try: 
        query = "UPDATE tblkaryawan SET jabatan = %s Where nama = %s"
        cursor.execute(query,(new_jabatan,nama))

        # Commit untuk perubahan didatabase 
        connection.commit()

        if cursor.rowcount > 0 :
            print(f"Data Karyawan atas nama = '{nama}',Berhasil diUpdate")
        else:
            print("Data Karyawan tidak ditemukan")
    except psycopg2.Error as e :
        connection.rollback()
        print("Kesalahan eksekusi SQL : " ,e )
    finally:
        # Menutup kursos 
        cursor.close()

def main():
    # membuat koneksi terlebih dahulu 
    connection = create_connection()

    if connection :
        nama = input("Masukan Nama karyawan yang ingin diUpdate: ")
        new_jabatan = input("Masukan Jabatan baru: ")

        update_db(connection,nama,new_jabatan)

        #menutup koneksi 
        connection.close()

if __name__ == "__main__":
    main()