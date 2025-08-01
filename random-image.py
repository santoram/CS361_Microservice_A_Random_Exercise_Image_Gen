import os
import random
from flask_cors import CORS
from flask import Flask, send_file

IMAGE_DIR = 'random_exercise_photos'
app = Flask(__name__) #r eferenced this file
CORS(app)


@app.route('/random-image')
def get_random_image():
    # Get a list of all files in the image directory
    image_files = os.listdir(IMAGE_DIR)
    # Select a random image from the directory
    # Then create the file path - random_exercise_phots/random_image.jpeg
    random_image_filename = random.choice(image_files)
    random_image_path = os.path.join(IMAGE_DIR, random_image_filename)

    # Send the selected image file back to the client
    return send_file(random_image_path, mimetype='image/jpeg') # Adjust mimetype as needed


if __name__ == '__main__':
    os.makedirs(IMAGE_DIR, exist_ok=True)
    app.run(port=5555, debug=True)