# A toy visualization for extracted files....
import pandas as pd
import sqlite3
import argparse
import seaborn as sns
import matplotlib.pyplot as plt

args = None
database_path = None

parser = argparse.ArgumentParser(description='Read database with data and shows a set of visualizations for data.')
parser.add_argument('db', help='Complete path of .db file (sqlite database). Example: ../data/database.db')
args = parser.parse_args()

if args == None:
    database_path = 'data/database2.db'
else:
    database_path = str(args.db)


# Read sqlite query results into a pandas DataFrame
con = sqlite3.connect(database_path)
sql = """
        Select addr.Latitude as Latitude, addr.Longitude as Longitude, stt.StreetName as Rua,
            addr.Number as Número, addr.DistrictName as Bairro, addr.CityName as Cidade,
            stt.PostalCode as CEP, addr.RegionName as Estado, addr.CountryName as País,
            addr.Occurences as Ocorrências
        from Address as addr inner join Street as stt on stt.PostalCode=addr.PostalCode
      """
df = pd.read_sql_query(sql, con)
print("First, shows the head of dataframe with data in the required format.")
print(df.drop(['Ocorrências'], axis=1).head())

print("Press Enter to continue...")
input()

no_rows = df.shape[0]
print(f"The Dataframe has {no_rows} rows")

no_district_na = df['Bairro'].isna().sum()
print(f"""Number of rows with empty district: [{no_district_na}] or [{(no_district_na/no_rows)*100}%]""")
print("Press Enter to continue...")
input()

print("Now, will plot a barplot with District x No of occurences (remember, the NA is discarded).")
print("Press Enter to continue...")
input()

fig, ax = plt.subplots(figsize=(11,8))
sns.countplot(y="Bairro", data=df, orient='v', order = df['Bairro'].value_counts().index)
plt.xlabel("Número de Pontos")
plt.tight_layout()
plt.show()
print("Press Enter to continue...")
input()

print("Now, will see the top points (more occurences on the files.)")
print(df.sort_values("Ocorrências", ascending=False).head())
print("Press Enter to continue...")
input()

print("Finished, for more stuff, you have my resume and know what to do :)")
