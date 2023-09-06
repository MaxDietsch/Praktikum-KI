from PIL import Image
import os

def resize_images(src_dir, dst_dir, target_size):
    for img_name in os.listdir(src_dir):
        # Ensure the file is an image
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            continue

        # Open and resize the image
        img_path = os.path.join(src_dir, img_name)
        with Image.open(img_path) as img:
            img_resized = img.resize(target_size)
            
            # Save the resized image to the destination directory
            img_resized.save(os.path.join(dst_dir, img_name))

src_directory = '../data_dir/kvasir/val'
dst_directory = '../data_dir/kvasir/val'
resize_images(src_directory, dst_directory, target_size=(1280, 1024))
