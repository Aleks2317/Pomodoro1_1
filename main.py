import customtkinter
import time as t
import pygame


class App(customtkinter.CTk):
    customtkinter.set_appearance_mode("dark")

    def __init__(self):
        super().__init__()
        self.title("Pomodoro_1.1")
        self.geometry('200x200')
        self.iconbitmap('pomodoro_1_1.ico')
        self.grid_columnconfigure(0, weight=1)
        self.resizable(0, 0)

        self.pygame = pygame
        self.time = t
        self.duration = 60 * 25
        self.working = 'running'  # переменная, от статуса которой зависит работа приложения (running, stopped, updated)
        self.name = customtkinter.CTkLabel(self, text='Pomodoro 1.1', font=('Caveat', 20))  #
        self.name.pack(pady=5)

        self.count_digit = customtkinter.CTkLabel(self, text='25:00', font=('Caveat', 30), )
        self.count_digit.pack(pady=10)

        # кнопка для старта
        self.btn_start = customtkinter.CTkButton(self, text='Старт', font=('Caveat', 15), command=self.running_app)
        self.btn_start.pack(pady=10)
        # кнопка для остановки
        self.btn_stopped = customtkinter.CTkButton(self, text='Пауза', font=('Caveat', 15), command=self.stopped_app)
        # кнопка для обновления
        self.btn_updated = customtkinter.CTkButton(self, text='Обновить', font=('Caveat', 15), command=self.updated_app)
        # кнопка для отключения уведомления (мелодии)
        self.btn_music = customtkinter.CTkButton(self, text='Выключить', font=('Caveat', 15), command=self.music)

    def pomodoro(self):
        if self.working == 'stopped':
            self.btn_start.pack(pady=10)
            self.btn_updated.pack(pady=10)
            self.btn_stopped.pack_forget()  # прячем кнопку btn_stopped

        if self.working == 'updated':
            self.duration = 60 * 25
            self.count_digit.configure(text='25:00')
            self.btn_start.pack()
            self.btn_updated.pack_forget()  # прячем кнопку btn_updated
            self.btn_stopped.pack_forget()  # прячем кнопку btn_stopped

        if self.working == 'running':
            self.btn_stopped.pack(pady=10)
            self.btn_start.pack_forget()  # прячем кнопку btn_start
            self.btn_updated.pack_forget()  # прячем кнопку btn_updated

        while self.duration and self.working == 'running':
            self.min, self.sec = divmod(int(self.duration), 60)
            self.m_s_format = f'{self.min:02}:{self.sec:02}'
            self.count_digit.configure(text=self.m_s_format)
            self.count_digit.update()  # обновляем текст
            self.time.sleep(1 - self.time.time() % 1)
            self.duration -= 1
        else:
            if self.working == 'running':
                self.sound()

    def running_app(self):
        self.working = 'running'
        self.pomodoro()

    def stopped_app(self):
        self.working = 'stopped'
        self.pomodoro()

    def updated_app(self):
        self.working = 'updated'
        self.pomodoro()

    def sound(self):
        self.duration = 60 * 25
        self.count_digit.configure(text='25:00')
        self.btn_stopped.pack_forget()  # прячем кнопку btn_stopped
        self.btn_start.pack(pady=10)
        self.btn_music.pack(pady=10)
        self.pygame.mixer.init()  # инитиализация pygame.mixer
        self.pygame.mixer.music.load('one_pice.mp3')  # 3 загружаем файл с аудио в pygame.mixer
        self.pygame.mixer.music.play()  # запуск аудио файла

    def music(self):
        self.pygame.mixer.music.pause()
        self.btn_music.pack_forget()


if __name__ == '__main__':
    App().mainloop()
