#Corey Brewer Shark Attacks Analysis
#11/7/2017

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#here I am importing the data from a csv file... Not sure why I had to use "ISO-8859-1" but thats what the internet said
df = pd.read_csv('shark_attacks.csv', encoding = "ISO-8859-1")

#print(df.head())

#print(df['Country'].value_counts())

df_surfers = df.groupby(['Activity']).get_group('Surfing')

print(df_surfers['Country'].value_counts())

print(df_surfers['Fatal (Y/N)'].value_counts())

#Here I will try to isolate only the countries
# with more than 10 surf shark attacks

surf_by_country = df_surfers.groupby(['Country']).filter(lambda x: x['Country'].value_counts() > 10)

print(surf_by_country['Country'].value_counts())

#print(surf_by_country.describe())


print(surf_by_country['Fatal (Y/N)'].value_counts())

surf_df = pd.DataFrame(columns=['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'BRAZIL', 'REUNION', 'NEW ZEALAND'],
                       index=['Y', 'N', 'UNKNOWN'])
print(surf_df)

usa = surf_by_country.groupby(['Country']).get_group('USA')
aus = surf_by_country.groupby(['Country']).get_group('AUSTRALIA')
s_afr = surf_by_country.groupby(['Country']).get_group('SOUTH AFRICA')
bra = surf_by_country.groupby(['Country']).get_group('BRAZIL')
reu = surf_by_country.groupby(['Country']).get_group('REUNION')
n_zea = surf_by_country.groupby(['Country']).get_group('NEW ZEALAND')

usa1 = usa['Fatal (Y/N)'].value_counts()
aus1 = aus['Fatal (Y/N)'].value_counts()
s_afr1 = s_afr['Fatal (Y/N)'].value_counts()
bra1 = bra['Fatal (Y/N)'].value_counts()
reu1 = reu['Fatal (Y/N)'].value_counts()
n_zea1 = n_zea['Fatal (Y/N)'].value_counts()

print(usa1)

finald = pd.DataFrame(data=[usa1, aus1, s_afr1, bra1, reu1, n_zea1], index=['USA', 'AUSTRALIA', 'SOUTH AFRICA', 'BRAZIL', 'REUNION', 'NEW ZEALAND']).fillna(0)
print(finald)

#data to plot
n_groups = 6
N = finald['N']
Y = finald['Y']
Unk = finald['UNKNOWN']

#create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
pos = list(range(len(N))) #this is to set the position of each bar

rects1 = plt.bar(pos, N, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Not Fatal')

#Next bar position is the index plus the width... and so on
rects2 = plt.bar([p + bar_width for p in pos], Y, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Fatal',
                 bottom=0)

rects3 = plt.bar([p + bar_width*2 for p in pos], Unk, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Unknown',
                 bottom=0)

plt.xlabel('Country')
plt.ylabel('Total Amount')
plt.title('Surf Shark Attacks')
plt.xticks(index + bar_width, ('USA', 'AUSTRALIA', 'SOUTH AFRICA', 'BRAZIL', 'REUNION', 'NEW ZEALAND'))
plt.legend()

plt.tight_layout()
plt.show()
