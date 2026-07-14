# Dynamo Log Report Fixed Task

This repository contains the repaired Terminal-Bench 2 Harbor task under `task/`.

Validation was run locally with Harbor 0.18.0 using the Apple container backend:

```text
cd task
harbor run -p . -a oracle --env apple-container --job-name final-task-oracle --n-concurrent 1
reward: 1
tests: 4 passed, 0 failed
```

```text
cd task
harbor run -p . --agent nop --env apple-container --job-name final-task-nop --n-concurrent 1
reward: 0
tests: 0 passed, 4 failed
```

The fixed task writes `/app/report.json`, and the verifier emits `/logs/verifier/reward.txt` plus `/logs/verifier/ctrf.json`.
