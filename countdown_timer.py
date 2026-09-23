import threading
import time


# Convert seconds into HH:MM:SS
def fmt(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


# Get a positive number from the user
def get_number(message):
    while True:
        value = input(message).strip()

        if value.isdigit() and int(value) >= 0:
            return int(value)

        print("Please enter a whole number.")


# Ask the user for hours, minutes, and seconds
def get_time():
    while True:
        hours = get_number("Enter hours: ")
        minutes = get_number("Enter minutes: ")
        seconds = get_number("Enter seconds: ")

        # Make sure the total time is not zero
        total = (hours * 3600) + (minutes * 60) + seconds

        if total > 0:
            return total

        print("Please enter a time greater than 0.")


class Timer:

    def __init__(self, total):
        self.total = total
        self.remaining = total
        self.running = threading.Event()
        self.stop_flag = threading.Event()
        self.reset_flag = threading.Event()
        self.active = False

    def _run(self):
        self.running.set()

        while self.remaining >= 0 and not self.stop_flag.is_set():

            # Reset timer
            if self.reset_flag.is_set():
                self.remaining = self.total
                self.reset_flag.clear()
                print(f"Reset to {fmt(self.total)}")

            # If paused, wait
            if not self.running.is_set():
                time.sleep(0.2)
                continue

            # Display remaining time
            print(f"Time remaining: {fmt(self.remaining)}")

            # Stop when timer reaches zero
            if self.remaining == 0:
                break

            # Wait one second
            for _ in range(10):
                if (
                    self.stop_flag.is_set()
                    or self.reset_flag.is_set()
                    or not self.running.is_set()
                ):
                    break

                time.sleep(0.1)

            else:
                self.remaining -= 1

        self.active = False

        if not self.stop_flag.is_set() and self.remaining <= 0:
            print("Time's up!\a")

    def start(self):
        if self.active:
            print("Already running.")
            return

        self.stop_flag.clear()
        self.remaining = self.total
        self.active = True

        threading.Thread(
            target=self._run,
            daemon=True
        ).start()

    def pause(self):
        self.running.clear()
        print("Paused.")

    def resume(self):
        self.running.set()
        print("Resumed.")

    def reset(self):
        self.reset_flag.set()

    def stop(self):
        self.stop_flag.set()
        self.running.set()


def main():

    while True:

        # Get the countdown time
        total_time = get_time()

        # Create and start timer
        timer = Timer(total_time)
        timer.start()

        print("\nCommands:")
        print("p = pause")
        print("r = resume")
        print("x = reset")
        print("s = stop")
        print("Enter = watch")

        # Listen for commands
        while timer.active:

            command = input().strip().lower()

            if command == "p":
                timer.pause()

            elif command == "r":
                timer.resume()

            elif command == "x":
                timer.reset()

            elif command == "s":
                timer.stop()
                break

        # Ask whether to start another timer
        again = input(
            "Start another timer? (y/n): "
        ).strip().lower()

        if again != "y":
            break


if __name__ == "__main__":
    main()