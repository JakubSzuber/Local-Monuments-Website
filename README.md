# Local-Monuments-Website
This project is containerized web application created form scratch. Whole application is totally my autorship. This project show plenty of ways to run this app but I recommend you to choose the standard Docker commands or Docker Compose because of they complexity and short time required to run an app. When you already run this app you could enter [localhost](https://localhost:80) (default port 80) to see page interface where you can click to see next slide with next Poland's monument.
 
![image](https://user-images.githubusercontent.com/90647840/174489265-b7abd087-1823-4bcd-9f2d-d313f2702a20.png) 

---

# Tools used in the project
*Main tools:* [![](https://img.shields.io/badge/Python-C1E1C1?style=for-the-badge&logo=Python&logoColor=blue)](https://www.python.org/) [![](https://img.shields.io/badge/PostgreSQL-FFFFFF?style=for-the-badge&logo=PostgreSQL&logoColor=blue)](https://www.python.org/) [![](https://img.shields.io/badge/Docker-FFFFFF?style=for-the-badge&logo=Docker&logoColor=blue)](https://www.docker.com/) <br>
*Python libraries:* `Flask`, `Psycopg2` 
<br>
*Other tools:* `Kubernetes`, `Docker Compose`, `Docker Swarm`

---

# How to run app
> **Note**
> If you will see error: "Internal Server Error" in browser that means you have to additionally use below command after run your containers:
```
docker exec -it web python main_python_files/init_db.py
```

## Requirments
Whatever method to run the application you will chose you need to have [Docker](https://www.docker.com/) installed you your computer. You can download docker on any OS [here](https://docs.docker.com/get-docker/).

# Recommended method:
## Docker Compose

To run app with compose file you have to create directory wherever you want and then clone from that repo...docker-compose up -d if...ordocker-compose up

# Other methods:
## Docker commands
You can deploy localy this app by creating containers one by one by using docker commands in some kind of terminal like e.g Powershell, cmd. The order of the command isn't important.
Run your nginx proxy server by this command:
```shell
docker container run --name nginx-server --network flask_network -p 80:80 custom-nginx
```

Run your main container responsible for the application logic (this container contains all necessary files) by this command:
```shell
docker container run --name web -p 5000:5000 --network flask_network flask_app
```

Run your postgres database by this command
```shell
docker container run --name flask-database -d --network flask_network -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=flask_db -v postgres_data:/var/lib/postgresql/data -p 5432:5432 postgres:13
```

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
do zakladni used tools dodaj nginx

```mermaid
C4Context
title System Context diagram for Internet Banking System

Person(customerA, "Banking Customer A", "A customer of the bank, with personal bank accounts.")
Person(customerB, "Banking Customer B")
Person_Ext(customerC, "Banking Customer C")
System(SystemAA, "Internet Banking System", "Allows customers to view information about their bank accounts, and make payments.")

Person(customerD, "Banking Customer D", "A customer of the bank, <br/> with personal bank accounts.")

Enterprise_Boundary(b1, "BankBoundary") {

  SystemDb_Ext(SystemE, "Mainframe Banking System", "Stores all of the core banking information about customers, accounts, transactions, etc.")

  System_Boundary(b2, "BankBoundary2") {
    System(SystemA, "Banking System A")
    System(SystemB, "Banking System B", "A system of the bank, with personal bank accounts.")
  }

  System_Ext(SystemC, "E-mail system", "The internal Microsoft Exchange e-mail system.")
  SystemDb(SystemD, "Banking System D Database", "A system of the bank, with personal bank accounts.")

  Boundary(b3, "BankBoundary3", "boundary") {
    SystemQueue(SystemF, "Banking System F Queue", "A system of the bank, with personal bank accounts.")
    SystemQueue_Ext(SystemG, "Banking System G Queue", "A system of the bank, with personal bank accounts.")
  }
}

BiRel(customerA, SystemAA, "Uses")
BiRel(SystemAA, SystemE, "Uses")
Rel(SystemAA, SystemC, "Sends e-mails", "SMTP")
Rel(SystemC, customerA, "Sends e-mails to")
```

```mermaid
pie showData
    title Key elements in Product X
    "Calcium" : 42.96
    "Potassium" : 50.05
    "Magnesium" : 10.01
    "Iron" :  5
```

<details>
<summary>Result</summary>

https://user-images.githubusercontent.com/1161307/171013513-95f18734-233d-45d3-aaf5-d6aec687db0e.mov

</details>

![](https://www.contrastsecurity.com/hs-fs/hubfs/images/DevOps%20Solutions/devops-old-way.gif?width=1322&name=devops-old-way.gif)

