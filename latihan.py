
# Masukkan nilai
presensi = float(input("Masukkan presensi:"))
tugas = float(input("Masukkan tugas:"))
uts = float(input("Masukkan UTS:"))
uas = float(input("Masukkan UAS:"))

# Hitung nilai
nilai_presensi = presensi * 0.10
nilai_tugas = tugas * 0.20
nilai_uts = uts * 0.30
nilai_uas = uas * 0.40

# Hitung nilai akhir
nilai_akhir = nilai_presensi + nilai_tugas + nilai_uts + nilai_uas

# Tentukan kelulusan
if nilai_akhir >= 55:
    status = "LULUS"
else:
    status = "TIDAK LULUS"

# Cetak hasil
print("Nilai akhir:", nilai_akhir)
print("Status     :", status)