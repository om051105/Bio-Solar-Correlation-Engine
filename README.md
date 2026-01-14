# Bio-Solar Correlation Engine ☀️🧠

> **A High-Performance Predictive System for Seasonal Affective Disorder (SAD)**
>
> *Correlating biological rhythms with solar environmental data to forecast mood volatility.*

---

## 📖 Overview
The **Bio-Solar Correlation Engine** is a data intelligence platform designed to detect early warning signs of Seasonal Affective Disorder (SAD). 

Unlike simple wellness apps that track mood manually, this engine builds a **causal link** between external environmental factors (UV Index, Cloud Cover, Sunlight Hours) and internal biological metrics (Sleep Efficiency, HRV, Step Count).

By leveraging **Gradient Boosting Machines (LightGBM)** on time-series data, the system predicts "Mood Dips" up to 3 days in advance, allowing for proactive light therapy interventions.

## 🚀 Key Features
*   **📡 Multi-Source Ingestion Pipeline**: Asynchronously fetches weather data (OpenWeatherMap) and wearable health data (Apple Health/Fitbit).
*   **🧬 Biological-Environmental Correlation**: Merges disparately timed datasets (minute-level heart rate vs. hourly cloud cover) into a unified **Daily Risk Vector**.
*   **🤖 Predictive Intelligence**: Uses `LightGBM` (Gradient Boosting) to forecast `Mood_Volatility_Index` based on the previous 7-day sunlight deficit.
*   **📊 Executive Dashboard**: A specialized `Streamlit` interface for visualizing circadian drift and sunlight leverage ratios.

## 🛠️ Tech Stack
This project uses a production-grade Data Engineering & ML stack:

| Component | Technology | Reasoning |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Industry standard for AI/ML. |
| **API Backend** | FastAPI | High-performance async support for real-time ingestion. |
| **ML Engine** | LightGBM | Superior speed/accuracy for tabular time-series data vs. Deep Learning. |
| **Data Processing** | Pandas / NumPy | Vectorized operations for efficient ETL. |
| **Visualization** | Streamlit | Rapid deployment of interactive data apps. |
| **Database** | PostgreSQL | (Planned) For robust storage of time-series logs. |

## 📂 Project Structure
```bash
Bio-Solar-Correlation-Engine/
├── data/
│   ├── raw/             # Raw CSV exports from APIs/Wearables
│   └── processed/       # Cleaned, merged, and vectorized datasets
├── src/
│   ├── api/             # FastAPI backend endpoints
│   ├── ingestion/       # Scripts to fetch/generate data
│   ├── models/          # ML training and inference logic
│   ├── processing/      # ETL Pipelines (Cleaning, Merging)
│   └── __init__.py
├── notebooks/           # Jupyter notebooks for EDA and prototyping
├── tests/               # Unit tests for pipelines
├── IMPLEMENTATION_PLAN.md # Detailed engineering roadmap
└── requirements.txt     # Python dependencies
```

## ⚡ Quick Start

### 1. Prerequisites
*   Python 3.10 or higher
*   Git

### 2. Installation
```bash
# Clone the repository
git clone https://github.com/om051105/Bio-Solar-Correlation-Engine.git
cd Bio-Solar-Correlation-Engine

# Create a virtual environment (Optional but Recommended)
python -m venv venv
# Windows
.\venv\Scripts\activate
# Mac/Linux
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
```

### 3. Generate Synthetic Data
Since you may not have immediate API access to 60 days of historical data, use the generator to create a realistic research dataset:
```bash
python src/ingestion/mock_data.py
```
*This will create `solar_history.csv` and `bio_history.csv` in the `data/raw/` folder.*

## 🛣️ Roadmap
- [x] **Phase 1**: Project Initialization & Synthetic Data Generation.
- [ ] **Phase 2**: ETL Pipeline Development (Merging Bio & Solar data).
- [ ] **Phase 3**: Machine Learning Model Training (LightGBM).
- [ ] **Phase 4**: API & Dashboard Development.
- [ ] **Phase 5**: Dockerization & Cloud Deployment (AWS/GCP).

---
*Developed by Om Singh as part of the Advanced AI Engineering Portfolio.*
