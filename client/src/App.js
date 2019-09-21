import React, { useEffect, useState } from "react";
import logo from "./logo.png";
import "./App.css";
import ReactFlvPlayer from "./flvplayer";
const os = window.require("os");

function App() {
  useEffect(() => {
    let addresses = [];
    let interfaces = os.networkInterfaces();
    for (let k in interfaces) {
      for (let k2 in interfaces[k]) {
        let address = interfaces[k][k2];
        if (address.family === "IPv4" && !address.internal) {
          addresses.push(address.address);
        }
      }
    }
    setipaddress({ client_ip: addresses[0] });

  }, []);
  const [ipaddress, setipaddress] = useState({ client_ip: null });
  const [inputAddress, setinputAddress] = useState({ input_ip: null });
  const [player, setPlayer] = useState(0);
  const [loading, setLoading] = useState(0);
  const [error, setError] = useState({
    error: false,
    mensaje: ""
  });
  const handleChange = e => {
    setinputAddress({
      input_ip: e.target.value
    });
  };

  const handleClick = () => {
    setError({
      error: false,
      mensaje: ""
    });
    setLoading(1);
    fetch(`http://${inputAddress.input_ip}:3000/`)
      .then(response => response.json())
      .then(res => {
        console.log(res);
        setLoading(0);
        if (res.response) {
          setError({
            error: false,
            mensaje: ""
          });
          setPlayer(1);
        } else {
          setError({
            error: true,
            mensaje: "Respuesta FALSE por parte del servidor"
          });
        }
      })
      .catch(err => {
        setLoading(0);
        setError({
          error: true,
          mensaje: err.toString()
        });
      });
  };
  return (
    <div className="App">
      {player ? (
        <ReactFlvPlayer
        url={`http://${inputAddress.input_ip}:8000/live/video.flv` }
          />
      ) : (
        <div>
          <header className="App-header">
            <img style={{ marginTop: "100px" }} src={logo} className="App-logo" alt="logo" />
            <p>Dirección IPV4 cliente: {ipaddress.client_ip}</p>
            <label>Dirección IPV4 servidor (drone)</label>
            <input
              onChange={handleChange}
              style={{
                marginTop: "15px",
                height: "15px",
                width: "250px",
                paddingTop: "10px",
                paddingBottom: "10px",
                textAlign: "center"
              }}
              name="ip_manual"
              placeholder="192.168.1.x"
            />
            <button
              onClick={handleClick}
              style={{
                height: "50px",
                width: "254px",
                marginTop: "15px",
                backgroundColor: "#01a3a4",
                border: "none",
                color: "white"
              }}
            >
              Conectarse al drone
            </button>
            {loading ? <p>conectando...</p> : null}
            {error.error ? <p>Error: {error.mensaje}</p> : null}
          </header>
        </div>
      )}
    </div>
  );
}

export default App;
