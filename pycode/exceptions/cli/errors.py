class ArgumentError(Exception):
    pass

class TransitionError(Exception):
    def __init__(self, previous, next_state, message, *kwargs):
        self.previous = previous
        self.next_state = next_state
        self.message = message
        self.kwargs = kwargs
