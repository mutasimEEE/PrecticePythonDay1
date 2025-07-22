class Phone:
    """A simple attempt to represent a phone."""

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.call_log = []

    def get_description(self):
        return f"{self.year} {self.brand} {self.model}".title()

    def make_call(self, number):
        print(f"Calling {number}...")
        self.call_log.append(number)

    def show_call_log(self):
        print("Call Log:")
        for number in self.call_log:
            print(f"- {number}")

class SmartPhone(Phone):
    """Represent aspects of a phone, specific to smartphones."""

    def __init__(self, brand, model, year, os):
        super().__init__(brand, model, year)
        self.os = os  # operating system like Android or iOS

    def install_app(self, app_name):
        print(f"Installing {app_name} on {self.model} ({self.os})...")

class Tablet(Phone):
    """Represent aspects of a phone, specific to tablets."""

    def __init__(self, brand, model, year, screen_size):
        super().__init__(brand, model, year)
        self.screen_size = screen_size  # in inches

    def watch_video(self, video_title):
        print(f"Watching {video_title} on {self.model} ({self.screen_size}-inch screen)...")

# 🔍 Now your task:
my_phone = SmartPhone('Samsung', 'Galaxy S21', 2021, 'Android')

print(my_phone.get_description())     # Expected output: 2021 Samsung Galaxy S21
my_phone.make_call('01712345678')     # Simulates a call
my_phone.make_call('01887654321')     # Another call
my_phone.show_call_log()              # Shows the numbers called
my_phone.install_app('YouTube')       # Installs an app
