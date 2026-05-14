import requests

a = int(input("Enter the number a: "))
b = int(input("Enter the number b: "))


url = f"http://localhost:5000/add/{a}/{b}"

response = requests.get(url)

data = response.json()

print(f"Result is: {data['result']}")