import zipfile

def unzip_file(zip_filepath, dest_folder):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)

# Usage:
unzip_file('../../SUN/sundatabase_negative_part1.zip', './download_unzip/SUN/negative')
