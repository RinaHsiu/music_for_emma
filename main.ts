input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music._playDefaultBackground(music.builtInPlayableMelody(Melodies.Birthday), music.PlaybackMode.InBackground)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    music.play(music.stringPlayable("C C G G A A G - ", 120), music.PlaybackMode.UntilDone)
    music.play(music.stringPlayable("F F E E D D C - ", 120), music.PlaybackMode.UntilDone)
})
basic.forever(function on_forever() {
    
})
