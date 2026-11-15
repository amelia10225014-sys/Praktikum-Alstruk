#Setiap tiket/jadwal disimpan sebagai Tuple: (Kode, Rute, Jam_Berangkat, Nomor_Kursi)
tiket_kereta_1 = ("KA-102", "Gambir - Bandung", "08:30 WIB", "Eks-2 / 4A")
tiket_pesawat_1 = ("GA-404", "CGK - DPS", "14:15 WIB", "12F")

#Mengakses informasi spesifik berdasarkan indeks
print(f"Kode Perjalanan : {tiket_kereta_1[0]}")
print(f"Jam Keberangkatan: {tiket_kereta_1[2]}")

#Tuple Unpacking (Membongkar isi tuple ke variabel terpisah agar mudah dibaca)
kode, rute, jam, kursi = tiket_pesawat_1
print(f"\n[E-TICKET PESAWAT]\nPenerbangan {kode} ({rute}) berangkat pukul {jam} | Kursi: {kursi}")

#Menyimpan daftar jadwal keberangkatan (List berisi Tuple)
jadwal_stasiun = [
    ("KA-102", "Gambir - Bandung", "08:30 WIB", "Tepat Waktu"),
    ("KA-205", "Pasar Senen - Yogyakarta", "10:00 WIB", "Tepat Waktu"),
    ("KA-308", "Gambir - Surabaya", "13:45 WIB", "Delay 15 Menit")
]
print("\n--- Papan Informasi Keberangkatan ---")
for kode_ka, tujuan, waktu, status in jadwal_stasiun:
    print(f"{waktu} | {kode_ka} | Tujuan: {tujuan:<25} | Status: {status}")

#Keamanan Data (Immutability)
# Jika ada bagian kode yang mencoba mengubah nomor kursi atau jam secara langsung, Python akan menolak:
try:
    tiket_kereta_1[3] = "Eks-1 / 1A"
except TypeError as e:
    print(f"\nProteksi Sistem: Data tiket tidak dapat diubah langsung ({e})")
