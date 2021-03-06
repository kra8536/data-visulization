import csv
import pandas as pd
import numpy as np
import re

murderFile1="murder_data/Murder-2001-2012.csv"
murderFile2="murder_data/Murder-2013.csv"
murderFile3="murder_data/Murder-2015.csv"
def murderDataIntegration():
	df1=pd.read_csv(murderFile1)
	df2=pd.read_csv(murderFile2)
	df3=pd.read_csv(murderFile3,encoding = "ISO-8859-1")
	df1=df1[['STATE/UT','GENDER','YEAR','Total']]
	df2=df2[['STATE/UT','GENDER','YEAR','Total']]
	df3=df3[['State/UT','Number of Victims - Total of All Age Groups - T']]

	df1['GENDER']=(df1.loc[df1['GENDER']=='Total'])
	df1=df1.dropna()
	# print(df1.head)
	df2['GENDER']=(df2.loc[df2['GENDER']=='Total'])
	df2=df2.dropna()
	# df3=df3[(df3['State/UT']=="")]
	df3=df3.drop(df3[df3['State/UT'].isin(["TOTAL (STATES)","TOTAL (UTS)","TOTAL (ALL INDIA)"])].index)
	# appending data and renaming
	df=df1.append(df2)
	df=df.drop('GENDER',1)
	df=df.rename(columns={'STATE/UT':'State','YEAR':'Year','Total':'Total'})

	df3['Year']='2015'
	df3=df3.rename(columns={'State/UT':'State','Year':'Year','Number of Victims - Total of All Age Groups - T':'Total'})
	df=df.append(df3)
	print(df.shape)
	return df

murderDataIntegration()