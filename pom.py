from enum import Enum
from itertools import cycle
from sys import argv
from time import asctime, sleep

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
    indicator = tqdm(
        desc="Time remaining: ",
        total=seconds_to_count,
        unit="min",
        unit_scale=(1 / 60),
        mininterval=1,
        maxinterval=1,
        bar_format="{l_bar}{bar}{postfix}",
    )
    string_seconds_to_count = indicator.format_interval(seconds_to_count)
    for sec in range(seconds_to_count):
        curr_time_str = indicator.format_interval(sec)
        indicator.set_postfix_str(f"{curr_time_str}/{string_seconds_to_count}")
        indicator.update(1)
        sleep(1)


if __name__ == "__main__":
    out_file = open(argv[1], "a")
    prefix = "\nSummary of this pomodoro: "
    for pom in cycle(pattern):
        try:
            out_file.write("\nPomodoro starting at: " + asctime())
            run_pomodoro_timer(pom)

            user_input = input(prefix)
            out_file.write(f"\n{prefix}{user_input}\n")
        except KeyboardInterrupt:
            out_file.write("\n\n**Pomodoro interrupted**")
            break
