todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
n = 2

for i in range(n):
    str_todo = str(input('해야 할 일을 입력하시오 : '))
    int_remainder = int(input('남은 일 수를 입력하시오 : '))

    new_todo = (str_todo, int_remainder,)
    todo.append(new_todo)
print(todo)
