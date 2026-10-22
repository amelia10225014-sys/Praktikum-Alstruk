# Membuat variabel nilai dan kehadiran
nilai = 75
kehadiran = 90

print("=== PRAKTIKUM 3 OPERATOR PERBANDINGAN DAN LOGIKA ===")

# Operator >= untuk masing-masing syarat
print("Nilai >= 75        :", nilai >= 75)
print("Kehadiran >= 80    :", kehadiran >= 80)

# Menggunakan operator and
print("Lulus (and)        :", nilai >= 75 and kehadiran >= 80)

# Ubah nilai menjadi 70
print("\n--- Setelah nilai = 70 ---")
nilai = 70
print("Nilai >= 75        :", nilai >= 75)
print("Lulus (and)        :", nilai >= 75 and kehadiran >= 80)

# Menggunakan operator or (Pastikan variabel 'nilai' ditulis kembali di sebelah kiri)
print("Lulus (or)         :", nilai >= 75 or kehadiran >= 80)
