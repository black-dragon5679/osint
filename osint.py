import requests
from bs4 import BeautifulSoup
import subprocess
import os

def osint_image_search(directory):
    image_results = []

    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Adjust file extensions as needed
            image_url = os.path.join(directory, filename)
            url = f"https://www.google.com/searchbyimage?image_url={image_url}"

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            }

            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract relevant information from the search results
            # ...

            # Use exiv2 to extract metadata from the image
            exiv2_output = subprocess.run(["exiv2", image_url], capture_output=True, text=True)
            metadata = exiv2_output.stdout

            image_results.append({
                'filename': filename,
                'metadata': metadata
            })

    return image_results

# Example usage
directory = 'images/'
results = osint_image_search(directory)

for result in results:
    print(f"Image: {result['filename']}")
    print(f"Metadata:\n{result['metadata']}\n")