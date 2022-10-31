import pandas as pd
import matplotlib.pyplot as plt

def Break(x):
    txt='{} -------------------------------------------------------------------------------------------------------------'
    print(txt.format(x))

def Comm(x):
    txt='---- {} ----'
    print(txt.format(x))

print(pd.__version__)

mydataset = {
    'cars': ['BMW', 'Volvo', 'Ford'],
    'passings': [3, 7, 2]
}

myvar = pd.DataFrame(mydataset)
print(mydataset)
print(myvar)

Break('Series')
Comm('Pandos serija yra tarsi lentelės stulpelis. Tai vienmatis masyvas, kuriame saugomi bet kokio tipo duomenys.')

a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

myvar = pd.Series(a, index=["x", "y", "z"])
print(myvar)
print(myvar["y"])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

myvar = pd.Series(calories, index=["day1", "day2"])
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)

Break('DataFrame')
Comm('„Pandas DataFrame“ yra dvimatė duomenų struktūra, pavyzdžiui, dvimatis masyvas arba lentelė su eilutėmis ir stulpeliais.')

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df)

print(df.loc[0]) # Nurodomas tam tikras eilučių kiekis
print(df.loc[[0, 1]])

df = pd.DataFrame(data, index=["day1", "day2", "day3"]) # Suteikti indeksams pavadinimus
print(df)
print(df.loc["day2"])

Break('Read CSV')
df = pd.read_csv('data.csv') # Nuskaitome CSV failą
print(df)
print(df.to_string()) # Grąžina viską

print(pd.options.display.max_rows) # Galite patikrinti didžiausią sistemos eilučių skaičių naudodami teiginį pd.options.display.max_rows.

pd.options.display.max_rows = 9999
print(pd.options.display.max_rows)
print(df)

Break('Read JSON')

df = pd.read_json('data.json')

print(df.to_string())

df = pd.read_csv('data.csv')
print(df.head(10)) # pirmos 10 eilučių
print(df.tail()) # 5 paskutinės

print(df.info()) # Informacija

Break('Cleaning data')

df = pd.read_csv('data.csv')
new_df = df.dropna() # Tuščių eilučių pašalinimas
print(new_df.to_string())

df = pd.read_csv('data.csv')
df.dropna(inplace = True) # Pašalina iš pradinio rezultato
print(df.to_string())

df = pd.read_csv('data2.csv')
df.fillna(130, inplace = True) # suteikia cisur kur NULL reikšmę 130
df["Calories"].fillna(130, inplace = True) # Suteikia Calories stulpelio NULL reikšmes 130

Comm('Įprastas būdas pakeisti tuščius langelius yra apskaičiuoti stulpelio vidurkį, medianą arba režimo reikšmę. „Pandas“ naudoja vidurkio () median () ir mode () metodus, kad apskaičiuotų atitinkamas nurodyto stulpelio vertes:')


df = pd.read_csv('data2.csv')
x = df["Calories"].mean() # Apskaičiavimas
df["Calories"].fillna(x, inplace = True) # Pakeitimas
print(df.to_string())
print(df.duplicated()) # Dublikatu aptikimas
print(df.drop_duplicates()) # Dublikatu pašalinimas

Break('Corr')
Comm('Corr() metodas apskaičiuoja ryšį tarp kiekvieno duomenų rinkinio stulpelio.')

df = pd.read_csv('data2.csv')
print(df.corr())
df.plot()
plt.show()
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
df["Duration"].plot(kind = 'hist')
plt.show()

