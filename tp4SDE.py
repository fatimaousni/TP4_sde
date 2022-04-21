def on_button_pressed_b():
    basic.show_number(input.temperature())
input.on_button_pressed(Button.B, on_button_pressed_b)
def on_forever():
    is_logo_pressed = True
    if input.logo_is_pressed():
        is_logo_pressed = False
    if is_logo_pressed == True:
        basic.show_icon(IconNames.SQUARE)
    else:
        basic.show_icon(IconNames.SMALL_SQUARE)
def on_sound_loud():
    basic.show_icon(IconNames.LINE)
input.on_sound(DetectedSound.LOUD, on_sound_loud)
   
basic.forever(on_forever)