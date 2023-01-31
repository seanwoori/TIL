from launch.data.launch_people import *
from launch.control import *
from launch.control.get_non_participation import *
from launch.control.make_company import *
import tkinter
import tkinter.font


class_1_members = launch_people(class_1)
non_participation_lst = get_non_participation(class_1_members)
launch_company = make_company(class_1_members.launch_info, int(input("\n최소 조 인원을 숫자로 입력해주세요! \n")))

root = tkinter.Tk()
root.title('점심 조 짜기!!')
root.minsize(1600, 1200)

font = tkinter.font.Font(family = "맑은고딕", size = 25, slant="italic")

for index in range(len(launch_company)):
    label = tkinter.Label(root, text = str(launch_company[index]), font=font)
    label.place(x = 600, y = 100 * index + 50)

root.mainloop()








