import pluggy

hookimpl = pluggy.HookimplMarker("adapter")


class Plugin1(object):
    # test
    @hookimpl
    def testhook(self):
        return "Plugin2"
