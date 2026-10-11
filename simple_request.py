import requests

# The URL of the public web API endpoint
url = "https://fake.site.com/endpoint

try:
    # Send an HTTP GET request to the web API
    response = requests.get(url)
    
    # Check if the request was successful (HTTP Status Code 200)
    if response.status_code == 200:
        # Convert the JSON response into a usable Python dictionary
        data = response.json()
        
        print("Success! Data retrieved:")
        print(f"User ID:   {data['userId']}")
        print(f"Task ID:   {data['id']}")
        print(f"Title:     {data['title']}")
        print(f"Completed: {data['completed']}")
    else:
        print(f"Failed to fetch data. Server responded with status code: {response.status_code}")

except requests.exceptions.RequestException as error:
    # Handle connection issues or invalid URLs gracefully
    print(f"An error occurred: {error}")
