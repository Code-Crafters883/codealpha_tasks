import os
import shutil
import time
import pandas as pd
from datetime import datetime

def organize_files(directory):
    # Create a dictionary to map file extensions to folder names
    file_types = {
        'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
        'audio': ['.mp3', '.wav', '.aac'],
        'videos': ['.mp4', '.mkv', '.flv', '.mov'],
        'archives': ['.zip', '.rar', '.tar', '.gz']
    }
    
    # Create folders if they don't exist
    for folder_name in file_types.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Organize files
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = os.path.splitext(filename)[1].lower()
            moved = False
            for folder_name, extensions in file_types.items():
                if file_extension in extensions:
                    shutil.move(file_path, os.path.join(directory, folder_name, filename))
                    moved = True
                    break
            if not moved:
                # Move to 'others' folder if the file type is not recognized
                others_folder = os.path.join(directory, 'others')
                if not os.path.exists(others_folder):
                    os.makedirs(others_folder)
                shutil.move(file_path, os.path.join(others_folder, filename))

def clean_csv(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Remove rows with missing values
    df.dropna(inplace=True)
    
    # Convert text columns to lowercase
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.lower()
    
    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)

def delete_old_files(directory, days_old):
    # Get the current time
    current_time = time.time()
    
    # Calculate the time threshold
    time_threshold = current_time - (days_old * 86400)
    
    # Iterate over files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            # Get the file's last modification time
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < time_threshold:
                print(f"Deleting {file_path}")
                os.remove(file_path)

def backup_directory(source_dir, backup_dir):
    # Create a timestamp for the backup folder
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_folder = os.path.join(backup_dir, f'backup_{timestamp}')
    
    # Create the backup folder
    os.makedirs(backup_folder)
    
    # Copy files from source to backup folder
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            relative_path = os.path.relpath(source_file, source_dir)
            backup_file = os.path.join(backup_folder, relative_path)
            os.makedirs(os.path.dirname(backup_file), exist_ok=True)
            shutil.copy2(source_file, backup_file)
    
    print(f"Backup completed: {backup_folder}")

def main():
    print("Welcome to the Task Automation Script!")
    print("Choose an option:")
    print("1. Organize Files")
    print("2. Clean CSV Data")
    print("3. Delete Old Files")
    print("4. Backup Directory")
    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        directory = input("Enter the directory to organize: ")
        organize_files(directory)
        print("File organization completed.")
    elif choice == '2':
        input_file = input("Enter the input CSV file path: ")
        output_file = input("Enter the output CSV file path: ")
        clean_csv(input_file, output_file)
        print("Data cleaning completed.")
    elif choice == '3':
        directory = input("Enter the directory to clean up: ")
        days_old = int(input("Enter the number of days old for files to delete: "))
        delete_old_files(directory, days_old)
        print("Old files deletion completed.")
    elif choice == '4':
        source_dir = input("Enter the source directory to backup: ")
        backup_dir = input("Enter the backup directory: ")
        backup_directory(source_dir, backup_dir)
        print("Backup completed.")
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
