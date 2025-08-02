from flask import Flask
import requests
from PIL import Image
import io

app = Flask(__name__)

@app.route('/request-image')
def request_and_open_image():
    """
    Call the image-generator microservice to get an exercise-image
    """
    image_server_url = 'http://localhost:8000/random-image'
    try:
        response = requests.get(image_server_url)
        response.raise_for_status()
        if response.headers['Content-Type'] == 'image/jpeg':
            image_bytes = response.content
            image = Image.open(io.BytesIO(image_bytes))
            image.show()
            return "Image received and opened successfully!"
        else:
            return f"Received unexpected content type: {response.headers['Content-Type']}"

    except requests.exceptions.RequestException as e:
        return f"Error requesting image: {e}"
    except Exception as e:
        return f"Error processing image: {e}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)