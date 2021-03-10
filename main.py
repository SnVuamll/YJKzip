# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
import zipfile


def _zip(base_path, zip_lst):
    # save current direction and temporarily switch the zipping path
    saved_cwd = os.path.curdir
    working_dir, target_folder = os.path.split(base_path)
    os.chdir(working_dir)

    zip_name = target_folder + ".zip"

    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file in zip_lst:
                    base = os.path.join(root, file)
                    zf.write(base,
                             os.path.relpath(base, os.path.join(base_path, '.')))
    os.chdir(saved_cwd)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    saved_list = ["file.txt", "file1.txt"]
    YJK_folder = r"C:\Users\Jun-Jie.Liang\Documents\HOME\06_mycode\YJKzip\test\demo"

    _zip(YJK_folder, saved_list)
