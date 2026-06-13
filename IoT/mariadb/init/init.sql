CREATE TABLE IF NOT EXISTS estacions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id VARCHAR(50) NOT NULL,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS dades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    estacio_id INT NOT NULL,
    device_id VARCHAR(50) NOT NULL,
    temperatura FLOAT,
    humitat FLOAT,
    pressio_atmosferica FLOAT,
    velocitat_vent FLOAT,
    tipus VARCHAR(50),
    quality INT,
    recorded_at DATETIME,
    FOREIGN KEY (estacio_id) REFERENCES estacions(id)
);

INSERT INTO estacions (device_id, nom)
VALUES ('wemos01', 'Estació principal');

