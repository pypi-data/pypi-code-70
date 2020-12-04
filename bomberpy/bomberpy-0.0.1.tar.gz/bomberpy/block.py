import pygame as pg
from .utils import block_img

class Block(pg.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)
        self.image = block_img
        self.image = pg.transform.scale(self.image, [50, 50])
        self.rect = pg.rect.Rect(0, 0 , 50, 50)

        