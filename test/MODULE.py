
import pandas as pd
# Charger le fichier Excel
df = pd.read_excel('Lexique383.xlsb')

# Afficher les premières lignes du DataFrame
print(df.head())
# Sélectionner une colonne
colonne_1 = df['ortho']
print('colonne_1')
# Enregistrer dans un nouveau fichier Excel
df.to_excel('nouveau_fichier.xlsx', index=False)
