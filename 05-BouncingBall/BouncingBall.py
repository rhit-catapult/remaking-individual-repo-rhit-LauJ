import pygame
import sys
import random


# You will implement this module ENTIRELY ON YOUR OWN!
class Ball1:
    def __init__(self, screen):
        self.screen = screen
        self.x = 0
        self.y = 0
        self.speed_x = random.randint(2, 10)
        self.speed_y = random.randint(2, 10)

    def move(self):
        self.y = self.y + self.speed_y
        self.x = self.x + self.speed_x
        self.bounce()

    def bounce(self):
        self.top_and_bottom_boundary()
        self.right_and_left_boundary()

    def top_and_bottom_boundary(self):
        if self.y > self.screen.get_height():
            self.speed_y = -self.speed_y
        if self.y < 0:
            self.speed_y = -self.speed_y
    def right_and_left_boundary(self):
        if self.x > self.screen.get_width():
            self.speed_x = -self.speed_x
        if self.x < 0:
            self.speed_x = -self.speed_x

    def draw(self):
        pygame.draw.circle(self.screen, (75, 113, 154), (self.x, self.y), random.randint(10, 20))


# TODO: Create a Ball class.
# TODO: Possible member variables: screen, color, x, y, radius, speed_x, speed_y
# TODO: Methods: __init__, draw, move

def main():
    pygame.init()
    screen = pygame.display.set_mode((700, 400))
    pygame.display.set_caption('Bouncing Ball')
    screen.fill(pygame.Color('gray'))
    clock = pygame.time.Clock()

    # TODO: Create an instance of the Ball class called ball1
    Jeff = Ball1(screen)

    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        clock.tick(60)
        screen.fill(pygame.Color('gray'))

        # TODO: Move the ball
        Jeff.move()
        # TODO: Draw the ball
        Jeff.draw()
        pygame.display.update()


main()
# Optional challenges (if you finish and want do play a bit more):
#   After you get 1 ball working make a few balls (ball2, ball3, etc) that start in different places.
#   Make each ball a different color
#   Make the screen 1000 x 800 to allow your balls more space (what needs to change?)
#   Make the speed of each ball randomly chosen (1 to 5)
#   After you get that working try making a list of balls to have 100 balls (use a loop)!
#   Use random colors for each ball
