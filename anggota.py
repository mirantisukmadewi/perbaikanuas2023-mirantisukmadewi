import json
import random
import string
from datetime import datetime
import os

def generate_idanggota():
    id_length = 5
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters)for _ in range(id_length))

def create_tabungan_file(id_anggota):
    filename = f'tabungan{id_anggota}.json'
    if not os.path.exists(filename):
        with open (filename, 'w') as file:
            json.dump([], file)

def tambah_anggota():
    data_anggota = {}
    id_anggota = generate_idanggota()
    nama = input ('Nama: ')
    alamat = input ('Alamat: ')
    telepon = input ('Nomor Telepon: ')
    tanggal = datetime.now().strftime('%Y-%m-%d')

    data_anggota[id_anggota] = {
        "idanggota": id_anggota,
        "nama": nama,
        "alamat": alamat,
        "tanggal": tanggal,
        "telepon": telepon
    }
    with open('anggotas.json', 'r') as file:
        existing_data = json.load(file)

    existing_data.update(data_anggota)

    with open('anggotas.json', 'w') as file:
        json.dump(existing_data, file, indent=4)

        create_tabungan_file(id_anggota)

        print('Berhasil menambahkan data anggota.')
        print('ID Anggota Baru:', id_anggota)

def cari_anggota_by_id(id_anggota):
    with open ('anggotas.json', 'r') as file:
        data_anggota = json.load(file)

    if id_anggota in data_anggota:
        return data_anggota[id_anggota]
    else:
        return {}
    
def tampilkan_anggota(data_anggota):
    if data_anggota:
        print('ID Anggota:', data_anggota['idanggota'])
        print('Nama:', data_anggota['nama'])
        print('Alamat:', data_anggota['alamat'])
        print('Telepon:', data_anggota['telepon'])
        print('Tanggal Daftar:', data_anggota['tanggal'])
    else:
        print('Tidak ada data anggota!')

def edit_anggota():
    while True:
        print('Ketik ID anggota yang akan diedit:')
        id_anggota = input(' > ')

        data_anggota = cari_anggota_by_id(id_anggota)
        if not data_anggota:
            print('Data anggota tidak ditemukan!')
            jawaban = input('Cari lagi? (Y - Ya, T = Tidak): ')
            if jawaban.lower() != 'y':
                break
            else:
                #clear_screen()
                continue
        print('Nama:', data_anggota['nama'])
        nama_baru = input('Nama(kosongkan jika tidak ingin mengubah): ')

        print('Alamat:', data_anggota['alamat'])
        alamat_baru = input('Alamat(kosongkan jika tidak ingin mengubah): ')

        print('Telepon:', data_anggota['telepon'])
        telepon_baru = input('Telepon(kosongkan jika tidak ingin mengubah): ')

        if nama_baru:
            data_anggota['nama'] = nama_baru
        if alamat_baru:
            data_anggota['alamat'] = alamat_baru
        if telepon_baru:
            data_anggota['telepon'] = telepon_baru

        with open('anggotas.json', 'r') as file:
            existing_data = json.load(file)

        existing_data[id_anggota] = data_anggota

        with open ('anggotas.json', 'w') as file:
            json.dump(existing_data, file, indent=4)

        print('Data berhasil diubah.')
        break 