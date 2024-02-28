from tabulate import tabulate
database=[
    ["PST01",'Piston','Mobil',12,'Toyota','Avanza'],
    ["BLK02",'Block Head','Mobil',6,'Toyota','Innova'],
    ["BSI01",'Busi','Mobil',7,'Toyota','Innova']
]



HEADERS=("id","Sparepart","Kenadaraan","Stock","Merk","Jenis")
##fungsi menampilkan
def show(table, headers=HEADERS, title='\nTabel Daftar Barang\n'):
    print(title)
    print(tabulate(table, headers,tablefmt="grid"))


#Validasi
def validasi(promp):
    while True:
        Minput=input(promp)
        if Minput.isalnum():
            break
        else:
            print("Jangan Masukkan karakter!!")
    return Minput

#validasi string
def string(promp):
    while True:
        val=input(promp)
        if val.isalpha() or val.replace(' ','').isalpha():
            break
        else:
            print("Masukkan Huruf Saja !!")

    return val


#read data
def read_data():
    while True:
        print('''
        1. MENAMPILKAN SEMUA SPAREPART YANG TERSEDIA
        2. CARI SPAREPART
        3. MAIN MENU
        ''')
        #Memasukkan input sub menu read data
        option_sub=input("masukkan 1-3: ")
        #untuk menampilkan semua barang yang ada
        if option_sub=="1":
            if database==[]:
                print("Database Kosong")
            else:
                show(database)
            continue
        #untuk pencarian barang berdasarkan id barang
        elif option_sub=='2':
            if database==[]:
                print("Database Kosong,sehingga tidak dapat dilakukan pencarian produk")
            else:
                id_tertentu=input("masukkan id barang: ")
                for i,item in enumerate(database):
                    if id_tertentu.upper()==item[0]:
                        item1=[item]
                        print(tabulate(item1,HEADERS,tablefmt="grid"))
                        break
                else:
                    print("ID Barang Tidak Tersedia")
                    continue
        #Masuk ke main menu
        elif option_sub=='3':
            break
        else:
            print("masukkan angka 1-3:!")
            continue
        


#create/tambah

def tambah(table):
    while True:
        print("""
        ---------------Menambahkan sparepart------------
        1. menambahkan saprepart
        2. main menu""")
        #Memasukkan sub menu tambah
        option_sub=input("masukkan nomer 1/2: ")
        #jika kita memasukkan kode barang yang sudah ada maka barang tidak akan ditambahkan
        if option_sub=="1":
            while True:
                id=validasi("Masukkan ID Barang: ")
                for i,item in enumerate(table):
                    if id.upper() == item[0]:
                        print("Id sudah terdaftar")
                        break
            #untuk memasukkan input barang baru         
                else:
                    while True:
                        sparepart=string("Masukkan jenis sprepart: ")
                        jenis=string("Masukkan jenis kendaraan: ")
                        merk=string("Masukkan merk kendaraan: ")
                        for i,item in enumerate(table):
                            if sparepart.title()== item[1] and jenis.title()==item[5] and merk.title()==item[4]:
                                print("Jenis sparepart untuk kendaraan dan tipe tersebut sudah terdaftar")
                                break
                        else:
                            break
                    while True:
                        kendaraan=input("Masukkan Jenis Kendaraan Mobil/Motor: ")
                        if kendaraan.upper()=='MOTOR' or kendaraan.upper()=='MOBIL':
                            break
                        else:
                            print("Masukkan Jenis Kendaraan Mobil/Motor!")
                    while True:
                        stock=input("Masukkan Jumlah Sparepart: ")
                        if stock.isdecimal()==True:
                            break
                        else:
                            print("Masukkan stock dalam angka!")
                            continue
                        
                    tampilkan=[[id.upper(),sparepart.title(),kendaraan.capitalize(),int(stock),merk.title(),jenis.title()]]
                    show(tampilkan)
                    while True:
                        print("Apakah anda ingin menambahkan produk tersebut?(Y/N)")
                        konfirInput=input("Y/N: ")
                        if konfirInput.upper()=="Y":
                            table.append([
                                id.upper(),
                                sparepart.title(),
                                kendaraan.capitalize(),
                                int(stock),
                                merk.title(),
                                jenis.title()
                            ])
                            show(table)
                            print("Barang Berhasil Di Input")
                            break
                        elif konfirInput.upper()=="N":
                            print("Produk tidak diinput")
                            break
                        else:
                            print("Inputkan Y/N!")
                            continue
                    break
              
        #masuk ke main menu                      
        elif option_sub=='2':
            break
        else:
            print("masukkan angka 1/2")
            continue
        
#Update
def update(table):
    while True:
        print(""" 
        --------------Update Stock----------------
        1. tambah stock
        2. stock keluar
        3. main menu""")
        #memasukkan input sub menu update
        option_sub= input("Masukkan menu yang dipilih: ")
        if option_sub=='1':
            if database==[]:
                print("Database kosong sehingga tidak bisa dilakukan update!") 
            else:  
                while True: 
                    id=input("Masukkan ID Barang: ")  
                    for i,item in enumerate(database):
                        if id.upper()==item[0]:
                            break
                    else:
                        print("ID Barang Tidak Terdaftar")
                        continue
                    while True:
                        stock=input("Masukkan Stock Barang: ")
                        if stock.isdecimal()==True:
                            break
                        else:
                            print("Masukkan Stock Dalam Angka")
                            continue
                    
                    tampilUpStock=[[id.upper(),item[1],item[2],stock,item[4],item[5]]]
                    show(tampilUpStock)
                    while True:
                        print("Apakah anda ingin menambahkan stock produk tersebut?(Y/N)")
                        konfirInput=input("Y/N: ")
                        if konfirInput.upper()=="Y":
                            item[3]+=int(stock)
                            show(table)
                            print("Stock Barang Berhasil Ditambahkan")
                            break
                        elif konfirInput.upper()=="N":
                            print("Stock produk tidak ditambahkan")  
                            break     
                        else:
                            print("Inputkan Y/N!")
                            continue
                    break
        
        #Update stock barang keluar        
        elif option_sub=='2':
            if database==[]:
                print("Database kosong sehingga tidak bisa mengeluarkan barang!!")
            else:
                while True:
                    id=input("Masukkan ID Barang: ")
                    for i,item in enumerate(database):
                        if id.upper()==item[0]:
                            break
                    else:
                        print("ID Barang Tidak Tersedia")
                        continue

                    while True:    
                        stock=input("Masukkan jumlah barang keluar: ")
                        if stock.isdecimal()==True:
                            if int(stock)<=item[3]:
                                break
                            else:
                                print("Barang yang dimasukkan melebihi stock!")
                                continue
                        else:
                            print("Masukkan Stock Dalam Angka")
                            continue
                    
                    tampilKurang=[[id.upper(),item[1],item[2],stock,item[4],item[5]]]
                    show(tampilKurang)
                    while True:
                        print("Apakah benar produk tersebut dan quantitynya yang akan keluar?(Y/N)")
                        konfirInput=input("Y/N: ")
                        if konfirInput.upper()=="Y":
                            item[3]-=int(stock)
                            show(table)
                            break
                        elif konfirInput.upper()=="N":
                            print("Batal")  
                            break     
                        else:
                            print("Inputkan Y/N!")
                        continue
                    break
                 
    #Masuk Main menu
        elif option_sub=='3':
            break
        else:
            print("Masukkan angka 1-3")
            continue
        
#delete

def delete(table):
    while True:
        print(""" 
        ---------------Hapus Sparepart------------
        1. Hapus Barang
        2. Main Menu
        """)
        option_sub=input("Masukkan nomer yang dipilih 1/2: ")
        if option_sub=='1':
            if database==[]:
                print("Database kosong sehingga tidak ada barang yang dihapus!!")
            else:
                show(table)
                while True:
                    id=input("Masukkan ID barang yang akan dihapus: ")
                    for i,item in enumerate(database):
                        if id.upper()==item[0]:
                            break
                    else:
                        print("ID Tidak Terdaftar")
                        continue

                    tampilDel=[[id.upper(),item[1],item[2],item[3],item[4]]]
                    show(tampilDel)
                    while True:
                        print("Apakah anda yakin akan menghapus?")
                        konfir=input("Masukkan Y/N: ")
                        if konfir.upper()=='Y':
                            del table[i]
                            show(table)
                            print("Barang Berhasil Dihapus!")
                            break
                        elif konfir.upper()=='N':
                            print("barang tidak dihapus")
                            break
                        else:
                            print("Masukkan Y/N!")
                            continue 
                    break 
        elif option_sub=='2':
            break
        else:
            print("Masukkan pilihan anda angka 1/2")
            continue
        

#minimum
def minimum(table):
    while True:
        tampil=[]
        print(""" 
------------Menu Stock Yang Akan Habis--------
        1. Cek barang 
        2. Main Menu""")
        option_sub=input("Masukkan menu yang dipilih 1/2: ")
        if option_sub=='1':
            for i,item in enumerate(database):
                minimum=5
                if item[3]<minimum:
                    tampil.append(item)
                    show(tampil)
                    break
            else:
                print("stock Masih Aman, Stock Akan Tampil Jika Ada Stock Dibawah 5")
                continue

        elif option_sub=='2':
            break
        else:
            print("Masukkan angka 1/2")
            continue
        

#login
def login():
    print("-----SELAMAT DATANG DI APLIKASI GUDANG-----")
    user="Admin"
    passw="admin123"
    while True:
        username=input("Masukkan Username Anda: ")
        if username.upper()==user.upper():
            while True:
                password=input("Masukkan Password anda: ")
                if password==passw:
                    print("Selamat Datang")
                    break
                else:
                    print("password yang anda masukkan salah")
        else:
            print("Username yang anda masukkan salah: ")
            continue
        break
         

def main_menu():
    login()
    while True:
        print('''
    --------------------------------------------------------
    APLIKASI GUDANG SPAREPART OTOMOTIF

    Main Menu List:
    1. Menampilkan Daftar Sparepart
    2. Menambah Sparepart
    3. Update Sparepart
    4. Menghapus Sparepart
    5. Stock Minimum
    6. Keluar dari Program Gudang
    --------------------------------------------------------
        ''')
        option_main = input('Input Main Menu (1-5): ')

        if option_main == '1':
            read_data()
        elif option_main =='2':
            tambah(database)
        elif option_main=='3':
            update(database)
        elif option_main=='4':
            delete(database)
        elif option_main=='5':
            minimum(database)
        elif option_main=='6':
            break
        else:
            print("Opsi Yang Anda Pilih Tidak Valid! (Pilih Opsi 1-6)")
            continue

main_menu()
