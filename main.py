import os
from utils import *
from tkinter import *
from tkinter import filedialog, messagebox


class YJKzip_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

        self.check_lst = [IntVar() for _ in range(3)]
        self.root_path = ""
        self.files = []

    def set_init_window(self):
        self.init_window_name.title("YJK批量压缩工具")
        # self.init_window_name.geometry('500x800+50+50')

        # check box
        self.check_label = Label(self.init_window_name, text="压缩类型")
        self.check_label.pack(fill=X)
        self.check_box1 = Checkbutton(self.init_window_name,
                                   text="衬图",
                                   variable=self.check_lst[0],
                                   onvalue=1,
                                   offvalue=0)
        self.check_box1.pack(fill=X)
        self.check_box2 = Checkbutton(self.init_window_name,
                                   text="上部结构计算结果",
                                   variable=self.check_lst[1],
                                   onvalue=1,
                                   offvalue=0)
        self.check_box2.pack(fill=X)
        self.check_box3 = Checkbutton(self.init_window_name,
                                   text="基础计算结果",
                                   variable=self.check_lst[2],
                                   onvalue=1,
                                   offvalue=0)
        self.check_box3.pack(fill=X)

        # buttons
        self.select_btn = Button(self.init_window_name, text="选择工作路径", command=self.select_flash)
        self.select_btn.pack(fill=X)

        # list box
        self.list_box_label = Label(self.init_window_name, text="选择需压缩的YJK工程文件夹：")
        self.list_box_label.pack(fill=X)
        self.list_box = Listbox(self.init_window_name,
                                selectmode=EXTENDED)
        self.list_box.pack(fill=X)

        # buttons
        self.submit_btn = Button(self.init_window_name, text="压缩选中的YJK工程文件", command=self.submit)
        self.submit_btn.pack(fill=X)

    def select_flash(self):
        self.list_box.delete(0, END)
        self.root_path = filedialog.askdirectory().replace("/", "\\")
        for p in os.listdir(self.root_path):
            if os.path.isdir(os.path.join(self.root_path, p)):
                self.list_box.insert(END, p)
        # self.list_box.update()
        # self.list_box.pack()
        pass

    def submit(self):
        for i in self.list_box.curselection():
            self.files.append(self.list_box.get(i))
        paths = [os.path.join(self.root_path, f) for f in self.files]
        zip_all(paths, self.check_lst)
        messagebox.showinfo(message="完成")

init_window = Tk()
new_window = YJKzip_GUI(init_window)
new_window.set_init_window()
init_window.mainloop()