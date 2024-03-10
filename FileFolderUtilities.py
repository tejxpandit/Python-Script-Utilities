import shutil

# Target Folder Path
folder_path = "/path/folder"

try:
  shutil.rmtree(folder_path)
  print(f"Folder '{folder_path}' and its contents have been deleted.")
