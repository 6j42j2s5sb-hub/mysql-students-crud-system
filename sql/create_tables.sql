CREATE TABLE corsi (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome_corso VARCHAR(255)
);

CREATE TABLE studenti (
    id_stud INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(255),
    cognome VARCHAR(255),
    corso_di_studio INT,
    FOREIGN KEY (corso_di_studio) REFERENCES corsi(id)
);