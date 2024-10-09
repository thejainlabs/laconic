import os

def generate_html(folder_path, output_file):
    with open(output_file, 'w') as f:
        # Walk through the folder and its subfolders
        for root, dirs, files in os.walk(folder_path):
            folder_name = os.path.basename(root)
            print(f"Processing folder: {folder_name}")  # Debugging: Print current folder name
            for file in files:
                # Check if the file is an image, including .webp format
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                    image_name = file
                    print(f"Found image: {image_name}")  # Debugging: Print image file name
                    # Generating the HTML code
                    html_code = f'''<!-- Start Gallery Item -->
<div class="col-lg-4 col-md-6 portfolio-item isotope-item filter-{folder_name}">
  <img src="assets/img/gallery/{folder_name}/{image_name}" class="img-fluid" alt="">
  <div class="portfolio-info">
    <h4>{folder_name} 1</h4>
    <!-- <p>Lorem ipsum, dolor sit</p> -->
    <!-- <a href="assets/img/masonry-portfolio/masonry-portfolio-1.jpg" title="App 1"
    data-gallery="portfolio-gallery-app" class="glightbox preview-link"><i class="bi bi-zoom-in"></i></a> -->
  </div>
</div>
<!-- End Gallery Item -->\n\n'''
                    # Writing to the output file
                    f.write(html_code)
                else:
                    print(f"Skipping non-image file: {file}")  # Debugging: Skip non-image files

    print(f"HTML generation complete. Output written to: {output_file}")

# Provide the folder path where the images are stored and the output HTML file name
folder_path = 'images2'  # Change to your actual folder path
output_file = 'galleryListItems.html'  # Output file to store the HTML
generate_html(folder_path, output_file)
