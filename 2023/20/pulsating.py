import abc
from abc import ABC

from util.decorators import aoc_timed_solution
from util.util import lcm

MODULES = {}
COUNTS = [0, 0]  # Low, high
EVENT_QUEUE = []

# p2
BUTTON_PRESSED = 0


class Module(ABC):

    def __init__(self, line):
        self.name, self.connections = line.split('->')
        self.name = self.name.strip()
        self.connections = [c.strip() for c in self.connections.split(',')]

    def receive(self, pulse, from_c=None, count=True):
        # print(f'{from_c} -{pulse}-> {self.name}')
        if count:
            COUNTS[pulse] += 1
        self._receive_this(pulse, from_c)

    @abc.abstractmethod
    def _receive_this(self, pulse, from_c):
        pass

    def _send_to_connections(self, pulse):
        for con in self.connections:
            EVENT_QUEUE.append((con, pulse, self.name))

    def __repr__(self):
        return f'{self.name} -> {self.connections}'


class FlipFlop(Module):

    def __init__(self, line):
        super().__init__(line)
        self.name = self.name[1:]
        self.state = False

    def _receive_this(self, pulse, from_c):
        if pulse == 0:
            self.state = not self.state
            self._send_to_connections(int(self.state))


class Conjuction(Module):
    def __init__(self, line):
        super().__init__(line)
        self.state_length = -1
        self.name = self.name[1:]
        self.states = {}
        self.lcm = None

    def set_input_states(self, inputs):
        for i in inputs:
            self.states[i] = 0
        self.state_length = len(inputs)

    def _receive_this(self, pulse, from_c):
        self.states[from_c] = pulse
        if sum(self.states.values()) == self.state_length:
            self._send_to_connections(0)
        else:
            self._send_to_connections(1)
            if BUTTON_PRESSED > 0 and self.lcm is None:
                self.lcm = BUTTON_PRESSED


class Broadcaster(Module):
    def __int__(self, line):
        super().__init__(line)

    def _receive_this(self, pulse, from_c):
        self._send_to_connections(pulse)


class Output(Module):
    def __int__(self, line):
        super().__init__(line)

    def _receive_this(self, pulse, from_c):
        pass


def _load_input(filename):
    MODULES.clear()
    COUNTS[0] = 0
    COUNTS[1] = 0
    conjs = []
    with open(filename) as file:
        for line in file:
            if line[0] == '%':
                mod = FlipFlop(line.rstrip())
            elif line[0] == '&':
                mod = Conjuction(line.rstrip())
                conjs.append(mod)
            else:
                mod = Broadcaster(line.rstrip())
            MODULES[mod.name] = mod
    for c in conjs:
        c.set_input_states([mod.name for mod in MODULES.values() if c.name in mod.connections])


@aoc_timed_solution(2023, 20, 1)
def run_part1(filename, times=1000):
    _load_input(filename)
    _simulate_button_press(times=times)
    return COUNTS[0] * COUNTS[1]


def _simulate_button_press(times=1):
    for _ in range(times):
        EVENT_QUEUE.append(('broadcaster', 0, 'button'))  # To, pulse, from
        while len(EVENT_QUEUE) > 0:
            event = EVENT_QUEUE.pop(0)
            try:
                MODULES[event[0]].receive(event[1], event[2])
            except KeyError:
                COUNTS[event[1]] += 1


@aoc_timed_solution(2023, 20, 2)
def run_part2(filename):
    # Looking at the input, the final module 'rx' is the output of '&rs' which is connected by 4 other conjunctions
    # This problem is then solved by LCM on all other conjunctions
    _load_input(filename)
    return _press_button_until()


def _press_button_until():
    global BUTTON_PRESSED
    BUTTON_PRESSED = 0
    while True:
        EVENT_QUEUE.append(('broadcaster', 0, 'button'))  # To, pulse, from
        BUTTON_PRESSED += 1
        while len(EVENT_QUEUE) > 0:
            event = EVENT_QUEUE.pop(0)
            try:
                MODULES[event[0]].receive(event[1], event[2], count=False)
            except KeyError:
                pass
            if (ans := _check_lcm_solution()) is not None:
                return ans


def _check_lcm_solution():
    cons = [c for c in MODULES.values() if hasattr(c, 'lcm')]
    if not any([c.lcm is None for c in cons]):
        return lcm([c.lcm for c in cons])
    return None


if __name__ == "__main__":
    run_part1("example_1.txt", times=1)  # 32 (8L 4H)
    run_part1("example_1.txt")  # 32000000 (8000L 4000H)
    run_part1("example_2.txt", times=1)  # 16
    run_part1("example_2.txt")  # 11687500 (4250L 2750H)
    run_part1("input.txt")
    run_part2("input.txt")
