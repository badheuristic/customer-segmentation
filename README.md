# Customer Segmentation Analysis

This project performs customer segmentation using K-Means clustering. It groups customers based on their Age, Work Experience, Family Size, and Spending Score.

## Features
- Age
- Work Experience (Missing values imputed with median)
- Family Size (Missing values imputed with median)
- Spending Score (Categorical: Low/Average/High -> encoded to 1/2/3)

## Installation
Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

For NixOS users:
```bash
nix develop
```

## Usage
```bash
python main.py
```

## Output
-   `elbow_plot.png`: Elbow Method plot to determine optimal
-   `cluster_plot.png`: Scatter plot visualizing the customer segments
-   Console output with cluster insights (mean values for each cluster)

The analysis currently identifies 4 distinct customer segments, ranging from older high-spenders to younger low-spenders.
