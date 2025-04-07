# Desafio DevOps 2025 – Aplicações com Cache, Observabilidade e Infraestrutura Automatizada

## Objetivo

Este projeto apresenta duas aplicações simples (em Python e Node.js) com rotas HTTP distintas e cache configurado com diferentes tempos de expiração. A infraestrutura é automatizada com Docker Compose e observabilidade via Prometheus e Grafana.

## Aplicações

### App 1 – Python + Flask

- `/hello`: Retorna texto fixo "Hello from Flask!"
- `/time`: Retorna a hora atual do servidor
- Cache TTL: 10 segundos

### App 2 – Node.js + Express

- `/hello`: Retorna texto fixo "Hello from Node.js!"
- `/time`: Retorna a hora atual do servidor
- Cache TTL: 60 segundos

## 🔁Cache

Implementado com Redis.  
Cada app utiliza um cliente próprio para TTL independente (10s e 60s).

## Observabilidade

- Prometheus coleta métricas das aplicações e do Redis
- Grafana exibe painéis com estatísticas das rotas acessadas e cache hits
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

Cada aplicação (Flask e Node.js) foi implementada com **duas rotas obrigatórias**, mais rotas extras úteis para debug e observabilidade.

---

## App 1 – Flask (`localhost:5000`)

| Rota                   | Método | Função                                         | Exemplo de Resposta                         |
|------------------------|--------|-----------------------------------------------|---------------------------------------------|
| [`/hello`](http://localhost:5000/hello)   | GET    | Texto fixo                                     | `Hello from Flask!`                         |
| [`/time`](http://localhost:5000/time)     | GET    | Hora atual com cache de **10s** via Redis      | `Tue Apr  7 19:00:00 2025` ou `(cache) ...` |
| [`/`](http://localhost:5000/)            | GET    | (Extra) Hello + hora atual formatada            | `Olá!! A hora em Python é Tue Apr ...`      |
| [`/metrics`](http://localhost:5000/metrics) | GET  | (Extra) Métricas Prometheus                     | Exposição de `flask_hits_total`             |

---

## App 2 – Node.js (`localhost:3000`)

| Rota                   | Método | Função                                         | Exemplo de Resposta                         |
|------------------------|--------|-----------------------------------------------|---------------------------------------------|
| [`/hello`](http://localhost:3000/hello)   | GET    | Texto fixo                                     | `Hello from Node.js!`                       |
| [`/time`](http://localhost:3000/time)     | GET    | Hora atual com cache de **60s** via Redis      | `Tue Apr  7 19:00:00 2025` ou `(cache) ...` |
| [`/`](http://localhost:3000/)            | GET    | (Extra) Hello + hora atual formatada            | `👋 Hello! Time now is: 07/04/2025 19:00`    |
| [`/metrics`](http://localhost:3000/metrics) | GET  | (Extra) Métricas Prometheus                     | Exposição de `node_hits_total`              |

---

### Validação manual sugerida

- Acesse cada link acima e valide o conteúdo da resposta
- Aguarde o tempo de expiração do cache (`10s` no Flask, `60s` no Node)
- Refaça a requisição e compare o valor retornado

---

Se quiser, posso gerar esse conteúdo como `docs/rotas.md` para adicionar ao projeto. Deseja?

## Senha do Grafana

Por padrão, o container oficial do Grafana usa:

Usuário: admin

Senha: admin

Se quiser mudar, pode configurar com variáveis de ambiente:

environment:

- GF_SECURITY_ADMIN_USER=jeff
- GF_SECURITY_ADMIN_PASSWORD=senhaforte
