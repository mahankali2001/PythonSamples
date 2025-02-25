# import os

def parse_log_file(file_path):
    customer_urls = {}
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(",")
            if len(parts) < 2:
                continue
            customer_id, url = parts[2], parts[1]
            # print(customer_id, url)
            if customer_id not in customer_urls:
                customer_urls[customer_id] = set()
            customer_urls[customer_id].add(url)
    # print(customer_urls)
    return customer_urls

def find_loyal_customers(log_file_1, log_file_2):
    customers_day_1 = parse_log_file(log_file_1)
    customers_day_2 = parse_log_file(log_file_2)

    loyal_customers = set()
    for customer_id in customers_day_1:
        if customer_id in customers_day_2:
            if customers_day_1[customer_id] != customers_day_2[customer_id]:
                loyal_customers.add(customer_id)
                # print(f"Customer ID: {customer_id}, URLs visited on day 1: {customers_day_1[customer_id]}, URLs visited on day 2: {customers_day_2[customer_id]}")
    return loyal_customers

if __name__ == "__main__":
    log_file_1 = "../data/logfile_01_06_2025.csv"
    log_file_2 = "../data/logfile_01_07_2025.csv"

    print("Loyal Customers:")
    loyal_customers = find_loyal_customers(log_file_1, log_file_2)
    for customer in loyal_customers:
        print(f"Customer ID: {customer}")
    # print("Loyal Customers:", loyal_customers)