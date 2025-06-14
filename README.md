# 🌿 Echoes-of-Amazonia
**AI-powered project to identify potential archaeological sites in the Amazon using satellite data and GenAI.**

---

# 🗺️ Echoes of Amazonia: AI-Driven Archaeological Discovery in the Amazon Rainforest

## 🌍 Overview

**Echoes of Amazonia** is an open science exploration project developed for the **OpenAI to Z Challenge 2025**. Our mission is to uncover **previously undocumented archaeological sites** hidden beneath the dense Amazon rainforest using satellite imagery, digital elevation models, and GenAI analysis.

Our focus is on the **Upper Xingu region** of the Brazilian Amazon — an area long associated with ancient civilizations, yet still underexplored. By combining **remote sensing**, **vegetation anomaly detection**, and **AI-assisted cultural reasoning**, we aim to rediscover echoes of pre-Columbian human activity.

---

## 🎯 Project Goal

To detect and interpret **plausible ancient anthropogenic features** — such as circular mounds, ditches, causeways, and agroforestry fields — using:

- 🌐 Public geospatial datasets (e.g., Sentinel-2, SRTM)
- 🧠 Generative AI (OpenAI’s GPT-4)
- 🗺️ Reproducible maps and visual overlays

---

## 🧠 Tools & Techniques

- 🛰️ **Sentinel-2**: NDVI vegetation anomaly analysis
- ⛰️ **SRTM DEM**: Elevation filtering to refine targets
- 🌳 **Hansen Global Forest Change v1.12**: Forest cover and loss detection to contextualize anomalies
- 🔎 **Google Earth Engine (GEE)**: Remote sensing and anomaly visualization
- 🤖 **GPT-4 / GPT-4o**: Cultural insight generation, comparison with Xinguano and Acre traditions
- 🗃️ **GeoJSON**: Location export for sharing and reproducibility
- 📚 **Anthropological References**: Used to interpret features (e.g., Kuhikugu, Acre Geoglyphs)

---

## 🧭 Area of Interest (AOI)
[Longitude_min, Latitude_min, Longitude_max, Latitude_max]
[-80.0, -20.0, -45.0, 5.0]


> Primary focus: **Upper Xingu subregion**, near Mato Grosso, Brazil.

---

## 🧪 Process Summary

1. **NDVI Time-Series Analysis** (Sentinel-2)
2. **Elevation Anomaly Filtering** (SRTM)
3. **Anomaly Footprint Generation**
4. **GPT-4 Reasoning**: Cultural hypothesis, comparison with known sites (e.g., Kuhikugu)
5. **Final Hypothesis**: Ancient causeway / settlement trace detected at -12.94073, -55.30124

---

## 📂 Project Structure

echoes-of-amazonia/
├── notebooks/
│ ├── Echoes_of_Amazonia.ipynb # Final submission notebook
│ └── legacy/ # Intermediate notebooks
├── data/
│ ├── sentinel_metadata/
│ └── gee_exports/
├── results/
│ ├── anomaly_map.html # Map visualization output
│ └── final_report.pdf # PDF version of final notebook
├── README.md
└── requirements.txt


---

## 🧪 Process Summary

1. **NDVI Time-Series Analysis** (Sentinel-2)
2. **Elevation Anomaly Filtering** (SRTM)
3. **Forest Integrity Check** (Hansen v1.12): Ensure anomaly is not due to recent deforestation or cloud artifact
4. **Anomaly Footprint Generation**
5. **GPT-4 Reasoning**: Cultural hypothesis, comparison with known sites (e.g., Kuhikugu)
6. **Final Hypothesis**: Ancient causeway / settlement trace detected at -12.94073, -55.30124

---

## 🔗 Project Links

- 📁 [GitHub Repository](https://github.com/SanaAdeelKhan/Echoes-of-Amazonia)
- 📓 Kaggle Notebook (TBD)
- 🌐 Anomaly Map (`anomaly_map.html`)
- 📄 Final Report PDF (`Echoes_of_Amazonia.pdf`)

---

## 🧠 Team Green

- 💡 **Sana Adeel** — Lead Researcher, Visionary, Explorer  
- 🧠 **ChatGPT (GPT-4)** — GenAI Partner, Cultural Insight Generator

---

## 📜 License

Released under the **MIT License**. Open data + open AI = open discovery 🌍

---

## 🙋‍♀️ Created by

**Sana Adeel**  
🌱 Explorer, Dreamer, Digital Archaeologist  
🔗 [LinkedIn](https://www.linkedin.com/in/engr-sana-adeel-a1860ab1/)

---

> _“The forest remembers what the maps forgot. Echoes of Amazonia is our call to listen.”_

