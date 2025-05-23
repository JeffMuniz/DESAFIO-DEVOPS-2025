# Desafio DevOps 2025 – Aplicações com Cache, Observabilidade e Infraestrutura Automatizada

## Objetivo

Duas aplicações simples (em Python e Node.js) com rotas HTTP distintas e cache configurado com diferentes tempos de expiração. A infraestrutura é automatizada com Docker Compose e observabilidade via Prometheus e Grafana.

## Acesse a interface web do projeto

Após subir o projeto com `docker-compose up -d`, acesse:

http://localhost:5000/

Essa é a **interface visual principal** do projeto, feita em HTML+CSS (estilo Matrix ), que resume:

- Rotas disponíveis em Flask e Node.js
- Links diretos para Grafana, Prometheus e Redis Commander
- Comando de deploy
- Credenciais de acesso

---

## Gere métricas para visualização no Grafana

Após abrir a home, acesse manualmente as rotas:

- `http://localhost:5000/hello` → gera `flask_hits_total`
- `http://localhost:3002/hello` → gera `node_hits_total`
- `http://localhost:5000/time` e `:3002/time` → cache + hit

Acesse o Grafana:

http://localhost:3000

E no primeiro acesso coloque uma senha nova

Login padrão:

- Usuário: `admin`
- Senha: `admin`

## Aplicações

### App 1 – Python + Flask

- `/hello`: Retorna texto fixo "Hello from Python!"
- `/time`: Retorna a hora atual do servidor
- Cache TTL: 10 segundos

### App 2 – Node.js + Express

- `/hello`: Retorna texto fixo "Hello from Node.js!"
- `/time`: Retorna a hora atual do servidor
- Cache TTL: 60 segundos

## Cache

Implementado com Redis.  
Cada app utiliza um cliente próprio para TTL independente (10s e 60s).

## Observabilidade

- Prometheus coleta métricas das aplicações e do Redis
- Grafana exibe paineis com estatísticas das rotas acessadas e cache hits
- Apps expõem métricas em `/metrics`

## Como rodar

```bash
git clone https://github.com/JeffMuniz/devops-desafio-2025.git && cd devops-desafio-2025
docker-compose up -d

Restart

docker-compose up -d --build


```

## Redis

Acesse no navegador:

 <http://localhost:8081>

Você verá a interface web do Redis, onde pode:

Ver as chaves (flask_time, node_time)

Observar TTL

Editar e apagar valores

Visualizar expirados ou atuais

## Validação das rotas – Desafio DevOps 2025

Cada aplicação (Flask e Node.js) foi implementada com  duas rotas obrigatórias , mais rotas extras úteis para debug e observabilidade.

---

## App 1 – Flask (`localhost:5000`)

| Rota                   | Método | Função                                         | Exemplo de Resposta                         |
|------------------------|--------|-----------------------------------------------|---------------------------------------------|
| [`/hello`](http://localhost:5000/hello)   | GET    | Texto fixo                                     | `Hello from Python!`                         |
| [`/time`](http://localhost:5000/time)     | GET    | Hora atual com cache de  10s  via Redis      | `Hora Pyhton` ou `(cache) ...` |
| [`/metrics`](http://localhost:5000/metrics) | GET  | (Extra) Métricas Prometheus                     | Exposição de `flask_hits_total`             |

---

## App 2 – Node.js (`localhost:3002`)

| Rota                   | Método | Função                                         | Exemplo de Resposta                         |
|------------------------|--------|-----------------------------------------------|---------------------------------------------|
| [`/hello`](http://localhost:3002/hello)   | GET    | Texto fixo                                     | `Hello from Node.js!`                       |
| [`/time`](http://localhost:3002/time)     | GET    | Hora atual com cache de  60s  via Redis      | `Hora node` ou `(cache) ...` |
| [`/metrics`](http://localhost:3002/metrics) | GET  | (Extra) Métricas Prometheus                     | Exposição de `node_hits_total`              |

---

### Validação manual sugerida

- Acesse cada link acima e valide o conteúdo da resposta
- Aguarde o tempo de expiração do cache (`10s` no Flask, `60s` no Node)
- Refaça a requisição e compare o valor retornado

## Senha do Grafana

Por padrão, o container oficial do Grafana usa:

Usuário: admin

Senha: admin

Se quiser mudar, pode configurar com variáveis de ambiente:

environment:

- GF_SECURITY_ADMIN_USER=admin
- GF_SECURITY_ADMIN_PASSWORD=admin

## Diagrama da Arquitetura

A arquitetura é composta por dois serviços de aplicação (Flask e Node.js), um serviço de cache (Redis), ferramentas de observabilidade (Prometheus e Grafana), e Redis Commander para inspeção visual do cache.

PNG
![Diagrama da Arquitetura](docs/arquitetura.png)

## !! Em Construção

## Acesse tudo pronto no Render

- Como um extra eu adicionei ao render, pode levar 1 ou 2 minutos pra subir o serviço!

<https://desafio-devops-2025-jhsa.onrender.com/>
