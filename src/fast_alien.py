from alien import Alien

class FastAlien(Alien):
    """Alienígena mais rápido."""

    def update(self) -> None:
        self.x += (self.settings.alien_speed * 1.25) * self.settings.fleet_direction
        self.rect.x = self.x
