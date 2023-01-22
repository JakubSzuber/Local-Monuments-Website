# Local-Monuments-Website
This project is containerized web application created completely form scratch. Whole application is my autorship. Application is composed of 3 containers: postgres, nginx and gunicorn. In a nutshell: PostgreSQL works as our database that stores all data about monuments, gunicorn manages the traffic (content of the website) to the nginx server so you can just simple enter the localhost and use whole website. To see more information about how the website works run this application and enter the About page. This project shows plenty of ways on how to run this app but I recommend you to choose the Docker Compose because of they low complexity and short time required to run an app. When you already run this app you could enter [localhost](http://localhost:80) (default port 80) to see home page of the application.

https://user-images.githubusercontent.com/90647840/213920380-63ca8d57-2ef3-4bf2-9328-165cae569b28.mov

---

# Stack
Python-related tools:
- Flask
- Psycopg2
- Black

Container-related tools:
- Docker
- Docker Compose
- Docker Swarm Stack
- Kubernetes

Other:
- PostgreSQL
- Nginx
- Gunicorn WSGI server
- Bash
- Linux
- Git
- Web Lanuages (HTML, CSS, JavaScript)

<details>
<summary><b>Click to see the project structure:</b></summary>

```$ tree Local-Monuments-Website
.
├───.idea
│   └───...
├───.git
│   └───...
├─── docker-compose.yml
├─── docker-stack.yml
├─── visualizer.stack.yml
├─── k8s-manifests
│    ├── postgres.yml
│    ├── gunicorn.yml
│    ├── nginx.yml
│    └── namespace.yml
├─── README.md
├─── LICENSE
└─── services
     ├─── database
     │    ├─── Connecting.txt
     |    └─── Dockerfile
     ├─── proxy-server
     │    ├─── conf
     |    └─── Dockerfile
     └─── WSGI-server
          ├── Dockerfile
          ├── .dockerignore
          ├── infrastructure.png
          ├── docker-entrypoint.sh
          ├── main_python_files
          │   ├── __init__.py
          │   ├── config.py
          │   ├── init_db.py
          │   └── routes.py
          ├── requirements.txt
          ├── run.py
          └── src                    
              ├── static
              │   ├── css
              │   │   ├── about.css
              │   │   ├── base.css
              │   │   ├── gallery.css
              │   │   └── home.css
              │   └── js
              │       ├── base.js
              │       ├── gallery.js
              │       └── home.js
              └── template
                  ├── about.html
                  ├── base.html
                  ├── gallery.html
                  └── home.html
```
</details>

---

# How to run app
> **Note**
> Remember that this project implements only core functionality so you should add your additional stuff in case of deploying this app on the production environment

<details>
<summary><b>Click to look at the demo process of deploying this app (example with Docker Compose):</b></summary>

https://user-images.githubusercontent.com/90647840/213922371-848ff6b3-60a8-4db2-94fb-7b11dbf41b42.mov

</details>

## Requirements
Whatever method to run the application you will chose you need to have [Docker](https://www.docker.com/) and [Git](https://git-scm.com/downloads) installed you your computer first. You can download docker on any OS [here](https://docs.docker.com/get-docker/). Currently best way of installing a Docker is to install whole [Docker Desktop](https://www.docker.com/products/docker-desktop/) (supported for Windows, macOS, Linux). If you already have a Docker and Git you will have to download only a images used by containers but this process should consume not more that 400 MB and is automatically performed before each container is launched (every container use lightweight versions of the images to reduce memory and time while building them, and reduce vulnerabilities). **Rememeber to run docker daemon (by e.g. open Docker Desktop app) before deploying an app localy or to make sure that your are in the cluster if you want to deploy this app in it.**

# Recommended method:
## Docker Compose

To run the app with compose file first, you have to clone this repo wherever you:
```shell
git clone https://github.com/JakubSzuber/Local-Monuments-Website
```

Enter the project's directory:
```shell
cd Local-Monuments-Website
```

Launch all containers that will communicate between each other by using the same bridge network, created by docker compose by default. You can add -d flag to disable logs:
```shell
docker-compose up
```

# Other methods:
## Docker commands
You can deploy localy this app by creating containers one by one by using docker commands separately. The order of the command is important!

First create a bridge network for the containers:
```shell
docker network create monuments_net
```

Run your postgres database:
```shell
docker container run
-d
--name flask-database
--expose 5432
-e POSTGRES_USER=admin
-e POSTGRES_PASSWORD=admin
-e POSTGRES_DB=flask_db
-v postgres_data:/var/lib/postgresql/data
--cpus "0.50"
--memory 128M
--network monuments_net
--restart always
jakubszuber/custom-postgres
```

Run your main container responsible for the application logic (this container contains all necessary files):
```shell
docker container run
-d
--name
wsgi-server
--expose 5000
--cpus "0.50"
--memory 256M
--network monuments_net
--restart always
jakubszuber/custom-gunicorn
```

Run your nginx proxy server:
```shell
docker container run
-d
--name nginx-server
-p 80:80
--cpus "0.50"
--memory 32M
--network monuments_net
--restart always
jakubszuber/custom-nginx
```

## Docker Swarm Stack
You xxxtodonapisz o tym ze kontener nginx more pare razy sie zrestartowac przed finalnym dzialaniem aplikacji z powodu ze..wiec bedzie trzeba poprostu poczekac nie wiecej niz minute

To run the app with compose file first, you have to clone this repo wherever you:
```shell
git clone https://github.com/JakubSzuber/Local-Monuments-Website
```

Enter the project's directory:
```shell
cd Local-Monuments-Website
```

Furthermore you can use good looking [visualizer]([https://www.docker.com/](https://github.com/yandeu/docker-swarm-visualizer)) to https://github.com/yandeu/docker-swarm-visualizer to visualize your Docker Swarm cluster. To see dashboard enter http://localhost:9500
```shell
docker stack deploy --replicas -c visualizer.stack.yml visualizer
```

## Docker Swarm commands
You can deploy localy this app by creating containers one by one by using docker commands in some kind of terminal like e.g Powershell, cmd. The order of the command is important!

> **Note**
> TODOyou won't have x, y, z..."placement:" part that is in docker-stack.yml and you will have only one replica instad of two as it's specified in docker-stack.yml

First create a bridge network for the containers (you can additionally add flags to specify your gateway, network's private IPv4, and subnet mask e.g. "--gateway 127.0.0.1" --subnet 127.0.0.1/24):
```shell
docker network create --driver overlay monuments_net
```

Run your postgres database by this command
```shell
docker service create
--name flask-database
--label app=local-monument-website
--update-parallelism 2
--update-delay 10s
--restart-condition on-failure
--restart-delay 10s
--restart-max-attempts 3
--restart-window 120s
--limit-cpu 0.50
--limit-memory 256M
--reserve-cpu 0.25
--reserve-memory 128M
--env POSTGRES_USER=admin
--env POSTGRES_PASSWORD=admin
--env POSTGRES_DB=flask_db
--mount type=volume,src=postgres_data,dst=/var/lib/postgresql/data
--network monuments_net
jakubszuber/custom-postgres
```

Run your main container responsible for the application logic (this container contains all necessary files) by this command:
```shell
docker service create
--name wsgi-server
--label app=local-monument-website
--update-parallelism 2
--update-delay 10s
--restart-condition on-failure
--restart-delay 10s
--restart-max-attempts 3
--restart-window 120s
--limit-cpu 0.50
--limit-memory 512M
--reserve-cpu 0.25
--reserve-memory 256M
--with-registry-auth
--network monuments_net
jakubszuber/custom-gunicorn
```

Run your nginx proxy server by this command:
```shell
docker service create
--name proxy-server
--label app=local-monument-website
--update-parallelism 2
--update-delay 10s
--restart-condition on-failure
--restart-delay 10s
--restart-max-attempts 3
--restart-window 120s
--limit-cpu 0.50
--limit-memory 256M
--reserve-cpu 0.25
--reserve-memory 128M
--publish published=80,target=80
--with-registry-auth
--network monuments_net jakubszuber/custom-nginx
```

Furthermore you can use good looking [visualizer]([https://www.docker.com/](https://github.com/yandeu/docker-swarm-visualizer)) to https://github.com/yandeu/docker-swarm-visualizer to visualize your Docker Swarm cluster. To see dashboard enter http://localhost:9500
```shell
docker stack deploy --replicas -c visualizer.stack.yml visualizer
```

## Kubernetes
> **Note**
> Directory k8s-manifests contains manifest files that are made generic because there are always many external tools in the kubernetes production environment so those manifest files only implement the most core and basic infrastructure (if you want to use it you will have to enhance them significantly)

xxx
kubectl create namespace local-monument-website

## Kubernetes Iperative commands
xxx

## Kubernetes Iperative objects
xxx

## Docker Declarative objects
xxxtodo...
kubectl create namespace Local-Monuments-Website
kubectl apply -f k8s-manifests

# Final result & Clean up
dodaj jak usunac kontener i obraz irp. czyli zeby wyczyscic co trzrba

![image](https://user-images.githubusercontent.com/90647840/209741199-e433f15f-7473-4e12-8705-b3c049ba8bd7.png)
todoxxxxafter launching all containers you should see in Docker Desktop containers list similar view to above what means that every conatiner is running successively. Now you can click on whatever container to see information about it's image layers or enter the container's inspection, terminal, logs or stats.

<details><summary>Text source</summary>

https://pl.wikipedia.org/wiki/Kolegiata_Naj%C5%9Bwi%C4%99tszej_Maryi_Panny_Kr%C3%B3lowej_%C5%9Awiata_w_Stargardzie
https://www.pomorzezachodnie.travel/Zaplanuj_pobyt-Przydatne_informacje-Miejsca_kultu_religijnego-Kosciol_Rzymskokatolicki/a,4146/Kosciol_pw_sw_Jana_Chrzciciela
https://pl.wikipedia.org/wiki/Ko%C5%9Bci%C3%B3%C5%82_%C5%9Bw._Jana_w_Stargardzie
https://pl.wikipedia.org/wiki/Brama_Pyrzycka_w_Stargardzie
https://pomorzezachodnie.travel/Poznawaj-Dziedzictwo_Pomorza-Fortyfikacje_i_militaria-Obwarowania_miejskie/a,6195/Brama_Pyrzycka
https://sciaga.pl/tekst/51768-52-stargardzkie_zabytki_brama_pyrzycka
https://pl.wikipedia.org/wiki/Brama_Wa%C5%82owa
https://pomorzezachodnie.travel/Spedzaj_czas-Kulturalnie-Galerie/a,5123/Brama_Walowa
https://pl.wikipedia.org/wiki/Brama_M%C5%82y%C5%84ska_w_Stargardzie
http://baza-turystyczna.eu/wojewodztwo-zachodnio-pomorskie--4/miasto-stargard_szczecinski--66/zabytki/obiekt-brama_portowa_mlynska--120/
https://pl.wikipedia.org/wiki/Wie%C5%BCa_ci%C5%9Bnie%C5%84
http://baza-turystyczna.eu/wojewodztwo-zachodnio-pomorskie--4/miasto-stargard_szczecinski--66/zabytki/obiekt-wieza_cisnien--118/
https://pl.wikipedia.org/wiki/Wie%C5%BCa_ci%C5%9Bnie%C5%84_w_Stargardzie
https://www.wikiwand.com/pl/Wie%C5%BCa_ci%C5%9Bnie%C5%84_w_Stargardzie
https://pomorzezachodnie.travel/Poznawaj-Dziedzictwo_Pomorza-Zabytki_techniki_i_inzynierii/a,6197/Wieza_cisnien
https://pl.wikipedia.org/wiki/Baszta
https://pl.wikipedia.org/wiki/Baszta_Morze_Czerwone
https://pomorzezachodnie.travel/Poznawaj-Dziedzictwo_Pomorza-Fortyfikacje_i_militaria-Obwarowania_miejskie/a,6196/Baszta_Morze_Czerwone
https://tropter.com/pl/polska/stargard/baszta-morze-czerwone
https://pl.wikipedia.org/wiki/Baszta_Bia%C5%82og%C5%82%C3%B3wka
https://www.polska.travel/pl/muzea/baszta-bialoglowka
https://pl.wikipedia.org/wiki/Ratusz_w_Stargardzie
https://pomorzezachodnie.travel/Zaplanuj_pobyt-Przydatne_informacje-Urzedy_publiczne/a,2763/Urzad_Miasta_Stargard_Ratusz_Staromiejski_
https://zabytek.pl/pl/obiekty/stargard-ratusz)

Links to each used image is in the file [init_db.py](https://github.com/JakubSzuber/Local-Monuments-Website/blob/main/services/web/main_python_files/init_db.py)
 
</details>
