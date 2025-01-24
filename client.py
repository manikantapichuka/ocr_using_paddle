import requests
from requests.exceptions import Timeout
import time

def process_file(file_path):
    print("Sending file path to PaddleOCR service...")
    url = "http://localhost:5000/ocr"
    timeout = 600
    # Send the file path as JSON
    try:
        start_time = time.time()
        response = requests.post(url, json={"file_path": file_path}, timeout=timeout)
        end_time = time.time()
        elapsed_time = end_time - start_time

        print(f"Time taken for API call: {elapsed_time:.2f} seconds")

        if response.status_code == 200:
            result = response.json().get("concatenated_text", "")
        else:
            result = f"Error: {response.status_code}, {response.text}"
        
        print(f"Extracted Text:\n{result}")
        return result

    except Timeout:
        print(f"The request timed out after {timeout} secs.")
    

# file_name = "testImage.png" # normal png image file
# file_name = "vector-db-source-available.png" # normal png image file
# file_name = "hindi2.jpg" # Hindi image
file_name = "newspaper.PNG" # Big image
# file_name = "images.jpg" # empty image
# file_name = "output4.mp4" # video

process_file(file_name)