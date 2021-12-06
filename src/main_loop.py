import sys
import pygame

from constants import MOVE_ENEMIES
from game.level import Level
from renderer import Renderer


class MainLoop:

    def __init__(self, level: Level, renderer: Renderer, clock):
        self._level = level
        self._renderer = renderer
        self._clock = clock

    def _handle_events(self, events, current_direction):
        move_enemies = False
        do_quit = False
        direction = current_direction
        for event in events:
            if event.type == pygame.QUIT:
                do_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_LEFT]:
                    direction = event.key
            if event.type == pygame.KEYUP:
                direction = None
            if event.type == MOVE_ENEMIES:
                move_enemies = True
        return (direction, move_enemies, do_quit)

    def start(self):
        direction = None
        while True:
            events = pygame.event.get()
            direction, move_enemies, do_quit = self._handle_events(
                events, direction)
            if do_quit:
                sys.exit()
            self._level.do_update(move_enemies, direction)
            self._renderer.render()
            self._clock.tick(10)
