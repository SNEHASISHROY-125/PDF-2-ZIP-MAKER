# '''
# CREATE SUB DIRECTORIES BASSED ON THE LIST OF NUMERIC VALUES OF FILES
# '''


# import os
# import shutil

# def create_subdirs(source_folder, destination_folder):
#     pdf_files = [file for file in os.listdir(source_folder) if file.endswith('.pdf')]

#     if not pdf_files:
#         print("No PDF files found in the source folder.")
#         return

#     # Extract numeric parts from filenames and filter out non-numeric parts
#     numeric_parts = [int(os.path.splitext(file)[0]) for file in pdf_files if file[:-4].isdigit()]

#     if not numeric_parts:
#         print("No valid numeric parts found in PDF filenames.")
#         return

#     # Find the lowest and highest numeric values
#     lowest_value = min(numeric_parts)
#     highest_value = max(numeric_parts)

#     # Create 's_pdf' directory if it doesn't exist
#     s_pdf_directory = os.path.join(destination_folder, zip_file_dir, sub_zip_file_dir)
#     os.makedirs(s_pdf_directory, exist_ok=True)

#     # Create subdirectories with increments of 10 within the specified range
#     for sub_dir_value in range(lowest_value, highest_value + 10, 10):
#         sub_dir_path = os.path.join(s_pdf_directory, str(sub_dir_value))
#         try:
#             os.makedirs(sub_dir_path, exist_ok=False)
#         except FileExistsError:
#             print(f"Subdirectory {sub_dir_path} already exists.")
#         print(f"Created subdirectory: {sub_dir_path}")

# # Replace these paths with your actual paths
# source_folder = r'C:\Users\Snehasish\Downloads\all-pdfs'
# destination_folder = r'C:\Users\Snehasish\Downloads'

# # Main zip file dir
# zip_file_dir = 'pdf-ZIP'
# # Sub dir contains all the pdf-s and dirs within main zip file 
# sub_zip_file_dir = 'serially_pdf'

# create_subdirs(source_folder, destination_folder)


import os

def create_subdirs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir, increment=10):
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

    # Determine the range for subdirectories with the specified increment
    range_start = (lowest_value // increment) * increment
    range_end = ((highest_value + increment) // increment) * increment

    # Create 's_pdf' directory if it doesn't exist
    s_pdf_directory = os.path.join(destination_folder, zip_file_dir, sub_zip_file_dir)
    os.makedirs(s_pdf_directory, exist_ok=True)

    # Create subdirectories with the specified increment within the specified range
    for sub_dir_start in range(range_start, range_end, increment):
        sub_dir_end = sub_dir_start + increment
        sub_dir_name = f"{sub_dir_start} - {sub_dir_end}"
        sub_dir_path = os.path.join(s_pdf_directory, sub_dir_name)
        try:
            os.makedirs(sub_dir_path, exist_ok=True)
        except FileExistsError:
            print(f"Subdirectory {sub_dir_path} already exists.")
        print(f"Created subdirectory: {sub_dir_path}")


# Replace these paths with your actual paths
source_folder = r'C:\Users\Snehasish\Downloads\all-pdfs'
destination_folder = r'C:\Users\Snehasish\Downloads'

# Main zip file dir
zip_file_dir = 'pdf-ZIP'
# Sub dir contains all the pdf-s and dirs within the main zip file
sub_zip_file_dir = 'serially_pdf'

# create_subdirs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir)

# create_subdirs(source_folder, destination_folder, zip_file_dir, sub_zip_file_dir, increment=100)
