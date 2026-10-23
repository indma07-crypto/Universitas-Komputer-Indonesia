import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set tampilan visual grafik agar lebih menarik
# sns.set_theme(style="whitegrid")
sns.set(style="whitegrid")

# ==========================================
# 1. READ DATASET DARI DRIVE D
# ==========================================
# Lokasi file dataset di Drive D folder Dataset
file_path = r"E:\Dataset\cybersecurity_linear_regression_dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    print("Dataset berhasil dimuat!")
    print("\n--- 5 Baris Pertama Data ---")
    print(df.head())
    print("\n--- Ringkasan Informasi Data ---")
    print(df.info())
else:
    print(f"File tidak ditemukan di path: {file_path}")
    exit()

    # B. Scatter Plot: Severity Score vs Response Time
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="Severity_Score",
    y="Response_Time_Minutes",
    color="crimson",
    scatter_kws={'alpha':0.6}
)
plt.title("Pengaruh Severity Score terhadap Waktu Respon", fontsize=12, fontweight="bold")
plt.xlabel("Severity Score (Tingkat Keparahan)")
plt.ylabel("Response Time (Menit)")
plt.tight_layout()
plt.show()

# C. Scatter Plot: Pengalaman Analis vs Waktu Respon
plt.figure(figsize=(8, 5))
sns.regplot(
    data=df,
    x="Analyst_Experience",
    y="Response_Time_Minutes",
    color="teal",
    scatter_kws={'alpha':0.6}
)
plt.title("Pengaruh Pengalaman Analis terhadap Waktu Respon", fontsize=12, fontweight="bold")
plt.xlabel("Pengalaman Analis (Tahun)")
plt.ylabel("Response Time (Menit)")
plt.tight_layout()
plt.show()

# D. Distribusi Target Variable (Response Time)
plt.figure(figsize=(8, 5))
# sns.histplot(df["Response_Time_Minutes"], kde=True, color="purple", bins=15)
sns.distplot(df["Response_Time_Minutes"], color="purple", bins=15)
plt.title("Distribusi Waktu Respon (Response Time Minutes)", fontsize=12, fontweight="bold")
plt.xlabel("Response Time (Menit)")
plt.ylabel("Frekuensi")
plt.tight_layout()
plt.show()