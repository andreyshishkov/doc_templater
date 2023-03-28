import tkinter as tk
from windows.mode_create import CreateModeWindow


class MainWindow(tk.Tk):

    def __init__(self, width=1200, height=800):
        super().__init__()
        self.geometry(f'{width}x{height}')
        self.config(bg='green')
        self.title('Программа автоматизации создания отчетов')

        self._create_buttons()

    def _create_buttons(self):
        # button of mode "create"
        self.make_criteria_btn = tk.Button(
            self,
            text='Создать критерии проверки (Режим создания)',
            width=40,
            height=5,
            command=self.create_window_mode_create
        )
        self.make_criteria_btn.pack(pady=200)

        # button of mode "choose"
        self.choose_criteria_btn = tk.Button(
            self,
            text='Выбрать критерии проверки (Режим проверки)',
            width=40,
            height=5
        )
        self.choose_criteria_btn.pack()

    def create_window_mode_create(self):
        mode_create = CreateModeWindow(self, 1200, 800)
        mode_create.grab_focus()

    def run(self):
        self.mainloop()


if __name__ == '__main__':
    window = MainWindow()
    window.run()
