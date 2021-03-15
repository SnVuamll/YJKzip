import os
import zipfile


def _zip(base_path, zip_lst):
    # save current direction and temporarily switch the zipping path
    saved_cwd = os.path.curdir
    working_dir, target_folder = os.path.split(base_path)
    os.chdir(working_dir)

    zip_name = target_folder + ".zip"

    # zip files
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(base_path):
            for file in files:
                if file in zip_lst:
                    base = os.path.join(root, file)
                    zf.write(base, os.path.relpath(base, os.path.join(base_path, '.')))
    os.chdir(saved_cwd)


def _get_zip_lst(base_path, check_lst):
    # model files without “衬图”
    zip_lst = ["dsnctrl.ini",
               "dsnjc.data",
               "fea.dat",
               # "jccad.pre",
               "Jccad_0",
               "Jccad_0.dat",
               # "jcdlg.pre",
               "jcsr.jc",
               "KF.dat",
               "KF.dat.md5",
               "SPara.par",
               "spretobase.dat",
               "spretobase2.dat",
               "yjkTransLoad.sav"
               ]
    prj_name = ""
    for f in os.listdir(base_path):
        if os.path.isfile(os.path.join(base_path, f)) and f.split('.')[-1] in "pre-rel-yjb-yjk-yjc":
            if f.split('.')[-1] == "yjk":
                prj_name = f.split('.')[0]  # 获取工程名称，打包计算结果需要
            zip_lst.append(f)

    # 勾选“衬图”选项
    if check_lst[0].get() == 1:
        chentu_path = os.path.join(base_path, "衬图")
        if os.path.exists(chentu_path):
            for f in os.listdir(chentu_path):
                zip_lst.append(f)

    # 勾选“上部结构计算结果”选项
    if check_lst[1].get() == 1:
        zip_lst.extend([
            # root path
            "fea.dat-RESULT.DAT",
            "spretoslab.dat",
            # temp data
            "dsncompj.data",
            "dsnpro.data",
            "ghcomrel.dat",
            "fea-debug.log"])

        for f in os.listdir(base_path):
            if os.path.isfile(os.path.join(base_path, f)) and prj_name in f:
                print(111)
                zip_lst.append(f)

        # design data
        design_data_path = os.path.join(base_path, "设计结果")
        if os.path.exists(design_data_path):
            print(1)
            for f in os.listdir(design_data_path):
                zip_lst.append(f)

        # temp data
        yjkcombine_path = os.path.join(base_path, "中间数据", "Yjkcombine")
        yjkfea_path = os.path.join(base_path, "中间数据", "Yjkfea")
        if os.path.exists(yjkcombine_path):
            for f in os.listdir(yjkcombine_path):
                if r".RESULT.DB" in f:
                    zip_lst.append(f)
        if os.path.exists(yjkfea_path):
            for f in os.listdir(yjkfea_path):
                if r".RESULT.DB" in f:
                    zip_lst.append(f)


    # 勾选“基础计算结果”选项
    if check_lst[2].get() == 1:
        zip_lst.append("Jccad_0.mdb")
        jc_path = os.path.join(base_path, "基础计算及结果输出")
        if os.path.exists(jc_path):
            for f in os.listdir(jc_path):
                zip_lst.append(f)

    return zip_lst


def zip_all(path_lst, check_lst):
    for base_name in path_lst:
        zip_lst = _get_zip_lst(base_name, check_lst)
        _zip(base_name, zip_lst)