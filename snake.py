import tkinter as tk
from PIL import Image, ImageTk


class Snake(tk.Canvas):
    def __init__(self):
       super().__init__(width=600, height=600, background="black", highlightthickness=0)
       self.snake_positions = [(100,100), (80,100), (60,100)]
       self.food_position = (200,200)
       self.score = 0

       self.load_assets()
       self.create_objects()

    def load_assets(self):
        try:
            snake_body_image = Image.open("assets/snake_body.png")
            self.snake_body = ImageTk.PhotoImage(snake_body_image)

            food_image = Image.open("assets/food.png")
            self.food = ImageTk.PhotoImage(food_image)
        except IOError as error:
            print(error)
            root.destroy()  

    def create_objects(self):
        self.create_text(45, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=("TkDefaultFont",14))
        self.create_rectangle(7, 27, 593, 593, outline="grey")

        for x_pos, y_pos in self.snake_positions:
            self.create_image(x_pos, y_pos, image=self.snake_body, tag="snake")
        
        self.create_image(self.food_position[0], self.food_position[1], image=self.food, tag="food")



root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = Snake()
canvas.pack()
root.mainloop()




