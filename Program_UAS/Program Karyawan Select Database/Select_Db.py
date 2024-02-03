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

def select_db (connection):
    cursor = connection.cursor()

    try :
        query ="Select * From tblkaryawan"
        cursor.execute(query)

        record = cursor.fetchall()

        # Menampilkan data 
        if not record :
            print("Tidak terdapat data Karyawan")
        else :
            print("Data Karyawan")
            for row in record :
                print(f'Nama {row[2]},Jabatan {row[3]},Departemen {row[4]}')
    except psycopg2.Error as e :
        print("Kesalahan query sql ",e)    

    finally :
        cursor.close()

def main():
    connection = create_connection()

    if connection :
        select_db(connection)

        connection.close()

if __name__ == "__main__" :
    main()