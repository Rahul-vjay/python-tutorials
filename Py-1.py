
#%%
import pandas as pd
data = pd.read_excel('Python1.xlsx', engine= 'openpyxl')
print (data)

# %%
l1 = ["sunny, don't run", 1]
d1 = {
    "name" : "sunny",
    "college": "iim"
}

type(l1)
type(d1)


# %%
name_age_dict = dict(zip(data['Name'], data['Age']))


# %%
min_income = data['Income'].min()
# %%
max_income = data['Income'].max()
# %%
avg_income = data['Income'].mean()
# %%
