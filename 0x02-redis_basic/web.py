import requests
import redis
import time

# Connect to Redis
r = redis.Redis(host='localhost', port=6379, db=0)

def get_page(url: str) -> str:
    # Check if the URL is in the cache
    cached_content = r.get(url)
    if cached_content:
        print("Retrieving from cache...")
        return cached_content.decode('utf-8')

    # If not in cache, fetch the content
    print("Fetching from URL...")
    response = requests.get(url)
    content = response.text

    # Store the content in cache with expiration time
    r.setex(url, 10, content)

    # Update the access count for this URL
    count_key = f"count:{url}"
    r.incr(count_key)

    return content
