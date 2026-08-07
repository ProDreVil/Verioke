import vlc

class AudioPlayer:
    def __init__(self):
        self.player = None

    def load(self, path):
        self.player = vlc.MediaPlayer(path)

    def play(self):
        if self.player:
            self.player.play()

    def stop(self):
        if self.player:
            self.player.stop()

    def is_playing(self):
        if self.player:
            return self.player.is_playing()
        return False