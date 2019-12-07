angka1 =int(input('Masukan Angka pertama :'))
angka2 =int(input('Masukan Angka Kedua   :'))
print('operator \n: 1.Jumlah \n 2.Kurang \n' 
        '3.Perkalian \n4.Pembagian')
pilih=int(input('Pilih Operator : '))
if pilih == 1 :
    tambah = angka1 + angka2
    print('Hasilnya Adalah : ',tambah )

elif pilih == 2 :
    kurang = angka1 - angka2
    print('Hasilnya  Adalah : ',kurang )

elif pilih == 3 :
    kali = angka1 * angka2
    print('Hasilnya  Adalah : ',kali )

elif pilih == 4 :
    bagi = angka1 / angka2
    print('Hasilnya Adalah : ',bagi )


else:
    print('OPerator yang anda masukan salah !!!!')
