from enum import Enum


class Direct:
    def __init__(self):
        self._top = False
        self._right = False
        self._down = False
        self._left = False

    def stop(self):
        for d in self.__dict__:
            self.__dict__[d] = False
    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, v):
        self.stop()
        self._top = v

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, v):
        self.stop()
        self._right = v

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, v):
        self.stop()
        self._down = v

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, v):
        self.stop()
        self._left = v

    def __repr__(self):
        return 't={}, r={}, d={}, l={}'.format(*list(self.__dict__.values()))

if __name__ == '__main__':
    d = Direct()
    print(d)
    d.top = True
    d.left = True
    print(d)