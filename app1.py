import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

pd.options.display.mpl_style = 'default'
plt.style.use('ggplot')
plt.interactive(False)

mcro = pd.read_excel('D://USW/PM/Assessment/EIKON/MCRO_L_31_Dec_2011_To_30_Sep_2016.xlsx',sheetname='Sheet1')

print(mcro['%Chg'].std(axix=0))

years = pd.Series([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999])

guitars = pd.DataFrame({'Store1': [584, 601, 403, 480],
                        'Store2': [1032, 960, 1400, 1355],
                        'Year': [2012, 2013, 2014, 2015]})
model = ols('Store1 ~ Store2', guitars).fit()
#print(guitars['Store1'])
#print(guitars[guitars['Store1'] > 500])
#print(guitars[['Store1', 'Year', 'Store2']])
#print(guitars.loc[3])
#print(guitars.loc[0:2])

_2016 = pd.DataFrame([[None, 300, 2016]], columns=guitars.columns)
guitars = guitars.append(_2016, ignore_index=True)
#print(guitars)
guitars = guitars.fillna(method='ffill')
#print(guitars)
guitars = guitars.set_index('Year')
guitars.index = pd.to_datetime(guitars.index,format='%Y')
#print(model.summary())
#guitars.plot(ylim=0)
#guitars.plot(kind='bar')
#plt.show()