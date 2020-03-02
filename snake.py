import tkinter as tk
from PIL import Image, ImageTk


class Snake(tk.Canvas):
    def __init__(self):
       super().__init__(width=600, height=600, background="black", highlightthickness=0)
       self.snake_positions = [(100,100), (80,100), (60,100)]

       self.load_assets()

    def load_assets(self):
        try:
            snake_body_image = Image.open("assets/snake_body.png")
            self.snake_body = ImageTk.PhotoImage(snake_body_image)

            food_image = Image.open("assets/food.png")
            self.food = ImageTk.PhotoImage(food_image)
        except IOError as error:
            print(error)
            root.destroy()



root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

board = Snake()
board.pack()
root.mainloop()




