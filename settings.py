import pygame

class Settings:
    """A class to store all settings for Tunnel escape"""
    
    def __init__(self):
        """A class to store all settings for Tunnel escape"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #bulletl settings
        self.bullet_speed = 2.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #fleet_direction of 1 represent right; -1 represent left
        self.fleet_direction = 1