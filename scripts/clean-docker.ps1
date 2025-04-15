docker-compose down -v

docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
docker rmi -f $(docker images -aq)
docker volume prune -f
docker network prune -f
docker builder prune -af
docker system df
docker buildx prune --all --force

Remove-Item -Path "grafana/grafana.db" -Force

Remove-Item -Path "grafana/data/grafana.db" -Force
docker-compose up -d --build
