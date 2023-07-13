with open('artifacts.txt', 'a') as f:
    f.write('I am writing something new to see the change in DVC lock and in DAG')

with open('artifacts.txt', 'r') as f:
    text = f.read()

print(text)
