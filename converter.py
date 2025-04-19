import os
from PIL import Image

def convert_webp_to_jpeg():
    # Define the source and destination folders
    source_folder = "cats"
    destination_folder = "catjpg"

    # Ensure the destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        # Check if the file is a .webp image
        if filename.lower().endswith(".webp"):
            source_path = os.path.join(source_folder, filename)
            # Keep the same name but change the extension to .jpeg
            new_filename = os.path.splitext(filename)[0] + ".jpeg"
            destination_path = os.path.join(destination_folder, new_filename)

            # Open the .webp image and convert it to .jpeg
            with Image.open(source_path) as img:
                rgb_image = img.convert("RGB")  # Convert to RGB mode
                rgb_image.save(destination_path, "JPEG")
                print(f"Converted '{source_path}' to '{destination_path}'")

if __name__ == "__main__":
    convert_webp_to_jpeg()