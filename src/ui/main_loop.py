from typing import List
import pygame

from constants import DIRECTION_KEYS, DIRECTION_MAP, \
    MOVE_ENEMIES, \
    MOVE_VULNERABLE_ENEMIES, \
    PAC_CHANGE_MOUTH, \
    QUIT_EVENT
from game.level import Level
from ui.renderer import Renderer


class MainLoop:
    """Class responsible for running the game loop"""

    def __init__(self, level: Level, renderer: Renderer, clock: pygame.time.Clock):
        """Constructor

        Args:
            level (Level): Level object
            renderer (Renderer): Renderer object
            clock (pygame.time.Clock): Clock used to control framerate
        """
        self._level = level
        self._renderer = renderer
        self._clock = clock

    def _handle_events(self, events: List[pygame.event.Event], current_direction):
        move_enemies = False
        move_vul_enemies = False
        do_quit = False
        change_pac_mouth = False
        direction = current_direction
        for event in events:
            if event.type in (pygame.QUIT, QUIT_EVENT):
                do_quit = True
            if event.type == pygame.KEYDOWN and event.key in DIRECTION_KEYS:
                direction = DIRECTION_MAP[event.key]
            if event.type == pygame.KEYUP and event.key in DIRECTION_KEYS:
                if DIRECTION_MAP[event.key] == direction:
                    direction = None
            if event.type == MOVE_ENEMIES:
                move_enemies = True
            if event.type == MOVE_VULNERABLE_ENEMIES:
                move_vul_enemies = True
            if event.type == PAC_CHANGE_MOUTH:
                change_pac_mouth = True
        return (direction, move_enemies, move_vul_enemies, do_quit, change_pac_mouth)

    def start(self):
        """Starts the game loop"""
        direction = None
        while True:
            events = pygame.event.get()
            direction, move_enemies, move_vul_enemies, do_quit, change_pac_mouth = self._handle_events(
                events, direction)
            if do_quit:
                break
            self._level.do_update(
                move_enemies=move_enemies,
                move_vulnerable_enemies=move_vul_enemies,
                direction=direction,
                change_pac_mouth=change_pac_mouth
            )
            if self._level.is_finished:
                direction = None
            self._renderer.render(self._level)
            self._clock.tick(10)
