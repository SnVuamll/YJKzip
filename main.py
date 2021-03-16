from utils import *
from tkinter import *
from tkinter import filedialog, messagebox
import windnd


root = Tk()

check_lst = [IntVar() for _ in range(3)]
root_path = ""
files = []

# root config
root.title("YJK批量压缩工具")
root.wm_attributes('-topmost', 1)

# check box
lf_check = LabelFrame(root, text="打包类型")
lf_check.grid(row=0, column=0, padx=10)
check_box1 = Checkbutton(lf_check,
                         text="衬图",
                         variable=check_lst[0],
                         onvalue=1,
                         offvalue=0)
check_box1.pack(side=LEFT, fill=X, pady=5)
check_box2 = Checkbutton(lf_check,
                         text="上部结构计算结果",
                         variable=check_lst[1],
                         onvalue=1,
                         offvalue=0)
check_box2.pack(side=LEFT, fill=X, pady=5)
check_box3 = Checkbutton(lf_check,
                         text="基础计算结果",
                         variable=check_lst[2],
                         onvalue=1,
                         offvalue=0)
check_box3.pack(side=LEFT, fill=X, pady=5)

# select button frame
lf_select_btn = LabelFrame(root, text="工程选择")
lf_select_btn.grid(row=1, column=0, sticky=E+W, padx=10)


# select button
def select_flash():
    list_box.delete(0, END)
    global root_path
    root_path = filedialog.askdirectory().replace("/", "\\")
    for p in os.listdir(root_path):
        if os.path.isdir(os.path.join(root_path, p)):
            list_box.insert(END, p)
    pass


select_btn = Button(lf_select_btn, text="选择工作路径 或 直接拖拽文件夹", command=select_flash)
select_btn.pack(fill=X, padx=10, pady=5)

# list box
list_box_label = Label(lf_select_btn, text="选择需压缩的YJK工程文件夹：")
list_box_label.pack(fill=X, padx=10, pady=5)

list_box = Listbox(lf_select_btn,
                   selectmode=EXTENDED)
list_box.pack(fill=X, padx=10, pady=5)


# submit button
def submit():
    for i in list_box.curselection():
        files.append(list_box.get(i))
    paths = [os.path.join(root_path, f) for f in files]
    zip_all(paths, check_lst)
    messagebox.showinfo(message="完成")


submit_txt = StringVar()
submit_txt.set("压缩选中的YJK工程文件")
submit_btn = Button(root, textvariable=submit_txt, command=submit)
submit_btn.grid(row=2, column=0, sticky=E+W, padx=10, pady=10)


# drag and drop
def dnd(dnd_files):
    dnd_files = [item.decode('gbk') for item in dnd_files]
    list_box.delete(0, END)
    global root_path
    if dnd_files:
        root_path = os.path.dirname(dnd_files[0])
        for item in dnd_files:
            if os.path.isdir(item):
                list_box.insert(END, os.path.basename(item))
    pass


windnd.hook_dropfiles(root, func=dnd)

root.mainloop()
