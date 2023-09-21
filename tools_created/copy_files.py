import os
import shutil

def copy_all_files(src_dir, dest_dir):
    # Iterate through all files in the source directory
    i = 0
    for dir in os.listdir(src_dir):
        if dir =="annotation.txt":
            continue
        for filename in os.listdir(os.path.join(src_dir, dir)):
            src_file_path = os.path.join(src_dir, dir, filename)
            dest_file_path = os.path.join(dest_dir, filename)

        # Check if it's a file and not a directory
            if os.path.isfile(src_file_path):
                shutil.copy(src_file_path, dest_file_path)
                i += 1
                print(i)
            """
            if i == 1:
                break
            """

if __name__ == "__main__":
    source_directory = "./download_unzip/SUN/positive"
    destination_directory = "../data_dir/SUN/positive"
    
    copy_all_files(source_directory, destination_directory)
