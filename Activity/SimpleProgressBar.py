import sys, time

for i in range(21):
    percent = i * 5
    sys.stdout.write(f"\rLoading... {percent}%")
    sys.stdout.flush()
    time.sleep(0.2)

print("\nDone!")
