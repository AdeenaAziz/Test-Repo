import requests

# Data to create a new post
new_post = {
    "title": "My New Post",
    "body": "This is the content of my post.",
    "userId": 1
}

# Make a POST request to create new data
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)

# Check if the request was successful (HTTP status code 201 for created)
if response.status_code == 201:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')