import os

""" Notes = 1. os.system('cls') digunakan untuk membersihkan tampilan terminal
            2. input() digunakan untuk memberikan kontrol kepada user agar tampilan tidak langsung hilang."""
          
def tampilanMenu():
    inp = input('''**************************'
* 1. View Data Siswa     *
* 2. Add Data Siswa      *
* 3. Update Data Siswa   *
* 4. Delete Data Siswa   *
* 5. Exit                *
**************************
Input :''')
    return inp

""" Menu 1 <Starts Here>"""

def tampilanMenuView():
    inp = input('''**************************'
* 1. View All Data       *
* 2. View Data by NISN   *
* 3. Back                *
**************************
Input :''')
    return inp

def viewAllData():
    os.system('cls')
    print('Data Siswa\n')
    print(' NISN\t\t| Nama\t\t\t| Kelas\t\t\t| Nilai UTS\t\t| Nilai UAS')
    print('------------------------------------------------------------------------------------------------------')
    for i in range(len(data['NISN'])):
        print(f''' {data['NISN'][i]}\t\t| {data['Nama'][i]}\t\t| {data['Kelas'][i]}\t\t| {data['Nilai UTS'][i]}\t\t\t| {data['Nilai UAS'][i]}''')


def viewDatabyNISN(nisn):
    os.system('cls')
    if nisn in data['NISN']:
        for idx,val in enumerate(data['NISN']):
            if val == nisn:
                print('Data Siswa\n')
                print(' NISN\t\t| Nama\t\t\t| Kelas\t\t\t| Nilai UTS\t\t| Nilai UAS')
                print('------------------------------------------------------------------------------------------------------')
                print(f''' {data['NISN'][idx]}\t\t| {data['Nama'][idx]}\t\t| {data['Kelas'][idx]}\t\t| {data['Nilai UTS'][idx]}\t\t\t| {data['Nilai UAS'][idx]}''')
    else:
        print('Data tidak ditemukan')

""" Menu 1 <Starts Here>"""

""" Menu 2 <Starts Here>"""

def tampilanMenuAdd():
    inp = input('''**************************'
* 1. Add Data            *
* 2. Back                *
**************************
Input :''')
    return inp

def addData():
    nisn = input('Masukkan NISN :')
    if not(nisn in data['NISN']):
        nama = input('Masukkan Nama :')
        kelas = input('Masukkan Kelas :')
        uts = input('Masukkan Nilai UTS :')
        uas = input('Masukkan Nilai UAS :')
        inp = input('\nTambahkan data (yes/no)? ')
        if inp.lower() == 'yes':
            data['NISN'].append(nisn)
            data['Nama'].append(nama)
            data['Kelas'].append(kelas)
            data['Nilai UTS'].append(uts)
            data['Nilai UAS'].append(uas)
            os.system('cls')
            print('\nData Tersimpan')
            input()
        else:
            os.system('cls')
            print('\nGagal menyimpan data')
            input()
    else:
        os.system('cls')
        print('Data Sudah Ada')
        input()

""" Menu 2 <Ends Here>"""

""" Menu 3 <Starts Here>"""

def tampilanMenuUpdate():
    inp = input('''**************************'
* 1. Update Data         *
* 2. Back                *
**************************
Input :''')
    return inp

def updateData():
    os.system('cls')
    nisn = input('Masukkan NISN :')
    if nisn in data['NISN']:
        for idx,val in enumerate(data['NISN']):
            if val == nisn:
                print('Nama         :',data['Nama'][idx])
                print('Kelas        :',data['Kelas'][idx])
                print('Nilai UTS    :',data['Nilai UTS'][idx])
                print('Nilai UAS    :',data['Nilai UAS'][idx])
                inp = input('\nLanjutkan pengeditan (yes/no)?')
                if inp.lower() == 'yes':
                    kolom = input('\nPilih Kolom yang ingin di edit (nama kolom bersifat case sensitif) : ')
                    value_baru = input('Masukkan value baru : ')
                    inp = input('\nEdit data (yes/no)? ')
                    if inp.lower() == 'yes':
                        data[kolom][idx] = value_baru
                        os.system('cls')
                        print('Berhasil mengedit data')
                        input()
                    else:
                        os.system('cls')
                        print('Gagal Mengedit data')
                        input()
                else:
                    os.system('cls')
                    print('Gagal Mengedit data')
                    input()
    else:
        os.system('cls')
        print('Data yang ingin anda cari, tidak ada')
        input()

""" Menu 3 <Ends Here>"""

""" Menu 4 <Starts Here>"""

def tampilanMenuDelete():
    inp = input('''**************************'
* 1. Delete Data         *
* 2. Back                *
**************************
Input :''')
    return inp

def deleteData():
    os.system('cls')
    nisn = input('Masukkan NISN :')
    if nisn in data['NISN']:
        for idx,val in enumerate(data['NISN']):
            if val == nisn:
                print('Nama         :',data['Nama'][idx])
                print('Kelas        :',data['Kelas'][idx])
                print('Nilai UTS    :',data['Nilai UTS'][idx])
                print('Nilai UAS    :',data['Nilai UAS'][idx])
                inp = input('\nYakin untuk menghapus data ini (yes/no)? ')
                if inp.lower() == 'yes':
                    del data['NISN'][idx]
                    del data['Nama'][idx]
                    del data['Kelas'][idx]
                    del data['Nilai UTS'][idx]
                    del data['Nilai UAS'][idx]
                    os.system('cls')
                    print('Berhasil menghapus data')
                    input()
                else:
                    os.system('cls')
                    print('Gagal Menghapus data')
                    input()
    else:
        os.system('cls')
        print('Data yang ingin anda cari, tidak ada')
        input()


""" Menu 4 <Ends Here>"""
              
os.system('cls') # Digunakan agar terminal bersih ketika program pertama kali dijalankan

# Inisiasi Data
data = {                                    
    'NISN' : ['1','10'],
    'Nama' : ['Raihan','Muhith'],
    'Kelas' : ['IF-42-03','IF-42-03'],
    'Nilai UTS' : [84,79],
    'Nilai UAS' : [90,83]
    }

# Contoh ketika data kosong
# data = {                                  
#     'NISN' : [],
#     'Nama' : [],
#     'Kelas' : [],
#     'Nilai UTS' : [],
#     'Nilai UAS' : []
#     }

# Main Program     
while True:
    os.system('cls')
    inp = tampilanMenu()
    if inp == '1':
        os.system('cls')
        while True:
            os.system('cls')
            inp = tampilanMenuView()
            if inp == '1':
                if len(data['NISN']) == 0:
                    os.system('cls')
                    print('Tidak Ada data')
                    input()
                else:
                    viewAllData()
                    input()
            elif inp == '2':
                if len(data) == 0:
                    print('Tidak Ada data')
                    input()
                else:
                    os.system('cls')
                    inp = input('Masukkan NISN :')
                    viewDatabyNISN(inp)
                    input()
            elif inp == '3':
                break
            else:
                print('Menu Tidak ada, Ulang!')
                input()
    elif inp == '2':
        os.system('cls')
        while True:
            os.system('cls')
            inp = tampilanMenuAdd()
            if inp == '1':
                addData()
            elif inp == '2':
                break
            else:
                print('Menu Tidak ada, Ulang!')
                input()
    elif inp == '3':
        os.system('cls')
        while True:
            os.system('cls')
            inp = tampilanMenuUpdate()
            if inp == '1':
                updateData()
            elif inp == '2':
                break
            else:
                print('Menu Tidak ada, Ulang!')
                input()
    elif inp == '4':
        os.system('cls')
        while True:
            os.system('cls')
            inp = tampilanMenuDelete()
            if inp == '1':
                deleteData()
            elif inp == '2':
                break
            else:
                print('Menu Tidak ada, Ulang!')
                input()
    elif inp == '5':
        break
    else:
        print('menu tidak ada, ulang!')
        input()
    