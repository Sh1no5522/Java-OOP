import time
import random
import msvcrt

print("Wait for it...")
time.sleep(random.uniform(2, 4))
print("!!! GO !!!")

start = time.perf_counter()
# This waits for a single RAW keypress (like a mouse click)
msvcrt.getch() 
end = time.perf_counter()

print(f"Your hardware-level reaction: {(end - start) * 1000:.2f}ms")