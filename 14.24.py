with open('24/24.5.txt', 'r') as file:
    data = file.read()

data = data.lower()

# It works only because we have no intersection
# between first and last letters
print(data.count('helloitmo'))
