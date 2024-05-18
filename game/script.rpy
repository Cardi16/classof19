define r = Character("Rinku")
define rk = Character("Rika")


label splashscreen:
    scene black with Pause(1)

    show text "Warning: None of the characters in this game are intended to reference real-life figures or characters.\nViewer discretion is advised." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return

label start:
    scene room
    show aimotorinku
    
    r "Wow, I sure do love being in the void."
    r "Happy Around!"
    hide aimotorinku

    show setorika
    rk "I love the void!!"
    rk "Don't you want to have fun with Merm4id?\ngay ass mf"
    hide rk

    return
