# UAS Big Data Analytics

## Deskripsi
Aplikasi analisis pengunjung retail menggunakan PySpark, Machine Learning, dan Streamlit Dashboard.

## Teknologi
- Python
- PySpark
- Pandas
- Scikit-Learn
- Streamlit
- Plotly

## Cara Menjalankan

### 1. Aktivasi Virtual Environment

```bash
venv\Scripts\activate
```

### 2. Generate Data

```bash
python scripts/generate_data.py
```

### 3. Proses Data dengan Spark

```bash
python scripts/spark_processing.py
```

### 4. Training Model

```bash
python scripts/train_model.py
```

### 5. Jalankan Dashboard

```bash
streamlit run app.py
```

## Fitur
- KPI Total Visitor
- Grafik Pengunjung per Zona
- Analisis Tren Pengunjung
- Prediksi Pengunjung dengan Linear Regression
- Peak Hour Analysis