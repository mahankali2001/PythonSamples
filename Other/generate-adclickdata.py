import random
import datetime

# Define parameters for data generation
num_entries = 10000
ad_ids = ['ad1', 'ad2', 'ad3', 'ad4', 'ad5']
countries = ['US', 'CA', 'GB', 'DE', 'FR', 'IN', 'JP', 'CN', 'AU', 'BR']
user_ids = [f'user{i}' for i in range(1, 1001)]
start_date = datetime.datetime(2023, 10, 1)
end_date = datetime.datetime(2023, 10, 10)

# Function to generate a random timestamp between two dates
def random_date(start, end):
    return start + datetime.timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())))

# Generate test data
with open('test_data.csv', 'w') as file:
    for _ in range(num_entries):
        ad_id = random.choice(ad_ids)
        timestamp = random_date(start_date, end_date).strftime('%Y-%m-%d %H:%M:%S')
        ip = f'192.168.{random.randint(0, 255)}.{random.randint(0, 255)}'
        country = random.choice(countries)
        user_id = random.choice(user_ids)
        file.write(f'{ad_id},{timestamp},{ip},{country},{user_id}\n')

print("Test data generated successfully!")