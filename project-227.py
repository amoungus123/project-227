import json
import csv
import
data_from_csv = []
with open('data_set.txt', 'r') as f: 
	data_from_txt = json.loads(f.read())

field_names = ['brake', 'hand_brake',  'throttle', 'steer']
csvfilestore = open('project_227.csv', 'w', newline='')
writer = csv.DictWriter(csvfilestore, fieldnames=field_names)
writer.writeheader()
writer.writerows(store_driving_data)

with open('project_227.csv', 'r') as file:
	reader = csv.reader(file)
	for row in reader:
		data_from_csv.append(row)
print(data_from_csv)