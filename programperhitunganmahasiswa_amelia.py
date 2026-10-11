# Input nama mahasiswa
nama = input("Masukkan nama mahasiswa: ")

# Input nilai tugas, UTS, dan UAS
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

# Menghitung nilai akhir berdasarkan bobot (Tugas 30%, UTS 30%, UAS 40%)
nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)

# Menentukan status kelulusan (Minimal 60 untuk Lulus)
if nilai_akhir >= 60:
    status = "Lulus"
else:
    status = "Belum Lulus"

# Menampilkan hasil
print("\n--- HASIL PENILAIAN ---")
print(f"Nama Mahasiswa : {nama}")
print(f"Nilai Akhir    : {nilai_akhir:.2f}")
print(f"Status         : {status}")
