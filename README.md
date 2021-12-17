# Site de Lembretes
[![NPM](https://img.shields.io/apm/l/react)](https://github.com/Kaue-Silva/Site_Lembretes/blob/main/LICENSE)

## Sobre o Projeto

Projeto pensado na intenção de exercitar meus conhecimentos,
Site de Lembretes que guarda seus lembretes em um banco de dados.

## Informações sobre o projeto
- Docker
- Para contruir a imagem do docker foi utilizado volumes 
vinculando o diretorio do projeto ao mesmo no container,
ou seja toda alteração nos arquivos com o container em execução sera aplicado.

## Layout

Layout construido com auxilio do sistema de templates do Django e Bootstrap.

![lembretes listagens](https://github.com/Kaue-Silva/Site_Lembretes/blob/main/assets/Tela%20inicial.PNG)
![lembretes adição](https://github.com/Kaue-Silva/Site_Lembretes/blob/main/assets/Tela%20de%20adi%C3%A7%C3%A3o%20de%20lembretes.PNG)

## Tecnologias Utilizadas
## Back end
- Python
- Django
- postgreSQL

## Front end
- HTML / CSS
- Bootstrap

## Como executar o projeto
Pré-requisitos: Docker e Docker Compose
``` bash
# clonar o repositorio
git clone https://github.com/Kaue-Silva/Site_Lembretes

# entrar na pasta
cd Site_Lembretes

# iniciar com docker-compose
docker-compose up -d

# migração para o banco de dados pelo Django
docker-compose exec python3 manage.py migrate

# criação de um Super Usuario
docker-compose exec python3 manage.py createsuperuser
```

## Autor
Kauê Silva de Carvalho

https://www.linkedin.com/in/kaue-silva2004/
