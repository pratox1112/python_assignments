# Import PySpark
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("TestPySpark").getOrCreate()

# Create a DataFrame
data = [("Alice", 25), ("Bob", 30), ("Charlie", 35)]
df = spark.createDataFrame(data, ["Name", "Age"])

# Show the DataFrame
df.show()

# Select rows from the DataFrame
selected = df.select("Name", "Age").filter("Age > 30")

# Show the selected DataFrame
selected.show()

# Stop the SparkSession
spark.stop()