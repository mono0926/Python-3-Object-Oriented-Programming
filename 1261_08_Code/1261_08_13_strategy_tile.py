from pygame import image
from pygame.transform import scale
from pygame import Surface

class TiledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        out_img = Surface(desktop_size)
        for x in range((out_img.get_width(
            ) // in_img.get_width()) + 1):
            for y in range((out_img.get_height(
                ) // in_img.get_height()) + 1):
                out_img.blit(in_img, (in_img.get_width() * x,
                    in_img.get_height() * y))
        return out_img

class CenteredStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        out_img = Surface(desktop_size)
        out_img.fill((0,0,0))
        left = (out_img.get_width() - in_img.get_width()) / 2
        top = (out_img.get_height() - in_img.get_height()) / 2
        out_img.blit(in_img, (left, top))
        return out_img

class ScaledStrategy:
    def make_background(self, img_file, desktop_size):
        in_img = image.load(img_file)
        return scale(in_img, desktop_size)
