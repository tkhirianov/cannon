from PIL import Image, ImageTk
import tkinter


class MainWindow:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("640x480")
        self.menu = self._create_menu()
        self.root.config(menu=self.menu)
        self.canvas = tkinter.Canvas(self.root)
        self.canvas.pack()
        
        self.balls = []
        

    def _create_menu(self):
        menu = tkinter.Menu(self.root)
        file_menu = tkinter.Menu(menu)
        file_menu.add_command(label="Exit", command=hello)
        file_menu.add_command(label="Start game",
                              command=self._start_game)
        menu.add_cascade(label="File", menu=file_menu)
        return menu

    def _exit(self):
        print("Clicked Exit from menu.")
        self.root.quit()
        
    def _start_game(self):
        print("Started game.")
        self.balls.append(Ball(self.canvas, 100, 100))
        
    def loopback(self):
        print("Hello!")
        self.canvas.after(500, self.loopback)

    def mainloop(self):
        self.canvas.after(500, self.loopback)
        self.root.mainloop()


class Ball:
    image_file = 'magic_ball.png'
    ball_image = ImageTk.PhotoImage(Image.open(self.image_file))
    
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y
        self.avatar = canvas.create_image(x, y, image=self.ball_image)


def main():
    main_window = MainWindow()
    main_window.mainloop()


if __name__ == "__main__":
    main()

