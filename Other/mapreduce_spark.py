from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_trunc, count

# Initialize Spark session
spark = SparkSession.builder \
    .appName("AdDataAggregation") \
    .getOrCreate()

# Load the raw ad data from the CSV file
input_file = "test_data.csv"
raw_data = spark.read.csv(input_file, header=False, inferSchema=True)

# Rename columns for better readability
raw_data = raw_data.withColumnRenamed("_c0", "ad_id") \
                   .withColumnRenamed("_c1", "datestamp") \
                   .withColumnRenamed("_c2", "ip") \
                   .withColumnRenamed("_c3", "country") \
                   .withColumnRenamed("_c4", "userid")

# Filter data by country (example: filter for US)
country_filter = "US"
filtered_data = raw_data.filter(col("country") == country_filter)

# Convert datestamp to minute level
filtered_data = filtered_data.withColumn("minute_bucket", date_trunc("minute", col("datestamp")))

# Group by ad_id and minute_bucket and count occurrences
aggregated_data = filtered_data.groupBy("ad_id", "minute_bucket").agg(count("*").alias("count"))

# Save the aggregated data to a CSV file
output_file = "aggregated_data.csv"
aggregated_data.write.csv(output_file, header=True)

# Stop the Spark session
spark.stop()