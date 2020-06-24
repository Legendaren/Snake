import pygame, os, sys

# Singleton class
class AudioPlayer:
    __instance = None
    __APP_FOLDER = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if AudioPlayer.__instance is None:
            __instance = AudioPlayer()
        return AudioPlayer.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if AudioPlayer.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            AudioPlayer.__APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
            AudioPlayer.__instance = self

    # Use this method when loading files
    def full_path(self, filename):
        return os.path.join(AudioPlayer.__APP_FOLDER, filename)

    def play(self, filename):
        pygame.mixer.music.load(self.full_path(filename))
        pygame.mixer.music.play()