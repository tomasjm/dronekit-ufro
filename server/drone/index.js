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
const express = require("express");
const cors = require("cors");
const sys = require("sys");
const exec = require("child_process").exec;

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

app.get("/start_streaming_drone", (req, res) => {
  // se inicia el Listen de ffmpeg del video de raspivid y se redirecciona a rtmp de node media server que esta en la central
  exec(
    "nc -l 2222 | ffmpeg -i - -c copy -f flv rtmp://192.168.8.130:1935/live/video",
    () => {}
  );
  // raspivid -t 0 -w 500 -h 500 -fps 20 -o - | nc 0.0.0.0 2222
  exec("raspivid -t 0 -w 500 -h 500 -fps 20 -o - | nc 0.0.0.0 2222", () => {});
  res.send({
    response: true
  });
});

app.get("/fly", (req, res) => {
  // se inicia el Listen de ffmpeg del video de raspivid y se redirecciona a rtmp de node media server que esta en la central
  exec(
    "python ~/dronecode/main.py --connect udp:192.168.8.120:14555",
    () => {}
  );
  res.send({
    response: true
  });
  
});


app.listen(3000, () => {
  console.log("Servidor andando en puerto 3000");
});
