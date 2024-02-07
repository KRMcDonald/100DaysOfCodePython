# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
# FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.start_x = 0
        self.start_y = -280
        self.move_distance = 10
        self.finish_line_y = 280

    def move_up(self):
        self.forward(self.move_distance)

    def detect_car_collision(self, car_list):

        for car in car_list:
            car_top_bound = car.ycor() + 10
            car_bot_bound = car.ycor() - 10
            car_left_bound = car.xcor() - 20
            car_right_bound = car.xcor() + 20

            car_coord = []

            car_coord.append(self.distance(car_right_bound, car_top_bound))
            car_coord.append(self.distance(car_right_bound, car_bot_bound))
            car_coord.append(self.distance(car_left_bound, car_top_bound))
            car_coord.append(self.distance(car_left_bound, car_bot_bound))

            for distance in car_coord:
                if distance < 10:
                    return True

    def detect_top_reached(self):
        if self.ycor() >= self.finish_line_y:
            return True

    def level_up(self):
        self.teleport(0,-280)
