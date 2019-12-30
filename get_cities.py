import mysql.connector
import csv


mydb = mysql.connector.connect(
    host="localhost",
    port="8889",
    user="root",
    passwd="root",
    database="cities_of_the_world"
    )

mycursor = mydb.cursor()

sql =   "INSERT INTO cities (name, name_ascii, lat, lng, country, iso2, iso3, admin_name, capital, population, id_city) \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
values = []

with open('worldcities.csv') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        city = row['city']
        city_ascii = row['city_ascii']
        lat = row['lat']
        lng = row['lng']
        country = row['country']
        iso2 = row['iso2']
        iso3 = row['iso3']
        admin_name = row['admin_name']
        capital = row['capital']
        population = row['population']
        id_city = row['id']
        val = [city, city_ascii, lat, lng, country, iso2, iso3, admin_name, capital, population, int(id_city)]
        values.append(val)


mycursor.executemany(sql,values)
mydb.commit()

print(mycursor.rowcount, "was inserted.") 

        
