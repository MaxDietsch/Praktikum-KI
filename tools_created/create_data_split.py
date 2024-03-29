import os
import shutil

classes = {
    "positive": " 0", 
    "negative": " 1"
}

meta_dir = "../data_dir/SUN/meta"
train_dir = "../data_dir/SUN/train"
val_dir = "../data_dir/SUN/val"
test_dir = "../data_dir/SUN/test"
train_percentage = 40
val_percentage = 10
test_percentage = 50

if os.path.exists(meta_dir):
    shutil.rmtree(meta_dir)
os.mkdir(meta_dir)

if os.path.exists(train_dir):
    shutil.rmtree(train_dir)
os.mkdir(train_dir)

if os.path.exists(val_dir):
    shutil.rmtree(val_dir)
os.mkdir(val_dir)

if os.path.exists(test_dir):
    shutil.rmtree(test_dir)
os.mkdir(test_dir)


train_files, val_files, test_files = [], [], []

dir = "../data_dir/SUN"
dirs = os.listdir(dir)
for directory in dirs:
    if directory == "train" or directory == "val" or directory == "test" or directory == "meta":
        continue
    path = os.path.join(dir, directory)
    files = os.listdir(path)
    i = 0
    for file in files:
        if i % 1000 == 0:
            print(i)
        if i <= len(files) * train_percentage / 100:
            i += 1
            train_files.append(file + classes[directory])
            shutil.move(os.path.join(dir, directory, file), os.path.join(train_dir, file))
            continue
        if i <= len(files) * (train_percentage + val_percentage) / 100:
            i += 1
            val_files.append(file + classes[directory])
            shutil.move(os.path.join(dir, directory, file), os.path.join(val_dir, file))
            continue
        if i <= len(files) * (train_percentage + val_percentage + test_percentage) / 100:
            i += 1
            test_files.append(file + classes[directory])
            shutil.move(os.path.join(dir, directory, file), os.path.join(test_dir, file))
            continue
    #os.rmdir(path)

train_file = meta_dir + "/train.txt"
val_file = meta_dir + "/val.txt"
test_file = meta_dir + "/test.txt"

with open(train_file, "w") as file:
    for line in train_files:
        file.write(line + '\n')

with open(val_file, "w") as file:
    for line in val_files:
        file.write(line + '\n')

with open(test_file, "w") as file:
    for line in test_files:
        file.write(line + '\n')

        