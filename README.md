
# easy_data

Este repositorio contiene el código fuente que responde a los reuqerimientos de las pruebas técnicas para el cargo de Data Scientist - ML Engineer en Easy Data.

  

El proyecto cuenta con dos archivos:

- main.py: Contiene el código en el cual se maneja la API de la aplicación. (Está basada en la librería FastAPI)💻

- model.py: Contiene el código en el cual se genera la extración de los comentarios de la app de claro colombia y se genera el análisis de sentimientos basado en el modelo BERT entrenado para varios lenguajes. (Está basado en la librería transformers) 🤖

  

## Uso de la API

1) Para usar el endpoint el cual devuelve una cantidad n de comentarios y su respectiva clasificación de estrellas se debe acceder a la siguiente url: https://easy-data-classifier.azurewebsites.net/comments/<n_comments>

	- En dicha url la variable n_comments corresponde a la cantidad de comentarios que el usuario desea obtener de la API, por ejemplo:

		https://easy-data-classifier.azurewebsites.net/comments/3

		Retornará un objeto similar a este:

  

		{"content":{"0":"Ninguna contraseña acepta .la elimine no sirbe para nada","1":"Claro tiene una cobertura de su señal de regular a buena, pero su cobertura de Internet 4g no es mala es realmente muy mala muy pésima, y su atención al cliente pésima como todos los operadores supongo.","2":"Buena"},"ModelStarts":{"0":1,"1":1,"2":4}}

  

	Es un diccionario con dos llaves "content" y "ModelStars":

	* content: Contiene un diccionario en el cual las llaves serán los id unicos de cada uno de los comentarios extraidos en el proceso de web scrapping. Los valores de dichas llaves serán el contenido de cada uno de los comentarios extraídos, es decir, el comentasrio en si.

  

	* ModelStars: Contiene un diccionario en el cual las llaves serán los id unicos de cada uno de los comentarios extraidos en el proceso de web scrapping. Los valores de dichas llaves será la clasificación (1 - 5) que el modelo otorgó al comentario. Donde 1 se refiere a un comentario muy negativo y 5 muy positivo.

  

2) Para usar el endpoint el cual devuelve una clasificación de estrellas basado en el texto que se le ingrese via URL se debe acceder a la siguiente url: https://easy-data-classifier.azurewebsites.net/predict/?text=<texto_a_clasificar>

- En dicha url la variable texto_a_clasificar corresponde al texto que se quiere clasificar en el sistema de estrellas, por ejemplo:

	https://easy-data-classifier.azurewebsites.net/predict/?text=Esta es la mejor aplicación que he probado en el último mes.

	Retornará un objeto similar a este:
	
	{"label":"5 stars","score":0.8936758041381836,"Sentimiento":"Muy Positivo"}

  

	Es un diccionario con tres llaves "label", "score", "Sentimiento".

	- Label: Calificación que el model le ha dado al comentario.

	- Score: Puntaje que el modelo le ha dado a su clasificación, es decir, "que tan seguro está de que su clasificación fue hacertada".

	- Sentimiento: Clasificación del sentimiento hacia el comentario de manera cualitativa.

			Muy Positivo
			Positivo
			Neutro
			Negativo
			Muy Negativo
