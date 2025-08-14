import os
import platform
import sys

def shutdown(delay_seconds=0):
    system_platform = platform.system()

    if system_platform == "Windows":
        os.system(f"shutdown /s /t {delay_seconds}")
    elif system_platform in ("Linux", "Darwin"):  # Darwin = macOS
        if delay_seconds > 0:
            os.system(f"sudo shutdown -h +{delay_seconds // 60}")  # Linux/macOS uses minutes
        else:
            os.system("sudo shutdown now")
    else:
        print("Unsupported operating system.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            delay = int(sys.argv[1])
        except ValueError:
            print("Please provide delay in seconds (Windows) or minutes (Linux/macOS).")
            sys.exit(1)
    else:
        delay = 0

    shutdown(delay)
