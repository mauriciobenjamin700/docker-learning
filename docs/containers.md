# Acessando Containers diretamente e os Manipulando

Para que seu container fique em execução e possa vir a ser acessado, deve sempre deixar um processo rodando em primeiro plano, assim o container não será fechado

Exemplo

```Dockerfile
FROM ubuntu:24.04

RUN apt-get update && apt-get install -y \
    curl gnupg2 ca-certificates lsb-release ubuntu-keyring

RUN curl https://nginx.org/keys/nginx_signing.key | gpg --dearmor | tee /usr/share/keyrings/nginx-archive-keyring.gpg >/dev/null

RUN gpg --dry-run --quiet --no-keyring --import --import-options import-show /usr/share/keyrings/nginx-archive-keyring.gpg

RUN echo "deb [signed-by=/usr/share/keyrings/nginx-archive-keyring.gpg] \
http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list

RUN while lsof /var/lib/dpkg/lock-frontend; do sleep 1; done; \
    apt-get update && apt-get install -y --no-install-recommends nginx

CMD ["nginx", "-g", "daemon off;"]

#CMD [ "tail", "-f", "/dev/null" ]
```

## Detalalhando a instrução CMD

Para o exemplo acima, foi deixado em primeiro plano, o servidor web nginx

- `CMD` Esta instrução no Dockerfile especifica o comando que será executado quando um container for iniciado a partir da imagem. Diferente de RUN, que é executado durante a construção da imagem, CMD é executado quando o container está em execução.

- `nginx`: Este é o comando que inicia o servidor NGINX.

- `-g`: Esta flag permite que você passe diretivas de configuração diretamente na linha de comando. As diretivas passadas com -g têm precedência sobre as diretivas no arquivo de configuração do NGINX.

- "`daemon off;`": Esta é a diretiva de configuração passada com a flag -g. A diretiva daemon off; instrui o NGINX a rodar no primeiro plano (foreground) em vez de se tornar um processo daemon (background). Isso é importante em um ambiente Docker porque o processo principal do container deve continuar em execução para que o container permaneça ativo. Se o NGINX rodasse em segundo plano, o processo principal do container terminaria e o container seria encerrado.


### Caso o nginx não seja de seu interesse, pode usar a seguinte têcnica também

O comando `CMD ["tail", "-f", "/dev/null"]` é usado para manter o container em execução sem fazer nada de útil. Onde:

- `CMD`: Esta instrução no Dockerfile especifica o comando que será executado quando um container for iniciado a partir da imagem.

- `tail`: Este é o comando Unix que exibe as últimas linhas de um arquivo.

- `-f`: Esta flag faz com que o tail continue a monitorar o arquivo para novas linhas, mantendo o comando em execução indefinidamente.

- `"/dev/null"`: Este é um arquivo especial que descarta qualquer entrada e não produz saída. É frequentemente usado para redirecionar a saída de comandos que não precisam ser vistos.

- Em resumo, CMD ["tail", "-f", "/dev/null"] mantém o container em execução sem fazer nada, porque o comando tail -f /dev/null nunca termina. Isso pode ser útil para manter o container ativo para depuração ou para outros propósitos onde você precisa que o container continue rodando, mas não tem um processo específico para executar.


## Como acessar?

Existem algumas formas, mas iremos para a mais simples!

```bash
docker exec -it SEU-CONTAINER /bin/bash
```
onde troque `SEU-CONTAINER` pelo ID ou nome do container que deseja acessar o terminal

desta forma, você conseguirá acessar e manipular o container como se fosse uma segunda maquina, mas lembre-se que todas as mudanças serão perdidas ao encerrar o container

