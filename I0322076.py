import os
import json
from anggota import tambah_anggota, cari_anggota_by_id, tampilkan_anggota, edit_anggota
from tabungansampah import tambah_tabungan, tarik_tabungan, tampilkan_tabungan
from os import system, listdir, getcwd

def input_of_options(prompt:str, ls_opt:list):
    while True:
        try:
            masuk = input(prompt)
            assert masuk.strip() in ls_opt, 'Input tidak valid!'
            break
        except AssertionError as er:
            print(er)

    return masuk.strip()

def input_normal(prompt):
    while True:
        try:
            masuk = input(prompt)
            assert len(masuk.strip()) > 0, 'Input tidak boleh kosong atau hanya spasi!'
            break
        except AssertionError as er:
            print(er)

    return masuk.strip()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print('=========================================')
    print('** Program Pengelolaan Tabungan Sampah **')
    print('=========================================')
    print('Pilihan Menu:')
    print('1. Pengelolaan Keanggotaan')
    print('   1a. Penambahan Data Anggota')
    print('   1b. Pengubahan Data Anggota')
    print('   1c. Pencarian Data Anggota')
    print('2. Pengelolaan Tabungan Anggota')
    print('   2a. Penambahan Tabungan')
    print('   2b. Penarikan Tabungan')
    print('   2c. Menampilkan Data Tabungan')
    print('9. Exit')


def main_menu():
    while True:
        clear_screen()
        show_menu()
        pilihan = input('Masukan Pilihan Anda: ')

        if pilihan == '1a':
            clear_screen()
            print('Penambahan Data Anggota')
            tambah_anggota()
            input('Tekan enter untuk melanjutkan')

        elif pilihan == '1b':
            clear_screen()
            print('Pencarian Data Anggota')
            id_anggota = input ('Masukan ID Anggota: ')
            data_anggota = cari_anggota_by_id(id_anggota)
            clear_screen()
            tampilkan_anggota(data_anggota)
            input('Tekan enter untuk melanjutkan')

        elif pilihan == '1c':
            clear_screen()
            print('Pengubahan Data Anggota')
            edit_anggota()
            input('Tekan enter untuk melanjutkan')

        elif pilihan == '2a':
            clear_screen()
            id_dicari = input('Masukan ID Anggota: ')
            data = cari_anggota_by_id(id_dicari)

            if data == {}:
                print('ID tidak ditemukan!')
                input('Tekan enter untuk melanjutkan')
                continue


            print(f"""============================================= 
    IDAnggota : {id_dicari:<15} | Nama  : {data["nama"]} 
    Telepon   : {data["telepon"]:<15} | Alamat: {data["alamat"]} 
    ============================================= 
    --------------------------------------------- 
    Kode    | Jenis Sampah  | Harga Satuan (Rp)     
    --------------------------------------------- 
    1       | Kardus        |  500      
    2       | Botol plastic |  300 
    3       | Logam besi    |  800 
    4       | Tembaga       | 1000 
    ---------------------------------------------""")
            
            kode = input("Pilih jenis sampah     : ", ["1", "2", "3", "4"])

            while True:
                try:
                    kuantitas = float(input('Kuantitas sampah       :'))
                    break
                except ValueError:
                    print('Input tidak valid!')

            tambah_tabungan(id_dicari, kode, kuantitas)

        elif pilihan == '2b':
            id_dicari = input_normal('Masukan ID Anggota : ')
            data = cari_anggota_by_id(id_dicari)

            if data == {}:
                print('ID Tidak Ditemukan!')
                input('Tekan enter untuk melanjutkan')
                continue

            if f'tabungan{id_dicari}.json' not in listdir(getcwd()):
                print('Belum memiliki tabungan!')
                input('Tekan enter untuk melanjutkan')
                continue
            tarik_tabungan(id_dicari) 

        elif pilihan == '2c':
            id_dicari = input_normal('Masukkan ID Anggota : ')
            data = cari_anggota_by_id(id_dicari)

            if data == {}:
                print('ID Tidak Ditemukan!')
                input('Tekan enter untuk melanjutkan')
                continue
            if f'tabungan{id_dicari}.json' not in listdir(getcwd()):
                print('Belum memiliki tabungan!')
                input('Tekan enter untuk melanjutkan')
                continue

            tampilkan_tabungan(id_dicari)

        elif pilihan == '9':
            clear_screen() 
            print('Terima kasih!')
            break

        else:
            print('Pilihan tidak valid. Silakan pilih menu yang tersedia.')

main_menu()

            