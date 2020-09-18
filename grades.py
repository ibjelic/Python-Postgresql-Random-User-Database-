import psycopg2
t_host = "localhost"
t_port = "5432"
t_dbname = "postgres"
t_user = "postgres"
t_pw = "toor"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_conn.autocommit = True
db_cursor = db_conn.cursor()

db_cursor.execute("select * from public.profesor")
profesori = db_cursor.fetchall()

db_cursor.execute("select * from public.ucenik")
ucenici = db_cursor.fetchall()

import random
random.seed()

predmeti = [ 
            [5]*3 + [4]*8 + [1]*4 + [2]*5 + [3]*5, #Matematika
            [5]*4 + [4]*9 + [1]*2 + [2]*4 + [3]*6, #srpski
            [5]*5 + [4]*10 + [3]*5 + [2]*3 + [1]*2, #geografija
            [5]*5 + [4]*10 + [3]*5 + [2]*3 + [1]*2, #istorija
            [5]*8 + [4]*10 + [3]*5 + [2]*1 + [1]*1, #muzicko
            [5]*8 + [4]*10 + [3]*5 + [2]*1 + [1]*1, #likovno
            [5]*10 + [4]*10 + [3]*3 + [2]*1 +[1]*1, #fizicko
            [5]*4 + [4]*7 + [3]*6 + [2]*5 + [1]*3, #hemija
            [5]*4 + [4]*7 + [3]*6 + [2]*5 + [1]*3, #fizika
            [5]*5 + [4]*6 + [3]*7 + [2]*5 + [1]*2, #biologija 
            [5]*4 + [4]*9 + [1]*2 + [2]*4 + [3]*6 #engleski
] #random weighted grades 

for i in range(len(profesori)):
    for j in range(len(ucenici)):
        query = "insert into public.predmeti(predmet,profesor, ucenik, ocena) values('"+profesori[i][7]+"',"+str(profesori[i][0])+","+str(ucenici[j][0])+","+str(random.choice(predmeti[i]))+")"
        db_cursor.execute(query)

db_cursor.close()
db_conn.close()