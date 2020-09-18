create table ucenik (
id serial primary key,
korisnik varchar(50) unique not null ,
ime varchar(50) not null,
prezime varchar(50) not null,
sifra varchar(50) not null,
email varchar(50) unique not null,
godine int not null,
prosek numeric 
)

create table profesor(
id serial primary key,
korisnik varchar(50) unique not null,
ime varchar(50) not null,
prezime varchar(50) not null,
sifra varchar(50) not null,
email varchar(50) unique not null,
godine int not null,
predmet varchar(50) not null
)


create table predmeti(
predmet varchar(50) not null,
profesor int not null,
ucenik int not null,
ocena int ,
primary key (ucenik, profesor),
foreign key (ucenik) 
	references ucenik(id),
foreign key (profesor) 
	references profesor(id)
)