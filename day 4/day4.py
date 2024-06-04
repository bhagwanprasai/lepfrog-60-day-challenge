import pandas as pd

a = [1,7,2]

myvar = pd.Series(a)

print(myvar)
print(myvar[0])


#labels
myvar = pd.Series(a,index=["x","y","z"])

print(myvar)

print(myvar["y"])

#key value as series

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)


calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

myvar = pd.DataFrame(data)

print(myvar)
print(myvar.loc[0])

print(myvar.loc[[0,1]])

df = pd.read_csv('data.csv')

print(df.to_string())

#without using to string

print(df)

print(pd.options.display.max_rows)


#json file 
df = pd.read_json('data.json')

print(df.to_string())

#anaalysing data
df = pd.read_csv('data.csv')
print(df.head(10))


#dropping data
df = pd.read_csv('data1.csv')

new_df = df.dropna()

print(new_df.to_string())

#remove all null values

df = pd.read_csv('data1.csv')

df.dropna(inplace = True)

print(df.to_string())

#remove null values and replace empty cells
df = pd.read_csv('data1.csv')

df.fillna(130, inplace = True)

