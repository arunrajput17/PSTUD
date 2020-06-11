## Matplotlib introduction

import matplotlib.pyplot as plt
# %matplotlib inline      # to render chart in jupiter notebook

x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

# printing the chart
print(plt.plot(x,y))
plt.show()

# changing color
print(plt.plot(x,y, color='green'))
plt.show()

# for thicker line and line style
print(plt.plot(x,y, color='green',linewidth=5,linestyle='dashdot'))
plt.show()

# setting X & Y label and title of chart
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title('Weather')
print(plt.plot(x,y, color='green',linewidth=5,linestyle='dotted'))
plt.show()

