## Matplotlib - Axes labels, Legend, Grid

import matplotlib.pyplot as plt
# %matplotlib inline      # to render chart in jupiter notebook


days=[1,2,3,4,5,6,7]
max_t=[32,51,52,48,47,49,56]
min_t=[43,42,40,44,33,35,37]
avg_t=[45,48,48,46,40,42,41]

# all min, max avg in one graoh
plt.xlabel('Days')                  # x axis name defined
plt.ylabel('Temperature')           # y axis name defined
plt.title('Weather')                # Chart name defined
print(plt.plot(days,max_t, label='Max'))        # set labels to define legends
print(plt.plot(days,min_t, label='Min'))
print(plt.plot(days,avg_t,label='Avg'))
# plt.legend()
# plt.legend(loc='lower left')    # to show legends in graph and loc for location of legends to be displayed
plt.legend(loc='best', shadow=True, fontsize='small')

plt.grid()      # to show grid lines in graph

plt.show()





