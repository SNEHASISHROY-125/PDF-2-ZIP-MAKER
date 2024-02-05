'''
PDF MANAGER 2 ZIP FILE
'''

import os
import shutil

def copy_pdfs_in_range(source_folder, destination_folder, start_num, end_num):
    pdf_files = [file for file in os.listdir(source_folder) if file.endswith('.pdf')]

    for pdf_file in pdf_files:
        file_num_str, extension = os.path.splitext(pdf_file)
        try:
            file_num = int(file_num_str)
            if start_num <= file_num <= end_num:
                source_path = os.path.join(source_folder, pdf_file)
                destination_path = os.path.join(destination_folder, pdf_file)
                shutil.copyfile(source_path, destination_path)
                print(f"Copied {pdf_file} to {destination_folder}")
        except ValueError:
            print(f"Skipped {pdf_file} as it does not have a valid numeric part")

# Replace these paths with your actual paths
source_folder = r'C:\Users\Snehasish\Downloads\all-pdfs'     #
destination_folder = r'C:\Users\Snehasish\Downloads\pdf-move'    #
start_num = 8769
end_num = 8771

copy_pdfs_in_range(source_folder, destination_folder, start_num, end_num)
