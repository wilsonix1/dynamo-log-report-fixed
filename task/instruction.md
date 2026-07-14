Parse the Apache-style access log at `/app/access.log` and write a JSON report to
`/app/report.json`.

The report must be a JSON object with exactly these keys:
`total_requests`, `unique_ips`, and `top_path`.

Success criteria:

1. `/app/report.json` exists and contains only a valid JSON object with the three
   required keys listed above.
2. `total_requests` is the number of non-empty request lines in `/app/access.log`.
3. `unique_ips` is the number of distinct client IP addresses in the log.
4. `top_path` is the most frequently requested path. If there is a tie, use the
   path that appears first among the tied paths in the log.

You have 120 seconds to complete the task.
