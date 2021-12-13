import pygame

from constants import DIRECTION_KEYS, MOVE_ENEMIES, MOVE_VULNERABLE_ENEMIES, MOVEMENTS, QUIT_EVENT
from game.level import Level
from ui.renderer import Renderer


class MainLoop:

    def __init__(self, level: Level, renderer: Renderer, clock):
        self._level = level
        self._renderer = renderer
        self._clock = clock

    def _handle_events(self, events, current_direction):
        move_enemies = False
        move_vul_enemies = False
        do_quit = False
        direction = current_direction
        for event in events:
            if event.type in (pygame.QUIT, QUIT_EVENT):
                do_quit = True
            if event.type == pygame.KEYDOWN and event.key in DIRECTION_KEYS:
                direction = MOVEMENTS[event.key]
            if event.type == pygame.KEYUP and event.key in DIRECTION_KEYS:
                if MOVEMENTS[event.key] == direction:
                    direction = None
            if event.type == MOVE_ENEMIES:
                move_enemies = True
            if event.type == MOVE_VULNERABLE_ENEMIES:
                move_vul_enemies = True
        return (direction, move_enemies, move_vul_enemies, do_quit)

    def start(self):
        direction = None
        while True:
            events = pygame.event.get()
            direction, move_enemies, move_vul_enemies, do_quit = self._handle_events(
                events, direction)
            if do_quit:
                break
            self._level.do_update(
                move_enemies=move_enemies,
                move_vulnerable_enemies=move_vul_enemies,
                direction=direction
            )
            if self._level.is_finished:
                direction = None
            self._renderer.render()
            self._clock.tick(10)