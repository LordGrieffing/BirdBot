import os
import random


def main():

    # Get folder paths
    imageStart = "birdsnap/data/birdImages"
    imageTrain = "birdsnapDataset/train/images"
    imageValid = "birdsnapDataset/valid/images"
    imageTest = "birdsnapDataset/test/images"

    labelStart = "birdsnap/data/yolo_annotations"
    labelTrain = "birdsnapDataset/train/labels"
    labelValid = "birdsnapDataset/valid/labels"
    labelTest = "birdsnapDataset/test/labels"

    # Loop through all the images
    for filename in os.listdir(imageStart):

        
        # Roll the dice
        randNum = random.randint(1, 100)

        # Move to train set
        if randNum <= 70:
            # Move the image 
            oldName = os.path.join(imageStart, filename)
            newName = os.path.join(imageTrain, filename)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")
            
            # Move the label
            labelname = filename.removesuffix(".jpg") + ".txt"
            oldName = os.path.join(labelStart, labelname)
            newName = os.path.join(labelTrain, labelname)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")

        # Move to validation set
        elif randNum > 70 and randNum < 85:
            # Move the image 
            oldName = os.path.join(imageStart, filename)
            newName = os.path.join(imageValid, filename)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")
            
            # Move the label
            labelname = filename.removesuffix(".jpg") + ".txt"
            oldName = os.path.join(labelStart, labelname)
            newName = os.path.join(labelValid, labelname)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")

        # Move to test set
        else:
            # Move the image 
            oldName = os.path.join(imageStart, filename)
            newName = os.path.join(imageTest, filename)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")
            
            # Move the label
            labelname = filename.removesuffix(".jpg") + ".txt"
            oldName = os.path.join(labelStart, labelname)
            newName = os.path.join(labelTest, labelname)
            os.rename(oldName, newName)
            # Print update
            print(f"Image {oldName} is now {newName}")




if __name__ == "__main__":
    main()