# 📊 Asset Allocation Radar

**Asset Allocation Radar** je analytický nástroj pro sledování relativní valuace globálních tříd aktiv pomocí **Z-score (směrodatné odchylky od historického průměru)**.

Projekt slouží k:
- identifikaci **podhodnocených / nadhodnocených** aktiv
- mean-reversion analýze
- podpoře **rebalancování portfolia**

⚠️ *Nejde o investiční doporučení. Pouze edukativní nástroj.*

---

## ✨ Funkce
- 📈 Z-score analýza (rolling mean / std)
- 🕸️ Radar chart
- 🔷 Hexagonální vizualizace
- 🌡️ Heatmapa valuací
- 🔁 Rebalancing signály
- 🌍 Cross-asset ratio analýza
- 🌐 Streamlit dashboard
- 🧩 Připraveno pro REST API

---

## 🛠️ Instalace

```bash
git clone git@github.com:Matthew-pros/asset-allocation-radar.git
cd asset-allocation-radar
pip install -r requirements.txt
```

---

## ▶️ Spuštění (CLI)

```bash
python scripts/run_analysis.py
```

Výstupy se uloží do složky `outputs/`.

---

## 🌐 Streamlit Dashboard

```bash
streamlit run streamlit_app/app.py
```

---

## 🧠 Metodologie

Viz: `docs/methodology.md`

---

## 📜 Licence
MIT License
