from ursina import *
from ursina.prefabs.first_person_controller \
import FirstPersonController

if __name__ == "__main__":


    app = Ursina()
    Sky()
    player = FirstPersonController()

    boxes  = []
    for n in range(-8,8):
        for k in range(-8,8):
            box = Button(
                parent = scene,
                model='cube',
                origin_y = 0.5,
                texture = 'white_cube',
                color=color.orange,
                highlight_color = color.lime,
                position=(k,0,n)
            )
            boxes.append(box)

    def input(key):
        for box in boxes:
            if box.hovered:
                if key=="left mouse down":
                    boxes.append(
                        Button(
                            parent=scene,
                            model='cube',
                            origin_y=0.5,
                            texture='white_cube',
                            color=color.orange,
                            highlight_color=color.lime,
                            position=mouse.normal + box.position
                        )
                    )
                if key=='right mouse down':
                    boxes.remove(box)
                    destroy(box)

    app.run()