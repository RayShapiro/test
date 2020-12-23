scene.set_background_color(6)
my_sprite = sprites.create(img("""
        ..........bbbbbb................
            .......bbb444444bb..............
            .....2244444ddd444b.............
            ....244444444dddd44e............
            ...244444444444ddd4be...........
            ..244444444444444d44be..........
            .2b444444444444444d4be..........
            .2b44444444444444444bbe.........
            2bbb4444444444444444bbe.........
            2bbb4444444444444444bbe.........
            2bb4b4444444444444444bbe........
            2bb4444444444444444444be........
            2bb44444444444444444444e........
            2bbb444bbb4444444444444e........
            22bbb444bb4bb444444444be........
            .2bbbbb44bbbb44444444bbe........
            .22bbbbbbbb44bbb444444bbe.......
            ..eeebbbbbbb44bbb444444be.......
            ...eeeeebbbbbbbb44b4444be.......
            .....eeeeee222bb44bbb4bbe.......
            .......eeeee222bb44bbbbee.......
            ............e222bbbbbbbec.......
            ..............ee2bbbbeebdb......
            .................eeeeecdddb.....
            .......................cd11bbbb.
            ........................cd111dbb
            .........................b11111c
            .........................c11dd1c
            .........................cd1dbc.
            .........................cb11c..
            ..........................ccc...
            ................................
    """),
    SpriteKind.player)
controller.move_sprite(my_sprite)

#add a comment
while True:
    test = my_sprite.x
    print(test)
    pause(100)