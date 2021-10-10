import pandas as pd

cv19 = pd.read_csv('caso_full.csv')

cv19 = cv19.drop("epidemiological_week", axis=1)
cv19 = cv19.drop("city_ibge_code", axis=1)
cv19 = cv19.drop("is_last", axis=1)
cv19 = cv19.drop("is_repeated", axis=1)
cv19 = cv19.drop("last_available_confirmed_per_100k_inhabitants", axis=1)
cv19 = cv19.drop("order_for_place", axis=1)
cv19 = cv19.drop("estimated_population_2019", axis=1)
cv19 = cv19.drop("last_available_date", axis=1)

colSP = cv19.loc[cv19["state"] == ("SP")]

x = str(input("digite:(1) para as cidades e (2) para estadoSP:")).lower()

while x != ("1","2"):

    x = str(input("digite:(1) para as cidades e (2) para estadoSP:")).lower()

    if x == "2":

        colSP1 = colSP.loc[colSP["place_type"] == "state"]

        css = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")
        
# Erro usando o código data2 = pd.to_datetime(css, '%d-%m-%y').date() abaixo

#        Digite
#        a
#        data
#        nesse
#        formato(ano - mês - dia)
#        ex: yyyy - mm - dd:20 - 12 - 2020
#        Traceback(most
#        recent
#       call
#        last):
#        File
#        "C:\Users\Jooj\APIG3\teste2.py", line
#        30, in < module >
#        data2 = pd.to_datetime(css, '%d-%m-%y').date()
#    File
#    "C:\Users\Jooj\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\tools\datetimes.py", line
#   914, in to_datetime
#    result = convert_listlike(np.array([arg]), format)[0]
#File
#"C:\Users\Jooj\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\tools\datetimes.py", line
#401, in _convert_listlike_datetimes
#result, tz_parsed = objects_to_datetime64ns(
#    File
#"C:\Users\Jooj\AppData\Local\Programs\Python\Python39\lib\site-packages\pandas\core\arrays\datetimes.py", line
#2167, in objects_to_datetime64ns
#assert errors in ["raise", "ignore", "coerce"]
#AssertionError

        colDTS = colSP1.loc[colSP1["date"] == css]

        colDTS = colDTS.drop("date", axis=1)
        colDTS = colDTS.drop("state", axis=1)
        colDTS = colDTS.drop("place_type", axis=1)

        print(colDTS)
        break


    elif x == "1":

        colSP1 = colSP.loc[colSP["place_type"] == "city"]

        cd = str.title(input("Digite o nome da cidade(escreva com letras maiusculas e acento)ex:São Paulo:"))

        colCD = colSP1.loc[colSP1["city"] == cd]

        dt = input("Digite a data nesse formato(ano-mês-dia)ex:yyyy-mm-dd:")

        colDT = colCD.loc[colCD["date"] == dt]

        colDT = colDT.drop("date", axis=1)
        colDT = colDT.drop("state", axis=1)
        colDT = colDT.drop("place_type", axis=1)

        print(colDT)
        break


