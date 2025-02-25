import requests
from tenacity import retry, stop_after_attempt, wait_exponential
import time

def fetch_url_with_retry(url, max_retries=5):
    attempt = 0
    while attempt < max_retries:
        try:
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
            return response.text  # Successful response

        except requests.RequestException as e:
            wait_time = 2 ** attempt  # Exponential backoff: 1s, 2s, 4s, 8s, ...
            print(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
            attempt += 1

    raise Exception("❌ Max retries reached. Failed to fetch URL.")

# Example Usage
try:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_url_with_retry(url)
    print("✅ Success:", data[:100])  # Print first 100 chars
except Exception as e:
    print(e)


# 🔹 Retry up to 5 times with exponential backoff (2^x seconds)
@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, min=1, max=10))
def fetch_url(url):
    print("Fetching URL:", url)
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raises HTTPError for 4xx/5xx responses
    return response.text  # Return response content

# 🔹 Example Usage
try:
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_url(url)
    print("✅ Success:", data[:100])  # Print first 100 chars
except requests.RequestException as e:
    print("❌ Failed to fetch:", e)
