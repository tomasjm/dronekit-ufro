/**
 * ANTES QUE NADA, INSTALAR PAQUETES CON:
 * npm install o yarn
 *
 *
 * Para inicializar el servidor, utilizar comando "node index.js"
 *
 * Para comenzar con el streaming, primero, inicializar un listening con ffmpeg y netcat (sudo apt-get install ffmpeg netcat)
 * : nc -l 2222 | fffmpeg -i - -c copy -f flv rtmp://localhost/live/video <- entrada al servidor rtmp
 *
 * Para inicializar el streaming, se comienza a grabar y enviar via netcat:
 * : raspivid -t 0 -w 500 -h 500 -fps 20 -o - | nc 0.0.0.0 2222
 */
const NodeMediaServer = require("node-media-server");
const express = require("express");
const cors = require("cors");
const sys = require("sys");
const exec = require("child_process").exec;
let listening_stream;

// Configuración de express
let app = express();
app.use(cors());
app.use(express.json());

// Ruta de confirmacion para el cliente
/**
 * Si el cliente no recibe el response: true, no continuara su ejecucion
 */
app.get("/", (req, res) => {
  res.send({ response: true });
});

app.get("/start_stream_drone", (req, res) => {
  fetch("http://192.168.8.120:3000/start_streaming_drone")
    .then(res => res.json())
    .then(res => {
      if (res.response) {
        res.send({
          response: true
        });
      } else {
        res.send({
          response: false
        });
      }
    });
});

app.get("/start_mission", (req, res) => {
  fetch("http://192.168.8.120:3000/fly").then(res = res.json()).then(res => {
    if (res.response) {
      res.send({
        response: true
      });
    } else {
      res.send({
        response: false
      })
    }
  })

});

app.get("/start_stream_central", (req, res) => {
  // se inicia el Listen de ffmpeg del video de camara central (ip servidor de la camara,
  // no de la raspberry de la central) y se redirecciona a rtmp de node media server
  exec(
    "ffmpeg -i rtmp://192.168.8.160:1935/flash/11:admin:admin -c copy -r 1 -f flv rtmp://localhost/live/videocentral",
    () => {}
  );
  res.send({
    response: true
  });
});

// Configuracion de node media server para streaming
/**
 * Ruta de salida formato "rtmp/flv": http://localhost:8000/live/video.flv
 */

// chunk 30000
const config = {
  rtmp: {
    port: 1935,
    chunk_size: 30000,
    gop_cache: false,
    ping: 30,
    ping_timeout: 60
  },
  http: {
    port: 8000,
    allow_origin: "*"
  }
};

var nms = new NodeMediaServer(config);
nms.run();

app.listen(3000, () => {
  console.log("Servidor andando en puerto 3000");
});


exec("python /home/pi/server/central/exec.py", (a, b, c) => { console.log("executed")});


