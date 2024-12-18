# Flow Cytometry Auto-Analysis

This repository provides a suite of functions designed to automate the analysis of flow cytometry data in .fcs file formats. 

## Project Structure

The repository contains the following main directories and files: 

```
flow_cytometry_analysis/
|
├── analyzer/
|   ├── analysis.py
|   ├── parser.py
|   ├── preprocessing.py
|   ├── reporting.py
|   ├── visualization.py
|
├── data/
|   ├── 215_0.fcs
|
├── tests\
|   ├── test_analysis.py
|   ├── test_parser.py
|   ├── test_preprocessing.py
|   ├── test_reporting.py
|   ├── test_visualization.py
|
├── README.md
└── requirements.txt
```

### Key Components

- **analyzer/**: This directory contains the core functionality for analyzing flow cytometry data of the .fcs format, including various preprocessing and analysis tools. 
    - `analysis.py` 
    - `parser.py`
    - `preprocessing.py`
    - `reporting.py`
    - `visualization.py`

## Installation

This project has minimal dependencies that can be installed using `pip` alongside a virtual environment to avoid conflicts. 

### Requirements

- **Python 3.x** is required.
- **Dependencies**: Listed in the  `requirements.txt` file. 