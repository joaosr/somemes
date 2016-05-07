# Só Memes

## Aplicação utilizada na prática de dojo

### Executando com pyenv
 - É importante ter um ambiente Python configurado em sua máquina, então é fortemente recomendado a instalação do gerenciador de versões Python <a href="https://github.com/yyuu/pyenv" target="blank">pyenv</a>
 
 - É recomendado também ter o Python em sua versão 3.5.0, então para usar essa versão execute:
 
```sh
$ pyenv install 3.5.0
$ pyenv global 3.5.0
```
 - Clone o repositório:

```sh
$ git clone https://github.com/joaosr/somemes.git
```

 - Dentro do repositório local crie um ambiente Python com o virtualenv:
 
```sh
$ cd /path/somemes/
$ python -m venv .somemes
$ source .somemes/bin/activate
```

### Executando com docker

- Instale e o <a href="https://docs.docker.com/engine/installation/" target="blank">docker</a>

- Execute a seguinte linha:
```sh
docker build -t joao/memes:1.0 .
```

- E depois

```sh
docker exec -ti memes python manage.py createsuperuser --username superuser --email user@mail
```
