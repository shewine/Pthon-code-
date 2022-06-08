import numpy as np
import pandas as pd




data = pd.read_excel (r'C:\Users\Shewine\Desktop\course\python\Data1.xlsx')
df =  pd.DataFrame(data, columns= ['edible','Size','shape','colour'])
print (df)
