class Student:
    def __init__(self,name,chinese,math,english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english
    def __str__(self):
        return f"姓名：{self.name} | 语文：{self.chinese} | 数学：{self.math} | 英语：{self.english} " \
               f"|总分：{self.chinese+self.math+self.english}"

    def update_score(self,chinese=None,math=None,english=None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# if __name__ == "__main__":
#     s1=Student("zhangsan",90,95,93)
#     print(s1)
#     s1.update_score(english=100)
#     print(s1)

class eduManagement:
    system_version="1.0"
    system_name="教务管理系统"
    def __init__(self):
        self.student_list = []
    def add_Student(self):
        name = input("请输入姓名：")
        for i in self.student_list:
            if i.name == name:
                print("该学生已存在")
                return
        chinese = eval(input("请输入语文成绩："))
        math = eval(input("请输入数学成绩："))
        english = eval(input("请输入英语成绩："))
        if 0<=chinese<=100 and 0<=math<=100 and 0<=english<=100:
            stu = Student(name,chinese,math,english)
            self.student_list.append(stu)
            print("添加成功")
        else:
            print("成绩输入错误")

    def update_Student(self):
        name = input("请输入姓名：")
        for i in self.student_list:
            if i.name == name:
                print(f"该学生的信息是：{i}")
                chinese = eval(input("请输入语文成绩："))
                math = eval(input("请输入数学成绩："))
                english = eval(input("请输入英语成绩："))
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    i.update_score(chinese,math, english)
                    print("更新成功")
                    print(f"更新后的信息是：{i}")
                    return
                else:
                    print("成绩输入错误")
                    return
        print("该学生不存在")

    def delete_Student(self):
        name = input("请输入要删除的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                self.student_list.remove(i)
                print("删除成功")
                return
        print("该学生不存在")

    def query_Student(self):
        name = input("请输入要查询的学生姓名：")
        for i in self.student_list:
            if i.name == name:
                print(f"该学生的信息是：{i}")
                return
        print("该学生信息不存在")

    def show_Student(self):
        for i in self.student_list:
            print(i)

    def run(self):
        print(f"欢迎使用{self.system_name}系统版本：{self.system_version}")
        print("1.添加学生2.更新学生3.删除学生4.查询学生5.显示所有学生6.退出系统")

        while True:
            choice = eval(input("请输入您的选择：1-6\n"))
            try:
                if choice == 1:
                    self.add_Student()
                elif choice == 2:
                    self.update_Student()
                elif choice == 3:
                    self.delete_Student()
                elif choice == 4:
                    self.query_Student()
                elif choice == 5:
                    self.show_Student()
                elif choice == 6:
                    print("谢谢使用")
                    break
                else:
                    print("输入错误重新输入1-6")
            except Exception as e:
                print("有错误，错误为：",e)
                continue


if __name__ =="__main__":
    edu = eduManagement()
    edu.run()




