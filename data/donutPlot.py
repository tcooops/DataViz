# Libraries
import matplotlib.pyplot as plt
 
# Make data: I have 3 groups and 7 subgroups
group_names=['Canada', 'America', 'Germany']
group_size=[239,243,157]
subgroup_names=['Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze', 'Gold', 'Silver', 'Bronze']
subgroup_size=[123,75,41,60,112,71,58,60,39]
 
# Create colors
a, b, c=[plt.cm.Reds, plt.cm.Blues, plt.cm.Greens]
 
# First Ring (outside)
fig, ax = plt.subplots()
ax.axis('equal')
mypie, _ = ax.pie(group_size, radius=1.3, labels=group_names, colors=[a(0.9), b(0.7), c(0.5)] )
plt.setp( mypie, width=0.3, edgecolor='white')
 
# Second Ring (Inside)
mypie2, _ = ax.pie(subgroup_size, radius=1.3-0.3, labels=subgroup_names, labeldistance=0.7, colors=[a(0.8), a(0.4), a(0.3), b(0.3), b(0.7), b(0.5), c(0.5), c(0.6), c(0.3)])
plt.setp( mypie2, width=0.4, edgecolor='white')
plt.margins(0,0)
 
# show it
plt.show()
