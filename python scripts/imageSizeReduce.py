import os
from PIL import Image

# Hardcoded paths (can be changed later)
input_folder = '/Users/nejain/Documents/workspace/laconic/images'
output_folder = '/Users/nejain/Documents/workspace/laconic/images2'

# List of valid image extensions
valid_extensions = ['.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff']

def create_output_folder_structure(input_folder, output_folder):
    """
    Create the same folder structure as input_folder inside output_folder.
    """
    for root, dirs, files in os.walk(input_folder):
        structure = os.path.join(output_folder, os.path.relpath(root, input_folder))
        if not os.path.exists(structure):
            os.makedirs(structure)

def compress_image(image_path, output_path, target_size=None, percentage=None):
    """
    Compress the image based on the target size or percentage.
    """
    try:
        image = Image.open(image_path)

        # Change the output path extension to .webp
        output_path = os.path.splitext(output_path)[0] + '.webp'

        # Apply logic for size or percentage compression (to be implemented)
        if target_size:
            # Compress to target size (logic to be added)
            pass
        elif percentage:
            # Compress by percentage (logic to be added)
            pass
        
        # Save the image to the output path in WebP format
        image.save(output_path, 'WEBP')

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def process_images(input_folder, output_folder, target_size=100*1024, percentage=None, convert_to_best=True):
    """
    Process all images in the input folder and save them in the output folder with the same structure.
    """
    create_output_folder_structure(input_folder, output_folder)
    
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            # Skip non-image files
            if not any(file.lower().endswith(ext) for ext in valid_extensions):
                continue
            
            input_path = os.path.join(root, file)
            output_path = os.path.join(output_folder, os.path.relpath(input_path, input_folder))
            
            # Compress and convert images
            compress_image(input_path, output_path, target_size=target_size, percentage=percentage)

# Example usage:
process_images(input_folder, output_folder, target_size=100*1024, convert_to_best=True)
