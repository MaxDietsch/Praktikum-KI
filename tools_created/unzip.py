import zipfile

def unzip_file(zip_filepath, dest_folder, password=None):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        if password:
            zip_ref.setpassword(password.encode())
        zip_ref.extractall(dest_folder)

# Usage:
unzip_file('../../SUN/sundatabase_negative_part1.zip', './download_unzip/SUN/negative', 'pS2oU0lN2yP0')
