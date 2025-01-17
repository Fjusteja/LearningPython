# program manage contact
from random import choice

from setuptools.msvc import PLAT_SPEC_TO_RUNTIME

kontak1 = {'nama' : "Steven", 'HP': '123456789', 'email': 'S@gmail.com'}
kontak2 = {'nama' : "Felix", 'HP': '987654321', 'email': 'F@gmail.com'}
kontak3 = {'nama' : "J", 'HP': '87654321', 'email': 'J@gmail.com'}
kontak =[kontak1,kontak2,kontak3]

while True:
    print("\nMenu Kontak")
    print("1. View All Contact")
    print("2. Add new contact")
    print("3. Del Contact")
    print("4. Exit")

    Choice = input("Masukan pilihan (1,2,3,4) : ")

    if Choice == '1':
        # melihat semua kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print("kontak masih kosong!")

    elif Choice == '2':
        # + kontak
        nama = input("Masukan Nama: ")
        HP = input("Masukan HP: ")
        email = input ("Masukan Email: ")
        kontakb = {'nama':nama, 'HP':HP, 'email':email}
        kontak.append(kontakb)
        print("success")

    elif Choice == '3':
        # hapus kontak
        if kontak:
            for num, item in enumerate(kontak, start=1):
                print(f'\n{num}. {item["nama"]} ({item["HP"]}, {item["email"]})')
        else:
            print ("kontak masih kosong!")
            continue

        i_del = int(input("masukan ID del: "))
        del kontak[i_del-1]
        print("kontak sudah dihapus")
    elif Choice == '4':
        # Keluar
        break
    else:
        print("pilihan salah")