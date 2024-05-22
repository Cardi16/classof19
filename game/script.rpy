define m = Character('Maddison')
define j = Character('Juliet')

# label splashscreen:
#     scene black with Pause(1)

#     show text "Warning: None of the characters in this game are intended to reference real-life figures or characters.\nViewer discretion is advised." with dissolve
#     with Pause(2)

#     hide text with dissolve
#     with Pause(1)

#     return

doom = 0 # for bad endings

label start:
    scene bus
    with fade
    show juliet default at right
    show maddison default at left
    m "Why the fuck are we on a bus"
    j "I don't know it was your idea"
    show maddison angry 
    m "bruh"
    return
