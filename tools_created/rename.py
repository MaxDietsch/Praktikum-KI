import os

dir_path = '../kvasir/esophagitis'


def rename_files(dir_path):
    dir_name = os.path.basename(dir_path)
    files = os.listdir(dir_path)
    for i, file in enumerate(files):
        old_file_path = os.path.join(dir_path, file)
        new_file_path = os.path.join(dir_path, dir_name + str(i) + ".jpg")
        os.rename(old_file_path, new_file_path)
        print(f'Renamed: {old_file_path} -> {new_file_path}')


rename_files(dir_path)
