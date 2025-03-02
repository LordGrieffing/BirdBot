import os
import pandas as pd
import csv


def main():
    pass


    # Write a new label csv
    image_Folder = "birdsnap/data/birdImages"
    image_Output = "birdsnap/data/birdImagesReindex"
    label_Output = "birdsnap/data/label_reindex.csv"

    label_headers = ["filename", "speices_id", "bb_x1", "bb_y1", "bb_x2", "bb_y2"]

    if not os.path.exists(label_Output):
        with open(label_Output, mode="w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(label_headers)

    # Read old label csv
    labelFrame = pd.read_csv("birdsnap/data/label.csv")        

    # Loop through each file in folder
    count = 0
    for filename in os.listdir(image_Folder):

        # find its corresponding label
        label = labelFrame[labelFrame['filename'].str.contains(filename, na=False)]

        # Rename file
        oldName = os.path.join(image_Folder, filename)
        newName = os.path.join(image_Output, f"image_{count}.jpg")
        os.rename(oldName, newName)

        # Print update
        print(f"Image {oldName} is now {newName}")

        # Rename label
        speices_id = label.iloc[0]['speices_id']
        bb_x1 = label.iloc[0]['bb_x1']
        bb_y1 = label.iloc[0]['bb_y1']
        bb_x2 = label.iloc[0]['bb_x2']
        bb_y2 = label.iloc[0]['bb_y2']

        # Add new label
        with open(label_Output, mode="a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([newName, speices_id, bb_x1, bb_y1, bb_x2, bb_y2])
        
        # Update count
        count += 1











































if __name__ == "__main__":
    main()