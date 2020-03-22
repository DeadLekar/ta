from pathlib import Path
db_paths = ['C:/Scripts/db/', 'C:/my_folder/kinoman/', 'C:/kovalenko/scripts/kinoman_project', 'C:/kovalenko/scripts/db']
driver_paths = ['C:/Users/илья/Dropbox/Ilya-Papa/father_files/drivers/chromedriver.exe', 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe', 'C:/Users/Vlad/Dropbox/Ilya-Papa/father_files/drivers/chromedriver.exe', 'C:/kovalenko/scripts/chromedriver.exe']
files = ['C:/Scripts/kinoman_files/', 'C:/my_folder/kinoman/kinoman_files/', 'C:/kovalenko/scripts/kinoman_project/kinoman_files/']


def get_right_path(paths):
    """
    detect if a path from paths exists
    :param paths: a list of paths
    :return: first existing path
    """
    for path in paths:
        my_file = Path(path)
        if my_file.exists():
            return path
