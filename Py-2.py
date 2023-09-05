#%%
l1 = ["a","b","c","d"]
l2 = [1,2,3,4,5] #list(range(1,6))

len(l1)

# %%
l1.append("e")
print(l1)

# %%
del l1[1]
print(l1)
# %%
combined = l1+l2
#%%
print(combined)

#%%

for i in range(0, len(l1)):
    print(i)

# %%

x = 0
for abc in range(0, len(l1)):
    x += 1 # x = x + 1
    print("x = ", x)
    print(l1[abc])

# %%
