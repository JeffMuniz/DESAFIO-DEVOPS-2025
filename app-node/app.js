const express = require('express');
const redis = require('redis');
const promClient = require('prom-client');

const app = express();
const client = redis.createClient({ url: 'redis://redis:6379' });
client.connect();

const counter = new promClient.Counter({
  name: 'node_hits_total',
  help: 'Total hits to Node app',
});

app.get('/hello', (req, res) => {
  counter.inc();
  res.send("Hello from Node.js!");
});

app.get('/time', async (req, res) => {
  counter.inc();
  const cached = await client.get("node_time");
  if (cached) return res.send(`(cache) ${cached}`);
  const now = new Date().toString();
  await client.setEx("node_time", 60, now);
  res.send(now);
});

app.get('/metrics', async (req, res) => {
  res.set('Content-Type', promClient.register.contentType);
  res.end(await promClient.register.metrics());
});

app.listen(3000, () => console.log("Node app listening on 3000"));