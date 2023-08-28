import requests

def is_valid_api_key(api_key):
    url = "https://api.openai.com/v1/engines/davinci"  # You can use any endpoint for this check
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return True
    else:
        return False

# Replace 'YOUR_API_KEY' with the actual API key you want to check
def valid(API_Key):
    api_key = API_Key
    if len(api_key)!=51:
        return 0
    validity = is_valid_api_key(api_key)

    if validity:
        return 1
    else:
        return 0
