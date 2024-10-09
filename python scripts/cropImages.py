import os
from PIL import Image

def crop_center(image, target_size):
    width, height = image.size
    target_width, target_height = target_size
    
    # If either dimension is less than the target, keep the smaller side as it is
    if width < target_width or height < target_height:
        target_width = min(width, target_width)
        target_height = min(height, target_height)
    
    left = (width - target_width) / 2
    top = (height - target_height) / 2
    right = (width + target_width) / 2
    bottom = (height + target_height) / 2
    
    return image.crop((left, top, right, bottom))

def crop_images_in_folder(source_folder, destination_folder, target_size=(400, 400)):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            if file.lower().endswith(('png', 'jpg', 'jpeg')):
                source_file_path = os.path.join(root, file)
                relative_path = os.path.relpath(root, source_folder)
                destination_subfolder = os.path.join(destination_folder, relative_path)
                
                # Ensure the destination subfolder exists
                if not os.path.exists(destination_subfolder):
                    os.makedirs(destination_subfolder)
                
                destination_file_path = os.path.join(destination_subfolder, file)
                
                with Image.open(source_file_path) as img:
                    cropped_img = crop_center(img, target_size)
                    cropped_img.save(destination_file_path)  # Save cropped image in new folder

# Replace 'source_folder' and 'destination_folder' with actual paths
source_folder = '/Users/nejain/Documents/workspace/laconic/images'
destination_folder = '/Users/nejain/Documents/workspace/laconic/images2'
crop_images_in_folder(source_folder, destination_folder)
