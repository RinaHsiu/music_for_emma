def on_button_pressed_a():
    music._play_default_background(music.built_in_playable_melody(Melodies.BIRTHDAY),
        music.PlaybackMode.IN_BACKGROUND)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    music.play(music.string_playable("C C G G A A G - ", 120),
        music.PlaybackMode.UNTIL_DONE)
    music.play(music.string_playable("F F E E D D C - ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
