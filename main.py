# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import os
from shutil import copyfile, rmtree, make_archive


def _walk(root_path, saved_lst):
    ret = []
    for cur_dir, sub_dirs, files in os.walk(root_path):
        for f in files:
            if f in saved_lst:
                ret.append([cur_dir, f])
    return ret


def _zip(target_folder, src_lst):
    # create temp folder
    copy_path = target_folder + "_tmp"
    if os.path.isdir(copy_path):
        return
    os.mkdir(copy_path)

    # copy files to temp folder
    for scr_dir, scr_file in src_lst:
        from_path = os.path.join(scr_dir, scr_file)
        to_path = from_path.replace(target_folder, copy_path)

        # the destination path exists?
        is_path = os.path.dirname(to_path)
        if not os.path.isdir(is_path):
            # thanks to `os.walk()` which walks from top, here only need to create subdir
            os.mkdir(is_path)

        copyfile(from_path, to_path)

    # zip files
    make_archive(copy_path, "zip", root_dir=copy_path)

    # clean temp files
    rmtree(copy_path)
    pass


def yjk_zip(target, saved_lst):
    paths = _walk(target, saved_lst)
    _zip(target, paths)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    saved_list = ["file.txt", "file1.txt"]
    YJK_folder = r"C:\Users\Jun-Jie.Liang\Documents\HOME\06_mycode\YJKzip\test\demo"

    yjk_zip(YJK_folder, saved_list)
