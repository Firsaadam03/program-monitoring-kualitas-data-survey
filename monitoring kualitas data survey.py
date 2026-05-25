# === MONITORING KUALITAS DATA SURVEI ===
# Program ini digunakan untuk mencatat dan mengevaluasi kualitas data hasil survei dari enumerator.
# Fitur: input data, hitung persentase, evaluasi status, dan rekap statistik.

print("=== MONITORING KUALITAS DATA SURVEI ===")

# 1. Input jumlah enumerator
try:
    jumlah_enum = int(input("Masukkan jumlah enumerator: "))
except ValueError:
    print("Input harus berupa angka!")
    exit()

# 2. Siapkan struktur data
data_enum = []

# 3. Loop input data enumerator
for i in range(1, jumlah_enum + 1):
    print(f"\n--- Enumerator {i} ---")
    nama = input("Nama enumerator: ")

    try:
        total = int(input("Jumlah total entri data: "))
        valid = int(input("Jumlah data valid: "))
    except ValueError:
        print("Input harus berupa angka! Enumerator dilewati.")
        continue

    # Validasi agar valid tidak lebih besar dari total
    if valid > total or total <= 0:
        print("Data tidak sah! Enumerator dilewati.")
        continue

    invalid = total - valid
    persentase = (valid / total) * 100 if total > 0 else 0

    status = "Lolos" if persentase >= 80 else "Tidak Lolos"

    # Simpan ke struktur data
    data_enum.append(
        {
            "nama": nama,
            "total": total,
            "valid": valid,
            "invalid": invalid,
            "persentase": persentase,
            "status": status,
        }
    )

# 4. Tampilkan rekapitulasi
print("\n== Rekapitulasi Kualitas Data ==")
print(
    "{:<15} {:<10} {:<10} {:<10} {:<15} {:<10}".format(
        "Nama", "Total", "Valid", "Invalid", "Persentase", "Status"
    )
)
print("-" * 70)

for d in data_enum:
    print(
        "{:<15} {:<10} {:<10} {:<10} {:<14.2f}% {:<10}".format(
            d["nama"],
            d["total"],
            d["valid"],
            d["invalid"],
            d["persentase"],
            d["status"],
        )
    )

# 5. Hitung dan tampilkan statistik umum
if len(data_enum) > 0:
    rata2 = sum(d["persentase"] for d in data_enum) / len(data_enum)

    # Cari enumerator dengan persentase tertinggi dan terendah
    tertinggi = data_enum[0]
    terendah = data_enum[0]

    for d in data_enum:
        if d["persentase"] > tertinggi["persentase"]:
            tertinggi = d
        if d["persentase"] < terendah["persentase"]:
            terendah = d

    lolos = sum(1 for d in data_enum if d["status"] == "Lolos")
    tidak_lolos = sum(1 for d in data_enum if d["status"] == "Tidak Lolos")

    # 6. Tampilkan hasil statistik
    print("\n== Statistik Umum ==")
    print(f"Rata-rata validitas: {rata2:.2f}%")
    print(f"Performa terbaik: {tertinggi['nama']} ({tertinggi['persentase']:.2f}%)")
    print(f"Performa terendah: {terendah['nama']} ({terendah['persentase']:.2f}%)")
    print(f"Jumlah enumerator Lolos: {lolos}")
    print(f"Jumlah enumerator Tidak Lolos: {tidak_lolos}")
else:
    print("\nTidak ada data valid yang dapat dihitung.")
