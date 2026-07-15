"""Build the access-log summary report for the oracle solution."""

import json
import re
from collections import Counter
from pathlib import Path

paths, ips, total = Counter(), set(), 0
with Path("/app/access.log").open(encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        total += 1
        ips.add(line.split()[0])
        m = re.search(r'"(?:GET|POST|PUT|DELETE|HEAD|PATCH) (\S+) ', line)
        if m:
            paths[m.group(1)] += 1

with Path("/app/report.json").open("w", encoding="utf-8") as out:
    json.dump(
        {
            "total_requests": total,
            "unique_ips": len(ips),
            "top_path": paths.most_common(1)[0][0],
        },
        out,
    )
print("wrote /app/report.json")
