import os
import sys
import psycopg2

'''
def readImage():
        fin = open('./download.jpg', "rb")
        img = fin.read()
        fin.close()
        return img
'''
conn = psycopg2.connect(
        host="flask-database",  # Tutaj moze byc: localhost albo flask-database
        database="flask_db",
        user='admin',  # tu moze byc inaczej
        password='admin',
        port=5432)  # tu moze byc inaczej

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute('DROP TABLE IF EXISTS monuments;')
cur.execute('CREATE TABLE monuments (id serial PRIMARY KEY,'
                                 'name varchar (40) NOT NULL,'
                                 'description varchar (10000) NOT NULL,'
                                 'image_path varchar(200) NOT NULL);'
                                 )

# Insert data into the table

# cur.execute('INSERT INTO monuments (name, description, XXXXXX)'
#             'VALUES (%s, %s, %s)',
#             ('Kolegiata',
#              '''
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#                   Since ragdolls don’t have an undercoat, the amount of shedding and dander production is lower than that of heavier coated breeds. However, many people are still allergic to saliva and skin secretions from cats, and ragdolls produce these allergens, so they are not considered hypoallergenic. The ragdoll has a silky single coat (meaning that it doesn’t have an under-layer of fur). It’s meant to be lower-matting than other medium-haired cat coats. This breed still benefits from brushing at least twice a week to help avoid tangles.
#              ''',)
#             )
#
# cur.execute('INSERT INTO books (title, author, pages_num, review)'
#             'VALUES (%s, %s, %s, %s)',
#             ('Anna Karenina',
#              'Leo Tolstoy',
#              864,
#              'Another great classic!')
#             )
#data = readImage()
#binary = psycopg2.Binary(data)
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Cathedral of the Blessed Virgin Mary', 'Hi I am description', 'https://zabytki.tomekzuk.com/wp-content/uploads/2021/05/Stargard-kosciol-NMP-Krolowej-Swiata-01.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('St. Jan Church', 'Hi I am description', 'https://www.pomorzezachodnie.travel/media/cache/artykul_miniatura_big/media/original/media/default/0001/06/8197bedfd5a1277284357f83be8b29945aa49fc3.JPG')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Pyrzyce Gate', 'Hi I am description', 'https://pomorzezachodnie.travel/media/cache/artykul_miniatura_big/media/original/media/default/0001/11/0855d730bd2feba4dc7cf5ae01286aac2d9828d9.JPG')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('The shaft gate', 'Hi I am description', 'https://mapio.net/images-p/122772767.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Port gate', 'Hi I am description', 'https://polska-org.pl/foto/7646/Brama_Mlynska_ul_Portowa_Stargard_7646794.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Water tower', 'Hi I am description', 'http://baza-turystyczna.eu/image.php?size=800&file=20110810_4e42898f77874.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Red sea tower', 'Hi I am description', 'https://www.globtroter.pl/zdjecia/polska/b275173_polska_zachodniopomorskie_stargard.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('White head tower', 'Hi I am description', 'https://pomorzezachodnie.travel/media/cache/artykul_slider/media/default/0001/11/c367a0ae843c230a6080211ead5a63630c17523b.jpg')")
cur.execute("INSERT INTO monuments (name, description, image_path) VALUES ('Town hall', 'Hi I am description', 'https://pomorzezachodnie.travel/media/cache/artykul_miniatura_big/media/original/media/default/0001/11/d5d80db9a45a85e39f05887f41ea961f5a84e7b9.JPG')")

conn.commit()
cur.close()
conn.close()
