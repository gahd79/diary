# main.py
from template import Diary
import tkinter as tk
from tkinter import messagebox
import os

class DiaryApp:
    """
    日记应用程序的主窗口类
    
    提供图形界面让用户选择创建当天日记模板或进行日记汇总
    """
    
    def __init__(self, root):
        """
        初始化应用程序窗口
        
        参数:
            root: tkinter根窗口对象
        """
        self.root = root
        self.root.title("日记管理程序")
        self.root.geometry("600x400")
        self.diary = Diary()
        
        self.create_widgets()
    
    def create_widgets(self):
        """
        创建界面组件
        """
        # 创建标题标签
        title_label = tk.Label(self.root, text="日记管理系统", font=("微软雅黑", 16))
        title_label.pack(pady=10)
        
        # 创建按钮框架
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        # 创建日记模板按钮
        create_btn = tk.Button(button_frame, text="创建今日日记模板", 
                              command=self.create_template, 
                              width=20, height=2)
        create_btn.pack(pady=5)
        
        # 日记汇总按钮
        compile_btn = tk.Button(button_frame, text="日记汇总", 
                               command=self.compile_diary, 
                               width=20, height=2)
        compile_btn.pack(pady=5)
        
        # 退出按钮
        exit_btn = tk.Button(button_frame, text="退出", 
                            command=self.root.quit, 
                            width=20, height=2)
        exit_btn.pack(pady=5)
    
    def create_template(self):
        """
        创建当日日记模板文件
        """
        try:
            # 使用Diary类的方法创建文件结构和模板
            self.diary.mkfile()
            
            # 构建当前日期文件路径
            year = self.diary.year
            month = self.diary.month
            day = self.diary.day
            
            path = f"./{year}/{month}/{day}.md"
            
            # 创建模板文件
            self.diary.template(path)
            
            messagebox.showinfo("成功", f"已创建日记模板文件: {path}")
        except Exception as e:
            messagebox.showerror("杂鱼~~", f"今天的日记模板已经创建过了")
    
    def compile_diary(self):
        """
        执行日记汇总操作
        """
        try:
            # 记录当前目录
            original_dir = os.getcwd()
            
            # 执行日记汇总
            self.diary.readfile()
            
            # 恢复原始目录
            os.chdir(original_dir)
            
            messagebox.showinfo("成功", "日记汇总完成")
        except Exception as e:
            messagebox.showerror("错误", f"汇总日记时出错: {str(e)}")

def main():
    """
    主函数，启动应用程序
    """
    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()