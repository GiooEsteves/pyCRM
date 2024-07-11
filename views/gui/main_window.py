class MainWindow:
    def __init__(self, title):
        self.title = title

    def show(self):
        print(f"Opening GUI window: {self.title}")

    def close(self):
        print("Closing GUI window")
