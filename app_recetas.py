from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
from openai import OpenAI
import pymysql
import logging
from langchain.prompts import PromptTemplate 

# Configuramos la clave API de OpenAI

api_key1 = ''
client = OpenAI(api_key=api_key1)

app = FastAPI()

# Configuramos el registro

logging.basicConfig(level=logging.ERROR)

# Accedemos al directorio de archivos

app.mount("/static", StaticFiles(directory="static"), name="static")

# Conectamos con la base de datos

DB_CONFIG = {
    'host': 'db-recipes.ct46wkioy0f3.us-east-1.rds.amazonaws.com', 
    'port': 3306,
    'user': 'admin',
    'password': '12345678',
    'database': 'query_recipes',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def execute_insert_query(query, params):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()
    finally:
        connection.close()

# Configuramos el PromptTemplate con langchain

recipe_prompt_template = PromptTemplate.from_template(
    "Asume el rol de un cocinero experto. Con los ingredientes {ingredients} y con {time} minutos disponibles para cocinar, proporciona una receta detallada paso a paso."
)

# Inicio

@app.get("/")
async def hallo():
    return FileResponse("recetas.html")

# Endpoint para generar receta

@app.post("/generate_recipe")
async def generate_recipe(request: Request):
    data = await request.json()
    ingredients = data.get('ingredients')
    time = data.get('time')

    if not ingredients or len(ingredients) != 3 or not time:
        raise HTTPException(status_code=400, detail="Es necesario proporcionar tres ingredientes y el tiempo del que dispones para cocinar.")

    try:

        # Creamos el prompt usando el PromptTemplate de langchain

        prompt = recipe_prompt_template.format(ingredients=', '.join(ingredients), time=time)

        # Llamamos a la API de OpenAI con el prompt generado

        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un cocinero experto."
            },
            {
                "role": "user",
                "content": prompt
            }
        ])

        recipe = response.choices[0].message.content

        # Insertamos los datos en la base de datos

        insert_query = "INSERT INTO query_responses (ingredients, time, response) VALUES (%s, %s, %s)"
        insert_params = (', '.join(ingredients), time, recipe)
        execute_insert_query(insert_query, insert_params)

        return {"recipe": recipe}

    except Exception as e:
        logging.error(f"Error al generar la receta: {str(e)}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

# Fin

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)