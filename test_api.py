import requests

response = requests.get('http://localhost:5000/')
print(f"Status Code: {response.status_code}")
print(f"Content: {response.text}")

response = requests.get('http://localhost:5000/about')
data = response.json()
print(f"Name: {data.get('name')}")
print(f"Course: {data.get('course')}")
print(f"Semester: {data.get('semester')}")

name = "Devora"
response = requests.get(f'http://localhost:5000/greet/{name}')
if name in response.text:
    pass

response = requests.get('http://localhost:5000/calculate?num1=10&num2=5&operation=add')
print(response.json())
response = requests.get('http://localhost:5000/calculate?num1=7&num2=3&operation=multiply')
print(response.json())

test_data = {
    "message": "Hello Flask",
    "user": "Devora",
    "timestamp": "2026-02-16"
}
response = requests.post('http://localhost:5000/echo', json=test_data)
data = response.json()
if data.get('echoed') == True:
    pass

response = requests.get('http://localhost:5000/status/404')
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")
response = requests.get('http://localhost:5000/status/500')
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

response = requests.get('http://localhost:5000/')
custom_header = response.headers.get('X-Custom-Header')
print(f"Custom Header: {custom_header}")

response = requests.get('http://localhost:5000/calculate?num1=10&num2=0&operation=divide')
print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")
