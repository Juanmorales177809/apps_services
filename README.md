# Clase: DevOps, Integración Continua, Entrega Continua e Implementación Continua

## Contexto general de la clase

Esta clase parte de un caso cercano: el desarrollo de un software para la gestión de calidad del ITM. La idea no es comenzar con definiciones aisladas, sino entender cómo un equipo real trabaja alrededor de un sistema que debe evolucionar constantemente.

En este escenario intervienen dos actores principales. Por un lado está el personal de calidad, que conoce los procesos, los formatos, los requisitos, las auditorías, los registros, las evidencias y las necesidades reales del sistema. Por otro lado está el equipo de desarrollo, encargado de convertir esas necesidades en funcionalidades concretas: pantallas, formularios, bases de datos, validaciones, reportes, permisos, carga de archivos y flujos de trabajo.

El personal de calidad identifica necesidades o problemas. El equipo de desarrollo analiza esas solicitudes, implementa cambios, prueba el sistema y entrega nuevas versiones. En apariencia, este flujo parece simple, pero cuando el software crece aparecen problemas de comunicación, integración, pruebas, despliegue y retroalimentación.

Por ejemplo, el personal de calidad puede solicitar que el sistema permita registrar evidencias de capacitación para cada persona del laboratorio. El equipo de desarrollo debe traducir esa necesidad en una solución técnica: crear o ajustar tablas en la base de datos, construir endpoints en el backend, diseñar formularios en el frontend, validar campos, controlar permisos y permitir adjuntar archivos.

El problema aparece cuando estas entregas se manejan de manera manual, tardía o desorganizada. Si los requerimientos llegan incompletos, desarrollo puede construir algo que no cumple con lo esperado. Si desarrollo entrega tarde o sin pruebas suficientes, calidad detecta errores al final. Si operaciones recibe paquetes con instrucciones manuales, cada despliegue se vuelve una tarea lenta y riesgosa.

A partir de este caso se construye toda la clase: primero se analiza el flujo tradicional, luego se identifican sus puntos débiles, y finalmente se introducen los conceptos de integración continua, entrega continua e implementación continua.

## Flujo de trabajo tradicional

En un flujo tradicional de desarrollo de software, el proceso suele avanzar por etapas separadas.

Primero está el equipo de desarrollo de software. Este equipo recibe requerimientos, escribe código, modifica funcionalidades y prepara los cambios. Luego esos cambios se guardan en Git, que funciona como repositorio central del código. Git permite versionar, registrar cambios y conocer quién modificó qué parte del sistema.

Después aparece el equipo de integración. En un modelo tradicional, la integración no siempre ocurre de manera frecuente. Muchas veces cada desarrollador trabaja por su lado y, después de cierto tiempo, alguien debe juntar todos los cambios. En ese momento aparecen conflictos, errores de dependencias, diferencias entre versiones, funcionalidades que se pisan entre sí o cambios que funcionan individualmente pero fallan al combinarse.

Luego viene la compilación. En esta etapa se toma el código integrado y se intenta construir una versión funcional del sistema. En un proyecto web puede significar instalar dependencias, construir el frontend, preparar el backend, validar que el proyecto arranque correctamente o generar archivos finales.

Si la compilación falla, el equipo debe devolverse para encontrar la causa. El problema es que, si la integración se hizo tarde y con muchos cambios acumulados, no siempre es fácil identificar qué cambio produjo el fallo.

Después viene el empaquetado. Aquí se prepara una versión del sistema para ser entregada o instalada. El paquete puede ser una carpeta de build, un archivo comprimido, un instalador, una imagen Docker o un conjunto de archivos listos para ser desplegados.

El punto crítico es que, en el flujo tradicional, muchas validaciones importantes ocurren tarde. Primero se desarrolla, luego se integra, luego se compila, luego se empaqueta y solo después se detecta si algo quedó mal. Esto hace que los errores sean más costosos de corregir.

En el caso del software de gestión de calidad, esto sería como esperar varias semanas para juntar cambios del módulo de personal, laboratorios, evidencias, permisos y reportes, y apenas al final intentar construir una versión completa. Si algo falla, el equipo pierde tiempo tratando de ubicar el origen del problema.

## Entrega y despliegue tradicional

Después del empaquetado comienza otra parte del proceso: llevar el paquete a un entorno donde pueda probarse o utilizarse.

En el modelo tradicional, el equipo de desarrollo no entrega únicamente el software. También entrega instrucciones. Estas instrucciones pueden indicar qué archivos copiar, qué variables configurar, qué dependencias instalar, qué comandos ejecutar, qué servicios reiniciar o qué rutas modificar.

El equipo de operaciones recibe ese paquete y las instrucciones asociadas. Su responsabilidad es preparar el servidor, instalar la aplicación, configurar el entorno y dejar el sistema funcionando.

Luego el sistema se instala en un entorno de prueba. Este no es el sitio público final, sino un espacio controlado donde se revisa si la aplicación carga, si el backend responde, si la base de datos está disponible, si las rutas funcionan y si los cambios no dañaron funcionalidades existentes.

Después interviene el equipo de garantía de calidad. Este equipo revisa que lo entregado cumpla con lo solicitado. En el caso del sistema de gestión de calidad, puede validar si un formulario guarda correctamente, si una evidencia se carga, si los permisos funcionan, si el registro queda asociado a la persona correcta o si un reporte muestra la información esperada.

Finalmente, si todo está correcto, el sistema se publica en el sitio web público. Allí los usuarios finales acceden a la versión liberada.

El problema es que este flujo tiene mucha transferencia manual entre equipos. Desarrollo entrega a operaciones, operaciones despliega, calidad valida y solo después se publica. Cada paso implica espera, comunicación, instrucciones y riesgo de error.

Si algo falla en el entorno de prueba, hay que devolverse al equipo de desarrollo, corregir, volver a compilar, volver a empaquetar, volver a entregar y volver a probar. Este ciclo puede ser lento, especialmente cuando el sistema crece.

## Iteración en el desarrollo de software

El proceso no termina cuando el sitio web queda publicado. Cuando los usuarios empiezan a utilizar el sistema, aparecen nuevos hallazgos: errores, mejoras, ajustes de proceso o nuevas necesidades.

Por eso se habla de iteración. El software no se construye una sola vez y se abandona. El software evoluciona. Cada entrega genera retroalimentación, y esa retroalimentación alimenta una nueva versión.

En el caso del sistema de gestión de calidad, el personal puede encontrar que falta un campo, que una validación debe cambiar, que un reporte no filtra correctamente, que un permiso no está bien definido o que un proceso debe ajustarse. Esos hallazgos regresan al equipo de desarrollo y el ciclo comienza de nuevo.

El problema del enfoque tradicional es que cada iteración puede ser pesada. Si cada cambio debe pasar manualmente por integración, compilación, empaquetado, operaciones, pruebas, validación y publicación, entonces mejorar el sistema toma demasiado tiempo.

La necesidad es pasar de un ciclo manual, lento y frágil a un ciclo más automatizado, frecuente y confiable.

## Puntos débiles del modelo tradicional

El primer punto débil es la integración. En un flujo tradicional, integrar suele tomar mucho tiempo y esfuerzo porque muchas veces se hace tarde y de forma manual. Cuando varios desarrolladores trabajan en partes diferentes del sistema, los conflictos aparecen al juntar el código.

Un cambio puede funcionar bien de forma aislada, pero fallar al mezclarse con otros módulos. Por ejemplo, un desarrollador modifica el formulario de personal, otro cambia la estructura de la base de datos y otro ajusta permisos. Al integrar, pueden aparecer errores por variables renombradas, rutas inexistentes, migraciones incompletas o dependencias incompatibles.

El segundo punto débil son los problemas de fusión intermedia. Si al unir cambios aparece un conflicto o un error importante, el equipo puede detenerse hasta resolverlo. Esto atrasa el proceso y genera dependencia entre personas o áreas.

El tercer punto son las iteraciones largas. Cuando el ciclo de desarrollo, integración, pruebas y entrega toma mucho tiempo, la retroalimentación llega tarde. Los problemas pequeños se acumulan y terminan convirtiéndose en problemas grandes.

Otro punto crítico es que la solución de problemas ocurre al final de la iteración. En el modelo tradicional, muchos defectos se descubren cuando el sistema ya fue integrado, empaquetado o incluso desplegado en pruebas. Corregir tarde es más costoso que corregir temprano.

También aparece un ciclo largo de feedback para defectos funcionales. Un defecto funcional ocurre cuando el sistema técnicamente funciona, pero no hace exactamente lo que el usuario necesita. Por ejemplo, un formulario guarda datos, pero no guarda la evidencia correcta. Un reporte se genera, pero no filtra por laboratorio. Una pantalla permite crear un registro, pero no valida un campo obligatorio.

En un proceso tradicional, estos defectos suelen descubrirse demasiado tarde.

La conclusión es que el problema no es únicamente técnico. Es un problema de proceso. Si la integración es manual, los errores se descubren tarde, las iteraciones son largas y el feedback demora, el equipo termina gastando más tiempo corrigiendo fallos acumulados que entregando valor.

## Integración continua

La integración continua, conocida como CI por sus siglas en inglés, busca resolver los problemas asociados a la integración tardía.

CI no significa desplegar en producción. CI no significa publicar el sistema en internet. CI se enfoca en integrar cambios de código con frecuencia y validarlos automáticamente.

La idea principal es evitar que cada desarrollador trabaje aislado durante mucho tiempo y que al final todos intenten juntar el código en una integración gigante. Los cambios pequeños son más fáciles de revisar, integrar y corregir.

En integración continua, el equipo trabaja sobre un repositorio central. Los desarrolladores realizan commits regularmente. Cada cambio puede activar una compilación automática. El sistema toma el código actualizado e intenta construirlo.

La compilación debe ser automatizada y rápida. El equipo no debería esperar días para saber si el código funciona. El sistema debe responder pronto si el proyecto compila o si hay errores.

Además, una buena práctica de CI incluye pruebas automáticas. No basta con decir que el proyecto arranca. También se deben ejecutar pruebas para validar partes importantes del sistema.

Si la construcción falla, la prioridad debe ser corregirla. En CI, una compilación rota afecta a todo el equipo porque el repositorio principal deja de ser una base confiable.

Los resultados de compilación deben ser visibles para todos. El equipo debe saber si el proyecto está en buen estado o si hay errores. Esto puede verse en herramientas como GitHub Actions, GitLab CI, Jenkins, Azure DevOps u otras plataformas.

En el caso del sistema de gestión de calidad, CI sería que cada vez que un desarrollador suba un cambio al backend FastAPI o al frontend React, se ejecute automáticamente una validación: instalar dependencias, correr pruebas, revisar errores y confirmar si el proyecto sigue construyendo correctamente.

El cambio importante es detectar errores temprano, no al final.

## Integración continua frente a integración tradicional

La integración continua cambia varios aspectos del modelo tradicional.

Primero, la integración pasa a ser automatizada y rápida. Antes podía tomar mucho tiempo y esfuerzo porque se hacía manualmente o al final de una etapa larga. Con CI, cada cambio puede activar una validación automática.

Segundo, los problemas se reportan a tiempo. En el modelo tradicional, los errores se descubrían al final de la iteración. Con CI, los problemas aparecen cerca del momento en que se generaron, lo que facilita encontrar la causa.

Tercero, los problemas tienen prioridad para los desarrolladores. Si la construcción falla, no se deja para después. Se corrige rápido porque una base rota afecta a todo el equipo.

Cuarto, los ciclos de feedback son más cortos. El equipo recibe notificaciones inmediatas cuando algo falla. Esto reduce el tiempo entre cometer un error y corregirlo.

El resultado es una iteración más corta y un menor tiempo para entregar valor. La integración continua permite pasar de una integración pesada, manual y tardía a una integración frecuente, repetible y visible.

## Servidor de compilación

Antes de hablar de entrega continua completa, es útil entender el papel del servidor de compilación.

Un servidor de compilación recibe cambios desde uno o varios módulos del sistema y ejecuta tareas automáticas. En un proyecto real, esos módulos pueden ser perfil del cliente, catálogo de producto o rastreo de orden. En el sistema de gestión de calidad, podrían ser personal, laboratorios, equipos, evidencias, reportes o solicitudes.

El servidor toma el código desde Git, normalmente desde una rama principal o estable. Luego ejecuta la compilación, genera un paquete y puede ejecutar pruebas automatizadas.

En un backend FastAPI, esto puede incluir instalar dependencias, revisar que el proyecto arranque, ejecutar pruebas y validar estructura. En un frontend React, puede incluir instalar paquetes, construir el proyecto con Vite y generar los archivos finales.

El servidor también puede ejecutar pruebas unitarias automatizadas y pruebas de interfaz de usuario automatizadas. Esto representa un avance importante frente a un proceso completamente manual.

Sin embargo, todavía falta un punto clave: que el paquete generado pueda avanzar hacia entornos reales de manera controlada y repetible. Aquí empieza a aparecer la necesidad de entrega continua.

## Operaciones y paquetes con instrucciones

En la vieja escuela, cuando el servidor genera un paquete, el equipo de desarrollo suele entregarlo al equipo de operaciones junto con instrucciones.

El paquete puede contener archivos de la aplicación, configuraciones, dependencias, scripts parciales o una versión construida del sistema. Las instrucciones pueden indicar cómo copiar archivos, instalar parches, configurar variables de entorno o diferenciar entre ambiente de pruebas y producción.

Por ejemplo, para un entorno de prueba se pueden usar variables como:

```text
env=test
db=mockdb
url=test.electronica.com
```

Para producción se pueden usar otros valores:

```text
env=prod
db=productdb
url=electronica.com
```

El problema es que este enfoque depende demasiado de que una persona lea, interprete y ejecute correctamente cada paso.

Si operaciones copia un archivo en la carpeta equivocada, usa una variable incorrecta, instala un parche diferente o mezcla valores de prueba con valores de producción, el despliegue puede fallar.

En un sistema de gestión de calidad, esto puede significar que una versión apunte a la base de datos equivocada, que se carguen configuraciones incompletas o que un módulo funcione en pruebas pero falle en producción.

El conocimiento del despliegue existe, pero está escrito como instrucciones manuales. No necesariamente está automatizado ni versionado dentro del flujo técnico.

## Puntos débiles de las instrucciones manuales

El primer problema de las instrucciones manuales es su exactitud. Si una instrucción está incompleta, mal escrita o desactualizada, operaciones puede ejecutar un paso incorrecto. El software cambia, pero los documentos no siempre se actualizan al mismo ritmo.

El segundo problema es la diferencia entre instrucciones para distintos entornos. No es lo mismo desplegar en pruebas que en producción. Cambian variables, bases de datos, URLs, permisos, certificados y servicios. Si alguien mezcla valores, el sistema puede quedar apuntando al entorno incorrecto.

El tercer problema es la naturaleza propensa a errores por tareas manuales. Copiar archivos, cambiar variables, ejecutar comandos y reiniciar servicios manualmente siempre introduce riesgo. Una letra mal escrita en una variable de entorno puede tumbar un despliegue.

El cuarto problema es el impacto en tiempo de inactividad. Cuando el despliegue es complejo y manual, toma más tiempo. Mientras más tiempo tome, mayor es la posibilidad de que el sistema esté caído o funcionando parcialmente.

La solución no es eliminar a operaciones ni a calidad. La solución es quitar tareas repetitivas, reducir errores manuales y automatizar los pasos que siempre se ejecutan de la misma forma.

## De instrucciones a scripts

El siguiente paso lógico es convertir instrucciones manuales en scripts.

Un script es un archivo con comandos que automatiza tareas. En lugar de pedirle a una persona que copie archivos, el script ejecuta la copia. En lugar de pedirle que configure variables, el script las define. En lugar de pedirle que instale dependencias, el script ejecuta esos comandos.

Por ejemplo, si antes una instrucción decía copiar archivos `.properties` a una carpeta `etc/config`, ahora un script puede ejecutar ese paso automáticamente.

Si antes había instrucciones diferentes para pruebas y producción, el script puede recibir un parámetro y seleccionar la configuración correcta según el entorno.

Esto reduce errores porque el procedimiento se ejecuta siempre de la misma forma. El conocimiento del despliegue deja de estar únicamente en un documento y comienza a expresarse como código.

## Pipelines

A partir de los scripts aparece el concepto de pipeline.

Un pipeline es un flujo de trabajo automatizado compuesto por etapas. Cada etapa ejecuta una tarea específica y normalmente el resultado de una etapa alimenta la siguiente.

Un pipeline puede compilar el código, ejecutar pruebas, empaquetar la aplicación, preparar el entorno, desplegar en pruebas, validar resultados y dejar una versión lista para producción.

En integración continua, el pipeline valida que el código compile y pase pruebas. En entrega continua, el pipeline va más allá: también prepara paquetes, ambientes y despliegues para que la versión pueda liberarse cuando se decida.

En el sistema de gestión de calidad, un pipeline podría tomar el código desde Git, construir el backend FastAPI, construir el frontend React, ejecutar pruebas, crear una imagen Docker, subirla a un registro, desplegarla en un entorno de prueba y notificar al equipo de calidad para validar.

La idea es que las tareas repetitivas no dependan de copiar y pegar comandos a mano. Si una tarea se repite y siempre debe hacerse igual, debe vivir en un script o en un pipeline.

## Entrega continua

La entrega continua, conocida como CD por sus siglas en inglés, es una práctica de desarrollo de software donde el sistema puede lanzarse a producción en cualquier momento.

La palabra clave es puede. No significa que cada cambio se publique automáticamente. Significa que el software está en un estado suficientemente preparado, probado y controlado para ser liberado cuando el equipo lo decida.

La entrega continua no elimina el control. Al contrario, busca que el proceso sea tan confiable que publicar deje de ser un evento traumático.

El objetivo es que el software esté siempre listo para producción. No se trata de tener una versión que casi compila, casi funciona o solo necesita algunos ajustes manuales. La versión debe pasar por validaciones suficientes para ser considerada liberable.

El requisito principal para la entrega continua es la integración continua. No se puede hablar de entrega continua si primero no existe un proceso confiable para integrar, compilar y probar el código.

El resultado de la entrega continua es la generación frecuente de paquetes de lanzamiento. El equipo puede entregar mejoras pequeñas, correcciones urgentes o nuevas funcionalidades con menor riesgo y mayor frecuencia.

En el caso del sistema de gestión de calidad, entrega continua significa que una mejora en el módulo de personal, reportes o evidencias no queda esperando instrucciones manuales indefinidamente. El flujo la deja preparada para liberarse de manera controlada.

## Operaciones tradicionales frente a entrega continua

Cuando se comparan las operaciones tradicionales con la entrega continua, se observan mejoras claras.

La exactitud de las instrucciones mejora porque los scripts automatizados pueden verificarse en tiempo de creación. Ya no dependen únicamente de un documento interpretado por una persona.

La diferencia entre instrucciones de instalación para distintos entornos se gestiona mejor porque los scripts y pipelines pueden seleccionar tareas y variables según el ambiente: prueba, preproducción o producción.

La automatización reduce errores manuales. Copiar archivos, cambiar variables y ejecutar comandos a mano deja de ser el centro del proceso.

Los despliegues sofisticados se vuelven más repetibles. Un despliegue automatizado es más fácil de ejecutar varias veces, más fácil de auditar y más fácil de corregir.

Esto no significa que la automatización elimine todos los problemas. Significa que reduce la variabilidad humana en tareas repetitivas y hace que el proceso sea más confiable.

## Integración continua y entrega continua como flujo completo

Cuando se integran CI y CD, se obtiene una visión completa del flujo de trabajo.

La integración continua reduce el riesgo técnico del código. Cada cambio se integra, se compila y se prueba lo antes posible. La entrega continua reduce el riesgo operativo del despliegue. El software no solo se construye, sino que queda preparado para llegar a un entorno real.

Juntas, estas prácticas permiten que el software avance desde el desarrollo hasta entornos de prueba o producción de manera más controlada.

El pipeline se convierte en la columna vertebral del proceso. No es solo una herramienta que ejecuta comandos. Representa la forma en que el equipo entrega software.

## Implementación continua

La implementación continua, o Continuous Deployment, es un paso adicional.

En entrega continua, el sistema queda listo para publicarse, pero una persona o el equipo decide cuándo liberar.

En implementación continua, si el cambio pasa todas las validaciones definidas, el sistema puede desplegarse automáticamente.

Esto exige confianza en el proceso, pero no confianza ciega. Esa confianza se construye con pruebas, reglas, controles, validaciones y buenas prácticas.

La idea no es publicar sin pensar. La idea es quitar el paso manual final cuando ya no aporta valor.

En un sistema de gestión de calidad, la implementación continua podría aplicarse primero en ambientes de prueba o preproducción. Para producción se podría conservar una aprobación formal, especialmente si el sistema maneja procesos sensibles.

La implementación continua no significa publicar a lo loco. Significa automatizar la liberación cuando el proceso ya demostró que el cambio es seguro.

## Cierre de la clase

La clase muestra una evolución clara.

Primero se parte del desarrollo tradicional, donde los equipos trabajan por etapas separadas y muchas validaciones ocurren tarde.

Luego se identifican los puntos débiles: integración manual, problemas de fusión, iteraciones largas, feedback tardío, instrucciones propensas a errores y despliegues lentos.

Después aparece la integración continua, que permite validar el código temprano y con frecuencia.

Luego aparece la entrega continua, que convierte el software construido en una versión lista para ser liberada mediante procesos repetibles.

Finalmente se introduce la implementación continua, donde el despliegue puede automatizarse si todas las validaciones se cumplen.

La idea central no es usar herramientas por moda. La idea es mejorar el flujo de trabajo para que el software pueda evolucionar con menos riesgo, menos tareas manuales y mayor capacidad de respuesta.

DevOps no comienza instalando una herramienta. Comienza entendiendo dónde se rompe el proceso y qué partes deben automatizarse, medirse y mejorarse.
