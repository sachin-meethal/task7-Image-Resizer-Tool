import os
from PIL import Image

# --- Configuration ---
input_folder = "images_input"     # Folder with original images
output_folder = "images_output"   # Folder to save resized images
new_size = (800, 800)             # Resize width x height

# --- Create output folder if not exists ---
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# --- Loop through each file in the input folder ---
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)
        
        # --- Resize Image ---
        resized_img = img.resize(new_size)
        
        # --- Convert and Save ---
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")
        resized_img.save(output_path, "JPEG")
        
        print(f"✅ Resized and saved: {output_path}")

print("\n🎉 All images resized successfully!")
