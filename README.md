# Echoes-of-Amazonia
AI-powered project to identify potential archaeological sites in the Amazon using satellite data.

# 🗺️ Echoes of Amazonia: AI-Driven Archaeological Discovery in the Amazon Rainforest

## 🌍 Overview

**Echoes of Amazonia** is an open science exploration project developed for the **OpenAI to Z Challenge**. Our mission is to uncover **previously undocumented archaeological sites** hidden beneath the dense Amazon rainforest canopy using open-source satellite imagery, elevation data, and AI.

We focus on the **Upper Xingu region** of the Brazilian Amazon—an area rich in legend, yet under-explored by modern digital archaeology. By combining **remote sensing**, **AI-assisted pattern recognition**, and **historical context**, we aim to pinpoint potential ancient settlements and landscapes that align with pre-Columbian human activity.

---

## 🎯 Project Goal

To identify and highlight **plausible ancient archaeological features**—such as geometric earthworks, altered vegetation patterns, and elevation anomalies—using **publicly accessible satellite datasets** (e.g., Sentinel-2, SRTM) and **OpenAI’s GPT models**. All findings are geospatially reproducible, clearly visualized, and openly documented.

---

## 🧠 Tools & Techniques

- 🌐 **Google Earth Engine (GEE)**: NDVI analysis, SRTM elevation mapping, change detection
- 🛰️ **Sentinel-2 Multispectral Imagery**: Vegetation and landform feature extraction
- 📏 **SRTM DEM Data**: Terrain modeling to reveal elevation-based anomalies
- 🤖 **GPT-4 (OpenAI API)**: For anomaly explanation, pattern hypothesis, and writeup generation
- 🗃️ **GeoJSON & Shapefiles**: Used for precise AOI bounding and site marking
- 📚 **Academic Literature & Open Map Sources**: Used to correlate findings

---

## 🧭 Area of Interest (AOI)

The core AOI for this project is defined by the bounding box:

[Longitude_min, Latitude_min, Longitude_max, Latitude_max]
[-80.0, -20.0, -45.0, 5.0]


> For efficiency and memory handling, we focus particularly on the **Upper Xingu subregion**, known historically as a potential cluster of past civilizations.

---

## ✅ Checklist for Submission

- [x] At least **two public data sources** used and cited (e.g., Sentinel-2, SRTM)
- [x] No credential-locked or paywalled links in final writeup
- [x] AI usage integrated with traceable logic
- [x] Visual overlays and coordinates reproducible by judges
- [x] Novel, data-supported hypotheses generated

---

## 📂 Project Structure

echoes-of-amazonia/
├── notebooks/
│ ├── 01_ndvi_analysis.ipynb
│ ├── 02_elevation_detection.ipynb
│ └── 03_combined_ai_insight.ipynb
├── data/
│ ├── sentinel_metadata/
│ └── gee_exports/
├── results/
│ ├── overlays/
│ └── findings.geojson
├── src/
│ └── analysis_utils.py
├── README.md
└── requirements.txt


---

## 📌 Project Links (for writeup)

- 🔗 [GitHub Repository](https://github.com/SanaAdeelKhan/Echoes-of-Amazonia)
- 📓 Kaggle Notebook (TBD after EDA)
- 📍 Visual AOI map (generated via GEE, link coming soon)
- 🧠 AI prompt logs and generated insights (TBD)

---

## 📜 License

This project is released under the **MIT License** and complies with the OpenAI to Z Challenge rules.

---

## 🙋‍♀️ Created by

**Sana Adeel**  
🌱 Explorer, Dreamer, Digital Archaeologist  
✉️ [https://www.linkedin.com/in/engr-sana-adeel-a1860ab1/]

---

> *“History isn't buried — it's waiting to be rediscovered. Echoes of Amazonia is our call to listen.”*
