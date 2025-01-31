from elasticsearch import Elasticsearch
import urllib3

# Connect to Elasticsearch
# Define Elasticsearch connection parameters
# import certifi
# es = Elasticsearch(
#     ["https://elastic:<password>@localhost:9200"],
#     ca_certs=certifi.where()
# )

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

es = Elasticsearch(
    ["https://elastic:<password>@localhost:9200"],
    verify_certs=False
)

# Check connection
if es.ping():
    print("Connected to Elasticsearch")
else:
    print("Failed to connect")


# Define sample products
products = [
    {"name": "Apple iPhone 14", "category": "Mobile Phones", "price": 799, "description": "Latest Apple iPhone with A15 chip."},
    {"name": "Samsung Galaxy S23", "category": "Mobile Phones", "price": 699, "description": "New Samsung flagship phone."},
    {"name": "Google Pixel 7", "category": "Mobile Phones", "price": 599, "description": "Google's best camera phone."}
]

# Index products into Elasticsearch
for i, product in enumerate(products, start=1):
    es.index(index="products", id=i, body=product)

print("Products indexed successfully!")


# Perform a search query
query = {
    "query": {
        "match": {
            "name": "iPhone"
        }
    }
}

response = es.search(index="products", body=query)

# Print search results
print("Search Results:")
for hit in response["hits"]["hits"]:
    print(f"Product Name: {hit['_source']['name']}, Price: {hit['_source']['price']}")

# Fuzzy Search 
query = {
    "fuzzy": {
        "name": {
            "value": "iphne",
            "fuzziness": "AUTO"
        }
    }
}

# response = es.search(index="products", body=query)

# # Print search results
# print("Search Results:")
# for hit in response["hits"]["hits"]:
#     print(f"Product Name: {hit['_source']['name']}, Price: {hit['_source']['price']}")
