import os
import shutil
import logging

# Configure logging to a file
logging.basicConfig(filename='file_moving.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def start(parent_dir):
    dirx = os.listdir(os.path.join(parent_dir))
    for path in dirx:
        try:
            for px in os.listdir(os.path.join(parent_dir, path)):
                print(os.path.join(parent_dir, path, px))
                move_files_and_delete_folder(os.path.join(parent_dir, path, px))
        except NotADirectoryError:
            continue

def move_files_and_delete_folder(parent_dir):
    for root, dirs, files in os.walk(parent_dir):
        for file in files:
            if root != parent_dir:  # Exclude moving files directly in the parent directory
                src_path = os.path.join(root, file)
                dest_path = os.path.join(parent_dir, file)

                try:
                    shutil.move(src_path, dest_path)
                    logging.info(f'Moved: {src_path} to {dest_path}')
                except FileNotFoundError:
                    logging.warning(f'File not found: {src_path}')

    for root, dirs, files in os.walk(parent_dir, topdown=False):
        for dir_name in dirs:
            target_dir = os.path.join(root, dir_name)
            try:
                os.rmdir(target_dir)
                logging.info(f'Removed empty folder: {target_dir}')
            except OSError as e:
                logging.warning(f'Error removing folder: {target_dir} - {e}')

if __name__ == "__main__":
    parent_directory = '.'  # Specify the parent directory path here
    start(parent_directory)

    print("File moving and folder deletion completed. Check the log file for details.")
