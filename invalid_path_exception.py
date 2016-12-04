class InvalidPathException(Exception):
    def __init__(self, path):
        Exception.__init__(self)
        self.path = path

    def __str__(self):
        return "Path '{}' does not exist".format(self.path)
