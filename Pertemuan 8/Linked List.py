# Implementasi Kalender Meja Flip Harian (Doubly Linked List tanpa Class/Objek)
def buat_lembar(hari, tanggal, catatan):
    return {
        "hari": hari,
        "tanggal": tanggal,
        "catatan": catatan,
        "next": None,  # Penunjuk ke hari berikutnya
        "prev": None   # Penunjuk ke hari sebelumnya
    }
def lihat_kalender(lembar_aktif):
    if lembar_aktif:
        print("+---------------------------------------+")
        print(f"| {lembar_aktif['hari'].upper()}, {lembar_aktif['tanggal']:<29} |")
        print(f"| Catatan: {lembar_aktif['catatan']:<28} |")
        print("+---------------------------------------+")
def balik_maju(lembar_aktif):
    if lembar_aktif and lembar_aktif["next"]:
        print(">> Membalik kalender ke hari berikutnya...")
        lembar_aktif = lembar_aktif["next"]
        lihat_kalender(lembar_aktif)
    else:
        print("[!] Sudah mencapai lembar terakhir.")
    return lembar_aktif
def balik_mundur(lembar_aktif):
    if lembar_aktif and lembar_aktif["prev"]:
        print("<< Membalik kalender mundur ke hari sebelumnya...")
        lembar_aktif = lembar_aktif["prev"]
        lihat_kalender(lembar_aktif)
    else:
        print("[!] Ini adalah lembar pertama.")
    return lembar_aktif
# --- Simulasi Penggunaan ---
#Membuat data lembaran kalender
senin = buat_lembar("Senin", "16 November 2026", "Rapat Proyek Pagi")
selasa = buat_lembar("Selasa", "17 November 2026", "Deadline Tugas")
rabu = buat_lembar("Rabu", "18 November 2026", "Olahraga Sore")

#Menyambungkan rantai dua arah (Doubly Linked List)
senin["next"] = selasa
selasa["prev"] = senin

selasa["next"] = rabu
rabu["prev"] = selasa

#Menentukan lembar yang sedang menghadap ke depan
lembar_sekarang = senin
lihat_kalender(lembar_sekarang)

#Membalik maju ke Selasa, lalu Rabu
lembar_sekarang = balik_maju(lembar_sekarang)
lembar_sekarang = balik_maju(lembar_sekarang)

#Membalik mundur kembali ke Selasa
lembar_sekarang = balik_mundur(lembar_sekarang)
