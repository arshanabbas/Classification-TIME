import os
import shutil
import random

# Define paths
source_folder = "E:/TIME -Classification/Übergabe/Playground"  # Replace with the folder containing all your images
destination_folder = "E:/TIME -Classification/Übergabe/Output"   # Replace with the path to your output dataset

# Parameters
train_ratio = 0.8  # Percentage of images to be used for training (e.g., 80%)

# Create the required folder structure
train_folder = os.path.join(destination_folder, "train")
val_folder = os.path.join(destination_folder, "val")

os.makedirs(train_folder, exist_ok=True)
os.makedirs(val_folder, exist_ok=True)

# Organize data by classes
classes = [f for f in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, f))]

for cls in classes:
    class_folder = os.path.join(source_folder, cls)
    images = [f for f in os.listdir(class_folder) if os.path.isfile(os.path.join(class_folder, f)) and f.lower() != 'thumbs.db']

    # Shuffle images to ensure randomness
    random.shuffle(images)

    # Split into train and val sets
    train_count = int(len(images) * train_ratio)
    train_images = images[:train_count]
    val_images = images[train_count:]

    # Create class-specific subfolders in train and val folders
    train_class_folder = os.path.join(train_folder, cls)
    val_class_folder = os.path.join(val_folder, cls)

    os.makedirs(train_class_folder, exist_ok=True)
    os.makedirs(val_class_folder, exist_ok=True)

    # Move images to their respective folders
    for img in train_images:
        shutil.copy(os.path.join(class_folder, img), os.path.join(train_class_folder, img))

    for img in val_images:
        shutil.copy(os.path.join(class_folder, img), os.path.join(val_class_folder, img))

    print(f"Class '{cls}': {len(train_images)} training images, {len(val_images)} validation images.")

print("Dataset organized successfully!")
