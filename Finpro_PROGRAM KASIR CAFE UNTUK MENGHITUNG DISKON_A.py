def menu_minuman():
	print("    BEVERAGES           PRICE")
	print("-------------------------------------")
	print(" Ice Chocolate          12000")
	print(" Ice Matcha Latte       15000")
	print(" Ice Americano          10000")
	print(" Ice Thai Tea           10000")
	print(" Ice Vanilla Latte      20000")
	print("-------------------------------------")
	print("\n")

def menu_makanan():
	print("      FOODS             PRICE")
	print("-------------------------------------")
	print(" Spicy Karage Rice      20000")
	print(" Chicken Fried Rice     15000")
	print(" French Toast           13000")
	print(" BBQ French Fries       15000")
	print(" Choco Toast            14000")
	print("-------------------------------------")
	print("\n")

def daftar_diskon():
    print("       MENU LIST           DISCOUNT  ")
    print("---------------------------------------------")
    print(" 2 Ice Vanilla Latte         20%     ")
    print(" 2 Ice Americano             10%     ")
    print(" 2 BBQ French Fries          10%     ")
    print(" 2 Choco Toast               10%     ")
    print("----------------------------------------------")
    print("\n")

def pemesanan():
    global totalminum
    global jumlahminum
    global menuminum
    global pembeli
    global hargaminum
    global diskonmin
    pembeli=str(input("Masukkan nama Pembeli: "))
    print("\n")
    print("Menu Minuman")
    kode=(str(input("Masukkan nama menu : ")))
    if(kode=="Ice Chocolate"):
        menuminum=("Ice Chocolate")
        jumlahminum=int(input("Masukkan jumlah : "))
        totalminum=12000*jumlahminum
        print("Total harga minuman: ", totalminum)
    elif(kode=="Ice Matcha Latte"):
        menuminum=("Ice Matcha Latte")
        jumlahminum=int(input("Masukkan jumlah : "))
        totalminum=15000*jumlahminum
        print("Total harga minuman: ", totalminum)
    elif(kode=="Ice Americano"):
        menuminum=("Ice Americano")
        jumlahminum=int(input("Masukkan jumlah: "))
        if(jumlahminum==2):
            hargaminum=10000
            print("Harga satuan : ", hargaminum)
            diskonmin=("10%")
            print("Diskon : ", diskonmin)
            totalminum=(hargaminum*jumlahminum)-(hargaminum*(10/100))
            print("Total harga minuman : ", totalminum)
        else:
            totalminum=10000*jumlahminum
            print("Total harga minuman : ", totalminum)
    elif(kode=="Ice Thai Tea"):
        menuminum=("Ice Thai Tea")
        jumlahminum=int(input("Masukkan Jumlah : "))
        totalminum=10000*jumlahminum
        print("Total harga minuman : ", totalminum)
    elif(kode=="Ice Vanilla Latte"):
        menuminum=("Ice Vanilla Latte")
        jumlahminum=print(int(input("Masukkan jumlah : ")))
        if(jumlahminum==2):
            hargaminum=20000
            print("Harga satuan : ", hargaminum)
            diskonmin=("20%")
            print("Diskon : ", diskonmin)
            totalminum=(hargaminum*jumlahminum)-(hargaminum*(20/100))
            print("Total harga minuman : ", totalminum)
        else:
            totalminum=20000*jumlahminum
            print("Total harga minuman : ", totalminum)
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
    print("\n")
    global totalmakan
    global jumlahmakan
    global menumakan
    global hargamakan
    global diskonmak
    print("Menu Makanan")
    kode2=(str(input("Masukkan nama menu : ")))
    if(kode2=="Spicy Karage Rice"):
        menumakan=("Spicy Karage Rice")
        jumlahmakan=int(input("Masukkan jumlah : "))
        totalmakan=20000*jumlahmakan
        print("Total harga makanan: ", totalmakan)
    elif(kode2=="Chicken Fried Rice"):
        menumakan=("Chicken Fried Rice")
        jumlahmakan=int(input("Masukkan jumlah : "))
        totalmakan=15000*jumlahmakan
        print("Total harga makanan: ", totalmakan)
    elif(kode2=="BBQ French Fries"):
        menumakan=("BBQ French Fries")
        jumlahmakan=int(input("Masukkan jumlah: "))
        if(jumlahmakan==2):
            hargamakan=15000
            print("Harga satuan : ", hargamakan)
            diskonmak=("10%")
            print("Diskon : ", diskonmak)
            totalmakan=(15000*jumlahmakan)-(15000*(10/100))
            print("Total harga makanan: ", totalmakan)
        else:
            totalmakan=15000*jumlahmakan
            print("Total harga makanan: ", totalmakan)
    elif(kode2=="French Toast"):
        menumakan=("French Toast")
        jumlahmakan=int(input("Masukkan jumlah : "))
        totalmakan=13000*jumlahmakan
        print("Total harga makanan: ", totalmakan)
    elif(kode2=="Choco Toast"):
        menumakan=("Choco Toast")
        jumlahmakan=int(input("Masukkan jumlah: "))
        if(jumlahmakan==2):
            hargamakan=14000
            print("Harga satuan : ", hargamakan)
            diskonmak=("10%")
            print("Diskon : ", diskonmak)
            totalmakan=(14000*jumlahmakan)-(14000*(10/100))
            print("Total harga makanan: ", totalmakan)
        else:
            totalmakan=14000*jumlahmakan
            print("Total harga makanan: ", totalmakan)
    else:
        print("Pilihan tidak ada, silahkan masukan lagi!!")
    print("\n")
    global tunai
    global totalsemua
    global kembalian
    tunai=int(input("Berapa jumlah tunai: "))
    totalsemua=totalmakan+totalminum
    kembalian=tunai-totalsemua
    print("\n")

def struk_pembayaran():
    print("                              Lotus Cafe			                       ")
    print("     Jl. Rungkut Asri Tim. XVIII, Medokan Ayu, Kota SBY, Jawa Timur     ")
    print("------------------------------------------------------------------------")
    print("Customer : ",pembeli)
    print("Beverages : ", jumlahminum, menuminum, "(",totalminum,")")
    print("Foods : ", jumlahmakan, menumakan, "(",totalmakan,")")
    print("------------------------------------------------------------------------")
    print("Total : ", totalsemua)
    print("Cash : ", tunai)
    print("Charge : ", kembalian)
    print("\n")

def menu_awal():
		print("      CASHIER       ")
		print("--------------------")
		print(" Menu List Minuman  ")
		print(" Menu List Makanan  ")
		print(" Daftar Menu Diskon ")
		print(" Pemesanan          ")
		print(" Struk Pembayaran   ")
		print("--------------------")
		m=str(input("Apa yang ingin dipilih: "))
		print()
		if(m=="Menu List Minuman"):
			menu_minuman()
		elif(m=="Menu List Makanan"):
			menu_makanan()
		elif(m=="Daftar Menu Diskon"):
			daftar_diskon()
		elif(m=="Pemesanan"):
			pemesanan()
		elif(m=="Struk Pembayaran"):
			struk_pembayaran()
		else:
			exit()
menu_awal()

if __name__ == "__main__":

    while(True):
        menu_awal()