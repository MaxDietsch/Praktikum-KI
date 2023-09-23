import os 
import random
import shutil
import tqdm

def create_split(directory, percentage):
    filename = os.path.join(directory, 'meta/train.txt')

    lines = []
    with open(filename, "r") as f:
        for line in f:
            if random.random() < percentage:
                lines.append(line.strip())
    
    train_file = os.path.join(directory, 'meta', f'train{str(percentage * 100)}%.txt')

    with open(train_file, "w") as trainfile:
        for i, line in tqdm.tqdm(enumerate(lines)):
            if i % 100 == 0:
                print(f'{i} files copied')
            file, cls = line.split()
            shutil.copy(os.path.join(directory, 'train', file), directory, f'train{str(percentage * 100)}%')
            trainfile.write(line + '\n')


if __name__ == "__main__":
    directory = "../data_dir/SUN"
    percentage = 0.5
    create_split(directory, percentage)


    



