# Desafio DevOps 2025 – Aplicações com Cache, Observabilidade e Infraestrutura Automatizada

##  Objetivo
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

##  Observabilidade
- Prometheus coleta métricas das aplicações e do Redis
- Grafana exibe painéis com estatísticas das rotas acessadas e cache hits
- Apps expõem métricas em `/metrics`

## Como rodar
```bash
git clone https://github.com/JeffMuniz/devops-desafio-2025.git && cd devops-desafio-2025
docker-compose up -d
```

## Acessar:
- Flask: http://localhost:5000
- Node: http://localhost:3000
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3001 (admin / admin)


App 1 – Flask (porta 5000)
URL base: http://localhost:5000 ou https://<SEU-SERVIÇO>.onrender.com

Rota	Método	Descrição
/hello	GET	Retorna texto fixo: "Hello from Flask!"
/time	GET	Retorna hora atual (cache de 10s)
/metrics	GET	Exposição Prometheus das métricas