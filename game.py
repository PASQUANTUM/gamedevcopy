import pygame

"""""
ARGS:
Screen, States, Start State
Game inherits to Gameplay
Defines Functions Gameplay needs

"""""
class Game(object):
    def __init__(self, screen, states, start_state):
        self.done = False
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.states = states
        self.state_name = start_state
        self.state = self.states[self.state_name]

    def event_loop(self):
        """
        Handles events occurring in current states
        :return:
        """
        for event in pygame.event.get():
            self.state.get_event(event)

    def flip_state(self):
        """
        Handles transition between Game states

        persistent is information passed between states
        :return:
        """

        current_state = self.state_name
        next_state = self.state.next_state
        self.state.done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        self.state.startup(persistent)

    def update(self, dt):

        """
        Calls the flip_state function in case of State being done
        Updates the state
        :param dt:
        :return:
        """

        if self.state.quit:
            self.done = True
        elif self.state.done:
            self.flip_state()
        self.state.update(dt)

    def draw(self):
        """
        Only draws the screen in here
        :return:
        """
        self.state.draw(self.screen)

    def run(self):

        """
        Main Game Loop
        runs until Game is quit
        updating time
        calls event handling
        calls draw function
        :return:
        """
        while not self.done:
            dt = self.clock.tick(self.fps)
            self.event_loop()
            self.update(dt)
            self.draw()
            pygame.display.update()