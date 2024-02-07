import requests

url = "http://www.python.org"
response = requests.get(url)

# Check is the request was successful
if response.status_code == 200:
    # Display the first 600 characters of the content
    print(response.text[:600])
else:
    print(f"Error: {response.status_code}")
