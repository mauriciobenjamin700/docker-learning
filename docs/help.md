# Tutorial Docker: Do Básico a Alguma Lugar

Este tutorial te guiará pelo mundo do Docker, desde seus fundamentos até as técnicas mais avançadas. Prepare-se para aprender sobre essa poderosa ferramenta e transformar a forma como você desenvolve, implanta e gerencia seus aplicativos!

## 1. Introdução ao Docker

### O que é Docker?

O Docker é uma plataforma de containerização de aplicativos que permite empacotar seu software e suas dependências em unidades chamadas contêineres. Imagine contêineres como caixas que armazenam tudo que seu aplicativo precisa para funcionar, como código, bibliotecas, configurações e arquivos.

### Benefícios do Docker:

* **Isolamento:** Os contêineres são isolados uns dos outros, garantindo que seus aplicativos não interfiram entre si, aumentando a segurança e estabilidade.
* **Portabilidade:** Os contêineres podem ser executados em qualquer ambiente com Docker instalado, independentemente do sistema operacional, facilitando a implantação em diferentes ambientes.
* **Agilidade:** A criação e a implantação de contêineres são rápidas e fáceis, acelerando o desenvolvimento e o lançamento de aplicativos.
* **Eficiência:** Os contêineres são leves e compartilham recursos do sistema host, otimizando o uso de hardware e reduzindo custos.
* **Repetibilidade:** A natureza imutável dos contêineres garante que seu aplicativo seja executado da mesma maneira em diferentes ambientes, proporcionando confiabilidade.

### Casos de uso do Docker:

* **Desenvolvimento e testes:** Crie ambientes de desenvolvimento isolados para cada desenvolvedor ou teste diferentes versões de um aplicativo sem afetar a produção.
* **Implantação em produção:** Implante e gerencie seus aplicativos em servidores de produção de forma rápida, eficiente e escalável.
* **Microsserviços:** Arquitete seus aplicativos como microsserviços modulares e independentes, facilitando o gerenciamento e a escalabilidade.
* **Nuvem:** Execute seus aplicativos em plataformas de nuvem como AWS, Azure e Google Cloud Platform com facilidade e flexibilidade.

## 2. Instalação e Primeiros Passos

Se você ainda não instalou seguindo os passos que deixei no README pelo WSL, tente instalar seguindo a documentação.

1. Acesse o site oficial do Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Escolha o sistema operacional do seu computador e siga as instruções de instalação.
3. Verifique se o Docker está instalado executando o comando `docker version` no terminal.

### Criando seu primeiro contêiner:

1. Baixe uma imagem de contêiner do Docker Hub: `docker pull hello-world`
2. Execute o contêiner: `docker run hello-world`
3. Observe a saída do contêiner: `docker logs hello-world`

## 3. Conceitos Básicos do Docker

### Imagens:

* Imagens são modelos pré-construídos que contêm todo o código e as dependências necessárias para executar um aplicativo.
* As imagens são armazenadas localmente no seu computador ou podem ser baixadas do Docker Hub, um repositório público de imagens.

### Contêineres:

* Contêineres são instâncias executáveis ​​de imagens.
* Cada contêiner possui seu próprio espaço de arquivos, processo e rede isolados, garantindo a independência dos aplicativos.

### Comandos Docker:

* O Docker fornece uma variedade de comandos para gerenciar imagens e contêineres, como `docker pull`, `docker run`, `docker ps`, `docker stop`, `docker rm` e muitos outros.

## 4. Comandos Essenciais do Docker

| Comando | Descrição |
|---|---|
| `docker pull <imagem>` | Baixa uma imagem do Docker Hub. |
| `docker run <imagem>` | Executa um contêiner a partir de uma imagem. |
| `docker ps` | Lista os contêineres em execução. |
| `docker stop <container-id>` | Para um contêiner em execução. |
| `docker rm <container-id>` | Remove um contêiner. |
| `docker images` | Lista as imagens armazenadas localmente. |
| `docker rmi <imagem-id>` | Remove uma imagem local. |
| `docker exec -it <container-id> <comando>` | Executa um comando dentro de um contêiner. |
| `docker logs <container-id>` | Visualiza os logs de um contêiner. |
| `docker build -t <imagem-nome> .` | Constrói uma imagem a partir do diretório atual. |
| `docker push <imagem-nome>` | Envia uma imagem para o Docker Hub. |

Vale lembrar que cada comando tem suas variações de acordo com argumentos adicionais (flags) que você pode passar. Um exemplo é o `docker ps -a` que lista tanto os conteiners em execução quanto os parados.

Recomendo que consulte a documentação para saber mais dessas flegs

### Comandos e Suas Flags Essenciais para quem está Aprendendo

#### Removendo todos os Conteiners 

Para remover todos os conteiners, existem diversas formas e passos, como:

1. Listar Todos os Contêineres:
    - Primeiro, você pode listar todos os contêineres (tanto em execução quanto parados) usando o comando ``docker ps -a ``

2. Parar Todos os Contêineres em Execução:
    - Antes de remover, você precisa parar todos os contêineres que estão em execução. Você pode fazer isso com o comando: ``docker stop $(docker ps -q)``

3. Remover Todos os Contêineres:
    - Depois de parar os contêineres, você pode removê-los com o comando ``docker rm $(docker ps -a -q)``

##### Explicação dos Comandos

- ``docker ps -a``: Lista todos os contêineres, incluindo os que estão parados.
- docker ps -q: Retorna apenas os IDs dos contêineres em execução.
- docker stop $(docker ps -q): Para todos os contêineres em execução. 
- $(docker ps -q) é uma substituição de comando que retorna a lista de IDs de contêineres.
- docker rm $(docker ps -a -q): Remove todos os contêineres. 
- $(docker ps -a -q) é uma substituição de comando que retorna a lista de IDs de todos os contêineres (em execução e parados).

Existe também o "Comando Único" para parar e remover todos os contêineres, onde
você pode combinar os comandos acima em um único comando para parar e remover todos os contêineres: ``docker stop $(docker ps -q) && docker rm $(docker ps -a -q)``

#### Removendo Contêineres com Docker Compose

Se você está utilizando Docker Compose, pode remover todos os contêineres definidos no seu arquivo docker-compose.yml com o seguinte comando ``docker-compose down``.

Este comando irá parar e remover todos os contêineres, redes e volumes (opcionalmente) criados pelo Docker Compose.

#### Removendo Volumes e Redes (Opcional)

Se você também deseja remover volumes e redes associados aos contêineres, use o comando ``docker-compose down`` com as opções ``-v`` para volumes e ``--remove-orphans`` para redes órfãs: 
```docker
docker-compose down -v --remove-orphans

```

E se desejar remover volumes de contêineres não utilizados, pode usar: ``docker volume prune``

E para redes não utilizadas: ``docker network prune``
`
Esses passos e comandos irão garantir que todos os seus contêineres sejam completamente removidos, junto com quaisquer volumes e redes associados, se necessário.

## 5. Gerenciamento de Volume

Quando você executa um contêiner a partir de uma imagem, todos os dados gerados pelo contêiner são armazenados em uma camada de escrita temporária. Essa camada é removida quando o contêiner é interrompido. Isso pode ser problemático para aplicativos que precisam persistir dados, como bancos de dados ou sistemas de arquivos.

O Docker volumes oferecem uma solução para dados persistentes. Um volume é um diretório no sistema host que é mapeado para um diretório dentro do contêiner. Isso permite que o contêiner armazene e acesse seus dados de forma persistente, independentemente do ciclo de vida do contêiner.

Para usar volumes, você pode especificar a opção -v durante a execução do contêiner:

```bash
docker run -v <host-diretorio>:<container-diretorio> <imagem>
```

Por exemplo, para persistir os dados de um banco de dados MySQL em contêiner, você pode executar/:

```docker
docker run -v mysql-data:/var/lib/mysql mysql:latest
```
Neste comando, o diretório mysql-data no sistema host é mapeado para o diretório /var/lib/mysql dentro do contêiner MySQL. Dessa forma, os dados do banco de dados serão persistidos no diretório do host e acessíveis mesmo após a reinicialização do contêiner.

## 6. Docker Compose

Docker Compose é uma ferramenta que simplifica a definição e execução de aplicações multi-containers. Com Docker Compose, você usa um arquivo YAML para definir os serviços, redes e volumes necessários para sua aplicação. Em seguida, um único comando pode criar e iniciar todos os serviços definidos no arquivo.

### Como funciona o Docker Compose?

1. Definição dos Serviços:
    - Você cria um arquivo chamado docker-compose.yml onde define todos os serviços que compõem sua aplicação. Cada serviço é um container que será gerenciado pelo Docker Compose.

2. Configuração dos Serviços:
    - No arquivo docker-compose.yml, você especifica a imagem Docker a ser usada para cada serviço, as portas a serem expostas, as variáveis de ambiente, volumes e redes.

3. Comandos do Docker Compose:

    - ``docker-compose up``: Cria e inicia todos os containers definidos no arquivo docker-compose.yml.
    - ``docker-compose down:`` Para e remove todos os containers, redes e volumes - criados pelo comando up.
    - ``docker-compose ps``: Lista os containers em execução.
    -`` docker-compose logs``: Exibe os logs de todos os serviços.

O comando `docker-compose up -d` é usado para iniciar todos os serviços definidos no arquivo `docker-compose.yml` em modo destacado (detached), o que significa que os contêineres serão executados em segundo plano. No entanto, existem vários comandos e opções adicionais que você pode usar com `docker-compose` para gerenciar seus serviços. Aqui estão alguns dos mais úteis:

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


### Exemplo de um Arquivo ``docker-compose.yml```

Um exemplo básico de um arquivo docker-compose.yml que define uma aplicação web com um serviço de banco de dados:

```yaml
version: '3.8'
services:
  web:
    image: nginx:latest
    ports:
      - "80:80"
    volumes:
      - ./html:/usr/share/nginx/html
  database:
    image: postgres:latest
    environment:
      POSTGRES_USER: example
      POSTGRES_PASSWORD: example
      POSTGRES_DB: exampledb
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:

```

### Passos para Usar o Docker Compose:

1. Criar o Arquivo docker-compose.yml: 
    - No diretório do seu projeto, crie um arquivo chamado docker-compose.yml e adicione a configuração dos serviços.

2. Iniciar os Serviços: 
    - Navegue até o diretório do projeto no terminal e execute docker-compose up. Isso criará e iniciará todos os containers definidos no arquivo.

3. Gerenciar os Containers: 
    - Use comandos como ``docker-compose ps``, ``docker-compose logs`` e ``docker-compose down`` para gerenciar seus containers.

### Benefícios do Docker Compose

- Automação: Facilita a automação da criação, configuração e execução de ambientes multi-containers.
- Reprodutibilidade: Garante que o ambiente de desenvolvimento seja consistente com o de produção.
- Isolamento: Cada serviço é executado em um container separado, permitindo isolamento de dependências e evitando conflitos.
- Facilidade de Uso: Um único arquivo YAML simplifica a gestão de configurações complexas.
