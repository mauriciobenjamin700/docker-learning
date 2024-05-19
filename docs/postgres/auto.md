# Automatizando o Uso do Terminal usando Docker Compose

Criar ambientes complexos pode ser cansativo, portando visand6 automatizar o processo, usaremos dockerfiles (mais específicamente, docker compose para isso).

## Configurando usando docker-compose

abra a pasta que irá criar seu docker compose

crie o seguinte arquivo ``docker-compose.yaml`

o docker compose terá a seguinte estrutura:

```yaml

version: '3.8'
services:
  postgres:
    image: postgres
    container_name: my-postgres
    environment:
      POSTGRES_PASSWORD: postgres
    ports:
      - "3000:5432"
    networks:
      - my-network

  pgadmin:
    image: dpage/pgadmin4
    container_name: my-pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: test@gmail.com
      PGADMIN_DEFAULT_PASSWORD: postgres
    ports:
      - "3001:80"
    networks:
      - my-network

networks:
  my-network:
    driver: bridge
```

Agora execute o comando `docker-compose up -d` no local do arquivo

### Detalhamento das Seções

#### Versão do Compose

```yaml
version: '3.8'
```
- **version**: Especifica a versão do formato do Docker Compose. A versão 3.8 é uma das mais recentes e suporta um conjunto abrangente de recursos.

#### Serviços

##### Serviço PostgreSQL

```yaml
services:
  postgres:
    image: postgres
    container_name: my-postgres
    environment:
      POSTGRES_PASSWORD: postgres
    ports:
      - "3000:5432"
    networks:
      - my-network
```

- **services**: Define os serviços que compõem o aplicativo.
- **postgres**: Nome do serviço, que será utilizado para referenciar este contêiner.
  - **image**: Especifica a imagem Docker a ser usada. Aqui, a imagem oficial do PostgreSQL é usada.
  - **container_name**: Define o nome do contêiner, que será `my-postgres`.
  - **environment**: Define variáveis de ambiente para o contêiner. Aqui, apenas a senha do PostgreSQL é definida.
  - **ports**: Faz o mapeamento de portas do host para o contêiner. `3000:5432` mapeia a porta 5432 do contêiner (porta padrão do PostgreSQL) para a porta 3000 no host.
  - **networks**: Especifica a rede à qual o contêiner será conectado. Aqui, `my-network`.

##### Serviço PgAdmin

```yaml
  pgadmin:
    image: dpage/pgadmin4
    container_name: my-pgadmin
    environment:
      PGADMIN_DEFAULT_EMAIL: test@gmail.com
      PGADMIN_DEFAULT_PASSWORD: postgres
    ports:
      - "3001:80"
    networks:
      - my-network
```

- **pgadmin**: Nome do serviço para PgAdmin.
  - **image**: Especifica a imagem Docker a ser usada, que é a imagem oficial do PgAdmin.
  - **container_name**: Define o nome do contêiner, que será `my-pgadmin`.
  - **environment**: Define variáveis de ambiente para configurar o PgAdmin. `PGADMIN_DEFAULT_EMAIL` e `PGADMIN_DEFAULT_PASSWORD` são usados para configurar as credenciais iniciais.
  - **ports**: Faz o mapeamento de portas do host para o contêiner. `3001:80` mapeia a porta 80 do contêiner (porta padrão do PgAdmin) para a porta 3001 no host.
  - **networks**: Especifica a rede à qual o contêiner será conectado. Aqui, `my-network`.

#### Redes

```yaml
networks:
  my-network:
    driver: bridge
```

- **networks**: Define as redes personalizadas utilizadas pelos serviços.
- **my-network**: Nome da rede.
  - **driver**: Define o driver da rede. `bridge` é o driver padrão para redes Docker, permitindo a comunicação entre contêineres conectados à mesma rede.

### Resumo

Este arquivo `docker-compose.yml` define dois serviços (`postgres` e `pgadmin`), ambos conectados a uma rede personalizada chamada `my-network`:

1. **PostgreSQL**: Um banco de dados PostgreSQL, acessível na porta 3000 do host e configurado com a senha `postgres`.
2. **PgAdmin**: Uma interface gráfica para gerenciar o PostgreSQL, acessível na porta 3001 do host e configurada com o e-mail `test@gmail.com` e a senha `postgres`.

A rede `my-network` permite que esses dois serviços se comuniquem entre si internamente, facilitando a conexão do PgAdmin ao PostgreSQL.

## Comandos para Manipular o Docker-Compose

### Comandos Básicos do Docker Compose na prática

1. **Iniciar Serviços**:
   ```sh
   docker-compose up -d
   ```
   - **-d**: Executa os contêineres em segundo plano (modo destacado).

2. **Parar Serviços**:
   ```sh
   docker-compose stop
   ```
   - Para os contêineres sem removê-los.

3. **Parar e Remover Serviços e Recursos**:
   ```sh
   docker-compose down
   ```
   - Para e remove contêineres, redes e volumes definidos no `docker-compose.yml`.

### Opções do Comando `docker-compose up`

1. **Forçar a Recriação dos Contêineres**:
   ```sh
   docker-compose up --force-recreate
   ```
   - Recria os contêineres mesmo se não houver mudanças no `docker-compose.yml`.

2. **Recriar Apenas Contêineres com Mudanças**:
   ```sh
   docker-compose up --build
   ```
   - Recompila as imagens e recria os contêineres se houver mudanças nos arquivos de configuração.

3. **Remover Contêineres Órfãos**:
   ```sh
   docker-compose up --remove-orphans
   ```
   - Remove contêineres que não estão mais definidos no `docker-compose.yml`.

### Outros Comandos Úteis do Docker Compose

1. **Listar Serviços em Execução**:
   ```sh
   docker-compose ps
   ```
   - Lista todos os contêineres em execução gerenciados pelo `docker-compose`.

2. **Verificar Logs dos Serviços**:
   ```sh
   docker-compose logs
   ```
   - Mostra os logs dos contêineres.
   - Para seguir os logs em tempo real:
     ```sh
     docker-compose logs -f
     ```

3. **Executar Comandos em Contêineres em Execução**:
   ```sh
   docker-compose exec <service_name> <command>
   ```
   - Executa um comando em um contêiner em execução. Por exemplo, para abrir um shell no contêiner do PostgreSQL:
     ```sh
     docker-compose exec postgres bash
     ```

4. **Verificar o Estado dos Contêineres e Dependências**:
   ```sh
   docker-compose top
   ```
   - Exibe a árvore de processos dos contêineres.

5. **Reiniciar Serviços**:
   ```sh
   docker-compose restart
   ```
   - Reinicia todos os serviços ou um serviço específico:
     ```sh
     docker-compose restart <service_name>
     ```

6. **Remover Contêineres Parados e Volumes Não Utilizados**:
   ```sh
   docker-compose down --volumes
   ```
   - Remove todos os volumes definidos e associados aos serviços.

### Comandos de Manutenção

1. **Atualizar Imagens e Recriar Contêineres**:
   ```sh
   docker-compose pull
   ```
   - Puxa as versões mais recentes das imagens definidas no `docker-compose.yml`.

2. **Verificar Configuração**:
   ```sh
   docker-compose config
   ```
   - Verifica e valida o arquivo de configuração `docker-compose.yml`.

3. **Remover Contêineres Parados e Imagens Não Utilizadas**:
   ```sh
   docker-compose down --rmi all
   ```
   - Remove contêineres, redes, volumes e também todas as imagens usadas pelos serviços.

### Exemplo Completo de Uso

Para ilustrar um fluxo de trabalho completo, considere os seguintes passos:

1. **Inicializar Serviços em Segundo Plano**:
   ```sh
   docker-compose up -d
   ```

2. **Verificar Serviços em Execução**:
   ```sh
   docker-compose ps
   ```

3. **Seguir Logs em Tempo Real**:
   ```sh
   docker-compose logs -f
   ```

4. **Executar um Comando no Serviço PostgreSQL**:
   ```sh
   docker-compose exec postgres psql -U postgres
   ```

5. **Reiniciar um Serviço Específico**:
   ```sh
   docker-compose restart pgadmin
   ```

6. **Parar e Remover Todos os Serviços e Recursos**:
   ```sh
   docker-compose down --volumes --remove-orphans
   ```
