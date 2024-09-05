# Repositorio de prueba técnica de DE

# SQL
Bajo el contexto de desarrollo, que fue implementar el modelo en motor PostgreSQL, se obtuvieron los siguientes resultados:

- Para la pregunta 1 se creo el script hijos_avg.sql, se adjunta el plan de ejecución proporcionado por el motor de BD, donde basicamente podemos ver que los recursos se destinan mayormente a la tarea de join (cambio de grosor de flecha). Al resolver el requerimiento con la sentencia EXISTS reducimos el costo de procesamiento, dado que, el resultado se determina por un valor bool entregado por esta y no por un scan completo de la tabla hecho por un JOIN de descarte.
De todas maneras, agregar indices y/o un cambio en el modelo a partir de que las FK sean las PK de las tablas conyuges e hijos, harían permorfar mejor la consulta.

- Para la pregunta 2 se creo el script nietos_qty_rank.sql, se adjunta el plan de ejecución proporcionado por el motor de BD, donde basicamente podemos ver que los recursos se destinan mayormente a la tarea de join (cambio de grosor de flecha). Se asume que se quiere identificar la persona a quien corresponde la mayor cantidad de nietos, por lo que decido consultar el nombre más allá del id de persona que esta tenga. En función de lo anterior es inevitable tener dos join en la consulta, una para resolver la relación jerarquica padre-hijo y otra para darle el nombre al abuelo.
De todas maneras, agregar indices y/o un cambio en el modelo a partir de que las FK sean las PK de las tablas conyuges e hijos, harían permorfar mejor la consulta.

# Python
Con respecto al item python solo asumí que el tópico de tiempo es solo informativo y para toma de desición, por lo que, no lo considero como un insumo como para determinarlo como output, caso contrario son los output de cada función que si se podrían manipular en algun caso de uso.

Existen dos métodos para ejecutar el código, la primera usando terminal y la segunda vía jupyter notebook.

Como ejemplo para el caso de ejecutarlo por terminal, ejecutar los siguientes comandos en el directorio del repo:

- python3 ./python/src/main.py