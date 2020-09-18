import psycopg2
t_host = "localhost"
t_port = "5432"
t_dbname = "postgres"
t_user = "postgres"
t_pw = "toor"
db_conn = psycopg2.connect(host=t_host, port=t_port, dbname=t_dbname, user=t_user, password=t_pw)
db_conn.autocommit = True
db_cursor = db_conn.cursor()
db_cursor.execute("select ucenik from public.predmeti")
ucenici = db_cursor.fetchall()
ucenici = list(dict.fromkeys(ucenici))
ucenici = [ucenici[i][0] for i in range(len(ucenici))]

for i in ucenici:
    db_cursor.execute("select sum(ocena) from public.predmeti where ucenik = "+str(i))
    ocene = db_cursor.fetchall()
    db_cursor.execute("update public.ucenik set prosek ="+str(float(ocene[0][0])/11)+"where id="+str(i))

db_cursor.close()
db_conn.close()