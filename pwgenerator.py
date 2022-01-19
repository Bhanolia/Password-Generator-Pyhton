# import modul yang diperlukan
import random
import string
import glob

# definisi data
huruf = string.ascii_letters
nomor = string.digits
symbols = string.punctuation
campur = string.ascii_letters + string.digits + string.punctuation

# deklarasi variabel
password = []
bensal = True
jenis_password: int
panjang: int
password : any


def menu(value):
    global jenis_password
    global panjang
    print('\nProgram, Password generator!')
    print('\n1. Random password dari Alfabet')
    print('2. Random password dari Angka')
    print('3. Random password dari Symbols')
    print('4. Random password dari Alfabet, Angka dan Symbols')

    if value == True:
        # masukan jenis dan panjang password
        while value:
            try:
                jeniss_password = int(input('\nMasukan Jenis password (1,2,3,4): '))

                while jeniss_password != 1 and jeniss_password != 2 and jeniss_password != 3 and jeniss_password != 4:
                    jeniss_password = int(input('\nMasukan Jenis dengan benar: '))
                break
 
            except:
                bensal = False
                print('Tolong masukan diantara 1 sampai 4')
                # print(bensal)


    else:
        print('exit')
        sys.exit()

    jenis_password = jeniss_password
    print(jenis_password)
    return passlong(value)


def passlong(value):
    global panjang
    if value == True:
        while value:
            try:
                panjang = int(input('\nMasukan panjang Password: '))
                passmaker(value)
                # break
            except:
                print('Hanya bisa menerima angka')
    else:
        menu(value)


    return panjang

# pembuatan password
def passmaker(value):

    global panjang
    global jenis_password
    global password

    if value == True :
        if(jenis_password == 1):
            if (panjang == 0):
                # passlong(True)
                print("hanya dapat menerima panjang lebih dari 0 huruf")
                # exit()
                # bensal = True
                passlong(value)
            elif (panjang <= 52):
                ambil = random.sample(huruf, panjang)
                password = "".join(ambil)
                print(password)
                savefile(value)
            else:
                print("hanya dapat menerima panjang 52 huruf")
                passlong(value)
        elif(jenis_password == 2):
            if (panjang == 0):
                # passlong(True)
                print("hanya dapat menerima panjang lebih dari 0 angka")
                # exit()
                # bensal = True
                passlong(value)
            elif panjang <= 10:
                ambil = random.sample(nomor, panjang)
                password = "".join(ambil)
                print(password)
                savefile(value)
            else:
                print("hanya dapat menerima panjang 10 angka")
                passlong(value)
        elif(jenis_password == 3):
            if (panjang == 0):
                # passlong(True)
                print("hanya dapat menerima panjang lebih dari 0 symbols")
                # exit()
                # bensal = True
                passlong(value)
            elif panjang <= 32:
                ambil = random.sample(symbols, panjang)
                password = "".join(ambil)
                print(password)
                savefile(value)
            else:
                print('hanya dapat menerima panjang 32 symbols')
                passlong(value)
        elif(jenis_password == 4):
            if (panjang == 0):
                # passlong(True)
                print("hanya dapat menerima panjang lebih dari 0")
                # exit()
                # bensal = True
                passlong(value)
            if panjang <= 94:
                ambil = random.sample(campur, panjang)
                password = "".join(ambil)
                print(password)
                savefile(value)
            else:
                print('hanya dapat menerima panjang 94')
                passlong(value)
    else:
        menu(value)




# save password
def savefile(value):
    global password
    print('\nSave hasil dari Password generator?')
    
    while True:
        simpan = input('Yes or No: ').lower()


        if simpan == 'yes' or simpan == 'y':
            print('Format (namafile) .txt')
            nama_file = input('Masukan Nama File: ')
            f = open(f'{nama_file}.txt', "w")
            f.write(password)
            f.close()

            results = glob.glob(f'./**/{nama_file}.txt')
            print(f'Password berhasil disimpan dengan nama {nama_file} tersimpan satu folder dengan file python ini')
            break
            # keluarapp(value)
        elif simpan == 'no'or simpan == 'n':
            print("Password tidak disimpan")
            break
            # keluarapp(value)
        else:
            if not simpan:
                print("Anda tidak memasukan apapun, Password tidak disimpan")
                simpan = 'no'
                break
                # keluarapp(value)
            else:
                print('input yang anda masukan salah')
    return keluarapp(value)


def keluarapp(value):
    print('\nTutup aplikasi')
    keluar = input('Yes or No: ').lower()
    if keluar == "yes" or keluar == "y":
        print('exit')
        sys.exit()
    elif  keluar == "no" or keluar == "n":
        menu(value)
    else:
        print('\nTutup aplikasi')
        keluar = input('Yes or No: ').lower()

if bensal == True:
    menu(bensal)
    # passlong(bensal)
    # passmaker(bensal)
    keluarapp(bensal)
else:
    print('exit')
    sys.exit()




