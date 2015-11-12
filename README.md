# Student Performance App

Aplicación:
http://studentsapp.mybluemix.net/

Video:
https://www.youtube.com/watch?v=1pN6mzixJbk&feature=youtu.be

## Equipo:
* Aleph

## Integrantes:
* Julian Niebieskikwiat
* Fernando Lobato
* Alejandro Cassis

## Descripción de la solucion:

Como se explicó en el video, nuestra aplicación pretende facilitar el proceso de aprendizaje del alumno, y al mismo tiempo, facilitar el asesoramiento de un profesor hacia un alumno.

Nos basamos en el dataset "Student Performance Dataset" que se encuentra [disponible en UCI](https://archive.ics.uci.edu/ml/datasets/Student+Performance) , un repositorio de datasets para Machine Learning. Este conjunto de datos contiene información de aproximadamente 1000 estudiantes de una escuela en Portugal, junto con sus calificaciones en dos cursos diferentes.

De forma particular, utilizamos los datos pertenecientes al curso de matemáticas, que  cuenta con 33 atributos disponibles, entre los cuales se encuentra información del estudiante como sexo, edad, información de la educación de sus padres, nivel de relación intrafamiliar, entre otros. Las variables de respuesta, son las calificaciones del primero y segundo periodo de dicho curso, así como la calificación final.

En base a esto, identificamos dos problemas que se pueden abordar mediante el uso de Machine Learning:
* Identificar si un alumno va a pasar el curso contándo tan sólo con la nota del primer periodo (junto con toda la información mencionada anteriormente).
* Predecir la nota final del alumno contando con la nota del primer y segundo periodo (junto con toda la información mencionada anteriormente).

Para solucionar el primer problema, lo planteamos como una tarea de clasificación binaria. Es decir, clasificar a los estudiantes en dos categorias: los que pasan el curso, y los que no. De esta forma, probamos distintos algoritmos de clasificación, como Random Forests, Support Vector Machines y Regresión Logística. Finalmente, obtuvimos los mejores resultados con Regresión Logística, alcanzando un valor de 0.89 en la métrica F1 utilizando cross validation de 5 folds.

Se puede ver el modelado de los datos, pruebas de los algoritmos y los resultados obtenidos en el siguiente notebook de ipython: https://github.com/csssaz/StudentPerformance/blob/master/Classification.ipynb


Para solucionar el problema de predicción, lo planteamos como una tarea de regresión, donde la variable de respuesta es la calificación final. De igual forma, probamos varios algoritmos de Machine Learning para dicha tarea, como Epsilon-Support Vector Regressor, Regresión Linear (Ridge Regression), Gradient Boosting Regression, regresión de Lasso y Random Forest Regression. Obtuvimos los mejores resultados con Random Forest Regressor, obteniendo un error cuadrático medio de 3.38 utilizando 4 folds de cross validation.

Igualmente, se puede ver el modelado de datos y resultados en la siguiente liga: https://github.com/csssaz/StudentPerformance/blob/master/Regression.ipynb

Luego de obtener nuestros dos predictores, proseguimos a montar una aplicación Web utilizando el framework de Python "Flask" sobre la plataforma de Bluemix. La aplicación básicamente permite hacer estas dos predicciones, en forma de un cuestionario interactivo.

Si tuvieramos datos parecidos de escuelas en México, nos parece que se podría usar esta técnica para mejorar el desempeño académico de los alumnos, así como facilitar la labor de los profesores.


## Narración de la experiencia de desarrollo:

El reto fue muy divertido ya que al tener que incluir algo relacionado a BigData/Analytics (entre otras opciones), tuvimos que pensar cómo aplicar nuestros conocimientos de desarrollo y Machine Learning (para lo cuál no tenemos mucha experiencia aún). La plataforma de BlueMix fue muy útil ya que nos facilitó mucho el proceso de Deploy, que generalmente resulta mucho más tardado y complicado. Más aún considerando que utilizamos varias bibliotecas no tan comúnes de python.

Consideramos que pudimos desarrollar un demo de una idea interesante en poco tiempo. Y con un poco más de planeación se podría hacer algo mucho más interesante. Por ejemplo, el cuestionario que hicimos resulta tedioso, y evidentemente es sólo una muestra del poder de predicción. Sin embargo, para una idea más real, podríamos obtener esos datos directamente desde la base de datos de X escuela, y mas bien realizar sugerencias al maestro acerca de qué aspectos puede trabajar con x estudiante.

Finalmente, esta fue nuestra primera experiencia con la plataforma de Bluemix. Nosotros sólo utilizamos un poco de su poder, pero vimos que tiene muchas posibilidades y funciones que no usamos. Estamos seguros que en otra oportunidad, podríamos hacer un uso más provechoso de la misma para explotar todo su potencial, que se nota es mucho!


## Feedback del reto:

Quizá hubiera sido útil tener un poco más de información perteneciente a la plataforma en sí. Hubo un curso que dieron en línea, pero el horario nos dificultó ser parte del mismo a todos los integrantes. Más allá de eso nos parece una excelente iniciativa. ¡Muchas gracias!


