# Minha Jornada Aprendendo a Usar Docker

Saudações, Pessoal!

Este repositório se destina ao meu aprendizado sobre docker, desde a instalação até anotações sobre comandos, dúvidas, bugs e exemplos práticos.

Para a instalação, eu aprendi seguindo os passos [deste guia](https://github.com/codeedu/wsl2-docker-quickstart). Mas logo abaixo eu trago o passo rápido para quem vai executar via WSL igual a mim.

## Instalar o Docker com Docker Engine (Docker Nativo) pelo WSL (Ubuntu)

Para esta instalação, basta copiar cada bloco a baixo e executar no terminal do Ubuntu.

Atualização do sistema e download do Docker

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

Adicionando o repositório do Docker na lista de sources do Ubuntu:

```bash
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Dando permissão para rodar o Docker com seu usuário corrente:

```bash
sudo usermod -aG docker $USER
```

Instalando Docker-Compose

```bash
sudo apt  install docker-compose
```
Reinicie o WSL
Pronto, seu Docker está instalado.

Caso aconteça algum erro, execute:

```bash
 sudo apt-get update
 sudo apt-get install docker-compose-plugin
```

## Primeiros Passos

Se você assim como eu está dando seus primeiros passos com o Docker, [clique aqui](docs/help.md) para acessar um guia de comandos docker que montei enquanto estudava e ainda atualizo durante minha jornada.
