import pandas as pd
import os
import csv
import cv2


def main():

    # Define path variables
    label_output = "birdsnap/data/yolo_annotations"
    image_library = "birdsnap/data/birdImages"
    
    # Load label.csv as dataframe
    labelFrame = pd.read_csv("birdsnap/data/label.csv")

    # Loop over each item
    for row in labelFrame.iterrows():

        if row[0] > 18441:
            # load current image
            image_filename = os.path.join(image_library, f"image_{row[0]}.jpg")
            img = cv2.imread(image_filename, cv2.IMREAD_COLOR)

            # build name of .txt file
            label_filename = os.path.join(label_output, f"image_{row[0]}.txt")

            # get class
            speices = row[1]["speices_id"]
            
            # Find x center and y center
            box_width = row[1]["bb_x2"] - row[1]["bb_x1"]
            box_height = row[1]["bb_y2"] - row[1]["bb_y1"]


            x_center = int((row[1]["bb_x2"] + row[1]["bb_x1"])/2)
            y_center = int((row[1]["bb_y2"] + row[1]["bb_y1"])/2)

            # Get shape of image
            height, width, channels = img.shape

            # normalize all the data
            x_center = x_center / width
            y_center = y_center / height

            box_width = box_width / width
            box_height = box_height / height

            # save as .txt file
            with open(label_filename, 'w') as f:
                f.write(f"{speices} {x_center} {y_center} {box_width} {box_height}")

            print(f"{image_filename} : {speices} {x_center} {y_center} {box_width} {box_height}")
    
    
    
    








if __name__ == "__main__":


    main()