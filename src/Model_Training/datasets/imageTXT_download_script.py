import pandas as pd
import os
import requests
import time

def downloadImage(img_url, image_filename, retries = 3):

    for attempt in range(retries):
        try:
            # Download the image
            response = requests.get(img_url, timeout=10)
            response.raise_for_status()  # Raise an error for bad status codes
        
            # Save the image
            with open(image_filename, "wb") as f:
                f.write(response.content)
        
            print(f"Downloaded: {image_filename}")
            return True
    
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {img_url}: {e}")
            return False
        
        except requests.exceptions.SSLError as e:
            print(f"SSL error on {img_url}, attempt {attempt+1}/{retries}: {e}")
            time.sleep(2)

        except requests.exceptions.Timeout as e:
            print(f"Timeout on {img_url}: {e}")
            time.sleep(3)

        except requests.exceptions.ConnectionError as e:
            print(f"Connection error on {img_url}: {e}")
            time.sleep(5)

    print(f"Skipping: {img_url}")
    return False

def main():
    
    # Declare output folders
    image_Output = "birdsnap/data/birdImages"
    label_Output = "birdsnap/data"

    # Declare variable for flagging if download was a success
    DLsuccess = False

    # Open image.txt as a dataframe with pandas
    imageTXT = "birdsnap/images.txt"
    imageDF = pd.read_csv(imageTXT, sep="\t", header=None)

    # Build dataframe to store label information
    label_Frame = pd.DataFrame(columns=["speices_id", "bb_x1", "bb_y1", "bb_x2", "bb_y2"])

    # Strip and organize information out of the birdsnap file
    # len(imageDF)

    # Counting variable to deal with unavaliable images
    count = 0

    for i in range(len(imageDF)):

        # Get image url
        img_url = imageDF[0][i+1]

        # Build image name
        image_filename = os.path.join(image_Output, f"image_{count}.jpg")

        # Download the image
        DLsuccess = downloadImage(img_url, image_filename)

        if DLsuccess:
            # Get label information next
            count += 1
            species_id = imageDF[3][i+1]
            bb_x1 = imageDF[4][i+1]
            bb_y1 = imageDF[5][i+1]
            bb_x2 = imageDF[6][i+1]
            bb_y2 = imageDF[7][i+1]
    
            # Input label information
            label_Frame.loc[i] = [species_id, bb_x1, bb_y1, bb_x2, bb_y2]
    

    # Saving label dataframe as a csv file
    label_name = os.path.join(label_Output, "labels.csv")
    label_Frame.to_csv(label_name, index=False)

    # Hey Jacob you thought it would be smart to save without an index
    # So if you forgot what was what:
    # Column 1: species_id
    # Column 2: bb_x1
    # Column 3: bb_y1
    # Column 4: bb_x2
    # Column 5: bb_y2

























































if __name__ == "__main__":
    main()