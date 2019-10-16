#!/bin/bash
#mavproxy.py --master tcp:192.168.8.120:5760 --out udp:192.168.8.102:14550 --out udp:192.168.8.101:14552 --out udp:192.168.8.102:14551 --out udp:192.168.103:14553 --cmd=$
echo "INICIALIZACION DE MAVPROXY"
MASTER="tcp:192.168.8.120:5760"
SALIDA_TOM="udp:192.128.8.102:14550"
SALIDA_TOM_DRONEKIT="udp:192.128.8.102:14551"
SALIDA_ARTURO="udp:192.128.8.101:14552"
#mavproxy.py --master $MASTER --out $SALIDA_TOM --out $SALIDA_TOM_DRONEKIT --out $SALIDA_ARTURO --cmd="set shownoise False"
mavproxy.py  --master tcp:192.168.8.120:5760 --out udp:192.168.8.102:14550 --out udp:192.168.8.102:14551 --out udp:192.168.8.101:14552 --cmd="set shownoise False"

