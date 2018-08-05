"""
Pyglet Playground.

Description: A place to test new ideas.
Author: Erik Horton
"""

import pyglet
from pyglet.window import key

# index all resources
pyglet.resource.path = ["resources"]
pyglet.resource.reindex()

# Set up variables
running = True

# create window object
screen = pyglet.window.Window(800, 600)

# create batch group to put all objects in
main_batch = pyglet.graphics.Batch()

# create text label
score_label = pyglet.text.Label(
    text="Hello World",
    x=100,
    y=500,
    batch=main_batch)


def import_sprite(image, x, y, batch):
    """Import single image into batch."""
    img = pyglet.resource.image(image)
    sprite = pyglet.sprite.Sprite(img=img, x=x, y=y, batch=batch)
    return sprite


def import_spritesheet(spritesheet, rows, cols, item_width, item_height, x, y, batch, anim_slice=slice(0, None, 1), anim_speed=.1, should_loop=True):
    """Produce sprite sheet animation."""
    sprite_sheet = pyglet.resource.image(spritesheet)
    sprite_sheet_seq = pyglet.image.ImageGrid(sprite_sheet, rows, cols, item_width=item_width, item_height=item_height)
    sprite_sheet_texture = pyglet.image.TextureGrid(sprite_sheet_seq)
    sprite_sheet_anim = pyglet.image.Animation.from_image_sequence(sprite_sheet_texture[anim_slice], anim_speed, loop=should_loop)
    pyglet.sprite.Sprite(sprite_sheet_anim, x=x, y=y, batch=batch)


@screen.event
def on_key_press(symbol, modifiers):
    """Handle key press."""
    if symbol == key.SPACE:
        print("JUMP!")


@screen.event
def on_mouse_motion(x, y, dx, dy):
    """If mouse moves, print coords."""
    # print("{} - {}".format(x, y))
    pass


@screen.event
def on_mouse_press(x, y, button, modifiers):
    """If mouse button pressed, print."""
    print("{0} pressed at: {1},{2}.".format(button, x, y))


@screen.event
def on_draw():
    """Draw things as batch."""
    screen.clear()

    # draw batch group (vivi and text)
    main_batch.draw()


def update(dt):
    """Update objects here."""
    pass

if __name__ == "__main__":
    vivi = import_sprite("vivi.png", 400, 300, main_batch)
    import_spritesheet("sh-enemy.png", 1, 15, 100, 100, 400, 400, main_batch, slice(0, None, 1), .05, True)
    import_spritesheet("sh-explosion.png", 4, 5, 96, 96, 700, 400, main_batch, slice(0, None, 1), .1, True)
    import_spritesheet("sh-explosion.png", 4, 5, 96, 96, 100, 100, main_batch, slice(0, None, 1), .1, True)
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
