## Matplotlib - Histograms

import matplotlib.pyplot as plt
# %matplotlib inline      # to render chart in jupiter notebook


Blood_sugar = [113,85,90,150,149,88,93,115,135,80,77,82,129]

## Ploting histogram
# plt.hist(Blood_sugar, bins=3, rwidth=0.95)  # bins are used to defin how many bars needed, and rwidth for bar space
plt.hist(Blood_sugar, bins=(80,100,125,150),rwidth=0.95, color='g')
plt.show()


## two side by side histogram
Blood_sugar_men = [113,85,90,150,149,88,93,115,135,80,77,82,129]
Blood_sugar_women = [67,98,89,120,133,150,84,69,89,79,120,112,100]

plt.xlabel('Sugar range')
plt.ylabel('Total no. of patients')
plt.title('Blood sugar analysis')
plt.hist([Blood_sugar_men,Blood_sugar_women], bins=(80,100,125,150),rwidth=0.95, color=['green','orange'], 
label=['men','women'])
plt.legend()
plt.show()

## orientation to draw horizontally
plt.hist([Blood_sugar_men,Blood_sugar_women], bins=(80,100,125,150),rwidth=0.95, color=['green','orange'], 
label=['men','women'],orientation='horizontal')
plt.legend()
plt.show()


