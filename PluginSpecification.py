import pluggy

hookspec = pluggy.HookspecMarker("adapter")


class MySpec(object):

    @hookspec
    def testhook(self):
        """My special little hook that you can customize."""
