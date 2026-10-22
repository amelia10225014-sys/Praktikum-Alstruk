#Simpan nama mahasiswa dalam variabel string
nama_mhs1 = "Afni Nurafifah"
#Simpan nilai tugas dan nilai ujian dalam variabel numerik.
nilai_tugas1 = 70.0
nilai_ujian1 = 65.0
#Hitung rata-rata kedua nilai
rata_rata1 = (nilai_tugas1 + nilai_ujian1) / 2
#Memeriksa status kelulusan mahasiswa (minimal 75)
status_lulus1 = rata_rata1 >= 75
#Menampilkan hasil rekapan nilai
print("=== REKAP NILAI MAHASISWA UJI COBA) ===")
print(f"Nama Mahasiswa : {nama_mhs1}")
print(f"Nilai Tugas    : {nilai_tugas1}")
print(f"Nilai Ujian    : {nilai_ujian1}")
print(f"Rata-rata Nilai: {rata_rata1}")
print(f"Status Lulus   : {status_lulus1}")
print("-" * 40)





