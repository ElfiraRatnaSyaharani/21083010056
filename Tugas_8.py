from os import getpid
from time import time, sleep
from multiprocessing import cpu_count, Pool, Process

x = int(input())
def cetak(i):
    print(i+1, ("Ganjil" if (i%2==0) else "Genap"), "- ID proses", getpid())
    sleep(1)
print("\n")

print("Sekuensial")
sekuensial_awal = time()
for i in range(x):
    cetak(i)
sekuensial_akhir = time()
print("\n")

print("multiprocessing.Process")
kumpulan_proses = []
process_awal = time()
for i in range(x):
    p = Process(target=cetak, args=(i,))
    kumpulan_proses.append(p)
    p.start()
for i in kumpulan_proses:
    p.join()
process_akhir = time()
print("\n")

print("multiprocessing.Pool")
pool_awal = time()
pool = Pool()
pool.map(cetak, range(0,x))
pool.close()
pool_akhir = time()
print("\n")

print("Waktu eksekusi sekuensial :", sekuensial_akhir - sekuensial_awal, "detik")
print("Waktu eksekusi multiprocessing.Process :", process_akhir - process_awal, "detik")
print("Waktu eksekusi multiprocessing.Pool :", pool_akhir - pool_awal, "detik")
