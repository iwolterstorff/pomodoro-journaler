from enum import Enum
from itertools import cycle
from time import sleep

from tqdm import tqdm


class Pomodoro(Enum):
    POMODORO = 25
    SHORT_BREAK = 5
    LONG_BREAK = 30


pattern = [
    Pomodoro.POMODORO,
    Pomodoro.SHORT_BREAK,
    Pomodoro.POMODORO,
    Pomodoro.SHORT_BREAK,
    Pomodoro.POMODORO,
    Pomodoro.SHORT_BREAK,
    Pomodoro.POMODORO,
    Pomodoro.LONG_BREAK,
]


def pom_seconds(pom):
    return pom.value * 60


def run_pomodoro_timer(pom):
    seconds_to_count = pom_seconds(pom)
    indicator = tqdm(desc="Time remaining: ")
    for _ in range(seconds_to_count):
        indicator.update(1)
        sleep(1)


if __name__ == "__main__":
    for pom in cycle(pattern):
        run_pomodoro_timer(pom)
