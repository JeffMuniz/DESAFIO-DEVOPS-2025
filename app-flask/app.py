from flask import Flask, render_template, send_from_directory
import redis, time
import prometheus_client
from prometheus_client import Counter, generate_latest

app = Flask(__name__, static_folder='static', template_folder='templates')
r = redis.Redis(host='redis', port=6379, decode_responses=True)

hits = Counter('flask_hits_total', 'Total hits to Flask app')

# 🔹 Rota da nova interface web
@app.route("/")
def serve_home():
    return send_from_directory("web", "index.html")

@app.route("/assets/<path:filename>")
def serve_assets(filename):
    return send_from_directory("web/assets", filename)

# 🔹 API padrão
@app.route("/hello")
def hello():
    hits.inc()
    return "Hello from Python!"

@app.route("/time")
def get_time():
    hits.inc()
    cached = r.get("flask_time")
    if cached:
        return f"(cache) {cached}"
    now = time.ctime()
    r.setex("flask_time", 10, now)
    return now

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
