#Sistem Antrean Klinik Cahaya Medika Singaparna
def buat_pasien(no_antrean, nama, poli, daftar_keluhan):
    return {
        #TUPLE: Identitas tetap
        "identitas": (no_antrean, nama, poli),
        #ARRAY: Daftar keluhan dinamis  
        "keluhan": list(daftar_keluhan),
        #LINKED LIST: Penunjuk pasien berikutnya      
        "next": None                            
    }
def tambah_ke_antrean(head, pasien_baru):
    if not head:
        return pasien_baru
    sekarang = head
    while sekarang["next"]:
        sekarang = sekarang["next"]
    sekarang["next"] = pasien_baru
    return head
def tampilkan_antrean(head):
    print("\n=== DAFTAR ANTREAN KLINIK CAHAYA MEDIKA SINGAPARNA ===")
    if not head:
        print("Antrean saat ini kosong.\n")
        return
    sekarang = head
    while sekarang:
        no, nama, poli = sekarang["identitas"]
        keluhan_str = ", ".join(sekarang["keluhan"])
        print(f"[{no}] {nama} - {poli} | Keluhan: {keluhan_str}")
        sekarang = sekarang["next"]
    print()
# PROGRAM UTAMA (INPUT PENGGUNA)         
antrean_depan = None
nomor_urut = 1

while True:
    print("=================================================")
    print("| Sistem Antrean Klinik Cahaya Medika Singaparna|")
    print("=================================================")
    print("|1. Daftar Pasien Baru                          |")
    print("|2. Tambah Keluhan Pasien Terdepan              |")
    print("|3. Panggil Pasien Terdepan                     |")
    print("|4. Lihat Daftar Antrean                        |")
    print("|5. Keluar                                      |")
    print("=================================================")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        no_antrean = f"A-0{nomor_urut}"
        nama = input("Masukkan nama pasien: ")
        poli = input("Masukkan poli tujuan (Umum/Gigi): ")
        keluhan_awal = input("Masukkan keluhan awal: ")
        
        pasien_baru = buat_pasien(no_antrean, nama, poli, [keluhan_awal])
        antrean_depan = tambah_ke_antrean(antrean_depan, pasien_baru)
        nomor_urut += 1
        print(f"[Info] Pasien {nama} terdaftar dengan nomor {no_antrean}.\n")

    elif pilihan == "2":
        if antrean_depan:
            keluhan_baru = input("Masukkan keluhan tambahan: ")
            antrean_depan["keluhan"].append(keluhan_baru)  # Operasi Array
            print("[Info] Keluhan berhasil ditambahkan.\n")
        else:
            print("[!] Belum ada pasien di antrean.\n")

    elif pilihan == "3":
        if antrean_depan:
            no, nama, poli = antrean_depan["identitas"]  # Unpacking Tuple
            print("****************************************************")
            print(f"\n>> MEMANGGIL: Nomor {no} ({nama}) silakan masuk ke {poli}.\n")
            print("****************************************************")
            antrean_depan = antrean_depan["next"]  # Operasi Linked List
        else:
            print("[!] Antrean sudah kosong.\n")

    elif pilihan == "4":
        tampilkan_antrean(antrean_depan)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("[!] Pilihan tidak valid, silakan coba lagi.\n")