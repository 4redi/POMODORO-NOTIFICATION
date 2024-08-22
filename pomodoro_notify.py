from plyer import notification
import time
import sys


def send_notification():
    notification.notify(
        title= "Break time!",
        message= "It\'s okay to take a break. Good things take time. Don't overstress",
        app_icon='logo.ico',
        timeout=15
    )

def pomodoro_timer(work_time=1*60,break_time=5*60):
    print("Work has started!")
    time.sleep(work_time)

    print("Break time right now!")
    send_notification()
    time.sleep(work_time)


if __name__=='__main__':
       pomodoro_timer()