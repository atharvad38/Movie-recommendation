# Movie Recommender System

## Overview
This project is a movie recommender system that suggests movies based on user preferences. It uses the **TMDB_5000 dataset** and integrates with the **OMDB API** to fetch movie posters. The application is built with **Streamlit** for an interactive user experience.

## Features
- Recommends movies based on content similarity.
- Displays movie posters fetched via the OMDB API.
- Interactive user interface using Streamlit.

## Prerequisites
Make sure you have the following installed:
- Python 3.7+
- Required libraries (listed below)

## Installation
1. Install the required libraries:
    ```bash
    pip install numpy pandas matplotlib pickle-mixin streamlit requests
    ```

## Setup
### Step 1: Prepare Data
1. Run the `movie_recommender-2.ipynb` file to preprocess the data and generate the required files:
    - **Artifacts/movie_list.pkl**: Contains a list of movies.
    - **Artifacts/similarity.pkl**: Contains similarity matrices.
    
    ```bash
    jupyter notebook movie_recommender-2.ipynb
    ```

2. Ensure these files are created in the `Artifacts` directory.

### Step 2: OMDB API
- Obtain an API key from [OMDB API](http://www.omdbapi.com/).
- Update the `app.py` file with your OMDB API key:
  ```python
  API_KEY = "your_api_key_here"
  ```

## Run the Application
1. Launch the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the provided URL in your web browser to access the application.

## Required Libraries
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import streamlit as st
import requests
```

## Dataset
The project uses the **TMDB_5000 dataset** for movie data. Make sure the dataset is included in the project directory.

## File Structure
```
├── app.py                   # Main application script
├── movie_recommender-2.ipynb # Notebook for data preprocessing
├── Artifacts/               # Directory for generated pickle files
│   ├── movie_list.pkl       # Pickled file containing the movie list
│   └── similarity.pkl       # Pickled file containing the similarity matrix
├── README.md                # Project documentation
```

## Screenshots


## Contributions
Feel free to contribute by submitting a pull request or reporting issues.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

