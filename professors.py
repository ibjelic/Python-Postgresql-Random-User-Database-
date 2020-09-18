import psycopg2
t_host = "localhost"
t_port = "5432"
t_dbname = "postgres"
t_user = "postgres"
t_pw = "toor"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_conn.autocommit = True
db_cursor = db_conn.cursor()

#db_cursor.execute(query)
#result = db_cursor.fetchall()




from name import imena

ime = []
imena = imena.split("\n")
for i in range(len(imena)):
    if(len(imena[i])>2):
        ime.append(imena[i])

from surname import prezimena
prezime = []
prezimena = prezimena.split("\n")
for i in range(len(prezimena)):
    if(len(prezimena[i])>2):
        prezime.append(prezimena[i])

predmeti = ['Matematika', 'Srpski', 'Geografija', 'Istorija', 'Muzicko' , 'Likovno', 'Fizicko', 'Hemija', 'Fizika', 'Biologija','Engleski'] #exams
import random
random.seed()
import string

def pwgen(duzina):
    karakteri = string.ascii_letters + string.digits
    rezultat = ''.join(random.choice(karakteri) for i in range(duzina))
    return rezultat

for i in range(len(predmeti)):
    ime_broj = random.randrange(len(ime))
    prezime_broj = random.randrange(len(prezime))
    godine = random.randrange(30,65)

    user_ime_broj = random.randint(1,len(ime[ime_broj]))
    user_prezime_broj = random.randint(1,len(prezime[prezime_broj]))

    korisnicko_ime = ime[ime_broj][0:user_ime_broj].lower() + prezime[prezime_broj][0:user_prezime_broj].lower() + str(godine)

    user_ime_broj = random.randint(1,len(ime[ime_broj]))
    user_prezime_broj = random.randint(1,len(prezime[prezime_broj]))
    email = ime[ime_broj][0:user_ime_broj].lower() + prezime[prezime_broj][0:user_prezime_broj].lower() + str(prezime_broj) + "@ff.bg.ac.rs"
    sifra = pwgen(random.randrange(8,20))
    #print("Ime: " +ime[ime_broj] + "\nPrezime: " + prezime[prezime_broj] + "\nGodine: " + str(godine) + "\nUsername: " + korisnicko_ime + "\nMail: " + email +"\nPassword: " + sifra)
    try: 
        query = "insert into public.profesor(id, korisnik, ime, prezime, sifra, email, godine,predmet) values("+str(i+1)+", '"+korisnicko_ime+"','"+ime[ime_broj]+"','"+prezime[prezime_broj]+"','"+sifra+"','"+email+"',"+str(godine)+",'"+predmeti[i]+"')"
        db_cursor.execute(query)
    except:
        print("nesto ponovljeno")
        
db_cursor.close()
db_conn.close()