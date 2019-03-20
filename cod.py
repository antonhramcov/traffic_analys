import pandas as pd
i = pd.read_csv('input.csv', sep=',')
print ('how to sort?')
print ('1- length and destination')
print ('2- length and source')
print ('3- protocol and destination')
print ('4- protocol and source')
vb=int(input())
if vb==1:
    r = i.groupby(['Length', 'Destination'])['No.'].count()
if vb==2:
    r = i.groupby(['Length', 'Source'])['No.'].count()
if vb==3:
    r = i.groupby(['Protocol', 'Destination'])['No.'].count()
if vb==4:
    r = i.groupby(['Protocol', 'Source'])['No.'].count()
df = pd.DataFrame(r)
print(df)
df.to_csv('output.csv')
