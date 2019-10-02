import unicornhat

def test_flash():
    unicornhat.set_pixel(0, 0, 255, 255, 255)
    unicornhat.show()
    unicornhat.clear()
    unicornhat.show()
