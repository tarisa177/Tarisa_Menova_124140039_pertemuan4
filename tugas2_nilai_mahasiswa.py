"""Program pengelolaan nilai akhir dan grade mahasiswa."""


def hitung_nilai_akhir(nilai_uts, nilai_uas, nilai_tugas):
    """Menghitung nilai akhir dari UTS, UAS, dan tugas.

    Args:
        nilai_uts (float): Nilai UTS.
        nilai_uas (float): Nilai UAS.
        nilai_tugas (float): Nilai tugas.

    Returns:
        float: Nilai akhir berbobot.
    """
    return (0.30 * nilai_uts) + (0.40 * nilai_uas) + (0.30 * nilai_tugas)


def tentukan_grade(nilai_akhir):
    """Menentukan grade berdasarkan nilai akhir.

    Args:
        nilai_akhir (float): Nilai akhir mahasiswa.

    Returns:
        str: Grade A, B, C, D, atau E.
    """
    if nilai_akhir >= 80:
        return "A"
    elif nilai_akhir >= 70:
        return "B"
    elif nilai_akhir >= 60:
        return "C"
    elif nilai_akhir >= 50:
        return "D"
    return "E"


def main():
    """Menghitung dan menampilkan nilai seluruh mahasiswa."""
    mahasiswa = [
        {"nama": "Andi", "nim": "124140001", "nilai_uts": 85,
         "nilai_uas": 90, "nilai_tugas": 88},
        {"nama": "Budi", "nim": "124140002", "nilai_uts": 70,
         "nilai_uas": 75, "nilai_tugas": 80},
        {"nama": "Citra", "nim": "124140003", "nilai_uts": 92,
         "nilai_uas": 95, "nilai_tugas": 90},
        {"nama": "Dina", "nim": "124140004", "nilai_uts": 60,
         "nilai_uas": 65, "nilai_tugas": 70},
        {"nama": "Eko", "nim": "124140005", "nilai_uts": 45,
         "nilai_uas": 50, "nilai_tugas": 55},
    ]

    for data in mahasiswa:
        data["nilai_akhir"] = hitung_nilai_akhir(
            data["nilai_uts"], data["nilai_uas"], data["nilai_tugas"]
        )
        data["grade"] = tentukan_grade(data["nilai_akhir"])

    print("=== DAFTAR NILAI MAHASISWA ===")
    print("-" * 67)
    print(f"{'Nama':<12} {'NIM':<13} {'UTS':>6} {'UAS':>6} "
          f"{'Tugas':>7} {'Akhir':>8} {'Grade':>6}")
    print("-" * 67)

    for data in mahasiswa:
        print(f"{data['nama']:<12} {data['nim']:<13} "
              f"{data['nilai_uts']:>6.1f} {data['nilai_uas']:>6.1f} "
              f"{data['nilai_tugas']:>7.1f} "
              f"{data['nilai_akhir']:>8.2f} {data['grade']:>6}")

    tertinggi = max(mahasiswa, key=lambda data: data["nilai_akhir"])
    terendah = min(mahasiswa, key=lambda data: data["nilai_akhir"])

    print("-" * 67)
    print(f"Nilai tertinggi: {tertinggi['nama']} "
          f"({tertinggi['nilai_akhir']:.2f})")
    print(f"Nilai terendah : {terendah['nama']} "
          f"({terendah['nilai_akhir']:.2f})")


if __name__ == "__main__":
    main()
