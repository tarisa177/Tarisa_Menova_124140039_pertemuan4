"""Program sederhana untuk menghitung Body Mass Index (BMI)."""


def main():
    """Meminta data berat dan tinggi, lalu menampilkan kategori BMI."""
    print("=== PROGRAM PENGHITUNG BMI ===")
    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (m): "))

        if berat <= 0 or tinggi <= 0:
            print("Berat dan tinggi harus lebih dari 0.")
            return

        bmi = berat / (tinggi * tinggi)

        if bmi < 18.5:
            kategori = "Berat badan kurang"
        elif bmi < 25:
            kategori = "Berat badan normal"
        elif bmi < 30:
            kategori = "Berat badan berlebih"
        else:
            kategori = "Obesitas"

        print("\n=== HASIL PERHITUNGAN ===")
        print(f"BMI       : {bmi:.2f}")
        print(f"Kategori  : {kategori}")
    except ValueError:
        print("Masukkan angka yang valid.")


if __name__ == "__main__":
    main()
