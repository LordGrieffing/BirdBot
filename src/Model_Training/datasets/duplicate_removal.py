import os
import hashlib




def main():




    # Folder containing downloaded images
    image_folder = "testLibrary"

    # Dictionary to store hash -> filename mapping
    hashes = {}
    count = 0

    # Loop through all images
    for filename in os.listdir(image_folder):
        filepath = os.path.join(image_folder, filename)

        # Skip non-image files
        if not filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        # Compute file hash
        with open(filepath, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        # Check for duplicates
        if file_hash in hashes:
            print(f"🗑️ Duplicate found: {filename} (Same as {hashes[file_hash]})")
            os.remove(filepath)  # Delete duplicate
            count += count
        else:
            hashes[file_hash] = filename  # Store unique file

    print("✅ Duplicate removal complete!")
    print(f"{count} duplicates were removed")



    































if __name__ == "__main__":
    main()