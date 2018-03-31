import re

speech_pattern = '^.*[A-Z]+:.*$'
pattern = re.compile(speech_pattern)

lines = []

with open("pilot.txt", "r") as f:
    for line in f:
        if pattern.match(line) and 'SCENE' not in line:
            lines.append(line)

with open("output.txt", "w") as out:
    for l in lines:
        out.write(l)
