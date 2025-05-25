# Creating and Analyzing Data with Python

## Overview

This project was developed as part of my learning journey in **Data Analysis using Python**. It consists of two main stages:

1. **Data Creation**: I developed a complete and realistic synthetic database from scratch, with 23 structured variables simulating real-world logistics operations across multiple companies, products, and delivery regions. The dataset includes orders, clients, deliveries, transactions, geographic data, and more. To build it, I used the Faker and Random libraries in combination with loops, concatenation, and incremental aggregation to automate the generation process. Everything was formatted and organized using Pandas and NumPy, following best practices in data structuring. The final DataFrame contains 100 rows and represents a rich and diverse scenario for data exploration and insight generation.

2. **Data Analysis and Visualization**: After building the dataset, I applied descriptive analysis and created a variety of visualizations to extract insights. These included:
◦ Average delivery times and prices per region
◦ Total sales distribution
◦ Histograms and pie charts
◦ Regional comparisons using GeoPandas to map sales geographically

The main goal of this project was to practice the full data analysis cycle — from data creation to insight. During development, I faced technical challenges that helped me grow in several areas:
– Statistical and visual analysis using Seaborn, Matplotlib, Plotly, and GeoPandas
– GeoJSON file handling and integration with customized maps
– Clean directory structure and Git-based version control for project management

The project was written entirely in Python and focused on hands-on practice, reinforcing concepts in data handling, statistical thinking, and visual storytelling.

---

## Technologies

- `pandas` – for data manipulation and analysis  
- `numpy` – for numerical operations  
- `matplotlib` – for static visualizations  
- `seaborn` – for enhanced statistical plotting  
- `plotly` – for interactive graphs  
- `geopandas` – for geospatial mapping  
- `faker` – for generating synthetic but realistic data  

---

## Structure

- **/data** → contains the GeoJSON file used for geospatial mapping  
- **/src** → all source code used to generate and analyze the data  
- **/figures** → contains all the plot images used in the project  
- **/dashboards** → contains the interactive plot exported as HTML  
- **README.md** → project documentation  
- **requirements.txt** → list of dependencies to run the project

---

## How to Use

1. Clone this repository:
   ```bash
   git clone https://github.com/rodevdantas/creating-n-analyzing.git
   ```

2. Navigate into the project folder:
   ```bash
   cd creating-n-analyzing
   ```

3. Install all dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Python scripts from the `/src` folder in your IDE or terminal.

---

## Notes

The HTML file for the "Dashboard" page is included in the project, but due to its size and the fact that it contains an interactive chart, it won't render properly on GitHub. To view the chart as intended, you'll need to download the project and open the file locally in your browser.
This project was a complete exercise from **data creation** to **exploratory analysis and visualization**, allowing me to reinforce core skills in Python for Data Analysis. I combined static and interactive charts, used geospatial data for regional insights, and built a clean and modular project structure for future scalability.


