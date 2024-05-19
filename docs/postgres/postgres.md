# Aprendendo a criar um banco de dados postgres no docker

## Comandos básicos para conseguir informações sobre seus contaners

### Visualização de todos os conteiners em execução

```bash
docker ps
```

### Visualização de todos os Conteiners em execução e parados

```bash
docker ps -a
```

### Visualizando todas as imagens disponiveis

```bash
docker images
```

## Configurando imagem postgres para nosso uso pelo terminal

### Baixando a versão mais atualizada de uma imagem do postgrees

```bash
docker pull postgres
```

### Criando um conteiner com a imagem

```bash
docker run --name database -p 2222:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

### Argumentos que podem ser alterados

- docker run: Esse comando é usado para executar um contêiner a partir de uma imagem.
- --name database: Define o nome do contêiner como "database".
- -p 3000:5432: Mapeia a porta 3000 do host para a porta 5432 do contêiner. Isso permite que você acesse o PostgreSQL no contêiner através da porta 3000 do host.
- -e POSTGRES_PASSWORD=admin: Define a variável de ambiente POSTGRES_PASSWORD com o valor - "postgres", que é a senha para o usuário padrão "postgres".
- -d: Executa o contêiner em segundo plano (modo detached).
- postgres: Especifica a imagem que será usada para criar o contêiner, neste caso, a imagem oficial do PostgreSQL.

### Criando nosso Conteiner de testes no terminal

```bash
docker run --name database -p 3000:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

### Desligando nosso Conteiner

Para desligar (parar) um contêiner Docker, pode-se usar o comando docker stop.

```bash
docker stop database
```

### Ligando um conteiner já criado

Nesse caso, "database" é o nome do contêiner criado com o comando:

```bash
docker run --name database 
```

### Removendo meu Conteiner

```bash
docker rm -f database
```

O -f força a remoção do contêiner, mesmo que ele esteja em execução. Tenha cuidado ao usar -f, pois isso irá encerrar abruptamente o contêiner, o que pode resultar em perda de dados se houver processos em execução dentro do contêiner.

### Iniciando um Conteiner Parado/Desligado

```bash
docker start nome_do_contêiner
````

```bash
docker start id_do_contêiner
```

