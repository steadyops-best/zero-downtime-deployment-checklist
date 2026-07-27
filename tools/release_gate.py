#!/usr/bin/env python3
"""Fail a release review when mandatory zero-downtime controls are absent."""
from __future__ import annotations
import argparse, json, pathlib
REQUIRED=("readiness_tested","graceful_shutdown_tested","capacity_headroom_verified","migration_backward_compatible","previous_artifact_available","rollback_tested","traffic_reversal_available","technical_smoke_passed","business_transaction_passed","observability_ready")

def evaluate(payload: dict) -> dict:
    controls=payload.get("controls") or {}; missing=[name for name in REQUIRED if controls.get(name) is not True]
    return {"ready":not missing,"passed":len(REQUIRED)-len(missing),"total":len(REQUIRED),"missing":missing,"release":payload.get("release") or {}}

def markdown(report: dict) -> str:
    lines=["# Release Safety Gate", "", f"Result: **{'PASS' if report['ready'] else 'BLOCK'}**", f"Controls: **{report['passed']} / {report['total']}**"]
    if report["missing"]: lines += ["", "## Missing mandatory controls"]+[f"- `{name}`" for name in report["missing"]]
    return "\n".join(lines)+"\n"

def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("input"); p.add_argument("--output",default="release-gate-report.md"); a=p.parse_args(); report=evaluate(json.loads(pathlib.Path(a.input).read_text(encoding="utf-8"))); pathlib.Path(a.output).write_text(markdown(report),encoding="utf-8"); print(json.dumps(report,indent=2)); return 0 if report["ready"] else 1
if __name__=="__main__": raise SystemExit(main())
