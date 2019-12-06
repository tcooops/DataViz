import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify 

# If you have 2 lists
squarify.plot(sizes=[20,75,20,20,20,239,54,20,20,20,20,20,20,27,106,55,20,21,54,157,20,61,20,20,45,20,20,20,106,20,71,20,106,20,20,109,243,20,20], label=["AUS: 7", "AUT: 75", "BEL: 1", "BLR: 7", "BUL: 5", "CAN: 239", "CHN: 54", "CRO: 6", "CZE: 16", "DEN: 5", "ESP: 1", "EST: 3", "EUA: 9", "EUN: 27", "FIN: 106", "FRA: 55", "FRG: 19", "GBR: 21", "GDR: 54", "GER: 157", "HUN: 6", "ITA: 61", "JPN: 13", "KAZ: 2", "KOR: 45", "NZL: 1", "POL: 14", "PRK: 2", "RUS: 106", "SLO: 9", "SUI: 71", "SVK: 3", "SWE: 106", "TCH: 9", "UKR: 10", "URS: 109", "USA: 243", "UZB: 1", "YUG: 1"], alpha=.7 )
plt.axis('off')
plt.show()
 
# If you have a data frame
# import pandas as pd
#df = pd.DataFrame({'nb_people':[239,243,157], 'group':["Canada", "America", "Germany"] })
#squarify.plot(sizes=df['nb_people'], label=df['group'], alpha=.8 )
#plt.axis('off')
