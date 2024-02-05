'''
move pdfs
'''

# 01. creates subdirs at (r'C:\Users\Snehasish\Downloads\pdf-ZIP\serially_pdf') bassed on the range of pdfs present in the source folder (r'C:\Users\Snehasish\Downloads\all-pdfs')
    # - 01.1. creates subdirs with increments of 10 within the specified range  8770 - 8780
# 02. moves pdfs to the appropriate subdirs

#  uses create_sub_dirs.py to create the sub-dirs

import os
import shutil

def move_pdfs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir):
    # Import the logic for creating subdirectories from create_sub_dirs.py
    from create_sub_dirs import create_subdirs

    # Create subdirectories
    create_subdirs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir,increment=100)

    # Get the list of PDF files
    pdf_files = [file for file in os.listdir(source_folder) if file.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the source folder.")
        return

    # Extract numeric parts from filenames and filter out non-numeric parts
    numeric_parts = [int(os.path.splitext(file)[0]) for file in pdf_files if file[:-4].isdigit()]

    if not numeric_parts:
        print("No valid numeric parts found in PDF filenames.")
        return

    # Find the lowest and highest numeric values
    lowest_value = min(numeric_parts)
    highest_value = max(numeric_parts)

    # Determine the range for subdirectories
    range_start = (lowest_value // 10) * 10
    range_end = ((highest_value + 10) // 10) * 10

    # Move PDF files to the appropriate subdirectories
    for pdf_file in pdf_files:
        file_num_str, extension = os.path.splitext(pdf_file)
        try:
            file_num = int(file_num_str)
            # --deprecated
            # sub_dir_start = (file_num // 10) * 10
            # sub_dir_end = sub_dir_start + 10
            sub_dir_start = (file_num // 100) * 100
            sub_dir_end = sub_dir_start + 100

            sub_dir_name = f"{sub_dir_start} - {sub_dir_end}"
            sub_dir_path = os.path.join(destination_folder, zip_file_dir, sub_zip_file_dir, sub_dir_name)
            source_path = os.path.join(source_folder, pdf_file)
            destination_path = os.path.join(sub_dir_path, pdf_file)
            shutil.move(source_path, destination_path)
            print(f"Moved {pdf_file} to {sub_dir_path}")
        except ValueError:
            print(f"Skipped {pdf_file} as it does not have a valid numeric part")

# Replace these paths with your actual paths
source_folder = r'C:\Users\Snehasish\Downloads\all-pdfs'
destination_folder = r'C:\Users\Snehasish\Downloads'

# Main zip file dir
zip_file_dir = 'pdf-ZIP'
# Sub dir contains all the pdf-s and dirs within main zip file
sub_zip_file_dir = 'serially_pdf'

## EXEC
move_pdfs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir)
