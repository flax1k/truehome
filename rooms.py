import devices
import scenes
from scenehandler import SceneHanlder


class Bedroom():
    def __init__(self):
        self.scene_handler = SceneHanlder()
        self.scene_handler.add_scene(scenes.Scene_BR_OFF())
        self.scene_handler.add_scene(scenes.Scene_BR_ON())
        self.scene_handler.add_scene(scenes.Scene_BR_RED())
        self.scene_handler.add_scene(scenes.Scene_BR_PURPLE())
        self.scene_handler.add_scene(scenes.Scene_BR_BLUE())

        devices.switch_bedroom.on_on(self.scene_handler.toggle)
        devices.remote_bedroom.on_arrow_left_click(lambda: self.scene_handler.prev_scene())
        devices.remote_bedroom.on_arrow_right_click(lambda: self.scene_handler.next_scene())
        devices.remote_bedroom.on_toggle(self.scene_handler.toggle)
        devices.remote_bedroom.on_brightness_up_click(self.brightness_up)
        devices.remote_bedroom.on_brightness_down_click(self.brightness_down)
    
    def brightness_up(self):
        b = devices.light_bedroom_top.brightness()
        b = int(min(254, b + 254 / 10))
        devices.light_bedroom_top.brightness(b)

    def brightness_down(self):
        b = devices.light_bedroom_top.brightness()
        b = int(max(0, b - 254 / 10))
        devices.light_bedroom_top.brightness(b)


class LivingRoom():
    def __init__(self):
        self.scene_handler = SceneHanlder()
        self.scene_handler.add_scene(scenes.Scene_LR_OFF())
        self.scene_handler.add_scene(scenes.Scene_LR_ON())
        self.scene_handler.add_scene(scenes.Scene_LR_AMBIENT())
        self.scene_handler.add_scene(scenes.Scene_LR_WINDOW())

        devices.switch_living_room.on_on(self.toggle_all)
        devices.remote_living_room.on_arrow_left_click(lambda: self.scene_handler.prev_scene())
        devices.remote_living_room.on_arrow_right_click(lambda: self.scene_handler.next_scene())
        devices.remote_living_room.on_toggle(self.scene_handler.toggle)
        devices.remote_living_room.on_arrow_left_hold(self.arrow_hold)
        devices.remote_living_room.on_arrow_right_hold(self.arrow_hold)
        devices.remote_living_room.on_brightness_up_click(self.brightness_up)
        devices.remote_living_room.on_brightness_down_click(self.brightness_down)

    def toggle_all(self):
        if self.scene_handler.get_scene() == 'OFF':
            self.scene_handler.set_scene('ON')
        else:
            self.scene_handler.set_scene('OFF')
            devices.plug_shelf.off()

    def brightness_up(self):
        if self.scene_handler.get_scene() not in ['WINDOW', 'OFF']:
            b = devices.light_living_room_top.brightness()
            b = int(min(254, b + 254 / 10))
            devices.light_living_room_top.brightness(b)
            devices.light_living_room_shelf.brightness(b)

    def brightness_down(self):
        if self.scene_handler.get_scene() not in ['WINDOW', 'OFF']:
            b = devices.light_living_room_top.brightness()
            b = int(max(0, b - 254 / 10))
            devices.light_living_room_top.brightness(b)
            devices.light_living_room_shelf.brightness(b)

    def arrow_hold(self):
        if devices.plug_shelf.is_off():
            devices.plug_shelf.on()
        else:
            devices.plug_shelf.off()
