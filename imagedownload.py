import os
import requests

def download_image(url, save_directory, file_name=None):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        if not file_name:
            file_name = os.path.basename(url)

        save_path = os.path.join(save_directory, file_name)

        with open(save_path, 'wb') as image_file:
            for chunk in response.iter_content(1024):
                image_file.write(chunk)

        print(f"Image downloaded successfully: {save_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image. Error: {e}")

if __name__ == "__main__":
    url = input("enter url:")
    save_directory = "./python/images"  
    file_name = "downloaded_image.jpg"  

    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    download_image(url, save_directory, file_name)
