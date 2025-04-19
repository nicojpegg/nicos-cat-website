import os
from PIL import Image

def convert_to_webp(folder, image_extensions):
    for filename in os.listdir(folder):
        # Check if the file is an image (not already .webp)
        if filename.lower().endswith(image_extensions) and not filename.lower().endswith(".webp"):
            old_path = os.path.join(folder, filename)
            new_filename = os.path.splitext(filename)[0] + ".webp"
            new_path = os.path.join(folder, new_filename)

            # Convert the image to .webp
            with Image.open(old_path) as img:
                img.save(new_path, "WEBP")
                print(f"Converted '{old_path}' to '{new_path}'")

            # Optionally, remove the original file after conversion
            os.remove(old_path)
            print(f"Removed original file '{old_path}'")

def rename_images():
    # Define the folders to search
    folders = ["cats", "catjpg"]
    # Supported image file extensions
    image_extensions = (".jpg", ".jpeg", ".png", ".webp")
    # Counter for renaming
    counter = 0

    for folder in folders:
        if not os.path.exists(folder):
            print(f"Folder '{folder}' does not exist. Skipping...")
            continue

        # Convert all images to .webp first
        convert_to_webp(folder, image_extensions)

        for filename in os.listdir(folder):
            # Check if the file is a .webp image
            if filename.lower().endswith(".webp"):
                old_path = os.path.join(folder, filename)
                new_filename = f"cat{counter}.webp"
                new_path = os.path.join(folder, new_filename)

                # Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed '{old_path}' to '{new_path}'")

                counter += 1

if __name__ == "__main__":
    rename_images()