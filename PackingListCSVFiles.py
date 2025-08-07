import csv

data = [
  ['Item', 'Quantity'],
  ['Blender', 2],
  ['Posters', 30],
  ['Shoes', 2]
]

try:
    with open("PKList.csv",'r',encoding='utf8') as file:
        content = csv.reader(file)
        for row in content:
            print(row)

except FileNotFoundError:
    print("Packing list not found. Creating a new one.")
    with open('PKList.csv', 'w',newline='') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerows(data)
        print("List has beeen created")


