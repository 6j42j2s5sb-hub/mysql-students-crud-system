import mysql.connector
import logging

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="Scuola"
        )
        logging.info("Connessione al database riuscita.")
        return conn
    except mysql.connector.Error as e:
        logging.error(f"Errore di connessione: {e}")
        raise



def insert_student(cursor, db, nome, cognome, corso):
    try:
        sql = "INSERT INTO studenti (nome, cognome, corso_di_studio) VALUES (%s, %s, %s)"
        cursor.execute(sql, (nome, cognome, corso))
        db.commit()
        logging.info(f"Studente inserito: {nome} {cognome}")
    except Exception as e:
        logging.error(f"Errore inserimento studente: {e}")


def update_student(cursor, db, campo, nuovo_valore, id_stud):
    try:
        sql = f"UPDATE studenti SET {campo} = %s WHERE id_stud = %s"
        cursor.execute(sql, (nuovo_valore, id_stud))
        db.commit()
        logging.info(f"Studente {id_stud} aggiornato: {campo} -> {nuovo_valore}")
    except Exception as e:
        logging.error(f"Errore aggiornamento studente: {e}")


def delete_student(cursor, db, campo, valore):
    try:
        sql = f"DELETE FROM studenti WHERE {campo} = %s"
        cursor.execute(sql, (valore,))
        db.commit()
        logging.info(f"Studente eliminato dove {campo} = {valore}")
    except Exception as e:
        logging.error(f"Errore eliminazione studente: {e}")


def select_student(cursor, campo, valore):
    try:
        sql = f"SELECT * FROM studenti WHERE {campo} = %s"
        cursor.execute(sql, (valore,))
        risultati = cursor.fetchall()
        logging.info(f"Ricerca studenti per {campo} = {valore}")
        return risultati
    except Exception as e:
        logging.error(f"Errore ricerca studente: {e}")
        return []



def insert_course(cursor, db, nome_corso):
    try:
        sql = "INSERT INTO corsi (nome_corso) VALUES (%s)"
        cursor.execute(sql, (nome_corso,))
        db.commit()
        logging.info(f"Corso inserito: {nome_corso}")
    except Exception as e:
        logging.error(f"Errore inserimento corso: {e}")


def select_courses(cursor):
    try:
        cursor.execute("SELECT * FROM corsi")
        return cursor.fetchall()
    except Exception as e:
        logging.error(f"Errore lettura corsi: {e}")
        return []
