import csv
#cara melakukan import adalah dengan cara klik file browser setelah itu disana akan ada upload file, jadi upload file yang anda inginkan.
#Variabel nim dan nama untuk menampung data terlebih dahulu sebelum di outputkan 
#Deemiteri ";" berfungsi sebagai pembatas
nim = []
nama = []
#Def menu untuk menampilkan tampilan yang akan di eksekusi atau dijalankan 
def menu():
    print("Daftar Fitur: ")
    print("[1] Menampilakan isi data")
    print("[2] Menambahkan data")
    print("[3] Mencari data")
    print("[4] Menghapus data")
    print("[5] Exit", "\n")
#Variabel pilih untuk kita memilih mana yang akan dijalankan 
#saya dapet gambaran codingan ini di petanikode mas 
#seharusnya kalau saya ngetik exit, programnya selesai mas tapi entah mengapa tetep melakukan perulangan     
    pilih = input("Masukkan pilihan: ")
    
    if pilih.lower() == "1":
        isi_data()
    elif pilih.lower() == "2":
        menambahkan_data()
    elif pilih.lower() == "3":
        a = input("Masukkan nama mahasiswa: ")
        mencari_data(a)
    elif pilih.lower() == "4":
        menghapus_data()
    elif pilih.lower() == "5":
        exit()
    else:
        print("Tidak ada di menu")
        back_to_menu()
#Def Bak_to_menu untuk memulai kembali tampilan awal         
def back_to_menu():
    menu()
#csv_reader.close() itu dihaous karena kita sudah memakai fungsi with, jadi tidak perlu 2 fungsi dan jika tidak dihapus akan menyebabkan traceback.
#"DaftarNama.csv" itu unutk melakukan import pada data yang diimportkan 
#Def isi_data untuk menampilkan isi data yang diimportkan 
def isi_data():
    with open ("DaftarNama.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ";")
        line_count = 0
        for row in csv_reader:
            nim.append(row[0])
            nama.append(row[1])
    for row in nim:
        index = nim.index(row)
        print(row, end = "")
        print(nama[index])
    back_to_menu()
#Def menambahkan_data untuk memproses penambahan data 
#mas ini dah saya coba mas, malah outpuntya tuh kadang kesamping, kadang nimnya samanamanya kebalik, terus kadang juga bener 
#pertama unutk writer.wrterow itu tidak saya beri kurung kurawal mas jadinya yang kecetak manal nim sama nama, soalnya nama sama nimnya saya jadikan sttring, terus saya coba kasik kurung kurawal bisa kecetak meskipun tidak tahu kok bisa gitu. 
def menambahkan_data():
    with open ("DaftarNama.csv", mode = "a", newline = "\n") as csv_file:
        writer = csv.writer(csv_file, delimiter = ";", quoting = csv.QUOTE_MINIMAL)
        NIM = input("Masukkan NIM: ")
        NAMA = input("Masukkan NAMA: ")
        writer.writerow({NIM, NAMA})
    back_to_menu()
#Def mencari_data unutk mencari data yang diinginkan   
#Ini mas kalau saya carri data yang sudah disediakan tuh gak muncul, tapi kalau mencari data yang saya inputkan sendiri itu muncul  
def mencari_data(a):
    cari = []
    with open ("DaftarNama.csv", mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ";")
        line_count = 0
        for row in csv_reader:
            if row:
                nim.append(row[0])
                nama.append(row[1])

        for data in nama:
            if data == a:
                i = nama.index(data)
                cari.append(nim[i] + ' - ' + nama[i])

        if len(cari) > 0:
            print(cari[0])
        else:
            print("Tidak ada data ditemukan")
    back_to_menu()
#Dah mas nyerah yang menghapus data, konsepnya beda sama di petanikode
def menghapus_data():
    delete = []
    with open ("DaftarNama.csv", mode = "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ";")
        line_count = 0
        for row in csv_reader:
            delete.append(row)
    index = 0
    for hadeh in row:
        if hadeh["NIM"] == nim:
            delete.remove(row[index])
            index = index + 1

#If pada line terakhir berfungsi untuk melakukan perulangan
if __name__ == "__main__":
    while True:
        menu()