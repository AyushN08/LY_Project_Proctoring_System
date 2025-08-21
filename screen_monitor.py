class ScreenMonitor:
    def __init__(self, logger):
        self.logger = logger
        try:
            import pygetwindow as gw
        except Exception:
            gw = None
        try:
            import psutil
        except Exception:
            psutil = None
        self.gw = gw
        self.psutil = psutil

    def monitor_screen(self):
        try:
            if self.gw:
                active = self.gw.getActiveWindow()
                title = active.title if active else "None"
                return {"type": "active_window", "title": title}
            if self.psutil:
                proc_count = len(list(self.psutil.process_iter(["name"])))
                return {"type": "process_count", "count": proc_count}
        except Exception as e:
            return {"type": "monitor_error", "error": str(e)}
        return None
