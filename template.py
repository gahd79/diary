from datetime import date,datetime
import os
import re


class Diary:
    day = date.today()
    year = str(day)[:4]
    month = str(day)[5:7]
    time = datetime.now()
    current_dir  = os.getcwd()


    def mkfile(self):
        """
        创建年份和月份的目录结构
        
        参数:
            self: 类实例，包含year和month属性
            
        返回值:
            无返回值
            
        功能说明:
            1. 在当前目录下创建以年份命名的文件夹
            2. 进入该年份文件夹
            3. 在年份文件夹内创建以月份命名的子文件夹
            4. 如果文件夹已存在则忽略错误
        """
        try:
            # 创建年份目录并进入，然后创建月份目录
            os.mkdir(f'{self.year}')
            os.chdir(f'./{self.year}')
            os.mkdir(f'{self.month}')
        except FileExistsError:
            # 目录已存在时忽略错误，继续执行
            pass

    def template(self,path = f'./{year}/{month}/{day}.md'):
        """
        创建模板文件并写入初始内容
        
        参数:
            path (str): 文件路径，默认为当前日期的markdown文件路径
            
        返回值:
            无
        """
        # 切换到当前目录
        os.chdir(self.current_dir)
        # 打开文件并追加写入模板内容
        f = open(path,'a+',encoding='utf-8')
        f.seek(0)  
        if(f.read()==''):
            f.write(f'### {self.day}')
        else:
            pass
        f.close()


    def readfile(self):
        """
        递归读取当前目录下的年/月/日结构文件，并按层级合并内容到对应的年份和月份文件中
        
        该函数假设目录结构为：年份目录/月份目录/日期文件，其中：
        - 年份目录名由1-4位数字组成
        - 月份目录名由1-4位数字组成  
        - 日期文件名为yyyy-mm-dd.md格式
        
        函数会：
        1. 遍历当前目录找到所有年份目录
        2. 对每个年份目录，创建对应年份的markdown文件
        3. 进入年份目录，遍历所有月份目录
        4. 对每个月份目录，创建对应年月的markdown文件
        5. 进入月份目录，读取所有日期文件并合并到月份文件中
        6. 将月份文件内容合并到年份文件中
        
        参数:
            self: 类实例引用
            
        返回值:
            无返回值
        """
        yearlist = []
        monthlist = []
        daylist = []
        
        # 遍历当前目录，找出所有符合年份命名规则的目录
        for i in os.listdir():
            if re.match('^\d{1,4}$',i,0):
                yearlist.append(i)
        
        # 处理每个年份目录
        for y in yearlist:
            os.chdir(f'./{y}')
            yearf = open(f'./{y}.md','w',encoding='utf-8')
            # 加入年份标题
            yearf.write(f'# {self.year}\n')
            
            # 遍历年份目录下的所有月份目录
            for j in os.listdir():
                if re.match('^\d{1,4}$',j,0):
                    monthlist.append(j)
            
            # 处理每个月份目录
            for m in monthlist:
                os.chdir(f'./{m}')
                monthf = open(f'./{y}-{m}.md','w',encoding='utf-8')
                # 加入月份标题
                monthf.write(f'## {self.year}-{self.month}\n')
                
                # 遍历月份目录下的所有日期文件
                for k in os.listdir():
                    if re.match('^\d{4}-\d{2}-\d{2}.md$',k,0):
                        daylist.append(k)
                
                # 将所有日期文件内容写入月份文件
                for d in daylist:
                    dayf = open(d,'r',encoding='utf-8')
                    monthf.write(dayf.read())
                    dayf.close()
                
                monthf.close()
                
                # 将月份文件内容追加到年份文件
                monthf = open(f'./{y}-{m}.md','r',encoding='utf-8')
                yearf.write(monthf.read())
                monthf.close()
                os.chdir('../')
            
            yearf.close()
            os.chdir('../')

if __name__ == '__main__':
    t = Diary()
    print('start')
    t.mkfile()
    t.template()
    t.readfile()
    print('end')