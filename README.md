#Big Data Technologies - Healthcare Data Analysis
#Overview

This project is developed as part of ITS66904: Big Data Technologies coursework. The objective is to analyze healthcare datasets using Hadoop, PySpark, and Hive to extract insights on patient care, resource allocation, and predictive healthcare.
Features

    Data Cleaning & Preprocessing: Handling patient demographics, diagnosis codes, treatment data, and readmission rates using PySpark.
    Feature Engineering: Transforming and selecting relevant healthcare features for analysis.
    Patient Length of Stay Prediction: Comparing RDD, DataFrame, and Spark SQL for efficiency.
    Data Warehousing using Hive: Running SQL-like queries to analyze healthcare costs, readmission risks, and treatment effectiveness.
    Performance Analysis: Measuring execution time, CPU utilization, and memory usage.
    Results & Visualization: Data insights on patient treatment patterns, resource utilization, and cost analysis.

Tech Stack

    Hadoop Ecosystem (HDFS, YARN, MapReduce)
    Apache Spark (RDD, DataFrame, SQL)
    Apache Hive (Data Warehousing)
    Jupyter Notebook/PySpark for analysis
    Matplotlib/Seaborn for visualization

Setup & Installation

    Install Hadoop & Spark

sudo apt update
sudo apt install hadoop spark

Clone this repository

git clone https://github.com/yourusername/your-repo.git
cd your-repo

Run PySpark for Data Cleaning & Processing

pyspark --master local[*]

Execute Hive Queries

    hive

Project Structure

📂 BigData-Healthcare
 ├── 📁 data              # Raw and cleaned datasets  
 ├── 📁 notebooks         # Jupyter notebooks with analysis  
 ├── 📁 scripts           # PySpark scripts for data processing  
 ├── 📁 hive_queries      # SQL queries for Hive  
 ├── 📁 results           # Visualizations and findings  
 ├── README.md           # Project Documentation  
 └── requirements.txt     # Dependencies  

Usage

    Data Preprocessing: scripts/data_cleaning.py
    Patient Length of Stay Prediction: notebooks/length_of_stay.ipynb
    Hive Data Analysis: hive_queries/analysis.sql

Results & Insights

    Predicting hospital stay duration for better resource planning.
    Identifying high-risk readmission patients.
    Evaluating cost-effectiveness of treatments.

Contributors

    [Your Name]
    [Team Member 2]
    [Team Member 3]

License

This project is for academic purposes only.

Let me know if you want any modifications! 🚀
