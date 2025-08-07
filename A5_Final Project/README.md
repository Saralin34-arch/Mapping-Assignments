# A5_Final Project - Manhattan LEED & Zoning Analysis

## 📊 Project Overview
This project analyzes Manhattan LEED (Leadership in Energy and Environmental Design) projects in relation to NYC zoning districts, creating both interactive and static visualizations.

## 🗂️ Project Structure

### 📄 Main Files
- `A5_Final Assignment.ipynb` - Main Jupyter notebook with analysis
- `static_manhattan_map.py` - Static map generator
- `strict_manhattan_only.py` - Manhattan-only filtering script
- `README.md` - This file

### 📁 Data Files
- `data/leed_manhattan_projects.csv` - Manhattan LEED project data (1,464 projects)
- `data/nyc_building_energy_data.csv` - NYC building energy consumption data
- `data/manhattan_zoning_nyzd.geojson` - Manhattan zoning districts (1,673 districts)

### 🗺️ Map Outputs
- `maps/manhattan_leed_zoning_static.png` - High-quality static map
- `maps/manhattan_leed_zoning_static.pdf` - Vector format for publications
- `maps/manhattan_leed_zoning_simple_static.png` - Simple static map
- `maps/manhattan_leed_zoning_strict.html` - Interactive map (Manhattan only)
- `maps/manhattan_leed_zoning_complete.html` - Complete interactive map

## 🎯 Key Findings

### Top Manhattan ZIP Codes by LEED Projects:
1. **10019**: 141 projects (9.6%)
2. **10022**: 130 projects (8.9%)
3. **10001**: 127 projects (8.7%)
4. **10036**: 127 projects (8.7%)
5. **10017**: 117 projects (8.0%)

### Zoning Distribution:
- **Residential**: R1-R10 zones (Green)
- **Commercial**: C1-C8 zones (Red)
- **Manufacturing**: M1-M3 zones (Teal)
- **Special Districts**: SD/SP zones (Purple)
- **Parks**: PARK zones (Gray)

## 🛠️ Usage

### Generate Static Maps:
```bash
python static_manhattan_map.py
```

### Generate Interactive Maps:
```bash
python strict_manhattan_only.py
```

## 📈 Data Summary
- **Total Manhattan LEED Projects**: 1,464
- **Manhattan ZIP Codes**: 42
- **Zoning Districts**: 1,673
- **Max Projects per ZIP**: 141

## 🎨 Visualization Features
- **No zoning outlines** for clean appearance
- **Color-coded zones** by type
- **Project density circles** by ZIP code
- **Individual LEED markers** with clustering
- **Interactive popups** with detailed information
- **Comprehensive legends** showing all zone types

## 📋 Project Status
✅ **Complete** - All visualizations generated
✅ **Cleaned** - Unused files removed
✅ **Organized** - Project structure optimized
