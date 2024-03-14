import time
import keyboard
from datetime import datetime


def auto_timer(start_time, time_spawn, message):
    end_time = datetime.now()
    remaining_time = end_time - start_time
    total_time = max(time_spawn - remaining_time.total_seconds(), 0)
    if total_time == 0:
        return message
    elif total_time > 60:
        return f"{round(total_time / 60, 1)} m"
    else:
        return f"{int(total_time)} s"


def main():
    start_time = None
    spawn_times = [60, 120, 180, 240, 270, 285, 300, 360, 420, 450, 465, 480, 540, 600, 630, 645, 660]
    while True:
        if keyboard.is_pressed('1') and keyboard.is_pressed('2'):
            start_time = datetime.now()
        if start_time is not None:
            current_time = datetime.now()
            elapsed_time = (current_time - start_time).total_seconds()
            for spawn_time in spawn_times:
                if elapsed_time >= spawn_time - 1 and elapsed_time <= spawn_time + 1:
                    keyboard.press("enter")
                    time.sleep(0.1)
                    aegis_result = auto_timer(start_time, 300, "Aegis disappeared!")
                    first_roshan_result = auto_timer(start_time, 480, "First roshan up!")
                    second_roshan_result = auto_timer(start_time, 660, "Second roshan up!")
                    result = f"Aegis - {aegis_result} | First roshan - {first_roshan_result} | Second roshan - {second_roshan_result}"
                    keyboard.write(result)
                    time.sleep(0.1)
                    keyboard.press("enter")
                    time.sleep(0.1)
                    keyboard.press("enter")
                    break
        if keyboard.is_pressed('2') and keyboard.is_pressed('3'):
            keyboard.press("enter")
            time.sleep(0.1)
            aegis_result = auto_timer(start_time, 300, "Aegis disappeared!")
            first_roshan_result = auto_timer(start_time, 480, "First roshan up!")
            second_roshan_result = auto_timer(start_time, 660, "Second roshan up!")
            result = f"Aegis - {aegis_result} | First roshan - {first_roshan_result} | Second roshan - {second_roshan_result}"
            keyboard.write(result)
            time.sleep(0.1)
            keyboard.press("enter")
            time.sleep(0.1)
            keyboard.press("enter")
        time.sleep(0.1)


if __name__ == "__main__":
    main()
