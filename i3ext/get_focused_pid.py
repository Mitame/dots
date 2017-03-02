def get_active_window_title(self):
    root = Popen(["xprop", "-root", "_NET_ACTIVE_WINDOW"], stdout=PIPE
