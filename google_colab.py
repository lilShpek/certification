import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
categories = data['whoAmI'].unique()
for category in categories:
    data[category] = (data['whoAmI'] == category).astype(int)
data.drop(columns=['whoAmI'], inplace=True)
data.head()