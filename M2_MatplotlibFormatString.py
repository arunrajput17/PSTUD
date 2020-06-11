## Matplotlib format strings in plot function

import matplotlib.pyplot as plt
# %matplotlib inline      # to render chart in jupiter notebook


x=[1,2,3,4,5,6,7]
y=[50,51,52,48,47,49,46]

# plus marker visual and green color (g+) g = green, + = marker
print(plt.plot(x,y,'g+'))
plt.show()

# adding dash dash to above
print(plt.plot(x,y,'g+--'))
plt.show()

# adding dash dot
print(plt.plot(x,y,'g+-.'))
plt.show()

# can be specified in any order
print(plt.plot(x,y,'--r*'))
plt.show()

# Diamond marker
print(plt.plot(x,y,'rD--'))
plt.show()

# instead of format string we can also do this using keywords
print(plt.plot(x,y,color='red',marker='D',linestyle=''))
plt.show()

# marker size
print(plt.plot(x,y,color='red',marker='D',linestyle='',markersize=20))
plt.show()

# alpha for handling transperancy
print(plt.plot(x,y,color='red',alpha=0.2))
plt.show()




