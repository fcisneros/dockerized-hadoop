#!/usr/bin/env python

""" Read the ecobici dataset (csv) and generate tuples (id_station 1) """

import sys
from operator import itemgetter

# ecobici*.csv fields
#genero_usuario
#edad_usuario
#bici
#fecha_retiro
#hora_retiro_copy
#fecha_retiro_completa
#anio_retiro
#mes_retiro
#dia_semana_retiro
#hora_retiro
#minuto_retiro
#segundo_retiro
#ciclo_estacion_retiro
#nombre_estacion_retiro
#direccion_estacion_retiro
#cp_retiro
#colonia_retiro
#codigo_colonia_retiro
#delegacion_retiro
#delegacion_retiro_num
#fecha_arribo
#hora_arribo_copy
#fecha_arribo_completa
#anio_arribo
#mes_arribo
#dia_semana_arribo
#hora_arribo
#minuto_arribo
#segundo_arribo
#ciclo_estacion_arribo
#nombre_estacion_arribo
#direccion_estacion_arribo
#cp_arribo
#colonia_arribo
#codigo_colonia_arribo
#delegacion_arribo
#delegacion_arribo_num
#duracion_viaje
#duracion_viaje_horas
#duracion_viaje_minutos


separator = ','
fields = [12, 13]  # ciclo_estacion_retiro

for line in sys.stdin:
    stripped = line.strip().split(separator)
    values = itemgetter(*fields)(stripped)

    print("{}\t{}".format(values[0], 1))
