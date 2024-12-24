To run the script call: main.py using python3 path
First 2 parameters are for the Focus/Break time in minutes for the first half of the day (before lunch), then the following 2 are for the Focus/Break time in minutes for the second half of the day (after lunch) and the final parameter, how many rounds of Focus/Break you want to have in the first half of the day.
The timer lasts for 8 working hours (not counting lunch).

Script signature: pomodoro_timer(first_half_work, first_half_pause, second_half_work, second_half_pause, rounds, lunch_break)
Suggestion for input parameters: 30, 5, 25, 8, 4, 30. This would result in 30/5 Pomodoro timer in the first half (lasting for 4 total rounds before lunch), a lunch break lasting 30 minutes, and shorter Pomodoro timers in the second half untill the 8 hour mark is reached.


The idea behind the timer is to set longer focus timers in the first half of the day with shorter breaks. After eating your lunch, in the second half of the day, you can set shorter focus timers or longer breaks.

This script was inspired by a youtube comment I've read in the past.

The animation thread that plays during breaks is not visually pleasing. Initially it was meant to be better looking, but I've noticed it's more effective to raise me up from the desk when it's more distracting.
