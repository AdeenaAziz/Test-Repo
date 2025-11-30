import requests

# Data to update the post
updated_post = {
    "id": 1,
    "title": "Updated Title",
    "body": "This post has been updated.",
    "userId": 1
}

# Make a PUT request to update existing data
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)

# Check if the request was successful (HTTP status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.json())
else:
    # Print an error message if the request was not successful
    print(f'Error: {response.status_code}')