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

def create_table (connection):

    cursor = connection.cursor()

    try :
        query = """
        CREATE TABLE IF NOT EXISTS tblkaryawan (
            no_id text,
            tanggal date,
            nama VARCHAR(255) NOT NULL,
            jabatan VARCHAR(255) NOT NULL,
            departemen VARCHAR(255) NOT NULL          
        )
        """
        cursor.execute(query)

        # Commit perubahan ke database
        connection.commit()
        print("Tabel karyawan berhasil dibuat!")
        
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
        # Membuat tabel karyawan
        create_table(connection)

        # Menutup koneksi
        connection.close()

if __name__ == "__main__":
    main()