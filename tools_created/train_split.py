import os 
import random
import shutil
import tqdm

def create_split(directory, percentage):
    filename = os.path.join(directory, 'meta/train.txt')

    if os.path.exists(directory + f'/train{str(percentage * 100)}%'):
        shutil.rmtree(directory + f'/train{str(percentage * 100)}%')
    #os.mkdir(directory + f'/train{str(percentage * 100)}%')
    os.mkdir(directory + f'/train5000')


    lines = []
    with open(filename, "r") as f:
        for line in f:
            if random.random() < percentage:
                lines.append(line.strip())
    
    #train_file = os.path.join(directory, 'meta', f'train{str(percentage * 100)}%.txt')
    train_file = os.path.join(directory, 'meta', f'train5000.txt')


    with open(train_file, "w") as trainfile:
        for i, line in tqdm.tqdm(enumerate(lines)):
            file, cls = line.split()
            #shutil.copy(os.path.join(directory, 'train', file), directory + f'/train{str(percentage * 100)}%')
            shutil.copy(os.path.join(directory, 'train', file), directory + f'/train5000')
            trainfile.write(line + '\n')


if __name__ == "__main__":
    directory = "../data_dir/SUN"
    percentage = 0.25
    create_split(directory, percentage)


    



