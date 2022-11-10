#kita import library yang kita butuhkan
from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

#untuk mengambil input dari user
i=input("masukkan angka")
i =  int(i) #kita rubah jadi integer
#kita buat function untuk mengenentukan ganjil genap
def gg(i):
  i+=1
  if (i%2) ==  0:
    print(i, 'genap - ID Proses', getpid())
  else:
      print(i, 'ganjil - ID Proses', getpid())
  sleep(1)

#proses Sekuensial
print('sekuensial')
sekuensial_awal = time()

for a in range(i):
    gg(a)

sekuensial_akhir = time()

#proses MUlti processing 
print('Multi Processing proses')
kumpulan_proses = []

process_awal = time()

for a in range(i):
    p = Process(target=gg, args=(a,))
    kumpulan_proses.append(p)
    p.start()

for a in kumpulan_proses:
    p.join()
    
process_akhir = time()

#proses multi processing kelas pool
print('multi processing pool')

pool_awal = time()

pool = Pool()
pool.map(gg, range(0,i))
pool.close()

pool_akhir = time()

print("Sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Kelas Process :", process_akhir - process_awal, "detik")
print("Kelas Pool :", pool_akhir - pool_awal, "detik")
 
