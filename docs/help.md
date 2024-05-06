# Tutorial Docker: Do Básico ao Avançado

Este tutorial abrangente te guiará pelo mundo do Docker, desde seus fundamentos até as técnicas mais avançadas. Prepare-se para dominar essa poderosa ferramenta e transformar a forma como você desenvolve, implanta e gerencia seus aplicativos!

## 1. Introdução ao Docker

**O que é Docker?**

O Docker é uma plataforma de containerização de aplicativos que permite empacotar seu software e suas dependências em unidades chamadas contêineres. Imagine contêineres como caixas que armazenam tudo que seu aplicativo precisa para funcionar, como código, bibliotecas, configurações e arquivos.

**Benefícios do Docker:**

* **Isolamento:** Os contêineres são isolados uns dos outros, garantindo que seus aplicativos não interfiram entre si, aumentando a segurança e estabilidade.
* **Portabilidade:** Os contêineres podem ser executados em qualquer ambiente com Docker instalado, independentemente do sistema operacional, facilitando a implantação em diferentes ambientes.
* **Agilidade:** A criação e a implantação de contêineres são rápidas e fáceis, acelerando o desenvolvimento e o lançamento de aplicativos.
* **Eficiência:** Os contêineres são leves e compartilham recursos do sistema host, otimizando o uso de hardware e reduzindo custos.
* **Repetibilidade:** A natureza imutável dos contêineres garante que seu aplicativo seja executado da mesma maneira em diferentes ambientes, proporcionando confiabilidade.

**Casos de uso do Docker:**

* **Desenvolvimento e testes:** Crie ambientes de desenvolvimento isolados para cada desenvolvedor ou teste diferentes versões de um aplicativo sem afetar a produção.
* **Implantação em produção:** Implante e gerencie seus aplicativos em servidores de produção de forma rápida, eficiente e escalável.
* **Microsserviços:** Arquitete seus aplicativos como microsserviços modulares e independentes, facilitando o gerenciamento e a escalabilidade.
* **Nuvem:** Execute seus aplicativos em plataformas de nuvem como AWS, Azure e Google Cloud Platform com facilidade e flexibilidade.

## 2. Instalação e Primeiros Passos

**Instalando o Docker:**

1. Acesse o site oficial do Docker: [https://docs.docker.com/get-docker/](https://docs.docker.com/get-docker/)
2. Escolha o sistema operacional do seu computador e siga as instruções de instalação.
3. Verifique se o Docker está instalado executando o comando `docker version` no terminal.

**Criando seu primeiro contêiner:**

1. Baixe uma imagem de contêiner do Docker Hub: `docker pull hello-world`
2. Execute o contêiner: `docker run hello-world`
3. Observe a saída do contêiner: `docker logs hello-world`

## 3. Conceitos Básicos do Docker

**Imagens:**

* Imagens são modelos pré-construídos que contêm todo o código e as dependências necessárias para executar um aplicativo.
* As imagens são armazenadas localmente no seu computador ou podem ser baixadas do Docker Hub, um repositório público de imagens.

**Contêineres:**

* Contêineres são instâncias executáveis ​​de imagens.
* Cada contêiner possui seu próprio espaço de arquivos, processo e rede isolados, garantindo a independência dos aplicativos.

**Comandos Docker:**

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

## 5. Gerenciamento de Volume

Quando você executa um contêiner a partir de uma imagem, todos os dados gerados pelo contêiner são armazenados em uma camada de escrita temporária. Essa camada é removida quando o contêiner é interrompido. Isso pode ser problemático para aplicativos que precisam persistir dados, como bancos de dados ou sistemas de arquivos.

O Docker volumes oferecem uma solução para dados persistentes. Um volume é um diretório no sistema host que é mapeado para um diretório dentro do contêiner. Isso permite que o contêiner armazene e acesse seus dados de forma persistente, independentemente do ciclo de vida do contêiner.

Para usar volumes, você pode especificar a opção -v durante a execução do contêiner:

```bash
docker run -v <host-diretorio>:<container-diretorio> <imagem>
```

Por exemplo, para persistir os dados de um banco de dados MySQL em contêiner, você pode executar/:

docker run -v mysql-data:/var/lib/mysql mysql:latest
Neste comando, o diretório mysql-data no sistema host é mapeado para o diretório /var/lib/mysql dentro do contêiner MySQL. Dessa forma, os dados do banco de dados serão persistidos no diretório do host e acessíveis mesmo após a reinicialização do contêiner.
