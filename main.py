# import time

# def convert_to_seconds(hours, 
#                        minutes, 
#                        seconds=0):
    
#     return hours * 3600 + minutes * 60 + seconds

# def pomodoro_timer(total_work_hours, 
#                    first_half_work, 
#                    first_half_pause, 
#                    lunch_time,
#                    second_half_work, 
#                    second_half_pause, 
#                 #    rounds=0
#                    ):

#     start_time = time.time()
    

#     hours, minutes = map(int, total_work_hours.split(':'))
#     end_time = start_time + convert_to_seconds(hours, minutes)

#     half_duration = convert_to_seconds(hours, minutes) // 2

#     hours, minutes = map(int, lunch_time.split(':'))
#     lunch_time = convert_to_seconds(hours, minutes)
    
#     print(f"Total work hours: {total_work_hours}\n"
#           f"Start time: {time.ctime(start_time)}\n"
#           f"First half work: {first_half_work} seconds\n"
#           f"First half pause: {first_half_pause} seconds\n"
#         #   f"Rounds: {rounds}\n"
#           f"Lunch time: {lunch_time} seconds\n"
#           f"Second half work: {second_half_work} seconds\n"
#           f"Second half pause: {second_half_pause} seconds\n"
#           f"End time: {time.ctime(end_time)}\n"
#     )

#     while time.time() < end_time:
#         while time.time() < start_time + half_duration:
#             print(f"First half work time: {first_half_work} seconds")
#             time.sleep(first_half_work)
#             print(f"First half pause time: {first_half_pause} seconds")
#             time.sleep(first_half_pause)
#         print(f"Lunch time: {lunch_time} seconds")
#         time.sleep(lunch_time)
#         while time.time() < end_time:
#             print(f"Second half work time: {second_half_work} seconds")
#             time.sleep(second_half_work)
#             print(f"Second half pause time: {second_half_pause} seconds")
#             time.sleep(second_half_pause)

#     # for round in range(rounds):
#     #     print(f"Round {round + 1}/{rounds}")
        
#     #     # First half work time
#     #     print(f"First half work time: {first_half_work} seconds")
#     #     time.sleep(first_half_work)
        
#     #     # First half pause time
#     #     print(f"First half pause time: {first_half_pause} seconds")
#     #     time.sleep(first_half_pause)
    
#     # # Second half work time
#     # print(f"Second half work time: {second_half_work} seconds")
#     # time.sleep(second_half_work)
    
#     # # Second half pause time
#     # print(f"Second half pause time: {second_half_pause} seconds")
#     # time.sleep(second_half_pause)
    
#     print("Pomodoro session complete!")

# if __name__ == "__main__":
#     total_work_hours = input("Enter total work hours (HH:MM): ")
#     lunch_time = input("Enter lunch time (HH:MM): ")
#     first_half_work = int(input("Enter first half work time in seconds: "))
#     first_half_pause = int(input("Enter first half pause time in seconds: "))
#     second_half_work = int(input("Enter second half work time in seconds: "))
#     second_half_pause = int(input("Enter second half pause time in seconds: "))
#     # rounds = int(input("Enter number of rounds for first half: "))
    
    
#     pomodoro_timer(total_work_hours, first_half_work, first_half_pause, lunch_time, second_half_work, second_half_pause)


import time
import threading
from sprite import animate_ascii_art, clear_screen, fcontent, delay

def pomodoro_timer(first_half_work, first_half_pause, second_half_work, second_half_pause, rounds):
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
        print(f"First half work time: {first_half_work} seconds")
        time.sleep(first_half_work)
        
        # First half pause time
        print(f"First half pause time: {first_half_pause} seconds")
        stop_animation = threading.Event()
        animation_thread = threading.Thread(target=run_animation)
        animation_thread.start()
        time.sleep(first_half_pause)
        stop_animation.set()
        animation_thread.join()
    
    # Second half work time
    print(f"Second half work time: {second_half_work} seconds")
    time.sleep(second_half_work)
    
    # Second half pause time
    print(f"Second half pause time: {second_half_pause} seconds")
    stop_animation = threading.Event()
    animation_thread = threading.Thread(target=run_animation)
    animation_thread.start()
    time.sleep(second_half_pause)
    stop_animation.set()
    animation_thread.join()
    
    print("Pomodoro session complete!")

if __name__ == "__main__":
    first_half_work = int(input("Enter first half work time in seconds: "))
    first_half_pause = int(input("Enter first half pause time in seconds: "))
    second_half_work = int(input("Enter second half work time in seconds: "))
    second_half_pause = int(input("Enter second half pause time in seconds: "))
    rounds = int(input("Enter number of rounds for first half: "))
    
    pomodoro_timer(first_half_work, first_half_pause, second_half_work, second_half_pause, rounds)