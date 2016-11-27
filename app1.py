import pandas as pd
import matplotlib.pyplot as plt

pd.options.display.mpl_style = 'default'
plt.style.use('ggplot')
plt.interactive(False)
years = pd.Series([1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999])

guitars = pd.DataFrame({'Store1': [584, 601, 403, 480],
                        'Store2': [1032, 960, 1400, 1355],
                        'Year': [2012, 2013, 2014, 2015]})
print(guitars['Store1'])
print(guitars[guitars['Store1'] > 500])
print(guitars[['Store1', 'Year', 'Store2']])
print(guitars.loc[3])
print(guitars.loc[0:2])

_2016 = pd.DataFrame([[None, 300, 2016]], columns=guitars.columns)
guitars = guitars.append(_2016, ignore_index=True)
print(guitars)
guitars = guitars.fillna(method='ffill')
print(guitars)
guitars = guitars.set_index('Year')
print(guitars)
guitars.plot()
plt.show()