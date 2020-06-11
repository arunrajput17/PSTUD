## Matplotlib - save chart to file using savefig

import matplotlib.pyplot as plt
# %matplotlib inline      # to render chart in jupiter notebook

exp_vals = [1400,600,300,410,250]
exp_labels = ['Home Rent', 'Food','Phone/Internet Bill','Car','Other Utilities']

#autopct is used for displaying percentage and in which format upto decimal
# shadow will show shadow
#explode will cut out the pie
# startangle to rotate pie chart

plt.axis('equal')
plt.pie(exp_vals, labels=exp_labels, radius=1.5, autopct='%0.2f%%', shadow=True, explode=[0,0.1,0.1,0,0], startangle=180)

# png, pdf,
plt.savefig('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\piechart.png',bbox_inches='tight', 
pad_inches=2)
plt.savefig('D:\\Day Shift\\Zpyth\\Pstud\\ReadWriteFiles\\piechart.pdf',bbox_inches='tight', 
pad_inches=2)
plt.show()

