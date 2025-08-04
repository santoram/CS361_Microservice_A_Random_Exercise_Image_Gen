import os
import random
from flask_cors import CORS
from flask import Flask, send_file

# This is the directory containing approx 75 exercise images 
# Ensure this is rooted in the same directory as this program
IMAGE_DIR = 'random_exercise_photos'
app = Flask(__name__)
CORS(app)


@app.route('/random-image')
def get_random_image():
    """
    Gets a random exercise image from the diretory and returns it to the client
    """
    
    # Get a list of all files in the image directory
    image_files = os.listdir(IMAGE_DIR)
    
    # Select a random image from the directory
    # Then create the file path - random_exercise_phots/random_image.jpeg
    random_image_filename = random.choice(image_files)
    random_image_path = os.path.join(IMAGE_DIR, random_image_filename)

    # Send the selected image file back to the client
    return send_file(random_image_path, mimetype='image/jpeg') # Adjust mimetype as needed


if __name__ == '__main__':
    # check to make sure the file path exsists before execution
    # note this is running on port 8000
    os.makedirs(IMAGE_DIR, exist_ok=True)
    app.run(host='127.0.0.1', port=8000, debug=True)