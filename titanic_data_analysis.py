import pandas as pd

df = pd.read_csv('titanic3.csv')
df_male = df[df['sex']=='male']
df_female = df[df['sex']=='female']

df_class_group = df.groupby('pclass').mean()
df_class_group_male = df_male.groupby('pclass').mean()
df_class_group_female = df_female.groupby('pclass').mean()

print(df['survived'].mean())
print(df_female['survived'].mean())
print(df_male['survived'].mean())
print(df_class_group)
print(df_class_group_male)
print(df_class_group_female)
