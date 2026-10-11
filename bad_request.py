import requests

# SECURITY FLAW 1: Hardcoded API key/secret in source code
API_KEY = "fake_123456789abcdefghijklmnopqrstuvwxyz"
API_URL = "https://example.com"

def fetch_user_data(user_id):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    # SECURITY FLAW 2: Disabling SSL certificate verification (verify=False)
    # This exposes the request to Man-in-the-Middle (MitM) attacks.
    response = requests.get(
        f"{API_URL}/{user_id}",
        headers=headers,
        verify=False 
    )
    
    return response.json()

if __name__ == "__main__":
    data = fetch_user_data("42")
    print(data)
