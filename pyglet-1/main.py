"""
Pyglet Playground.

Description: A place to test new ideas.
Author: Erik Horton
"""

import pyglet
from pyglet.window import key

# index all resources
pyglet.resource.path = ['resources']
pyglet.resource.reindex()

# Set up variables
running = True

# create window object
screen = pyglet.window.Window(800, 600)

# create batch group to put all objects in
main_batch = pyglet.graphics.Batch()

# create vivi object
vivi_image = pyglet.resource.image("vivi.png")
vivi_sprite = pyglet.sprite.Sprite(
    img=vivi_image,
    x=400,
    y=300,
    batch=main_batch)

# create text label
score_label = pyglet.text.Label(
    text="Hello World",
    x=100,
    y=500,
    batch=main_batch)


# Load enemy sprite sheet
enemy_ship = pyglet.image.load("resources/sh-enemy.png")
enemy_ship_seq = pyglet.image.ImageGrid(enemy_ship, 1, 15, item_width=100, item_height=100)
enemy_ship_texture = pyglet.image.TextureGrid(enemy_ship_seq)
enemy_ship_anim = pyglet.image.Animation.from_image_sequence(enemy_ship_texture[0:], .05, loop=True)
enemy_sprite = pyglet.sprite.Sprite(enemy_ship_anim, x=400, y=400, batch=main_batch)

# Load explosion sprite sheet
explosion = pyglet.image.load("resources/sh-explosion.png")
explosion_seq = pyglet.image.ImageGrid(explosion, 4, 5, item_width=96, item_height=96)
explosion_texture = pyglet.image.TextureGrid(explosion_seq)
explosion_anim = pyglet.image.Animation.from_image_sequence(explosion_texture[0:], .05, loop=True)
explosion_sprite = pyglet.sprite.Sprite(explosion_anim, x=700, y=400, batch=main_batch)


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
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
