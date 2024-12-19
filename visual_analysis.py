import cc_data_analysis
import matplotlib.pyplot as plt
import seaborn as sns



df = cc_data_analysis.top_30_highest_calls

chart = sns.histplot(df['Incoming Calls'], kde= True)

plt.show()

