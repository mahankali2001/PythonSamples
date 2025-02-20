import datetime
from collections import defaultdict
from itertools import groupby

# Sample input data
raw_data = [
    "ad1,2023-10-01 12:00:45,192.168.1.1,US,user1",
    "ad1,2023-10-01 12:00:50,192.168.1.1,US,user6",
    "ad1,2023-10-01 12:02:00,192.168.1.5,US,user5",
    "ad2,2023-10-01 12:00:30,192.168.1.2,US,user2",
    "ad1,2023-10-01 12:01:00,192.168.1.3,US,user3",
    "ad2,2023-10-01 12:01:30,192.168.1.4,US,user4",   
    # Add more data as needed
]

def parse_line(line):
    ad_id, datestamp, ip, country, userid = line.split(',')
    return ad_id, datestamp, ip, country, userid


"""
The map function processes raw input data and transforms it into a list of key-value pairs.
Each key is a tuple consisting of an ad ID and a minute bucket (timestamp rounded to the nearest minute).
Each value is the integer 1, representing a single occurrence of the ad within that minute.
Args:
    data (list of str): A list of raw data strings, where each string contains comma-separated values
                        representing ad ID, timestamp, IP address, country, and user ID.
Returns:
    list of tuple: A list of tuples, where each tuple contains a key (ad ID, minute bucket) and a value (1).
"""
    # Parse the line into its components
    # Convert the datestamp string to a datetime object
    # Round the timestamp down to the nearest minute (bucket)
    # Create the key as a tuple of ad ID and minute bucket
    # Append the key-value pair (key, 1) to the mapped data list
def map_function(data):
    mapped_data = []
    for line in data:
        ad_id, datestamp, ip, country, userid = parse_line(line)
        timestamp = datetime.datetime.strptime(datestamp, "%Y-%m-%d %H:%M:%S") # Convert string to datetime object 
        minute_bucket = timestamp.replace(second=0) # Round down to the nearest minute (truncate seconds) 
        key = (ad_id, minute_bucket) # Create a tuple of ad ID and minute bucket
        mapped_data.append((key, 1)) # Append the key-value pair to the mapped data list, with value 1

    return mapped_data

def reduce_function(mapped_data):
    reduced_data = defaultdict(int)  # Initialize a dictionary with default value 0
    for key, count in mapped_data:
        reduced_data[key] += count
    return reduced_data

def run_mapreduce(data):
    # print ( "Data: ", data)
    # Map step
    mapped_data = map_function(data)
    
    # print (mapped_data), print()
    # Shuffle and sort step 
    mapped_data.sort(key=lambda x: x[0]) # Sort by key (ad ID, minute bucket)
    print (mapped_data)
    grouped_data = groupby(mapped_data, key=lambda x: x[0]) # Group by key (ad ID, minute bucket)
    
    # Prepare data for reduce function
    flattened_data = [(key, sum(count for _, count in group)) for key, group in grouped_data]
    
    # print(flattened_data)
    # Reduce step
    reduced_data = reduce_function(flattened_data)
    
    return reduced_data

# Run the MapReduce job
result = run_mapreduce(raw_data)

# Print the results
for key, count in result.items():
    ad_id, minute_bucket = key
    print(f"Ad ID: {ad_id}, Minute: {minute_bucket}, Count: {count}")