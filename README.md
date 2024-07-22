
# 🍽️ Masterchef - Generador de Recetas 🍽️

**Masterchef** es una aplicación de IA generativa que proporciona recetas personalizadas basadas en los ingredientes y el tiempo disponible que los usuarios proporcionan. Utilizando un modelo de lenguaje avanzado, la aplicación sugiere recetas detalladas paso a paso para ayudar a los usuarios a cocinar deliciosas comidas.

## Descripción del Proyecto

Este proyecto utiliza un modelo de lenguaje avanzado (OpenAI) para generar recetas culinarias personalizadas. Los usuarios ingresan los ingredientes disponibles y el tiempo que tienen para cocinar, y la aplicación devuelve una receta detallada. Los datos ingresados se almacenan en una base de datos en AWS, y se utiliza Langchain para manejar los prompts de generación de recetas.

## Estructura del Proyecto

- **app_recetas.py**: código para la aplicación FastAPI que maneja la generación de recetas y la interacción con la base de datos.
- **db_config.ipynb**: Jupyter notebook para la creación de la base de datos y la estructura de la tabla en AWS utilizando PyMySQL
- **Dockerfile**: archivo Docker para construir y ejecutar la aplicación en un contenedor Docker.
- **requirements.txt**: archivo de requerimientos para las dependencias de la aplicación.
- **recetas.html**: archivo HTML para la interfaz de usuario.
- **test_app.py**: código para probar la funcionalidad de la aplicación.
- **static/**: carpeta que contiene imágenes y otros recursos estáticos utilizados en el proyecto.

## Instalación a través de Docker

1. **Descargar la Imagen**:

   Descarga la imagen desde Docker Hub:
   ```bash
   docker pull alvaarado/recetas_app:v1
   ```

2. **Ejecutar el Contenedor**:

   Ejecuta el contenedor con el siguiente comando:
   ```bash
   docker run -p 8000:8000 alvaarado/recetas_app
   ```

## Uso

1. **Accede a la Interfaz Web**:

   Abre tu navegador y accede a la aplicación en:
   [http://localhost:8000](http://localhost:8000)

2. **Generar Recetas**:

   - Ingresa los ingredientes disponibles (debe proporcionar exactamente tres ingredientes) y el tiempo que tienes para cocinar en los campos proporcionados.
   - Envía el formulario y espera la receta detallada generada por el modelo de IA.

## Herramientas

- **Python**: lenguaje de programación utilizado.
- **FastAPI**: framework para construir la API de la aplicación.
- **MySQL**: sistema de gestión de bases de datos para almacenar datos de recetas.
- **Uvicorn**: servidor ASGI para ejecutar la aplicación FastAPI.
- **OpenAI**: API para generar recetas basadas en el modelo GPT-3.5-turbo.
- **Docker**: plataforma para construir y ejecutar contenedores.
- **HTML**: lenguaje para crear la interfaz web.
- **Langchain**: biblioteca para gestionar prompts y mejorar la interacción con modelos de lenguaje.

## Notas Adicionales

- Asegúrate de que la clave de API de OpenAI esté configurada correctamente en el archivo `app_recetas.py`.
- Verifica que la base de datos en AWS esté configurada y que la tabla `query_responses` esté creada utilizando el Jupyter Notebook en `db_config.ipynb`.
- Para modificar la aplicación o agregar nuevas funcionalidades, edita el archivo `app_recetas.py` y actualiza los requisitos en `requirements.txt`.

---

¡Gracias por usar Masterchef! Si tienes alguna pregunta, sugerencia o necesitas ayuda adicional, no dudes en contactar conmigo a traves de ruizfdezalvaro@gmail.com


---
