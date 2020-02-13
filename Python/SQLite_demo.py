import sys
import sqlite3
import os.path

def lisää_henkilö_tietokantaan(conn, cursor):
    # kysytään syöte
    etu = input("Anna henkilön etunimi: ")
    suku = input("Anna henkilön sukunimi: ")
    email = input("Anna henkilön sähköpostiosoite: ")

    # lisätään rivi tietokantaan
    # HUOM! SQL-injektiovaara
    sql = f"INSERT INTO nimet VALUES ('{etu}','{suku}','{email}')"
    cursor.execute(sql)
    conn.commit()
    print("Rivi lisätty tietokantaan.")

def listaa_asiakkaat(cursor):
    print("Haetaan asiakkaat tietokannasta...")
    sql = "SELECT * FROM nimet"
    rivit = cursor.execute(sql)
    for rivi in rivit:
        print(rivi)

def luo_tietokanta_taulu(cursor):
    # taulun luonti
    cursor.execute("""CREATE TABLE IF NOT EXISTS nimet
                      (etunimi text, sukunimi text, email text)""")
    print("Nimet-tietokantataulu luotu.")


print("Avataan tietokanta...")
tietokanta = r"C:\Academy\Oulu\1-2020\Python\Data\Tietokanta.sqlite.db"

# jos tietokantaa ei ole olemassa, luodaan se ja lisätään sinne uusi taulu
luo_taulu = False
if (not os.path.exists(tietokanta)):
    print("Tietokantaa ei ole olemassa, luodaan se.")
    luo_taulu = True

conn = sqlite3.connect(tietokanta)
c = conn.cursor()
if (luo_taulu):
    luo_tietokanta_taulu(c)
print("Tietokantayhteys avattu.")

if (len(sys.argv) > 1):
    if (sys.argv[1] == "listaa"):
        listaa_asiakkaat(c)
else:
    lisää_henkilö_tietokantaan(conn, c)

conn.close()
print("Tietokantayhteys suljettu.")
