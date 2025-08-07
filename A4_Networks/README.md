# Assignment 4: Network Analysis

## Overview
This assignment explores the differences between Euclidean and network distances in New York City, focusing on accessibility to street trees from residential buildings.

## Research Statement
The analysis investigates how network-based distance calculations provide more realistic representations of actual travel distances compared to straight-line Euclidean distances, particularly in urban environments with complex street networks.

## Key Components

### 1. Research Questions
- How do Euclidean and network distances differ for accessing street trees from residential buildings?
- What are the spatial patterns of accessibility to green infrastructure in NYC?
- How does network topology affect accessibility metrics?

### 2. Data Sources
- **Street Trees**: NewYorkCity_StreetTreeCensus_2005_20250710.geojson
- **Building Footprints**: BuildingFootprints.geojson
- **Street Network**: Downloaded from OpenStreetMap using OSMnx

### 3. Analysis Steps

#### Step 1: Data Loading and Preprocessing
- Load street tree and building footprint data
- Sample data for computational efficiency (focus on Manhattan)
- Prepare data for network analysis

#### Step 2: Network Creation
- Download street network for Manhattan using OSMnx
- Project to local coordinate system (NY State Plane)
- Convert to GeoDataFrames for analysis

#### Step 3: Define Analysis Points
- Sample buildings and trees for analysis
- Create origin-destination pairs
- Prepare for distance calculations

#### Step 4: Distance Calculations
- Calculate Euclidean distances between origins and destinations
- Calculate network distances using shortest path algorithms
- Compute distance ratios and statistics

#### Step 5: Analysis and Visualization
- Create comprehensive visualizations comparing distance types
- Generate statistical summaries
- Analyze spatial patterns

#### Step 6: Network Topology Analysis (Quantitative Exploration)
- Calculate network centrality measures
- Analyze connectivity patterns
- Explore network structure metrics

#### Step 7: Spatial Analysis and Mapping
- Create maps showing network, buildings, and trees
- Visualize distance ratios spatially
- Analyze accessibility patterns

#### Step 8: Statistical Analysis and Correlation
- Calculate correlation between distance types
- Perform regression analysis
- Compute error metrics

## Expected Outputs

### Maps and Visualizations
1. **Distance Comparison Scatter Plot**: Euclidean vs Network distances
2. **Distance Ratio Histogram**: Distribution of distance ratios
3. **Box Plot Comparison**: Distance distribution comparison
4. **Cumulative Distribution Plot**: Probability distributions
5. **Network Topology Visualizations**: Degree, centrality, and edge length distributions
6. **Spatial Maps**: Network with buildings/trees and distance ratio heatmap

### Statistical Results
- Correlation coefficients between distance types
- R-squared values for linear relationships
- Mean absolute percentage errors
- Network topology metrics (density, centrality, connectivity)

### Key Findings
- Network distances are consistently longer than Euclidean distances
- Complex street layouts show higher distance ratios
- Network topology significantly influences accessibility patterns

## Running the Assignment

### Prerequisites
```bash
pip install -r requirements.txt
```

### Execution
1. Open `A4_Networks_Analysis.ipynb` in Jupyter Notebook
2. Run cells sequentially
3. Review outputs and modify parameters as needed

### Data Requirements
Ensure the following files are available in the `../Data/` directory:
- `NewYorkCity_StreetTreeCensus_2005_20250710.geojson`
- `BuildingFootprints.geojson`

## Computational Notes
- The analysis samples data for computational efficiency
- Focus is on Manhattan for detailed analysis
- Network analysis can be computationally intensive
- Consider adjusting sample sizes based on available resources

## Bonus: Quantitative Exploration (Xin et al. 2022)
The notebook includes quantitative network analysis following the framework described in Xin et al. (2022):
- Network density and connectivity measures
- Centrality analysis (degree, betweenness, closeness)
- Path length distributions
- Correlation between network structure and accessibility outcomes

## Expected Learning Outcomes
- Understanding of network vs Euclidean distance concepts
- Experience with network analysis tools (NetworkX, OSMnx)
- Ability to perform quantitative network topology analysis
- Skills in creating comprehensive spatial analysis workflows
- Experience with statistical analysis of spatial data 