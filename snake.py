import tkinter as tk
from PIL import Image, ImageTk

SPEED = 200

class Snake(tk.Canvas):
    def __init__(self):
       super().__init__(width=600, height=600, background="black", highlightthickness=0)
       self.define_init_variables()
       self.init_assets()
       self.init_objects()
       self.bind_all("<Key>", self.on_key_press)
       self.after(SPEED, self.update_all)

    def define_init_variables(self):
        self.snake_positions = [(100,100), (80,100), (60,100)]
        self.food_position = (200,200)
        self.score = 0
        self.direction = "Right"

    def init_objects(self):
        self.create_text(45, 12, text=f"Score: {self.score}", tag="score", fill="#fff", font=("TkDefaultFont",14))
        self.create_rectangle(7, 27, 593, 593, outline="grey")
        self.create_image(self.food_position[0], self.food_position[1], image=self.food, tag="food")

        for x_pos, y_pos in self.snake_positions:
            self.create_image(x_pos, y_pos, image=self.snake_body, tag="snake")

    def init_assets(self):
        try:
            snake_body_image = Image.open("assets/snake_body.png")
            self.snake_body = ImageTk.PhotoImage(snake_body_image)

            food_image = Image.open("assets/food.png")
            self.food = ImageTk.PhotoImage(food_image)
        except IOError as error:
            print(error)
            root.destroy()  
  
    def move_snake(self):   # moving only right atm
        head = self.snake_positions[0]

        if self.direction == "Right":     
            new_head = head[0] + 20, head[1]    
        elif self.direction == "Left":
            new_head = head[0] - 20, head[1]  
        elif self.direction == "Down":     
            new_head = head[0], head[1] + 20 
        elif self.direction == "Up":
            new_head = head[0], head[1] - 20

        self.snake_positions = [new_head] + self.snake_positions[:-1]
        for segment, position in zip(self.find_withtag("snake"), self.snake_positions):
            self.coords(segment, position)

    def on_key_press(self, e):
        if self.direction == "Right" and e.keysym != "Left":
            self.direction = e.keysym
        elif self.direction == "Left" and e.keysym != "Right":
            self.direction = e.keysym            
        elif self.direction == "Up" and e.keysym != "Down":
            self.direction = e.keysym
        elif self.direction == "Down" and e.keysym != "Up":
            self.direction = e.keysym        

    def add_score(self):
        self.score +=1
        score = self.find_withtag("score")
        self.itemconfigure(score,text=f"Score: {self.score}", tag="score")

    def add_body_part(self):
        if self.food_position == self.snake_positions[0]:
            self.snake_positions.append(self.snake_positions[-1])
            self.create_image(self.snake_positions[-1][0], self.snake_positions[-1][1], image=self.snake_body, tag="snake")
            self.add_score()

    def update_all(self):
        self.add_body_part()
        self.move_snake()
        self.after(SPEED, self.update_all)


root = tk.Tk()
root.title("Snake")
root.resizable(False, False)

canvas = Snake()
canvas.pack()
root.mainloop()




