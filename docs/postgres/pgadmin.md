# Comunicação entre Conteiners

Para que nossos conteiners se comuniquem, precisamos construir uma rede que os conecta

## Criado uma Rede Usando Docker

```bash
docker network create --driver bridge my-network
```

Você pode trocar "my-network" pelo nome que preferir.

## Checando se a rede foi criada

```bash
docker network ls
```

## Criando o conteiner PostGrees dentro da nossa Rede

```bash
docker run --name my-postgres --network=my-network -p 3000:5432 -e POSTGRES_PASSWORD=postgres -d postgres
```

## Podemos inspecionar tudo que está ligado na nossa rede

```bash
docker inspect my-network
```

## Criando um Conteiner com PgAdmin dentro da rede para acessar o BD

```bash
docker run --name my-pgadmin --network=my-network -p 3001:80 -e PGADMIN_DEFAULT_EMAIL=test@gmail.com -e PGADMIN_DEFAULT_PASSWORD=postgres -d dpage/pgadmin4
```

## Para acessar o PgAdmin, vá para seu navegador e digite

```bash
localhost:3001

```

agora basta preencher com o email e senha que cadastrou:

```bash
email: test@gmail.com
senha: postgres
```

### Faça o seguinte processo na GUI

- Conto esquerdo superior
  - Server
    - Register
      - Server

  - General
    - name (docker)
    - Connection
    - hostname/address (my-postgres)
    - Port (5432)
    - Maintanance database (postgres)
    - username (postgres)
    - password (postgres)

- Save

[Tutorial-1](https://www.youtube.com/watch?v=CdoBvd_bPdk)
[Tutorial-2](https://www.youtube.com/watch?v=WzMpOnyLAU4)
