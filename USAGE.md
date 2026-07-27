# Zero-downtime release safety gate

`tools/release_gate.py` converts the checklist into a deterministic CI gate. A release is blocked unless every mandatory control is explicitly `true`.

## Run

```bash
python tools/release_gate.py examples/release.json \
  --output release-gate-report.md
```

Exit code `0` means every mandatory control passed. Exit code `1` means the generated Markdown report lists the missing controls.

## Mandatory controls

- readiness tested against real serving ability;
- graceful shutdown and connection draining tested;
- capacity headroom verified;
- migration backward compatibility confirmed;
- previous artifact available;
- rollback tested;
- traffic reversal available;
- technical smoke test passed;
- critical business transaction passed;
- production observability ready.

The gate deliberately does not deploy, switch traffic, or perform rollback. It verifies evidence supplied by the release process and can be called from GitHub Actions, GitLab CI, Jenkins, or a local release runbook.

## Validation and releases

Pull requests compile the utility, run unit tests, and evaluate the passing sample. Tags matching `v*` create a GitHub Release with the checklist, evidence template, tested utility, sample input, and SHA-256 checksum.
