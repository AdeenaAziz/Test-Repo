import requests

# Define custom headers
headers = {
    'Content-Type': 'application/json',
    'User-Agent': 'MyPythonApp/1.0'
}

# Make a GET request with headers
response = requests.get('https://jsonplaceholder.typicode.com/posts/1', headers=headers)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')