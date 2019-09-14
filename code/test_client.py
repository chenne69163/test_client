import time
import tkinter
import tkinter.messagebox
from tkinter.scrolledtext import *
from threading import Thread
import MySQLdb
import sys

def main():

    class ApiTest(Thread):

        def run(self):
            time.sleep(5)
            tkinter.messagebox.showinfo('提示', '测试完成!')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)
    
    class MySQLClient(Thread):

        def run(self):

            def back():
                top2.destroy()
                #top1.update()
                #top1.deiconify()

            def SQL_requests():

                def example():
                    tkinter.messagebox.showinfo('提示',
                '查询: select * from 表 where...\n\
                删除一行: DELETE FROM 表 where 条件\n\
                删除一列：ALTER TABLE 表 DROP COLUMN 列名称\n\
                增加: INSERT INTO 表(列名1，2...) VALUES(值1，2...)\n\
                插入列: alter table 表名称 add 列名称 数据类型 not null primary key first\n\
                修改列名：alter table test change column 列名 新列名 类型\n\
                修改列类型：alter table test modify 列名 新类型\n\
                更新数据: UPDATE 表名称 SET 列1=新值1,列2=新值2...where...and...')

                def delete_():
                    sql_.delete(1.0,'end')

                def disconect():
                    conn.close() #断开数据库连接

                def send():
                    sql = str(sql_.get(1.0,'end'))
                    c.execute(sql)
                    list_res = []
                    if sql.find('select') == 0:
                        for i in range(c.rowcount):  #rowcount自动计数全部行数
                            row = c.fetchone()
                            list_res.append(row)
                        sql_.insert(tkinter.END,'结果：'+'\n')                        
                        sql_.insert(tkinter.END, list_res)      
                    conn.commit()  #对数据库发生修改，必须加commit
                    #conn.close()  #必须有关闭语句      

                top2.withdraw()
                _host = Entry1.get()
                _user = Entry2.get()
                _password = Entry3.get()
                _db = Entry4.get()
                _charset = Entry5.get()
                _port = int(Entry6.get())

                conn = MySQLdb.connect(
                        host = _host,
                        user = _user,
                        passwd = _password,
                        db = _db,
                        charset = _charset,
                        port = _port
                        )
                
                c = conn.cursor()
                tkinter.messagebox.showinfo('成功','数据库{}已连接'.format(_db))

                top3 = tkinter.Tk()
                top3.title('数据库操作')
                top3.geometry()
                top3.wm_attributes('-topmost', 1)

                tkinter.Label(top3,text='SQL语句(请小写)').pack(side='top',fill='x') 
                tkinter.Button(top3,text='常用命令',command=example).pack(side='top',anchor='center')
                panel1 = tkinter.Frame(top3)                  
                sql_scroll = tkinter.Scrollbar(panel1)
                sql_scroll.pack(side="right", fill="y",expand=True)                   
                sql_ = tkinter.Text(panel1,width=50,height=40,yscrollcommand=sql_scroll.set)
                sql_.pack(side='top')
                sql_scroll.config(command=sql_.yview)
                panel1.pack(side='top',expand=True)
               
                panel2 = tkinter.Frame(top3)
                b_del = tkinter.Button(panel2,text='清空',command=delete_)
                b_del.pack(side='left')
                b_quit = tkinter.Button(panel2,text='退出',command=quit)
                b_quit.pack(side='right')
                b_send = tkinter.Button(panel2,text='执行',command=send)
                b_send.pack(side='left')
                b_dc = tkinter.Button(panel2,text='断开连接',command=disconect)
                b_dc.pack(side='right')
                panel2.pack(side='bottom',fill='both',expand=True)

                top3.mainloop()
                
            #top1.withdraw()    
            top2 = tkinter.Tk()
            top2.title('连接数据库')
            top2.geometry()
            top2.wm_attributes('-topmost', 1)
            top2.resizable(width=False,height=False)

            panel1 = tkinter.Frame(top2)
            Label1 = tkinter.Label(panel1, text='host:         ')
            Label1.pack(side='left')
            Entry1 = tkinter.Entry(panel1)
            Entry1.pack(side='left',fill='x', expand=True)
            panel1.pack(side='top',fill='both', pady='0',expand=True)  

            panel2 = tkinter.Frame(top2)
            Label2 = tkinter.Label(panel2, text='user:         ')
            Label2.pack(side='left')
            Entry2 = tkinter.Entry(panel2)
            Entry2.pack(side='left',fill='x', expand=True)
            panel2.pack(side='top',fill='both', expand=True)  

            panel3 = tkinter.Frame(top2)
            Label3 = tkinter.Label(panel3, text='password: ')
            Label3.pack(side='left')
            Entry3 = tkinter.Entry(panel3,show='*')
            Entry3.pack(side='left',fill='x', expand=True)
            panel3.pack(side='top',fill='both', expand=True)  

            panel4 = tkinter.Frame(top2)
            Label4 = tkinter.Label(panel4, text='dtabase:   ')
            Label4.pack(side='left')
            Entry4 = tkinter.Entry(panel4)
            Entry4.pack(side='left',fill='x', expand=True)
            panel4.pack(side='top',fill='both', expand=True)  

            panel5 = tkinter.Frame(top2)
            Label5 = tkinter.Label(panel5, text='charset:    ')
            Label5.pack(side='left')
            Entry5 = tkinter.Entry(panel5)
            Entry5.pack(side='left',fill='x', expand=True)
            panel5.pack(side='top',fill='both', expand=True) 

            panel6 = tkinter.Frame(top2)
            Label6 = tkinter.Label(panel6, text='port:        ')
            Label6.pack(side='left')
            Entry6 = tkinter.Entry(panel6)
            Entry6.pack(side='left',fill='x', expand=True)
            panel6.pack(side='top',fill='both', expand=True) 

            panel7 = tkinter.Frame(top2)
            button7 = tkinter.Button(panel7, text='连接', command=SQL_requests)
            button7.pack(side='left')
            button7 = tkinter.Button(panel7, text='返回', command=back)
            button7.pack(side='right')
            panel7.pack(side='bottom',fill='x', expand=True)

            top2.mainloop()

    def api_test():
        button1.config(state = tkinter.DISABLED)
        ApiTest(daemon=True).start()

    def mysql_client():
        MySQLClient(daemon=True).start()

    def show_about():
        tkinter.messagebox.showinfo('关于', '作者：陈能 时间：2019.09.11起')

    top1 = tkinter.Tk()
    top1.title('功能选择')
    top1.geometry('400x200')
    top1.wm_attributes('-topmost', 1)

    panel1 = tkinter.Frame(top1)
    button1 = tkinter.Button(panel1, text='接口测试', command=api_test)
    button1.pack(side='left',fill='x', expand=True)
    button2 = tkinter.Button(panel1, text='退出', command=quit)
    button2.pack(side='right',fill='x', expand=True)
    button3 = tkinter.Button(panel1, text='作者', command=show_about)
    button3.pack(side='right',fill='x', expand=True)
    button4 = tkinter.Button(panel1, text='数据库', command=mysql_client)
    button4.pack(side='left',fill='x', expand=True)
    panel1.pack(side='bottom',fill='x', expand=True)

    top1.mainloop()

if __name__ == '__main__':
    main()