import time
import threading
from sprite import animate_ascii_art, clear_screen, fcontent, delay

def pomodoro_timer(first_half_work, first_half_pause, second_half_work, second_half_pause, rounds, lunch_break):
    def run_animation():
        index = 0
        while not stop_animation.is_set():
            clear_screen()
            print(fcontent[index])
            index = (index + 1) % len(fcontent)  # Cycle through frames
            time.sleep(delay)

    for round in range(rounds):
        print(f"Round {round + 1}/{rounds}")
        
        # First half work time
        print(f"First half work time: {first_half_work} minutes")
        time.sleep(first_half_work * 60)
        
        # First half pause time
        print(f"First half pause time: {first_half_pause} minutes")
        stop_animation = threading.Event()
        animation_thread = threading.Thread(target=run_animation)
        animation_thread.start()
        time.sleep(first_half_pause * 60)
        stop_animation.set()
        animation_thread.join()
    
    # Lunch break
    print(f"Lunch break time: {lunch_break} minutes")
    stop_animation = threading.Event()
    animation_thread = threading.Thread(target=run_animation)
    animation_thread.start()
    time.sleep(lunch_break * 60)
    stop_animation.set()
    animation_thread.join()
    
    current_work_time = (first_half_work + second_half_work) * rounds

    while current_work_time < 8 * 60:

        # Second half work time
        print(f"Second half work time: {second_half_work} minutes")
        time.sleep(second_half_work * 60)
        current_work_time += second_half_work
        
        # Second half pause time
        print(f"Second half pause time: {second_half_pause} minutes")
        stop_animation = threading.Event()
        animation_thread = threading.Thread(target=run_animation)
        animation_thread.start()
        time.sleep(second_half_pause * 60)
        stop_animation.set()
        animation_thread.join()
        current_work_time += second_half_pause
        
    
    print("Pomodoro session complete!")

if __name__ == "__main__":
    first_half_work = int(input("Enter first half work time in minutes: "))
    first_half_pause = int(input("Enter first half pause time in minutes: "))
    second_half_work = int(input("Enter second half work time in minutes: "))
    second_half_pause = int(input("Enter second half pause time in minutes: "))
    rounds = int(input("Enter number of rounds for first half: "))
    lunch_break = int(input("Enter lunch break time in minutes: "))
    
    pomodoro_timer(first_half_work, first_half_pause, second_half_work, second_half_pause, rounds, lunch_break)