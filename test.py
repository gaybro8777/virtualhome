import json
from common import TimeMeasurement
from environment import EnvironmentGraph
from scripts import Script, parse_script_line
from execution import ScriptExecutor


def load_graph(file_name):
    with open(file_name) as f:
        data = json.load(f)
    return EnvironmentGraph(data)


def read_script(file_name):
    script_lines = []
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if len(line) > 0 and not line.startswith('#'):
                script_lines.append(parse_script_line(line))
    return Script(script_lines)


if __name__ == '__main__':
    graph = load_graph('c:/Work/Python/TestScene6_graph.json')
    script = read_script('test_scripts/script_test_000003.txt')
    executor = ScriptExecutor(graph)
    tm = TimeMeasurement.start('Execution')
    state_enum = executor.execute(script)
    state = next(state_enum, None)
    TimeMeasurement.stop(tm)
    print(state)
    print('Measurements:\n' + TimeMeasurement.result_string())
