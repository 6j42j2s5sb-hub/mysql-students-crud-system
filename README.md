Sistema CRUD (Create, Read, Update, Delete) per la gestione di studenti e corsi, sviluppato in Python con connessione a MySQL.
Il progetto dimostra competenze reali di:

interazione Python ↔ database

SQL
 
gestione dati relazionali

logging

modularità del codice

architettura pulita

CRUD completo

gestione errori

Perfetto per ruoli Data Analyst e Data Engineer.

Tecnologie utilizzate
Python 

MySQL

mysql-connector-python

Logging

SQL

Struttura del progetto
Codice
mysql-students-crud-system/
│
├── src/
│   ├── main.py

│
└── sql/
    ├── create_database.sql     → crea il database
    ├── create_tables.sql       → crea le tabelle
    └── sample_data.sql         → dati di esempio
    
Gestione studenti (CRUD)
Inserimento studente

Modifica nome/cognome

Eliminazione per nome/cognome/id

Ricerca per nome/cognome/id

 Gestione corsi
Inserimento corso

Visualizzazione corsi disponibili

 Logging
Ogni operazione viene registrata nel file app.log

Tracciamento errori e modifiche

 Gestione errori
Try/except su tutte le operazioni critiche

Messaggi chiari e logging degli errori

 Schema del database
Codice
+-----------+         +----------------+
|  corsi    | 1 ----∞ |   studenti     |
+-----------+         +----------------+
| id        |         | id_stud        |
| nome_corso|         | nome           |
|           |         | cognome        |
|           |         | corso_di_studio|
+-----------+         +----------------+
Relazione uno-a-molti:
un corso → molti studenti.
