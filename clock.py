"""Display a live 24-hour clock in the terminal."""

import time
from datetime import datetime


def main() -> None:
    """Update the displayed local time once per second."""
    try:
        while True:
            current_time = datetime.now().strftime("%H:%M:%S")
            print(f"Current time: {current_time}", end="\r", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()