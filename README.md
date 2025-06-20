# 🍼 Klasifikasi Status Gizi Balita dengan Machine Learning

Proyek ini merupakan bagian dari skripsi berjudul **"Klasifikasi Status Gizi Balita Menggunakan XGBoost, LightGBM, dan CatBoost"**. Tujuan dari proyek ini adalah membangun model machine learning untuk memprediksi status gizi balita berdasarkan parameter seperti **umur**, **tinggi badan**, dan **jenis kelamin**, berdasarkan standar WHO.

---

## 🧠 Latar Belakang

Masalah stunting dan wasting masih menjadi isu kesehatan utama di berbagai negara berkembang, termasuk Indonesia. Penanganan dini dapat dilakukan melalui sistem prediksi yang cepat dan akurat. Oleh karena itu, teknologi Machine Learning diterapkan untuk membantu mengklasifikasikan status gizi balita ke dalam kategori:

- **Gizi Baik**
- **Stunting**
- **Wasting**

---

## 📊 Dataset

Ada dua Dataset yang digunakan, untuk dataset yang pertama yaitu dataset **Stunting** yang terdiri dari fitur:
- `Umur (bulan)`
- `Tinggi Badan (cm)`
- `Jenis Kelamin (laki-laki/perempuan)`
- Label `Status Gizi` berdasarkan hasil perhitungan Z-Score WHO

Adapun untuk dataset yang kedua yaitu dataset **Wasting** yang terdiri dari fitur:
- `Umur (bulan)`
- `Berat Badan (kg)`
- `Jenis Kelamin (laki-laki/perempuan)`
- Label `Status Gizi` berdasarkan hasil perhitungan Z-Score WHO

💡 Dataset ini merupakan kombinasi data simulasi dan acuan dari standar WHO Growth Reference.

---

## 🔧 Algoritma yang Digunakan

Proyek ini menggunakan tiga algoritma klasifikasi utama:

| Algoritma       | Deskripsi Singkat |
|-----------------|-------------------|
| **XGBoost**     | Model boosting berbasis pohon yang cepat dan akurat. |
| **LightGBM**    | Model boosting yang efisien dan hemat memori. |
| **CatBoost**    | Model boosting yang menangani data kategorikal secara alami. |

---

## 🚀 Cara Menjalankan Aplikasi

Aplikasi ini dibangun menggunakan **Streamlit** untuk antarmuka interaktif.

### 🔗 Jalankan Lokal:
```bash
git clone https://github.com/username/klasifikasi-gizi-balita.git
cd klasifikasi-gizi-balita
pip install -r requirements.txt
streamlit run app.py
