import subprocess
import sys
import re

DEPTH = 6
fen = sys.argv[1]
print(f"evaluating fen {fen}")

out = fen + " "
process = subprocess.Popen(['./mperft', '-f', fen, '-d', str(DEPTH), '-l'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1)
depth = 1
for line in process.stdout:
    pattern = r'(\d+) leaves in'
    match = re.search(pattern, line)
    if match:
        leaves = match.group(1)
        out += f";D{depth} {leaves} "
        depth += 1
        if depth > DEPTH:
            break

print(out)

