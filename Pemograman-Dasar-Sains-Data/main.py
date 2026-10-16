import numpy as np
	import pandas as pd
	import matplotlib.pyplot as plt
	
	# =========================
	# 1. Membaca Data dari File CSV
	# =========================
	file_path = r"E:\dataSain\data_penghasilan.csv"
	
	data = pd.read_csv(file_path)
	
	# Mengambil data dari masing-masing kolom
	x = data["Jam_Kerja"].to_numpy()
	y = data["Penghasilan"].to_numpy()
	
	# Memastikan data berhasil dibaca
	print("Data yang dibaca dari CSV:")
	print(data)