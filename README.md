# 🎬 Anatomy of a Flop

> *"Bugetul mare garantează succesul unui film?"*

Proiect de econometrie avansată care analizează de ce filme cu bugete uriașe eșuează comercial, în timp ce filme cu resurse minime devin legendare.

Am construit un **Disappointment Index (DI)** — o metrică originală care măsoară discrepanța dintre ce merita un film să câștige și ce a câștigat în realitate — și am antrenat mai multe modele statistice pentru a-l prezice.

---

##  Autori

- Sasu Sabrina
- Săndulescu Crina
- Sandu Bianca Antonia

---

##  Structura Proiectului

- `data/` — datele brute și curățate
- `notebooks/` — notebooks în ordine (01 → 06)
- `src/` — funcții Python reutilizabile
- `requirements.txt` — dependențele proiectului

---

##  Disappointment Index

DI = revenue / (budget x 2.5)

- **DI < 0.5** → Flop total
- **DI < 1.0** → Sub așteptări
- **DI < 2.0** → Conform așteptărilor
- **DI ≥ 2.0** → Surpriză pozitivă

---

##  Modele Estimate

| Model | R² | RMSE |
|-------|----|------|
| OLS Simplu | 0.163 | 7.47 |
| OLS Log(DI) | 0.061 | — |
| OLS Standardizat | 0.163 | 7.47 |
| Random Forest | 0.477 | 5.90 |
| **Gradient Boosting**  | **0.494** | **5.81** |

**Modelul câștigător: Gradient Boosting** cu R² = 0.494

---

##  Concluzii Cheie

- **Bugetul mare nu garantează succesul** — corelație budget ↔ DI = −0.25
- **Anul lansării e cel mai important predictor** — industria devine tot mai impredictibilă
- **Modelele ML bat regresia liniară de 3x** — relația nu este liniară
- **50% din variație rămâne neexplicată** — magia unui film nu se poate cuantifica

---

##  Instalare

1. Clonează repo-ul:
git clone https://github.com/ccrinasandulescu/Anatomy-of-a-flop

2. Intră în folder:
cd Anatomy-of-a-flop

3. Activează virtual environment:
source venv/bin/activate

4. Instalează dependențele:
pip install -r requirements.txt

---

##  Rulare

Deschide notebooks în ordine în VS Code sau Jupyter:

1. 01_eda.ipynb — Analiza exploratorie a datelor
2. 02_preprocessing.ipynb — Curățare și feature engineering
3. 03_modeling.ipynb — Estimare și comparare modele
4. 04_feature_selection.ipynb — Selecție variabile
5. 05_error_analysis.ipynb — Analiza erorilor modelului câștigător
6. 06_conclusions.ipynb — Concluzii finale

---

##  Date

Datele provin din **TMDB (The Movie Database)** și conțin:
- 1000 filme, filtrate la **866 cu date financiare complete**
- Coloane: budget, revenue, vote_average, vote_count, popularity, runtime, release_date

---

##  Dependențe Principale

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- statsmodels
- streamlit
