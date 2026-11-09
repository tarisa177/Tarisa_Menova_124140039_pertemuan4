"""Program utama untuk menguji modul math_operations."""

import math_operations
from math_operations import (
    luas_persegi,
    keliling_persegi,
    celsius_ke_fahrenheit,
    celsius_ke_kelvin,
)


def main():
    """Memanggil seluruh fungsi dari modul matematika dan mencetak hasil."""
    print("=== PENGUJIAN MODUL MATEMATIKA ===")

    sisi = 5
    print("\n1. Persegi (sisi = 5)")
    print(f"Luas       : {luas_persegi(sisi):.2f}")
    print(f"Keliling   : {keliling_persegi(sisi):.2f}")

    panjang, lebar = 8, 4
    print("\n2. Persegi panjang (panjang = 8, lebar = 4)")
    print(f"Luas       : "
          f"{math_operations.luas_persegi_panjang(panjang, lebar):.2f}")
    print(f"Keliling   : "
          f"{math_operations.keliling_persegi_panjang(panjang, lebar):.2f}")

    jari_jari = 7
    print("\n3. Lingkaran (jari-jari = 7)")
    print(f"Luas       : "
          f"{math_operations.luas_lingkaran(jari_jari):.2f}")
    print(f"Keliling   : "
          f"{math_operations.keliling_lingkaran(jari_jari):.2f}")
    print(f"Konstanta PI: {math_operations.PI}")

    suhu = 25
    print("\n4. Konversi suhu (25 Celsius)")
    print(f"Fahrenheit : {celsius_ke_fahrenheit(suhu):.2f} F")
    print(f"Kelvin     : {celsius_ke_kelvin(suhu):.2f} K")


if __name__ == "__main__":
    main()
