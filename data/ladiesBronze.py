import csv
import matplotlib.pyplot as plt

# pie chart for men's hockey medal colors (gold, silver, bronze)
# arrays for each color

canadas = []
americas = []
germanys = []

categories = []

with open('ladiesBronze.csv') as csvfile:
		reader = csv.reader(csvfile)

		line_count = 0

		for row in reader:
			if line_count is 0:
				#parse that first row of text data out of the file
				categories.append(row)
				line_count += 1
			else:
				if row [4] == "CAN":
					print("Canadian female won bronze!")
					canadas.append(row[4])

				elif row [4] == "USA":
					print("American female won bronze!")
					americas.append(row[4])

				if row [4] == "GER":
					print("German female won bronze!")
					germanys.append(row[4])

					line_count += 1

print("Canada's Bronze medals: ", len(canadas))
print("America's Bronze medals: ", len(americas))
print("Germany's Bronze medals: ", len(germanys))

# plot a pie chart!
labels = ("Canada", "America", "Germany")
#Sizes are how many and how large t he slices of the pie chart will be
sizes = [len(canadas), len(americas), len(germanys)]
colors = ['red', 'blue', 'gold']
explode = (0.1, 0, 0)

plt.pie(sizes, explode=explode, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.axis('equal')

plt.legend(labels, loc=1)
plt.title("Bronze Medals for Female Winter Olympic Athletes")
plt.xlabel("Medals Since 1924")
plt.show()
