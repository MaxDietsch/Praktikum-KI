import cv2
import os

def calc_norm(dir):
    sum_r, sum_g, sum_b = 0.0, 0.0, 0.0
    sum_sq_diff_r, sum_sq_diff_g, sum_sq_diff_b = 0.0, 0.0, 0.0
    i = 0
    for img_name in os.listdir(dir):
        print(i)
        i += 1
        # Ensure the file is an image
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            continue

        # Open and resize the image
        img_path = os.path.join(dir, img_name)
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

        sum_r += image[:, :, 0].mean()
        sum_g += image[:, :, 1].mean()
        sum_b += image[:, :, 2].mean()   

        if i >= 10000:
            break     

    
    num_images = len(os.listdir(dir))
    mean_r = sum_r / num_images
    mean_g = sum_g / num_images
    mean_b = sum_b / num_images

    i = 0
    for img_name in os.listdir(dir):
        print(i)
        i += 1
        # Ensure the file is an image
        if not img_name.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            continue

        # Open and resize the image
        img_path = os.path.join(dir, img_name)
        image = cv2.imread(img_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert from BGR to RGB

        sum_sq_diff_r += ((image[:, :, 0] - mean_r) ** 2).mean()
        sum_sq_diff_g += ((image[:, :, 1] - mean_g) ** 2).mean()
        sum_sq_diff_b += ((image[:, :, 2] - mean_b) ** 2).mean()

        if i >= 10000:
            break

    var_r = sum_sq_diff_r / num_images
    var_g = sum_sq_diff_g / num_images
    var_b = sum_sq_diff_b / num_images

    std_r = var_r ** 0.5
    std_g = var_g ** 0.5
    std_b = var_b ** 0.5

    print(f"mean values: r: {mean_r}, g: {mean_g}, b: {mean_b}")
    print(f"standard deviations: r: {std_r}, g: {std_g}, b: {std_b}")


directory = './data_dir/LD/train'
calc_norm(directory)
