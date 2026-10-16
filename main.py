
import numpy as np
import matplotlib.pyplot as plt

# =========================
# 1. Data Jam Kerja dan Penghasilan
# =========================
x = np.array([10, 12, 15, 20, 22, 25, 30, 35])   # Jam kerja per minggu
y = np.array([110, 140, 165, 210, 230, 255, 310, 360])  # Penghasilan (ribu Rp)

# =========================
# 2. Hitung Koefisien Regresi (a dan b)
# =========================
x_mean = np.mean(x)
y_mean = np.mean(y)

b = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean)**2)
a = y_mean - b * x_mean

# =========================
# 3. Cetak Persamaan Model
# =========================
print("=== MODEL REGRESI LINEAR ===")
print(f"Persamaan: y = {a:.4f} + {b:.4f}x")

# =========================
# 4. Input nilai jam kerja (x) dari user
# =========================
try:
    x_input = float(input("\nMasukkan jumlah jam kerja per minggu: "))
    y_pred = a + b * x_input
    print(f"Perkiraan penghasilan untuk {x_input} jam kerja/minggu adalah: {y_pred:.2f} ribu rupiah")
except:
    print("Input tidak valid. Harap masukkan angka.")

# =========================
# 5. Visualisasi hasil prediksi
# =========================
plt.figure(figsize=(8,6))
plt.scatter(x, y, color='blue', s=80, label='Data Aktual')
plt.plot(x, a + b*x, color='red', linewidth=2, label='Garis Regresi')

# Titik hasil prediksi
plt.scatter(x_input, y_pred, color='green', s=120, label=f'Prediksi: ({x_input}, {y_pred:.2f})')

# Label & tampilan
plt.title("Model Regresi Linear: Jam Kerja vs Penghasilan", fontsize=14, fontweight='bold')
plt.xlabel("Jam Kerja per Minggu")
plt.ylabel("Penghasilan (ribu Rp)")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()
