from graphics import *


# GLOBAL PARAMETERS
SIZE_X = 600
SIZE_Y = 600
window = GraphWin("Model", SIZE_X, SIZE_Y)

ball_coords = Point(300, 300)
ball_velocity = Point(1, -2)

def update_point(point: Point, velocity: Point):
    new_point = Point(point.x + velocity.x, point.y + velocity.y)
    return new_point

def draw_ball(coords):
    ball = Circle(coords, 10)
    ball.setFill('red')
    ball.draw(window)

# CREATING MAIN WINDOW
def main(ball_coords):
    while True:
        draw_ball(ball_coords)
        ball_coords = update_point(ball_coords, ball_velocity)


if __name__ == "__main__":
    main(ball_coords)