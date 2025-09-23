import time
frames = ["(-_-)", "(o_o)", "(^_^)", "(^o^)", "(^_^)"]
while True:
    for f in frames:
        print(f"\r{f}", end="")
        time.sleep(0.3)