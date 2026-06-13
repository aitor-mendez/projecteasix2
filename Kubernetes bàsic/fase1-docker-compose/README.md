1. Descripció general

Aquesta fase implementa la versió inicial del projecte ShopMicro utilitzant Docker Compose.
L’objectiu és aixecar una arquitectura de microserveis funcional que inclou:

user-service → gestió d’usuaris i login

product-service → gestió i consulta de productes

order-service → creació de comandes

notification-service → processament d’esdeveniments

message-queue → RabbitMQ

cache → Redis

db-products i db-orders → MySQL

api-gateway → Nginx com a reverse proxy

frontend → interfície web HTML/JS

2. Estructura del directori

fase1-docker-compose/
│
├── docker-compose.yml
│
├── api-gateway/
│   └── nginx.conf
│
├── user-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── product-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── order-service/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── notification-service/
│   ├── worker.py
│   ├── requirements.txt
│   └── Dockerfile
│
└── frontend/
└── index.html

fase-2-3-docker-swarm/
|
├── api-gateway
│   └── nginx.conf
|
├── docker-stack.yml
├── frontend
│   └── index.html
|
├── notification-service
│   ├── Dockerfile
│   ├── requirements.txt
│   └── worker.py
|
├── order-service
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
|
├── product-service
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
|
└── user-service
    ├── Dockerfile
    ├── app.py
    └── requirements.txt

3. Requisits previs

- Docker instal·lat

- Docker Compose v2

- Port 8080 lliure (frontend)

- Port 8090 lliure (API Gateway)

- Ports de MySQL, Redis i RabbitMQ lliures

4. Com aixecar tota l’arquitectura

1) Construir i aixecar els serveis:

docker compose up -d --build

3) Comprovar l’estat dels contenidors:

docker compose ps

Els serveis principals han d’aparèixer com:

healthy → bases de dades, cache, message queue

up → microserveis Python

up → api-gateway i frontend

5. Accés a la plataforma

Frontend:
http://localhost:8080

API Gateway:
http://localhost:8090

RabbitMQ (panell de control):
http://localhost:15672

MySQL (productes i comandes):
Host: db-products o db-orders
Port: 3306

Usuari: definit al docker-compose

Contrasenya: definida al docker-compose

6. Flux de funcionament

1- L’usuari accedeix al frontend

2- Fa login → petició a /login via API Gateway

3- Carrega productes → /products

4- Crea una comanda → /order

5- L’order-service envia un missatge a RabbitMQ

6- El notification-service processa l’esdeveniment

7. Com aturar i eliminar els serveis

Aturar contenidors sense eliminar-los:

docker compose stop

Aturar i eliminar contenidors, xarxes i volums efímers:

docker compose down

Eliminar també volums persistents (ATENCIÓ: esborra dades):

docker compose down -v

docker compose down -v
