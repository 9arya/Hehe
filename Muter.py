from time import sleep

while True:
  for t in range(1,4):
    print("\rsedang proses mematikan program"+"."*t, end="", flush=True)
    sleep(0.7)