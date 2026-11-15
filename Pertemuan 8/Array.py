#Implementasi Daftar Pesanan Kafe menggunakan List (Array)
daftar_pesanan = ["Espresso", "French Fries", "Matcha Latte"]

#Menambah pesanan baru (Append - O(1))
daftar_pesanan.append("Cappuccino")
print(f"Pesanan masuk: {daftar_pesanan}")

#Mengakses pesanan berdasarkan urutan/indeks (Akses cepat - O(1))
print(f"Pesanan pertama yang harus dibuat: {daftar_pesanan[0]}")

#Pelanggan membatalkan pesanan tertentu
daftar_pesanan.remove("French Fries")
print(f"Setelah pembatalan: {daftar_pesanan}")

#Menyelesaikan pesanan pertama (Pop dari indeks 0)
selesai = daftar_pesanan.pop(0)
print(f"Pesanan '{selesai}' selesai! Sisa antrean: {daftar_pesanan}")
