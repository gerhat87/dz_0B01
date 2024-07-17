#Задача: Создай класс Task, который позволяет управлять задачами (делами).
#У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (
  #  выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных
#задач и вывода списка текущих (не выполненных) задач.


class Task():
    def __init__(self):
        self.tasks=[]

    def add_task(self, deadline, description):
        self.tasks.append({"deadline": deadline, "description": description, "status": "не выполнено"})

    def comlete_tasks(self, description):
        for tasks in self.tasks:
            if tasks["description"] == description:
                tasks["status"] = "выполнено"
                print(f"Задача  {description} считается выполненной")
            else:
                print("Задача не найдена")

    def show_task(self):
        print("текущие задачи")
        for task in self.tasks:
            if task["status"] == "не выполнено":
                print(f"{task['description']} - {task['deadline']}")

t = Task()
t.add_task('01.02.2024', 'выполнить ДЗ')
t.add_task('05.02.2024', 'оплатить счета')
t.add_task('06.02.2024', 'сделать важный звонок')

t.show_task()

t.comlete_tasks('оплатить счета')