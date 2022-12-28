# -*- coding: utf-8 -*-
#membuat function yang dibutuhkan
#function perhitungan
#deret aritmatika
def deret_aritmatika(a1, n, d):
    deret = []
    jumlah = 0
    for i in range(1, n + 1):
        elemen_berikutnya = a1 + (i - 1) * d
        deret.append(elemen_berikutnya)
        jumlah += elemen_berikutnya 
    return print('Baris deret aritmatika=', deret, 'menghasilkan jumlah',jumlah)

#deret geometri
def deret_geometri(a, n, r):
    deret = [ ]
    jumlah = 0
    for i in range(1, n+1):
        elemen_berikutnya = a * (r **(i-1))
        deret.append(elemen_berikutnya)
        jumlah += elemen_berikutnya
    return print('Baris deret geometri=', deret, 'menghasilkan ',jumlah)

#deret pangkat
def deret_pangkat(a, b):
    deret = [a, ]
    c=a
    for i in range(1, b):
        a*=c
        deret.append(a)
    return print(deret)
    
#deret ganjil
def deret_ganjil(u1,n):
    deret=[ ]
    while len(deret) < n:
        c = u1 % 2
        if c != 0:
            deret.append(u1)
        else:
            pass
        u1+=1
    return print(deret)

#deret genap
def deret_genap(u1,n):
    deret=[ ]
    while len(deret) < n:
        c = u1 % 2
        if c == 0:
            deret.append(u1)
        else:
            pass
        u1+=1
    return print(deret)

#function tampilan
#tampil (agar output teks terlihat seperti mengetik)
def tampil(teks):
    import time
    for char in teks:
        print(char, end="")
        time.sleep(0.05)

#tampil menu
def tampil_menu():
    print(' '.center(100, '~'))
    import datetime
    x = int(datetime.datetime.now().strftime("%H"))
    if x <= 12:
        tampil('Haiii, Selamat Pagi, Selamat Datang ditempat Menghitung Deret\n`Doing mathematics should always mean finding patterns and crafting beautiful and meaningful explanations.` — Paul Lockhart')
    elif x <= 15:
        tampil('Haiii, Selamat Siang, Selamat Datang ditempat Menghitung Deret,\n`Math is sometimes called the science of patterns.`- Ronald Graham')
          
    elif x <= 18:
        tampil('Haiii, Selamat Sore, Selamat Datang ditempat Menghitung Deret, \n`Mathematics is the key and door to the sciences.` — Galileo Galilei')
    else :
        tampil('Haiii, Selamat Malam, Selamat Datang ditempat Menghitung Deret, \n`Math is like going to the gym for your brain. It sharpens your mind.` — Danica Mckellar')
    
    tampil('\nKesusahan dalam menghitung deret matematika? \nGwenchana, kami akan membantu mu')
    jawab = int(input('Ketik\n 1 untuk Lanjut\n 2 untuk Exit\n'))
    print(' '.center(100, '~'))
    return jawab

#exit
def exit():
    print(' '.center(100, '~'))
    print('Terimakasih telah berkunjung'.center(100))
    print(''.center(100, '~'))
    return 2

#lanjut
def lanjut():
    print(' '.center(100, '~'))
    tampil('Shapp, Kami akan membantumu dalam menghitung deret matematika,\n Sebelum itu Deret apa yang kamu ingin kami bantu?')
    jawab = int(input('Untuk memilih deret ketik\n 1 untuk Deret Aritmatika\n 2 Deret Geometri\n 3 Deret Pangkat\n 4 Deret Ganjiln\ 5 Deret Genap'))
    print(' '.center(100, '~'))
    return jawab

#lanjut2
def lanjut2():
    print(' '.center(100, '~'))
    tampil('apakah kamu masih memerlukan bantuan kami?')
    jawab =  int(input('ketik\n 1 iyaa \n 2 tidak, saya sudah selesai'))
    print(' '.center(100, '~'))
    return jawab

#deret aritmatika penjelesan
def deret_aritmatika_penjelasan():
    print(' '.center(100, '~'))
    tampil('Sebelum itu, yuk kita pahamin dulu tentang deret aritmatika itu sendiri')
    tampil('\nDeret aritmatika adalah sebuah deret bilangan yang setiap bilangan di dalamnya merupakan hasil penambahan bilangan yang sama terhadap bilangan sebelumnya.\n Contohnya, deret aritmatika dengan beda 2 dan awal 4 adalah: 4, 6, 8, 10, 12, 14, 16, 18, dan seterusnya. ')
    tampil('\nUntuk menghitung deret aritmatika, kita harus mengetahui 3 hal antara lain \n U1 yaitu bilangan pertama pada deret\n n yaitu suku bilangan ke n yaang ingin diketahui pada deret\n d yaitu pembeda antar bilangan pada deret ')
    tampil('\nUntuk mengetahui d kita bisa memenghitung dengan cara d = (bilangan ke-n - bilangan awal) / (n - 1) ')
    tampil('\nUntuk menghitung deret aritmatika kita bisa menggunakan rumus bilangan ke-n = bilangan awal + (n - 1) * d')
    tampil('\nNah sekarang yuk kita hitung deret aritmatikanya')
    u1 = int(input('Masukkan nilai U1'))
    n = int(input('Masukkan nilai n'))
    d = int(input('Masukkan nilai d atau pembeda'))
    print(' '.center(100, '~'))
    return(u1, n, d)

#deret geometri penjelasan
def deret_geometri_penjelasan():
    print(' '.center(100, '~'))
    tampil('\nSebelum itu, yuk kita pahamin dulu tentang deret geometri itu sendiri')
    tampil('\nDeret Geometri adalah suatu deret bilangan yang memiliki rasio atau perbandingan yang tetap.')
    tampil('\nUntuk menghitung deret geometri, kita harus mengetahui 3 hal antara lain \n U1 yaitu bilangan pertama pada deret\n n yaitu suku bilangan ke n yaang ingin diketahui pada deret\n r yaitu rasio atau pembeda antar bilangan pada deret ')
    tampil('\nNah sekarang yuk kita hitung deret geometrinya')
    u1 = int(input('Masukkan nilai U1'))
    n = int(input('Masukkan nilai n'))
    r = int(input('Masukkan nilai r '))
    print(' '.center(100, '~'))
    return (u1, n, r)

#deret pangkat penjelasan
def deret_pangkat_penjelasan():
    print(' '.center(100, '~'))
    tampil('\nSebelum itu, yuk kita pahamin dulu tentang deret pangkat itu sendiri')
    tampil('\nDeret pangkat adalah suatu deret yang terdiri dari elemen yang merupakan pangkat dari suatu bilangan.')
    tampil('\nUntuk menghitung deret pangkat, kita harus mengetahui 2 hal antara lain \n U1 yaitu bilangan pertama pada deret\n n yaitu suku bilangan ke n yaang ingin diketahui pada deret')
    tampil('\nNah sekarang yuk kita hitung deret pangkat')
    u1 = int(input('Masukkan nilai U1'))
    n = int(input('Masukkan nilai n'))
    print(' '.center(100, '~'))
    return (u1, n)

#deret ganjil genap penjelasan
def deret_ganjilgenap_penjelasan():
    print(' '.center(100, '~'))
    tampil('\nSebelum itu, yuk kita pahamin dulu tentang deret ganjil/genap itu sendiri')
    tampil('\nDeret ganjil/genap suatu deret bilangan yang terdiri dari bilangan-bilangan ganjil/genap saja.')
    tampil('\nUntuk menghitung deret ganjil/genap, kita harus mengetahui 2 hal antara lain \n U1 yaitu bilangan pertama pada deret\n n yaitu suku bilangan ke n yaang ingin diketahui pada deret')
    tampil('\nNah sekarang yuk kita hitung deret pangkat')
    u1 = int(input('Masukkan nilai U1'))
    n = int(input('Masukkan nilai n'))
    print(' '.center(100, '~'))
    return (u1, n)


#membuat kode program dari function - function diatas
x = 0
jawab = tampil_menu()
while x <= 1:
    if jawab == 1:
        jawab = lanjut()
        if jawab == 1:
            u1, n, d = deret_aritmatika_penjelasan()
            deret_aritmatika(u1, n, d)
        elif jawab == 2:
            u1, n, d = deret_geometri_penjelasan()
            deret_geometri(u1, n, d)
        elif jawab == 3:
            u1, n = deret_pangkat_penjelasan()
            deret_pangkat(u1, n)
        elif jawab == 4:
            u1, n = deret_ganjilgenap_penjelasan()
            deret_ganjil(u1,n)
        elif jawab == 5:
            u1, n = deret_ganjilgenap_penjelasan()
            deret_genap(u1, n)
        jawab=lanjut2() 
    else:
        jawab = exit()
        x+=jawab