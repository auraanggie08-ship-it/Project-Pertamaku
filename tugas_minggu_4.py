# Input data buku
harga_buku = int(input("Harga buku :"))
jumlah_buku = int (input("Jumlah buku :"))
                   
# Input data pulpen
harga_pulpen = int(input("Harga pulpen :"))
jumlah_pulpen = int(input("Jumlah pulpen :"))

# Input data tas
harga_tas = int(input("Harga tas :"))
jumlah_tas = int(input("Jumlah tas :"))

# Hitung subtotal
total_buku = harga_buku * jumlah_buku
total_pulpen = harga_pulpen * jumlah_pulpen
total_tas = harga_tas * jumlah_tas

# Hitung total belanja
total_belanja = total_buku + total_pulpen + total_tas

# Tampilkan hasil
print("Total belanja: Rp", total_belanja)