import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)


    def keep_on_screen(self):
        margin = 0

        if self.position.x < -margin:
            self.position.x = SCREEN_WIDTH + margin
        elif self.position.x > SCREEN_WIDTH + margin:
            self.position.x = -margin

        if self.position.y < -margin:
            self.position.y = SCREEN_HEIGHT + margin
        elif self.position.y > SCREEN_HEIGHT + margin:
            self.position.y = -margin


    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shot_cooldown -= dt

        if keys[pygame.K_h]:
            self.rotate(-dt)
        if keys[pygame.K_l]:
            self.rotate(dt)
        if keys[pygame.K_j]:
            self.accelerate_forward(dt)
        if keys[pygame.K_k]:
            self.accelerate_backward(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.velocity *= PLAYER_FRICTION

        if self.velocity.length() > PLAYER_SPEED:
            self.velocity.scale_to_length(PLAYER_SPEED)

        self.position += self.velocity * dt

        self.keep_on_screen()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector










    def accelerate_forward(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity += direction * PLAYER_ACCELERATION * dt

    def accelerate_backward(self, dt):
        direction = pygame.Vector2(0, 1).rotate(self.rotation)
        self.velocity -= direction * (PLAYER_ACCELERATION * 0.5) * dt




    def shoot(self):
        if self.shot_cooldown > 0:
            return
        self.shot_cooldown = PLAYER_SHOOT_COOLDOWN_SECONDS
        Shot(self.position[0], self.position[1], SHOT_RADIUS).velocity = pygame.Vector2(0,1).rotate(self.rotation)* PLAYER_SHOOT_SPEED
