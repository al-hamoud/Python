import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
myindex = ['Store 1', 'Store 1', 'Store 2']
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=[myindex])
print('-------- df.head -------')
print(df.head())
print("-------- df['Cost'] --------")
print(df['Cost'])
print("-------- df.loc['Store 2'] --------")
print(df.loc['Store 2'])
print("-------- df.iloc[0] --------")
print(df.iloc[0])
print("-------- df.loc['Store 1', 'Cost'] --------")
print(df.loc['Store 1', 'Cost'])
print("-------- df.loc[:, ['Name', 'Cost']] --------")
print(df.loc[:,['Name', 'Cost']])
copy_df = df.copy()
copy_df = copy_df.drop('Store 1')
print('--------')
print(copy_df)
print('Adding new Culumn')
df['Location'] = None
print(df)