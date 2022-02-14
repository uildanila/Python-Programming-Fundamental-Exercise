mobil_matic = [
    {
        'plat': 'B 1234 CK',
        'jenis': 'Daihatsu Xenia',
        'tahun': '2016',
        'sewa_harian': 450000,
        'status' : 'Avaiable',
    },
    {
        'plat': 'B 1122 BE',
        'jenis': 'Toyota Calya',
        'tahun': '2015',
        'sewa_harian': 450000,
        'status' : 'Avaiable',
    },
    {
        'plat': 'B 9222 CE',
        'jenis': 'Honda Brio',
        'tahun': '2015',
        'sewa_harian': 385000,
        'status' : 'Avaiable',
    },
]
mobil_manual = [
    {
        'plat': 'B 1122 BE',
        'jenis': 'All New Avanza',
        'tahun': '2017',
        'sewa_harian': 350000,
        'status' : 'Avaiable',
    },
    {
        'plat': 'B 6136 QQ',
        'jenis': 'Honda Brio',
        'tahun': '2015',
        'sewa_harian': 370000,
        'status' : 'Avaiable',
    },
    {
        'plat': 'B 987 BD',
        'jenis': 'Toyota Agya',
        'tahun': '2016',
        'sewa_harian': 360000,
        'status' : 'Avaiable',
    },
]

list_penyewa = [] 
cart_sewa = [] 
list_sewa = []

def halo():
    print(f'''
        Selamat Datang di NIU RENTAL JABODETABEK
        List Menu:
        1. Menampilkan Daftar dan Report Mobil Rental
        2. Menambah & Update Mobil Rental
        3. Menghapus Mobil Rental
        4. Sewa dan Pengembalian Mobil
        5. Keluar Program
    ''')
def pilih_opsi():
    pilih = int(input('Masukkan Pilihan Anda: '))
    return pilih

def menu1():
    print(f'''
    ==============Menu #1: Daftar dan Report Mobil Rental====================
        1. Daftar Mobil Rental
        2. Report Mobil Rental
        3. Back
    ''')
def pilih_mobil():
    print(f'''
       Pilih Jenis Mobil:
        1. Mobil Matic
        2. Mobil Manual
        3. Back
    ''')
def menu2():
    print(f'''      
    ==============Menu #2: Menambah & Update Mobil Rental====================
       Pilih Menu:
        1. Tambah Mobil Rental
        2. Update Mobil Rental
        3. Back to Main Menu
    ''')
def menu4():
    print(f'''
       =======================Menu #4: Sewa dan Pengembalian Mobil======================
        1. Sewa Mobil
        2. Pengembalian Mobil Rental
        3. Back 
    ''')

def kembali():
    pilih = str(input('Kembali ke Menu Sebelumnya ? (Y/N): ').capitalize())
    return pilih

def lihat_mobil(mobil):
    print('Index\t|     Plat\t|\t Mobil\t\t|  Tahun  | Sewa Harian | Status')
    for i in range(len(mobil)):
        print(f"{i}\t| {mobil[i]['plat']}\t|{mobil[i]['jenis']}\t\t|  {mobil[i]['tahun']}   | {mobil[i]['sewa_harian']}\t| {mobil[i]['status']} ")
    return  

def lihat_report(list):
    print('Index\t|Nama Penyewa\t|Jenis Mobil\t|      Plat\t|\t Mobil\t\t|  Sewa Harian | Durasi (Hari)\t| Total\t')
    for i in range(len(list)):
        print(f'{i}\t| {list[i][0]}\t\t|{list[i][1]}\t\t|{list[i][2]}\t|{list[i][3]}\t\t|    {list[i][4]}    |{list[i][5]}\t\t| {list[i][6]}\t')
    return  

def tambah(mobil): 
    lihat_mobil(mobil)
    while True:
        plat = str(input('Masukkan plat mobil: '))
        for i in range(len(mobil)):
            if plat == (mobil[i]['plat']):
                print('Data mobil dengan plat yang sama sudah ada')
                break
        else:
            jenis = str.title(input('Masukkan jenis mobil: '))
            tahun = int(input('Masukkan tahun mobil: '))
            sewa_harian = int(input('Masukkan tarif sewa harian: '))
            cek = str(input('Apakah Anda yakin ingin menambah data ini? (Y/N) '))
            if cek == 'Y':
                mobil.append({
                'plat': plat,
                'jenis': jenis,
                'tahun': tahun,
                'sewa_harian': sewa_harian,
                'status' : 'Avaiable'
                })
                lihat_mobil(mobil)
                break
            else:
                print('Data tidak jadi ditambahkan')
                lihat_mobil(mobil)
                break
    return 

def update(mobil): 
    lihat_mobil(mobil)
    while True:
        index_mobil = int(input('Silahkan masukkan index data mobil rental yang ingin diupdate: '))
        if index_mobil not in range(len(mobil)):
            print('Data dengan index yang Anda cari tidak ada')
            continue
        else:
            for i in range(len(mobil)):
                if mobil[index_mobil] == mobil[i]:
                    jenis = str.title(input('Masukkan jenis mobil: '))
                    tahun = int(input('Masukkan tahun mobil: '))
                    sewa_harian = int(input('Masukkan tarif sewa harian: '))
                    cek = str(input('Apakah Anda yakin ingin update data ini? (Y/N) '))
                    if cek == 'Y':
                        mobil[i]['jenis'] = jenis
                        mobil[i]['tahun'] = tahun
                        mobil[i]['sewa_harian'] = sewa_harian
                        lihat_mobil(mobil)
                        continue
                    else:
                        break
        cek = str(input('Apakah Anda ingin mengupdate data lagi? (Y/N) '))
        if cek == 'Y':
            continue
        else:
            break
    return 

def hapus(mobil):
    lihat_mobil(mobil)
    index_mobil = int(input('Masukkan index data mobil rental yang ingin dihapus: '))
    del mobil[index_mobil]
    lihat_mobil(mobil)
    print('Data berhasil dihapus')
    return 

def sewa(mobil):
    lihat_mobil(mobil) 
    if mobil == mobil_matic:
        jenis_mobil = 'Matic'
    else:
        jenis_mobil = 'Manual'
    nama = str(input('Masukkan Nama Anda: '))
    while True:
        i  = int(input('Masukkan pilihan mobil yang ingin disewa: '))
        if i in range(len(mobil)) and mobil[i]['status'] == 'Avaiable':
            sewa = int(input('Berapa lama Anda ingin menyewa mobil? ... Hari :  '))
            total = sewa * mobil[i]['sewa_harian']
            status = 'Rented by ' + nama
            mobil[i]['status'] = status
            cart_sewa.append(
                [nama, jenis_mobil, mobil[i]['plat'], mobil[i]['jenis'],mobil[i]['sewa_harian'], sewa, total]
            )
            list_penyewa.append(
                [nama, jenis_mobil, mobil[i]['plat'], mobil[i]['jenis'],mobil[i]['sewa_harian'], sewa, total]
            )
            
            cek = input('Apakah Anda masih ingin menyewa? (Ya/Tidak): ').capitalize()
            if cek == 'Ya':
                lihat_mobil(mobil)
                continue
            else:
                break
        else:
            print(f"Index tidak tersedia/ mobil telah disewa. Silahkan input index kembali.")
            continue
    print('Isi Cart sewa:')
    print('Nama Penyewa\t|Jenis Mobil\t|      Plat\t|\t Mobil\t\t|  Sewa Harian | Durasi (Hari)\t| Total\t')
    for item in cart_sewa:
        print(f'{item[0]}\t\t|{item[1]}\t\t|{item[2]}\t|{item[3]}\t\t|    {item[4]}    |{item[5]}\t\t| {item[6]}\t')
    return

def detail_sewa():
    print('\nDetail sewa')
    total = []
    for j in cart_sewa:
        print(f'{j[3]} : {j[5]} hari x {j[4]} = {j[6]}')
        total.append(j[6])
    total_harga = sum(total)
    print(f'Total yang harus dibayar = {total_harga}')

    while True:
        uang = int(input('\nMasukkan Jumlah Uang: '))
        selisih = abs(uang - total_harga)
        if uang < total_harga:
            print('Uang tidak cukup, input kembali')
            continue
        elif uang > total_harga:
            print(f'Terima kasih, uang kembalian Anda sebesar {selisih:.0f}')
            break
        else:
            print('Terima kasih')
            break
    return

def pengembalian(list_penyewa): 
    while True:
        lihat_report(list_penyewa)
        index_mobil = int(input('Silahkan masukkan index data mobil rental yang ingin dikembalikan: '))
        if index_mobil not in range(len(list_penyewa)):
            print('Index tidak ditemukan, silahkan input index kembali')
            continue
        else:
            if list_penyewa[index_mobil] == 'Matic':
                mobil = mobil_matic
            else: 
                mobil = mobil_manual
            for i in range(len(mobil)):
                if mobil[index_mobil] == mobil[i]:
                    status = 'Avaiable'
                    cek = str(input('Apakah Anda yakin ingin menyimpan data ini? (Y/N) '))
                    if cek == 'Y':
                        mobil[i]['status'] = status
                        lihat_mobil(mobil)
                        continue
                    else:
                        break
        cek = str(input('Apakah Anda ingin mengembalikan mobil rental lagi? (Y/N) '))
        if cek == 'Y':
            continue
        else:
            break
    return

while True:
    halo()
    pilihan_menu = int(input('Masukkan angka menu yang ingin dijalankan: '))
    if(pilihan_menu == 1):
        while True:
            menu1()
            pilih = pilih_opsi()
            if(pilih == 1):
                while True:
                    print('==============Menu #1: Daftar Mobil Rental================================')
                    pilih_mobil()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        print('Daftar Mobil Rental Matic\n')
                        lihat_mobil(mobil_matic)
                    elif(pilih == 2):
                        print('Daftar Mobil Rental Manual\n')
                        lihat_mobil(mobil_manual)
                    elif(pilih == 3):
                        break
                    else:
                        print('Menu tidak tersedia')
                        continue
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue
            elif(pilih == 2):
                print('==============Menu #1.b: Report Mobil Rental================================')
                lihat_report(list_penyewa)
                continue
            elif(pilih == 3):
                break
            else:
                print('Menu tidak tersedia')
                continue
    elif(pilihan_menu == 2):
        while True:
            menu2()
            pilih = pilih_opsi()
            if(pilih == 1):
                while True:
                    print('==============Menu #2.1: Tambah Mobil Rental====================')
                    pilih_mobil()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        tambah(mobil_matic)
                    elif(pilih == 2):
                        tambah(mobil_manual)
                    elif(pilih == 3):
                        break
                    else:
                        print('Pilihan yang Anda masukkan Tidak Tersedia (Pilih 1-3)')

                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue
            elif(pilih == 2):
                while True:
                    print('==============Menu #2.2: Update Mobil Rental====================')
                    pilih_mobil()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        update(mobil_matic)
                    elif(pilih == 2):
                        update(mobil_manual)
                    elif(pilih == 3):
                        break
                    else:
                        print('Pilihan yang Anda masukkan Tidak Tersedia (Pilih 1-3)')
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue   
            elif(pilih == 3):
                break
            else:
                print('Pilihan yang Anda masukkan Tidak Tersedia (Pilih 1-3)')
                continue
    elif(pilihan_menu == 3):
        while True:
            print('=======================Menu #3: Menghapus Data Mobil Rental======================')
            pilih_mobil()
            pilih = pilih_opsi()
            if(pilih == 1):
                hapus(mobil_matic)
            elif(pilih == 2):
                hapus(mobil_manual)
            elif(pilih == 3):
                break
            else:
                print('Pilihan yang Anda masukkan Tidak Tersedia (Pilih 1-3)')
            pilih = kembali()
            if(pilih == 'Y'):
                break
            else:
                continue  
    elif(pilihan_menu == 4):
        while True:
            menu4()
            pilih = pilih_opsi()
            if(pilih == 1):
                while True:
                    print('==============Menu #4.1: Rental Mobil================================')
                    pilih_mobil()
                    pilih = pilih_opsi()
                    if(pilih == 1):
                        print('Daftar Mobil Rental Matic\n')
                        sewa(mobil_matic)
                        detail_sewa()
                        cart_sewa.clear()
                    elif(pilih == 2):
                        print('Daftar Mobil Rental Manual\n')
                        sewa(mobil_manual)
                        detail_sewa()
                        cart_sewa.clear()
                    elif(pilih == 3):
                        break
                    else:
                        print('Menu tidak tersedia')
                        continue
                    pilih = kembali()
                    if(pilih == 'Y'):
                        break
                    else:
                        continue 
            elif(pilih == 2):
                pengembalian(list_penyewa)
            elif(pilih == 3):
                break
            else:
                print('Menu tidak tersedia')
    elif(pilihan_menu == 5):
        break
    else:
        print('Pilihan yang Anda masukkan salah')
        continue