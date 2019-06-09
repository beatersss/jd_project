import tkinter as tk
import random
import codecs
import os
from dataprocess import comments_dict,info_dict,info_detail_dict,simliar,price_dict
from dataprocess import comments
# 弹窗
class PopupDialog(tk.Toplevel):
  def __init__(self, parent):
    super().__init__()
    self.title('请选择手机品牌')
    self.geometry('+750+100')
    self.parent = parent # 显式地保留父窗口

    # 第一行（两列）
    row1 = tk.Frame(self)
    row1.pack(fill="x")
    self.var_list = []
    row_i = 0
    column_i = 0
    total_result = list(info_dict.keys())
    for i,name in enumerate(total_result[:50]):
        self.var_list.append(tk.Button(row1, text="%s"%name, command=lambda x=i:self.set_mod(val=x)))

        if ((i)%3 == 0)&(i>0):
            row_i += 1
        if column_i >= 3:
            column_i = 0

        # print(row_i,column_i)
        self.var_list[-1].grid(row=row_i,column = column_i)
        column_i += 1


  def set_mod(self,val=0):
    # print(val)
    self.parent.mod = list(info_dict.keys())[val]
    print(self.parent.mod)
    self.parent.mod_v = self.parent.mod
    self.parent.flag = 1
    self.destroy()  # 销毁窗口

# 主界面
class PloyCompute(tk.Tk):
    def __init__(self):
        super().__init__()
        # self.pack() # 若继承 tk.Frame，此句必须有！！！
        # 八进制
        self.mod_v = "未选择"
        self.phoneId = ""
        self.mod_l_s = ""
        self.strList1 = []
        self.strList2 = []
        self.flag = 0
        self.text = ""
        # self.mod_l_s = ""
        self.setupUI()

    def setupUI(self):
        # 第一行（两列）
        self.title('手机信息查询系统')
        # self.geometry('550x400')

        row1 = tk.Frame(self)
        row1.pack(fill="x")
        tk.Label(row1, text='搜索的手机型号：', width=25).grid(row=0,column=1)
        self.entry1 = tk.Entry(row1,show=None, width=20)
        self.entry1.grid(row=0,column=2)

        tk.Label(row1, text="", width=5).grid(row=0, column=5)
        tk.Button(row1, text="搜索", command=self.hitSeach).grid(row=0, column=6)

        tk.Label(row1, text="", width=5).grid(row=0, column=5)
        tk.Button(row1, text="选择", command=self.setup_config).grid(row=0, column=8)

        tk.Label(row1, text="", width=5).grid(row=0, column=5)
        tk.Button(row1, text="选择后搜索", command=self.hitSeach).grid(row=0, column=9)
        # #
        row2 = tk.Frame(self)
        row2.pack(fill="x")
        tk.Label(row2, text='您搜索的手机型号为:', width=25).grid(row=0, column=0)
        self.mod_l_s= tk.StringVar()
        self.mod_l = tk.Label(row2, textvariable=self.mod_l_s, width=30)
        self.mod_l.grid(row=0, column=1)

        # 用来显示详细信息
        row3 = tk.Frame(self)
        row3.pack(fill="x")
        for i in range(10):
            self.strList1.append(tk.StringVar())
            self.strList2.append(tk.Label(row3, textvariable=self.strList1[i], width=30).grid(row=i, column=1))

        # 用来显示评论信息
        scroll = tk.Scrollbar()
        self.text = tk.Text()
        # 将滚动条填充
        scroll.pack(side=tk.RIGHT, fill=tk.Y)  # side是滚动条放置的位置，上下左右。fill是将滚动条沿着y轴填充
        self.text.pack(side=tk.LEFT, fill=tk.Y)  # 将文本框填充进wuya窗口的左侧，
        # 将滚动条与文本框关联
        scroll.config(command=self.text.yview)  # 将文本框关联到滚动条上，滚动条滑动，文本框跟随滑动
        self.text.config(yscrollcommand=scroll.set)  # 将滚动条关联到文本框
        # 设置文本框内容
        txt = '空'
        # 将文本内容插入文本框
        for i in range(10):
            self.text.insert('insert', txt)
        row4 = tk.Frame(self)
        row4.pack(fill="x")
        tk.Button(row4, text="获取评论", command=self.getComments).grid(row=0, column=6)

    def getMaxSim(self,v1):
        result_sim = 0
        phone_id = ""
        phone_name = ""
        for k,v in info_dict.items():
            sim = simliar(v1,k)
            if sim > result_sim:
                result_sim = sim
                phone_id = v
                phone_name = k
        self.phoneId = phone_id
        self.mod_v = phone_name
        self.flag = 1
        return phone_name

    def hitSeach(self):
        value_1 =self.entry1.get()
        if self.flag == 1:
            value_1 = self.mod_v
        phone_name = self.getMaxSim(v1=value_1)
        print(phone_name)
        self.mod_l_s.set(str(phone_name))
        self.strList1[0].set(str("价格：%s"%price_dict[self.phoneId]))
        for i,res in enumerate(info_detail_dict[self.phoneId][1:]):
            if i >8:
                break
            self.strList1[i+1].set(str(res))
        self.flag = 0

    def getComments(self):
        self.text.delete("1.0", 'end')

        try:
            comment_dict = comments("%s.csv" % self.phoneId)[self.phoneId]
            for score, comment in zip(comment_dict['score'], comment_dict['content']):
                self.text.insert("insert", "    评论分数：%s颗星；评论内容为：%s" % (score, comment))
                self.text.insert("insert", "\n--------------------------------------------\n")
        except:
            self.text.insert("insert","暂时没找到评论数据！")


    def setup_config(self):
        pw = PopupDialog(self)
        self.wait_window(pw) # 这一句很重要！！！


if __name__ == '__main__':
  app = PloyCompute()
  app.mainloop()