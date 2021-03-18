# OCP Aplicación para DEMO

El objetvio de esta aplicación es utlizarla como demo de OCP.
La misma crea registros en un lapso de tiempo configurable los cuales se componen de 2 partes, un timestamp y nombres random.
Además de mostrar la creación de aplicaciones y cambio de congifuración por environment variables se puede utilizar para
mostrar el uso del pod scaling y generar caga que puede visualizarse tanto en el Dashboard de OCP como en la parte de 
Observability de ACM.

## Uso:

```
genera_registros.py: Crea la tabla en el Postgresql y genera los registros.
lee_registros.py: Lee los registros del Postgresql y los muestra en un Flask.

Las variables que utilizan son:

hac_PHOST    : Nombre del host del Postgresql.
hac_PUSERNAME: Usuario para conectarse a la base.
hac_PPASSWORD: Password del usuario de la base.
hac_PDATABASE: Nombre de la Base de Datos.
hac_PTABLA   : Table donde se guardarán los registros (es creada por genera_registros.py).
hac_TIEMPO   : Segundos entre los cuales se produce la generación de los registros en formato de segundos (sólo usada por genera_registros.py).
```