CREATE USER IF NOT EXISTS 'ingestor'@'%' IDENTIFIED BY 'ingestorpass';
GRANT ALL PRIVILEGES ON meteorologia.* TO 'ingestor'@'%';
FLUSH PRIVILEGES;
