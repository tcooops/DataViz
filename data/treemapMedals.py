import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify 

squarify.plot(sizes=[123,75,41,60,112,71,58,60,39], label=["CAN- Gold", "CAN- Silver", "CAN- Bronze", "USA- Gold", "USA- Silver", "USA- Bronze", "GER- Gold", "GER- Silver", "GER- Bronze"], alpha=.7 )
plt.axis('off')
plt.show()
 
