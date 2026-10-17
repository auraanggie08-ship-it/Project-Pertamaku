nama = input("Masukkan nama: ")
berat = float(input("Masukkan berat badan (kg): "))
tinggi = float(input("Masukkan tinggi badan (meter): "))

bmi = berat / (tinggi ** 2)

print()
print("Nama :", nama)
print(f"BMI  : {bmi:.2f}")