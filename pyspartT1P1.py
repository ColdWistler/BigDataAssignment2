from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark Session
spark = SparkSession.builder.appName("HealthcareAnalysis").getOrCreate()

# Load dataset
df = spark.read.csv("healthcare_data.csv", header=True, inferSchema=True)

# Data Cleaning: Remove null values
df_cleaned = df.dropna()

# Feature Selection: Selecting relevant columns
df_selected = df_cleaned.select("PatientID", "Age", "Diagnosis", "LengthOfStay", "CostOfCare")

# Basic Analysis: Average length of stay per diagnosis
df_avg_stay = df_selected.groupBy("Diagnosis").avg("LengthOfStay")

# Show results
df_avg_stay.show()

# Stop Spark session
spark.stop()
