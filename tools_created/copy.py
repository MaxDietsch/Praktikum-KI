import os
import shutil

def copy_all_files(src_dir, dest_dir):
    # Iterate through all files in the source directory
    i = 0
    for dir in os.listdir(src_dir):
        for filename in os.listdir(os.path.join(src_dir, dir)):
            src_file_path = os.path.join(src_dir, filename)
            dest_file_path = os.path.join(dest_dir, filename)

        # Check if it's a file and not a directory
        print(src_file_path)
        print(dest_file_path)
        if os.path.isfile(src_file_path):
            shutil.copy(src_file_path, dest_file_path)
            i += 1
            print(i)
        if i == 1:
            break

if __name__ == "__main__":
    source_directory = "./download_unzip/SUN/negative"
    destination_directory = "../data_dir/SUN/negative"
    
    copy_all_files(source_directory, destination_directory)
