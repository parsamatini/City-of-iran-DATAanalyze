# book 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Resource 
with open("data.txt", "r", encoding="utf-8") as file:
    content = file.read()
# Data Extraction 
content_split_comma = content.split(',')

Content2 = []

for item in content_split_comma:
    Content2.extend(item.split('\n'))

# print(Content2)

number_columns = 4 

number_rows = len(Content2)// number_columns + (1 if len(Content2)% number_columns != 0 else 0 )

array = np.empty((number_rows, number_columns),dtype=object)


for i, i2 in enumerate(Content2):
    row = i// number_columns
    column = i % number_columns
    array[row,column] = i2



#DATA Cleaning 
data = {
    'City': array[:, 0],
    'Lat': [float(i.split('° N')[0]) if '° N' in i else np.nan for i in array[:, 1]],
    'Long': [float(i.split('° E')[0]) if '° E' in i else np.nan for i in array[:, 2]],
    'Population': array[:, 3],
}

df = pd.DataFrame(data)

# print(df['City'])

# picture : 
    # visualize: 
plt.scatter(df['Long'], df['Lat'], marker='o', s=df['Population'].astype(float)/10000, linestyle='-', color='b',alpha=0.3)
plt.xlim([40, 65])
plt.ylim([25, 40])
plt.xticks(np.arange(40, 65, 2))
plt.yticks(np.arange(25, 40, 2))

plt.title('Iran_City')
plt.xlabel('Long')
plt.ylabel('Lat')
plt.show()






