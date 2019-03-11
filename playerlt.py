""""
Using properties, modify the users
score by 1000 * change in level.
ensure new level is >= 1

If level increases, then
player.score = level increase * 1000
level must be >= one.

set new level =
check for new_level < 1 then = 1
determine d_level: new level - cur level
determine score change.
score = d_level * 1000
"""

class Player(object):

    def __init__(self, name):
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0


    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level

    def _set_level(self, level):
        return self._score

    def _get_score(self):
        return self._score

    lives = property(_get_lives, _set_lives)
    level = property(_set_scor)


    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)