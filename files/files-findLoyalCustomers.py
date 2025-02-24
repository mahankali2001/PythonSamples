import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the data file into a pandas DataFrame


file_path1 = 'data/logfile_01_06_2025.log'
df1 = pd.read_csv(file_path1, sep=',', header=None)
# Print the record count of the combined DataFrame
df1_record_count = df1.shape[0]
print(f"Record count of file1 : {df1_record_count}")
# print(df1.head(10))
# print(df1.tail(10))


file_path2 = 'data/logfile_01_07_2025.log'
df2 = pd.read_csv(file_path2, sep=',', header=None)
# Print the record count of the combined DataFrame
df2_record_count = df2.shape[0]
print(f"Record count of file 2 : {df2_record_count}")
# print(df2.head(10))

# Combine the two DataFrames by adding df2 records after df1 records
combined_df = pd.concat([df1, df2], ignore_index=True)
# Add column headings
combined_df.columns = ['day', 'url', 'customer_id']
# print(combined_df.head(10))
# Print the record count of the combined DataFrame
record_count = combined_df.shape[0]
print(f"Record count of combined DataFrame: {record_count}")
# write the combined DataFrame to a CSV file
combined_df.to_csv('data/combined_df.csv', index=False)
print("Combined DataFrame written to data/combined_df.csv")

# Collect customer-wise total visit days
customer_total_days_df = combined_df.groupby('customer_id')['day'].count().reset_index()
customer_total_days_df.columns = ['customer_id', 'total_days']
customer_total_days_df.to_csv('data/customer_total_days_df.csv', index=False)
print("customer-wise total visit days count written to data/customer_total_days_df.csv")
# Print the record count of customer-wise days DataFrame
customer_total_days_df_count = customer_total_days_df.shape[0]
print(f"Record count of customer-wise days: {customer_total_days_df_count}")

customer_total_days_gt1 = customer_total_days_df.groupby('customer_id').filter(lambda x: x['total_days'] > 1)
customer_total_days_gt1_count = customer_total_days_gt1.shape[0]
print(f"Customer count who visited more than 1 day: {customer_total_days_gt1_count}")
# print("Customers who visited more than 1 day:")
# print(customer_total_days_gt1.head(10))

# Collect customer-wise URLs
customer_total_urls_df = combined_df.groupby('customer_id')['url'].count().reset_index()
customer_total_urls_df.columns = ['customer_id', 'total_urls']
customer_total_urls_df.to_csv('data/customer_total_urls_df.csv', index=False)
print("customer-wise total visit URLs count written to data/customer_total_urls_df.csv")
customer_total_urls_df_count = customer_total_urls_df.shape[0]
print(f"Customer count who visited more than 1 page: {customer_total_urls_df_count}")


customer_total_urls_gt1 = customer_total_urls_df.groupby('customer_id').filter(lambda x: x['total_urls'] > 1)
customer_total_urls_gt1_count = customer_total_urls_gt1.shape[0]
print(f"Customers who visited more than 1 url count: {customer_total_urls_gt1_count}")
# print("Customers who visited more than 1 url:")
# print(customer_total_urls_gt1.head(10))


# Find the intersection of customers who visited more than 1 day and more than 1 URL
intersection_df = pd.merge(customer_total_days_gt1, customer_total_urls_gt1, on='customer_id')
intersection_count = intersection_df.shape[0]
print(f"Loyal customer count - who visited more than 1 day and more than 1 URL : {intersection_count}")
print("Loyal customers - who visited more than 1 day and more than 1 URL:")
print(intersection_df.head(10))

# Write the intersection DataFrame to a CSV file
intersection_df.to_csv('data/customer_intersection_df.csv', index=False)
print("Loyal customers who visited more than 1 day and more than 1 URL written to data/customer_intersection_df.csv")