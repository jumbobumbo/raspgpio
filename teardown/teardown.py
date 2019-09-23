class TearDown:

    @staticmethod
    def down(LED_board):
        LED_board.off()
        LED_board.close()
