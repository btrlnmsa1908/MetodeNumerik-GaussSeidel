# =====================================================
# TUGAS PORTOFOLIO AKHIR SEMESTER
# METODE NUMERIK - GAUSS SEIDEL
#
# Kelompok:
# Yericho Prasetya (C2455201011)
# Betralin Maulana S.A (C2455201010)
# Zakheus Ferdiyanto (C2455201012)
# =====================================================

print("=" * 60)
print("METODE GAUSS-SEIDEL")
print("Optimasi Jalur Pengiriman UMKM")
print("=" * 60)

# Sistem Persamaan:
# 2x1 + x2 + x3 = 100
# x1 + 3x2 + x3 = 120
# x1 + x2 + 2x3 = 110

toleransi = 0.00001
iterasi_maks = 100

x1 = 0
x2 = 0
x3 = 0

print("\nTabel Iterasi")
print("-" * 75)
print(f"{'Iterasi':<10}{'x1':<15}{'x2':<15}{'x3':<15}{'Error'}")
print("-" * 75)

for i in range(iterasi_maks):

    x1_baru = (100 - x2 - x3) / 2
    x2_baru = (120 - x1_baru - x3) / 3
    x3_baru = (110 - x1_baru - x2_baru) / 2

    error = max(
        abs(x1_baru - x1),
        abs(x2_baru - x2),
        abs(x3_baru - x3)
    )

    print(
        f"{i+1:<10}"
        f"{x1_baru:<15.6f}"
        f"{x2_baru:<15.6f}"
        f"{x3_baru:<15.6f}"
        f"{error:.6f}"
    )

    x1 = x1_baru
    x2 = x2_baru
    x3 = x3_baru

    if error < toleransi:
        break

print("\n" + "=" * 60)
print("HASIL AKHIR")
print("=" * 60)

print(f"x1 = {x1:.6f}")
print(f"x2 = {x2:.6f}")
print(f"x3 = {x3:.6f}")
print(f"Error Akhir = {error:.6f}")
print(f"Jumlah Iterasi = {i+1}")

print("\nKesimpulan:")
print("Metode Gauss-Seidel berhasil menemukan solusi konvergen.")