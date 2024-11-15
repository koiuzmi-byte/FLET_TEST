import flet as ft
 
def main(page):
    def add_task(e):
        if task_input.value:
            task_list.controls.append(ft.Text(value=task_input.value))
            task_input.value = ""
            page.update()
 
    task_input = ft.TextField(hint_text="Enter a task")
    add_button = ft.ElevatedButton(text="Add Task", on_click=add_task)  # 修正: ElevatedButtonを使用
    task_list = ft.Column()
 
    page.add(task_input, add_button, task_list)
 
ft.app(target=main)
