import os
import time
import win32api
import win32print

# Set the folder path to watch for auto printing
WATCH_FOLDER = r"C:\AutoPrintFolder"

def print_file(file_path):
    try:
        print(f"Printing: {file_path}")
        # Sends file to the default printer in Windows
        win32api.ShellExecute(
            0,
            "print",
            file_path,
            '/d:"%s"' % win32print.GetDefaultPrinter(),
            ".",
            0
        )
    except Exception as e:
        print(f"Error printing file: {e}")

def start_auto_print():
    print("Auto Print Software Started...")
    print(f"Monitoring folder: {WATCH_FOLDER}")
    
    already_printed = set()
    
    while True:
        if os.path.exists(WATCH_FOLDER):
            files = os.listdir(WATCH_FOLDER)
            for file_name in files:
                file_path = os.path.join(WATCH_FOLDER, file_name)
                
                # Check for files and prevent duplicate printing
                if os.path.isfile(file_path) and file_path not in already_printed:
                    print_file(file_path)
                    already_printed.add(file_path)
        
        time.sleep(5)  # Checks folder every 5 seconds

if __name__ == "__main__":
    start_auto_print()
