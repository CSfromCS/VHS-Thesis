from ultralytics import YOLO
import os
import random
from math import floor

def train_model(train_set_path: str):
    model = YOLO()
    model.train(data=train_set_path, epochs=50, imgsz=[320,240])

    return model

def validate_model(model):
    metrics = model.val()  
    metrics.box.map    
    metrics.box.map50  
    metrics.box.map75  
    metrics.box.maps  

def test_model(model: YOLO, image_link):
    print("Wow!")

def split_dataset():
    files = os.listdir('Thermal Ejeep Images/images')
    file_count = len(files)
    train_count = floor(file_count * 0.15)
    val_count = floor(file_count * 0.15)

    train_list = random.sample(files, train_count)
    new_file_list = [file for file in files if file not in train_list]

    val_list = random.sample(new_file_list, val_count)

    train_list.sort()
    val_list.sort()

    print("=========== Training List:")
    print(*train_list, sep="\n")
    print("\n")
    print("=========== Validation List")
    print(*val_list, sep="\n")
    

if __name__ == '__main__':
    model = train_model('/Users/francovelasco/Desktop/College/Thesis/VHS-Thesis/Thermal Camera Detection/Thermal Ejeep Images/data.yaml')
    validate_model(model)
    #split_dataset()