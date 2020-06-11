## Matplotlib - Bar Chart

import matplotlib.pyplot as plt
import numpy as np
# %matplotlib inline      # to render chart in jupiter notebook


company = ['GOOGL','AMZN','MSFT','FB']
revenue = [90,136,89,27]
profit = [40,2,34,12]

#### Bar chart
plt.ylabel('revenue(bln)')
plt.title('US Tech Stocks')
plt.bar(company,revenue,width=0.4, label='Revenue')
plt.bar(company,profit,width=0.4, label='Profit') # it will generate same bar in same chart
plt.legend()
plt.show()

#### using numpy we can crete bar graph side by side by assigning position

xpos= np.arange(len(company))
print(xpos)
# plt.bar(xpos,revenue) # it will show numbers in x axis
plt.xticks(xpos, company)    # to replace numbers with name of company
plt.ylabel('revenue(bln)')
plt.title('US Tech Stocks')
# -0.2 from xpos is used to show bar side by side
plt.bar(xpos-0.2,revenue,width=0.4, label='Revenue')
plt.bar(xpos+0.2,profit,width=0.4, label='Profit')
plt.legend()
plt.show()


#### Horizontal bar chart
plt.yticks(xpos, company)    
plt.title('US Tech Stocks')
plt.barh(xpos-0.2,revenue,height=0.4, label='Revenue')
plt.barh(xpos+0.2,profit,height=0.4, label='Profit')
plt.legend()
plt.show()

