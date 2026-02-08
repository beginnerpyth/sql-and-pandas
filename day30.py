import pandas as pd
import numpy as np
bios=pd.read_csv('bios.csv')
pand=pd.read_csv('pand.csv')
results=pd.read_csv("results.csv")
print(bios.columns)
print(pand.columns)
#print(bios.head())
#print(pand.tail())
#print(bios.loc[0:2,("born_date",'born_region')])
#print(pand.iloc[0:2,2:3])
#print(bios[(bios['name']=='Keith')&(bios['born_country']=='USA')])
#print(bios[bios['height_cm']>220])
#print(bios[bios['name'].str.contains("Keith",case=False)])#we can use "keith|patrick " it understnds this trick
#print(bios.loc[bios['height_cm']>120,["name","height_cm"]])
#print(bios[bios["name"]=="Keith"][["born_country","born_region"]])
#print(bios[(bios['born_country'].isin(["USA","UK","GBR"]))&(bios['name'].str.startswith("Keith","Patrick"))])
#print(bios.query('born_country=="USA" and born_city=="Washington"'))#it must be in string that gives us the value through condition
#pand['NAYAPULSE']=220
#pand['newpulse']=np.where(pand["Pulse"]<200,210,240)#that pulse <200 is condition i set and 210 is price and except that evryting becomes 240
#print(pand.head())
#print(pand.drop(columns='newpulse',inplace=True))#dropping for temporarily
#print(pand.drop(0))
#jand=pand.copy()
#jand['Pulse']=3.99
#print(jand.head())
#pand['totalpulse']=pand['Pulse']*pand['Maxpulse']
#print(pand.head())
#pand.rename(columns={'Pulse':"horw"})#when we do rename we use set brackets
#print(pand.head())
#cios=bios.copy()
#cios['naya']=cios["name"].str.split(' ').str[0]
#print(cios.head())
cios=bios
#cios["born.d"]=pd.to_datetime(cios['born_date'])
#cios['born_year']=cios['born.d'].dt.year
#print(cios.head())
#def add(anything):
#    if anything["height_cm"]<160 and anything['weight_kg']>70:
 #       return"its a light weight"
 #   elif anything['height_cm']<180 and anything['weight_kg']>80:
 #       return"its a average"
 #   else:
 #       return"its a heavyweight"
#cios["weight_class"]=cios.apply(add,axis=1)
#noc=pd.read_csv("noc_regions.csv")
#bios=pd.merge(bios,noc,left_on="born_country",right_on="NOC",how='left')
#print(bios.head())
#bios.rename(columns={"region":"realheaven"},inplace=True)
#print(bios.columns)
#print(bios[bios['NOC_x']!= bios['realheaven']][['name','NOC_x',"realheaven"]])
#usa=bios[bios["born_country"]=="USA"].copy()
#gbr=bios[bios["born_country"]=="GBR"].copy()
#data=pd.concat([gbr,usa])
#print(data.head())
#results=pd.merge(results,bios,on='athlete_id',how='left')
#print(results.head(5))
#print(results.columns)
#pand.loc[0:3,"Pulse"]=np.nan
#pand.loc[0:3,"Pulse"]=90
pand.loc[4:5,"Pulse"]=np.nan
#print(pand.head())
#print(pand.isna().sum())
#pand=pand.fillna(1000)
#pand=pand.fillna(pand['Pulse'].mean())#it gives the mean value
#pand=pand.fillna(pand['Pulse'].interpolate())#it gives the average between value before it value after it
pand['Pulse']=pand['Pulse'].interpolate()#so when we do pand[]=pand[] it is setting permanently
print(pand.head(6))
print(pand.dropna)#it removes all na and whole row

print(pand.dropna(subset=['Pulse'],inplace=True))#another way to clear specific column with na and change permanently
print(pand[pand['Pulse'].isna()])#to check specific column have na 
print(pand[pand["Pulse"].notna()])#shows data of column not na values
