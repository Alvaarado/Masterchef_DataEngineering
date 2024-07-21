import requests

def test_generate_recipe():
    url = 'http://localhost:8000/generate_recipe'
    data = {
        'ingredients': ['pollo', 'arroz', 'zanahoria'],
        'time': 30
    }
    
    try:
        # Enviamos una solicitud POST al endpoint con los datos de prueba

        response = requests.post(url, json=data)
        
        # Verificamos que el código de estado de la respuesta sea 200 OK

        assert response.status_code == 200
        
        # Verificamos que la respuesta contenga la clave 'recipe'

        response_json = response.json()
        assert 'recipe' in response_json
        print("Receta generada con éxito:", response_json['recipe'])
        
    except requests.exceptions.RequestException as e:

        # Capturamos cualquier error de solicitud y lo mostramos

        print(f"Error en la solicitud: {e}")
    except AssertionError as e:

        # Capturamos errores de aserción y los mostramos
        
        print(f"Error en la respuesta del servidor: {e}")

if __name__ == "__main__":
    test_generate_recipe()
