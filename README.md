# Local-Monuments-Website
This project is containerized web application created form scratch. Whole application is totally my autorship. This project show plenty of ways to run this app but I recommend you to choose the standard Docker commands or Docker Compose becouse of they complexity and short time required to run an app. When you already run this app you could enter [localhost:80](https://localhost:80) to see page interface where you can click to see next slide with next Poland's monument.
 
![image](https://user-images.githubusercontent.com/90647840/174489265-b7abd087-1823-4bcd-9f2d-d313f2702a20.png) 

---

# Tools used in the project
*Main tools:* [![](https://img.shields.io/badge/Python-C1E1C1?style=for-the-badge&logo=Python&logoColor=blue)](https://www.python.org/) [![](https://img.shields.io/badge/PostgreSQL-FFFFFF?style=for-the-badge&logo=PostgreSQL&logoColor=blue)](https://www.python.org/) [![](https://img.shields.io/badge/Docker-FFFFFF?style=for-the-badge&logo=Docker&logoColor=blue)](https://www.docker.com/) <br>
*Python libraries:* `Flask`, `Psycopg2` <br>
*Other tools:* `Kubernetes`, `Docker Compose`, `Docker Swarm`

---

# How to run app

## Requirments
Whatever method to run the application you will chose you need to have [Docker](https://www.docker.com/) installed you your computer. You can download docker on any OS [here](https://docs.docker.com/get-docker/).

# Recommended:
## Docker commands
First you have to run your main container with flask content

```shell
docker container run -d jakubszuber/munument-app-flask
```

Then you need to run your postgres database

```shell
docker container run -d jakubszuber/munument-app-database
```

Next stem is run your revere porxy server - nginx

```shell
docker container run -d jakubszuber/munument-app-nginx
```


## Docker Compose
xxx

# Other methods:
## Docker Swarm commands
xxx

## Docker Swarm Stack
xxx

## Kubernetes Iperative commands
xxx

## Kubernetes Iperative objects
xxx

## Docker Declarative objects
xxx



<br>
<br>
todo:

dodaj "drzewo glownego folderu" na repozytorium
dodaj zdjecia z docker desktop albo konsoli ze co powinno byc widac jesli kontener poprawnie chodzi
dodaj jak usunac kontener i obraz irp. czyli zeby wyczyscic co trzrba
dodaj do moich cutom images health check?

> **Note**
> This is a note

> **Warning**
> This is a warning

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013513-95f18734-233d-45d3-aaf5-d6aec687db0e.mov

</details>
