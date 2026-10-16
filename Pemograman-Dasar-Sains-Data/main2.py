import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# 1. Dataset Statis Langsung dalam Kode (In-Memory)
data = [
    {"severity": 4, "attack_type": "Ransomware", "affected_systems": 25, "team_experience_years": 5, "resolution_time_hours": 38.5},
    {"severity": 1, "attack_type": "Phishing", "affected_systems": 5, "team_experience_years": 10, "resolution_time_hours": 4.2},
    {"severity": 3, "attack_type": "DDoS", "affected_systems": 50, "team_experience_years": 7, "resolution_time_hours": 28.0},
    {"severity": 5, "attack_type": "Ransomware", "affected_systems": 80, "team_experience_years": 3, "resolution_time_hours": 92.1},
    {"severity": 2, "attack_type": "SQLi", "affected_systems": 12, "team_experience_years": 8, "resolution_time_hours": 11.5},
    {"severity": 2, "attack_type": "Malware", "affected_systems": 15, "team_experience_years": 6, "resolution_time_hours": 16.0},
    {"severity": 4, "attack_type": "DDoS", "affected_systems": 60, "team_experience_years": 4, "resolution_time_hours": 42.3},
    {"severity": 1, "attack_type": "Phishing", "affected_systems": 2, "team_experience_years": 12, "resolution_time_hours": 2.5},
    {"severity": 3, "attack_type": "SQLi", "affected_systems": 30, "team_experience_years": 5, "resolution_time_hours": 22.8},
    {"severity": 5, "attack_type": "Malware", "affected_systems": 70, "team_experience_years": 2, "resolution_time_hours": 75.0},
]

df = pd.DataFrame(data)

# 2. Preprocessing Data (One-Hot Encoding)
df_encoded = pd.get_dummies(df, columns=["attack_type"], drop_first=True)

X = df_encoded.drop(columns=["resolution_time_hours"])
y = df_encoded["resolution_time_hours"]

# Standardisasi Fitur
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Pelatihan Model Linear Regression
model = LinearRegression()
model.fit(X_scaled, y)

# 4. Fungsi Prediksi untuk Data Baru
def prediksi_waktu_penanganan(severity, attack_type, affected_systems, team_experience):
    input_data = pd.DataFrame(
        [{
            "severity": severity,
            "affected_systems": affected_systems,
            "team_experience_years": team_experience,
            "attack_type_DDoS": 1 if attack_type == "DDoS" else 0,
            "attack_type_Malware": 1 if attack_type == "Malware" else 0,
            "attack_type_Phishing": 1 if attack_type == "Phishing" else 0,
            "attack_type_Ransomware": 1 if attack_type == "Ransomware" else 0,
            "attack_type_SQLi": 1 if attack_type == "SQLi" else 0,
        }]
    )
    
    # Samakan struktur kolom
    input_encoded = input_data.reindex(columns=X.columns, fill_value=0)
    input_scaled = scaler.transform(input_encoded)
    
    estimasi_jam = model.predict(input_scaled)[0]
    return round(max(1.0, estimasi_jam), 2)

# Contoh Penggunaan:
hasil = prediksi_waktu_penanganan(
    severity=4, 
    attack_type="Ransomware", 
    affected_systems=30, 
    team_experience=4
)

print(f"[Hasil Prediksi] Estimasi waktu penanganan insiden: {hasil} jam")