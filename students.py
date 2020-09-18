import psycopg2
t_host = "localhost"
t_port = "5432"
t_dbname = "postgres"
t_user = "postgres"
t_pw = "toor"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_conn.autocommit = True
db_cursor = db_conn.cursor()


from name import imena #string that contains names

ime = []
imena = imena.split("\n")
for i in range(len(imena)):
    if(len(imena[i])>2): #when i gathered data for names and surnames I got some letters like 1 (a,b,c,d..) and 2 like (nj,dz)
        ime.append(imena[i])

from surname import prezimena #string with surnames
prezime = []
prezimena = prezimena.split("\n")
for i in range(len(prezimena)):
    if(len(prezimena[i])>2):
        prezime.append(prezimena[i])

import random
random.seed()
import string

def pwgen(duzina):
    karakteri = string.ascii_letters + string.digits
    rezultat = ''.join(random.choice(karakteri) for i in range(duzina))
    return rezultat

greska = 0 #error

for i in range(1000):
    ime_broj = random.randrange(len(ime)) #get random name from list
    prezime_broj = random.randrange(len(prezime))
    age = random.randrange(6,15) #random age

    user_ime_broj = random.randint(1,len(ime[ime_broj])+1) #first N characters from name (N is random)
    user_prezime_broj = random.randint(1,len(prezime[prezime_broj])+1)

    korisnicko_ime = ime[ime_broj][0:user_ime_broj].lower() + prezime[prezime_broj][0:user_prezime_broj].lower() + str(age) #username name[1:rand]+surname[1:rand]+age

    user_ime_broj = random.randint(1,len(ime[ime_broj])+1) #same process for email
    user_prezime_broj = random.randint(1,len(prezime[prezime_broj])+1)
    email = ime[ime_broj][0:user_ime_broj].lower() + prezime[prezime_broj][0:user_prezime_broj].lower() + str(prezime_broj) + "@ff.bg.ac.rs"
    sifra = pwgen(random.randrange(15,30))
    try:
    #print("Ime: " +ime[ime_broj] + "\nPrezime: " + prezime[prezime_broj] + "\nGodine: " + str(age) + "\nUsername: " + korisnicko_ime + "\nMail: " + email +"\nPassword: " + sifra)
        query = "insert into public.ucenik(id, korisnik, ime, prezime, sifra, email, godine) values("+str(i+1)+", '"+korisnicko_ime+"','"+ime[ime_broj]+"','"+prezime[prezime_broj]+"','"+sifra+"','"+email+"',"+str(age)+")"
        db_cursor.execute(query)
    except:
        greske=greske+1
        #print("nes ponovljeno")
print(str(i+1-greske) + " ucenika dodato")
print("Greska: " + str(float(greske)/(i+1))) #errors from repeating same uniqe values like username, email
db_cursor.close()
db_conn.close()