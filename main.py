import pygame
import sys
import time
from settings import *
from sprites import BG, Ground, Plane, Obstacle


class Program:

    # Display and Clock setup;
    def __init__(self):
        self.active = None
        pygame.init()
        self.display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("")
        self.clock = pygame.time.Clock()

        # Sprite Group
        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Scaling Factor
        bg_HEIGHT = pygame.image.load(
            "../IMFJ1---Laboratorio-de-Pygame-Projeto-Final/Assets/background.png").get_height()
        self.scaling_factor = HEIGHT / bg_HEIGHT

        # Sprite Configuration
        BG(self.all_sprites, self.scaling_factor)
        Ground([self.all_sprites, self.collision_sprites], self.scaling_factor)
        self.Plane = Plane(self.all_sprites, self.scaling_factor * 2)

        # Timer
        self.obstacle_timer = pygame.USEREVENT + 1
        pygame.time.set_timer(self.obstacle_timer, 1400)

    def collisions(self):
        if pygame.sprite.spritecollide(self.Plane, self.collision_sprites, False, pygame.sprite.collide_mask) \
                or self.Plane.rect.top <= 0:
            for sprite in self.collision_sprites.sprites():
                if sprite.sprite_type == "  obstacle":
                    sprite.kill()
            self.active = False
            self.Plane.kill()

    # Program main loop;
    def run(self):
        last_time = time.time()
        while True:

            dt = time.time() - last_time
            last_time = time.time()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    self.Plane.Jump()

                if event.type == self.obstacle_timer:
                    Obstacle([self.all_sprites, self.collision_sprites], self.scaling_factor * 1.2)

            # Updates the display and limits the frame-rate;
            self.display_surface.fill("black")
            self.all_sprites.update(dt)
            self.collisions()
            self.all_sprites.draw(self.display_surface)

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    program = Program()
    program.run()
