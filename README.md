<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** tomasjm, dronekit-ufro, TomJimenez05, t.jimenez03@ufromail.cl
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/tomasjm/dronekit-ufro">
    <img src="logo.png" alt="Logo" width="200" height="200">
  </a>

  <h3 align="center">Drone UFRO</h3>

  <p align="center">
    Código y documentación del desarrollo del Drone.
    <br />
    <a href="https://github.com/tomasjm/dronekit-ufro"><strong>Documentación</strong></a>
    <br />
    <br />
    <a href="https://github.com/tomasjm/dronekit-ufro/issues">Reportar Bug</a>
    ·
    <a href="https://github.com/tomasjm/dronekit-ufro/issues">Solicitar Mejora</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Contenidos

- [Contenidos](#contenidos)
- [Sobre el proyecto](#sobre-el-proyecto)
  - [Construido con](#construido-con)
- [Como comenzar](#como-comenzar)
  - [Requisitos](#requisitos)
  - [Instalación y configuración de hardware](#instalaci%c3%b3n-y-configuraci%c3%b3n-de-hardware)
  - [Instalación y configuración del repositorio](#instalaci%c3%b3n-y-configuraci%c3%b3n-del-repositorio)
- [Modo de uso](#modo-de-uso)
- [Roadmap](#roadmap)
- [Licencia](#licencia)
- [Contacto](#contacto)
- [Agradecimientos](#agradecimientos)



<!-- ABOUT THE PROJECT -->
## Sobre el proyecto

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Proyecto que se basa en la construcción de un Drone **programable y automatico**, y a la vez, que sea **accesible/economico**.

### Construido con

* [Raspberry Pi 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/)
* [Emlid Navio2](https://emlid.com/navio/)
* [Dronekit](https://dronekit.io/)



<!-- GETTING STARTED -->
## Como comenzar

En este repositorio se encuentra el código y los scripts para realizar la automatización y configuración del drone, sin embargo, son necesarios algunos requisitos.

### Requisitos

* Raspberry Pi 3
* Emlid Navio2
* Python 3.7
* Conocimientos de Linux

El drone está construido con la placa Emlid Navio2 que es un shield de raspberry pi 3 para drones, contiene todo lo necesario para hacer funcionar un drone.

### Instalación y configuración de hardware
 
 Es necesario hacer uso de la [documentación](https://docs.emlid.com/navio2/) entregada por Emlid que explica como configurar e instalar todo el hardware.
 Para continuar, es necesario realizar hasta la configuración del servicio de Ardupilot en la sección Ardupilot de la documentación de Emlid.

 **Es necesario, que durante la instalación de los servicios de Ardupilot, se actualice lo siguiente:** 
 1. La distribución Raspbian de Emlid.
```sh
sudo apt-get update && sudo apt-get dist-upgrade
```
 2. Los paquetes de python, especificamente pymavlink, mavlink y mavproxy.
```sh
pip install pymavlink mavlink mavproxy
```
### Instalación y configuración del repositorio

El objetivo es configurar e instalar el sistema de automatización del Drone que respecta a configurar [MavProxy](http://ardupilot.github.io/MAVProxy/html/index.html) que servirá como intermediario entre la comunicación de los centros de control ([QGroundControl](http://qgroundcontrol.com/)) del drone en conjunto del código de automatización y el servicio de Ardupilot.
 
1. Clonar dronekit-ufro
```sh
git clone https:://github.com/tomasjm/dronekit-ufro.git
```
2. Editar los scripts
```sh
vim iniciarMavproxy.sh
```

<!-- USAGE EXAMPLES -->
## Modo de uso

1. Se inicia el servicio ardupilot
```sh
sudo systemctl start ardupilot
```
2. Se inicia mavproxy
```sh
./iniciarMavproxy.sh
```
3. Se conecta QGroundControl
```sh
sudo chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
```
1. Se ejecuta el script de dronekit
```sh
python script.py --connect "tcp/udp:LA_DIRECCION_IP:PUERTO"
```



<!-- ROADMAP -->
## Roadmap

Revisar [open issues](https://github.com/tomasjm/dronekit-ufro/issues) para obtener una lista de futuras caracteristicas y los bugs conocidos.



<!-- LICENSE -->
## Licencia

Distribuido bajo la licencia MIT.



<!-- CONTACT -->
## Contacto

Tomás Jiménez - [@tomasjm](https://www.github.com/tomasjm) - t.jimenez03@ufromail.cl

Arturo Avendaño - [@ArturoAvendano](https://www.github.com/ArturoAvendano) - a.avendano04@ufromail.cl

Link del proyecto: [https://github.com/tomasjm/dronekit-ufro](https://github.com/tomasjm/dronekit-ufro)



<!-- ACKNOWLEDGEMENTS -->
## Agradecimientos

* [Universidad de la Frontera](https://www.ufro.cl/)
* [Departamento de Ingenieria Electrica](http://www.inele.ufro.cl/)
* [Ingenieria Civil Electronica](http://icelectronica.ufro.cl/)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/tomasjm/dronekit-ufro.svg?style=flat-square
[contributors-url]: https://github.com/tomasjm/dronekit-ufro/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/tomasjm/dronekit-ufro.svg?style=flat-square
[forks-url]: https://github.com/tomasjm/dronekit-ufro/network/members
[stars-shield]: https://img.shields.io/github/stars/tomasjm/dronekit-ufro.svg?style=flat-square
[stars-url]: https://github.com/tomasjm/dronekit-ufro/stargazers
[issues-shield]: https://img.shields.io/github/issues/tomasjm/dronekit-ufro.svg?style=flat-square
[issues-url]: https://github.com/tomasjm/dronekit-ufro/issues
[license-shield]: https://img.shields.io/github/license/tomasjm/dronekit-ufro?style=flat-square
[license-url]: https://github.com/tomasjm/dronekit-ufro
[product-screenshot]: images/screenshot.png
