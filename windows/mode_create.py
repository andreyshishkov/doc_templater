import tkinter as tk
import tkinter.messagebox as mb


class CreateModeWindow(tk.Toplevel):

    def __init__(self, parent, width, height, title='Режим создания критериев', resizable=(False, False), icon=None):
        super().__init__(parent)
        self.title(title)
        self.geometry(f'{width}x{height}+200+200')
        self.resizable(*resizable)
        self.config(bg='gray')

        if icon:
            self.iconbitmap(icon)

        self._create_input_fields()
        self._create_button_close()

    def _create_button_close(self):
        self.close_button = tk.Button(
            self,
            text='Завершить ввод',
            command=self.destroy
        )
        #self.close_button.pack()

    def _create_input_fields(self):
        self.criterion_label = tk.Label(self, text='Поле ввода критерия')
        self.input_criterion = tk.Entry()

        self.criterion_label.grid(row=3, columnspan=2)

    def confirm_exit(self):
        message = "Вы уверены, что хотите завершить ввод критериев?"
        if mb.askyesno(message=message, parent=self):
            self.destroy()

    def grab_focus(self):
        self.grab_set()
        self.focus_set()
        self.wait_window()
