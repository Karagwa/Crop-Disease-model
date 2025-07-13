import os

def clean_file_names(root_dir):
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            old_path = os.path.join(root, file)
            # Clean up whitespace and dots
            new_file = file.strip().replace("  ", " ").replace(" .", ".")
            new_path = os.path.join(root, new_file)
            if old_path != new_path:
                os.rename(old_path, new_path)
                print(f"Renamed: {old_path} → {new_path}")

# 👇 Use raw string to avoid issues with backslashes
clean_file_names(r"C:\Users\user\Crop Disease model\Dataset")
