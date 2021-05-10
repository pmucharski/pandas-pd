import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# s = pd.Series(np.random.randn(1000), pd.date_range('01/01/2020', periods=1000))
#
# s = s.cumsum()
# print(s)
# s.plot()
# plt.show()
#
# data = {"Kraj": ['Belgia', 'Indie', 'Brazylia', 'Polska'],
#         "Stolica": ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
#         "Kontynent": ['Europa', 'Azja', 'Ameryka Połudiowa', 'Europa'],
#         "Populacja": [412343243, 43214234, 54645736, 34635354]}
#
# df = pd.DataFrame(data)
# print(df)
#
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# wykres = grupa.plot.bar()
# wykres.set_xlabel('Populacja')
# wykres.set_ylabel("Mld")
#
# plt.xticks(rotation=0)
# plt.title('Populacja z przedziałem na kontynenty')
# plt.savefig('wykres.png')
# plt.show()

#zad.1
# xlsx = pd.ExcelFile('imiona.xlsx')
# df1 = pd.read_excel(xlsx, header=0)
# print(df1)
# df2 = df1.groupby(['Rok'])['Liczba'].sum()
# print(df2)
# df2.plot()
# plt.show()

#zad.2
# xlsx = pd.ExcelFile('imiona.xlsx')
#
# data = pd.read_excel(xlsx, header=0)
#
# df = pd.DataFrame(data)
#
# grupa = df.groupby(['Plec']).agg({'Liczba': {'sum'}})
#
# wykres = grupa.plot.bar()
# wykres.set_ylabel('Mld')
# plt.show()

#zad.3
grupa = df.where(df['Rok'] > 2012).groupby(['Plec']).agg({'Liczba': {'sum'}})