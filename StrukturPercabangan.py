# Program Menghitung Diskon Belanja
# Menggunakan Struktur Percabangan (if-elif-else)

print("=== SISTEM KASIR TOKO MATAHARI ===")

# Mengambil input total belanja dari pengguna
total_belanja = float(input("Masukkan total belanja pelanggan (Rp): "))

# Proses percabangan untuk menentukan persentase diskon
if total_belanja >= 500000:
    persen_diskon = 10
elif total_belanja >= 100000:
    persen_diskon = 5
else:
    persen_diskon = 0

# Menghitung jumlah potongan harga dan total yang harus dibayar
potongan_harga = total_belanja * (persen_diskon / 100)
total_bayar = total_belanja - potongan_harga

# Menampilkan hasil output
print("-" * 32)
print(f"Diskon yang didapat : {persen_diskon}%")
print(f"Potongan harga      : Rp {potongan_harga:,.0f}")
print(f"Total yang dibayar  : Rp {total_bayar:,.0f}")
print("================================")
