
import subprocess
import re
import platform


def scan_wifi():
    print("=" * 55)
    print("          PYTHON WI-FI NETWORK SCANNER")
    print("=" * 55)

    if platform.system() != "Windows":
        print("This version supports Windows only.")
        return

    try:
        # Scan nearby Wi-Fi networks
        result = subprocess.run(
            ["netsh", "wlan", "show", "networks", "mode=bssid"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace"
        )

        if result.returncode != 0:
            print("Wi-Fi scanning failed.")
            print(result.stderr)
            return

        output = result.stdout

        # Extract network details
        ssids = re.findall(
            r"^\s*SSID\s+\d+\s*:\s*(.*)$",
            output,
            re.MULTILINE
        )

        auth = re.findall(
            r"^\s*Authentication\s*:\s*(.*)$",
            output,
            re.MULTILINE
        )

        encryption = re.findall(
            r"^\s*Encryption\s*:\s*(.*)$",
            output,
            re.MULTILINE
        )

        signals = re.findall(
            r"^\s*Signal\s*:\s*(.*)$",
            output,
            re.MULTILINE
        )

        channels = re.findall(
            r"^\s*Channel\s*:\s*(.*)$",
            output,
            re.MULTILINE
        )

        if not ssids:
            print("No Wi-Fi networks found.")
            return

        print("\nNearby Wi-Fi Networks Found:\n")

        for i, ssid in enumerate(ssids):
            print("-" * 55)
            print(f"Network Number : {i + 1}")
            print(f"SSID           : {ssid or '<Hidden SSID>'}")
            print(f"Authentication : {auth[i] if i < len(auth) else 'N/A'}")
            print(f"Encryption     : {encryption[i] if i < len(encryption) else 'N/A'}")
            print(f"Signal         : {signals[i] if i < len(signals) else 'N/A'}")
            print(f"Channel        : {channels[i] if i < len(channels) else 'N/A'}")

        print("-" * 55)
        print(f"\nTotal Networks Found: {len(ssids)}")
        print("Wi-Fi scanning completed successfully!")

    except FileNotFoundError:
        print("Windows netsh command not found.")

    except Exception as e:
        print("Error:", e)


# Main Program
if __name__ == "__main__":
    scan_wifi()
