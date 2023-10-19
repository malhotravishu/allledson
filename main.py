/**
 * Display a custom pattern on the LED display
 */
//% icon="\uD83D\uDD0C"
//% blockId=allLEDSOn
//% block="display pattern $pattern"
def allLEDsOn():
    basic.show_leds("""
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        # # # # #
        """)
allLEDsOn()