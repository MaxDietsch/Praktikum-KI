import zipfile

def unzip_file(zip_filepath, dest_folder, password=None):
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        if password:
            zip_ref.setpassword(password.encode())
        zip_ref.extractall(dest_folder)

# Usage:
print("part 1")
unzip_file('../../SUN/sundatabase_negative_part1.zip', './download_unzip/SUN/negative', 'pS2oU0lN2yP0')

print("part 2")
unzip_file('../../SUN/sundatabase_negative_part2.zip', './download_unzip/SUN/negative', 'pS2oU0lN2yP0')

print("part 3")
unzip_file('../../SUN/sundatabase_negative_part3.zip', './download_unzip/SUN/negative', 'pS2oU0lN2yP0')

print("part 4")
unzip_file('../../SUN/sundatabase_negative_part4.zip', './download_unzip/SUN/negative', 'pS2oU0lN2yP0')

print("part 5")
unzip_file('../../SUN/sundatabase_positive_part1.zip', './download_unzip/SUN/positive', 'pS2oU0lN2yP0')

print("part 6")
unzip_file('../../SUN/sundatabase_positive_part2.zip', './download_unzip/SUN/positive', 'pS2oU0lN2yP0')
