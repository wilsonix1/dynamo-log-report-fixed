"""Verifier tests for the access-log JSON report."""

import json
from pathlib import Path


REPORT_PATH = Path("/app/report.json")


def load_report():
    """Load the generated report from the required artifact path."""
    assert REPORT_PATH.exists(), "no /app/report.json found"
    try:
        return json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise AssertionError(f"/app/report.json is not valid JSON: {exc}") from exc


def test_report_schema():
    """Verifies criterion 1: /app/report.json is a JSON object with the required keys."""
    report = load_report()
    assert isinstance(report, dict), "report must be a JSON object"
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Verifies instruction success criterion 2: total_requests counts non-empty request lines."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Verifies instruction success criterion 3: unique_ips counts distinct client IP addresses."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Verifies instruction success criterion 4: top_path is the most frequently requested path."""
    assert load_report()["top_path"] == "/index.html"
