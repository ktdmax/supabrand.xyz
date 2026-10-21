#!/usr/bin/env python3
"""Prove the validators bite: mutate the built manifest in memory and expect errors.

SYNTHETIC TEST DATA helper. Usage: python3 tools/negative_check.py --obds-repo <path>
"""
import argparse, copy, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(); parser.add_argument("--obds-repo", required=True); args = parser.parse_args()
sys.path.insert(0, str(Path(args.obds_repo) / "reference/foundation/src"))
from obds_ref.compiler import validate_manifest
from obds_ref.governed_io import load_data
from obds_ref.knowledge_records import validate_manifest_extension

base = load_data(ROOT / "manifest.yaml")
by_id = {e["id"]: e for e in base["elements"]}
cases = {}
m = copy.deepcopy(base); m["elements"][0]["value"] = "tampered"
cases["approval hash mismatch after edit"] = validate_manifest(m, verify_hash=True)
m = copy.deepcopy(base); e = next(x for x in m["elements"] if x["id"] == "rules.no-partner-endorsement-wording"); del e["value"]["checks"]
cases["rule value missing required field"] = validate_manifest(m, verify_hash=False)
m = copy.deepcopy(base); next(x for x in m["elements"] if x["id"] == "claim.c01-twelve-markets")["dependsOn"] = ["market.dealer-observation.de-q3-2026"]
cases["binding depends on unverified"] = validate_manifest_extension(m)
m = copy.deepcopy(base); del next(x for x in m["elements"] if x["id"] == "claim.c18-a8-vibration-draft")["caveats"]
cases["unverified without caveats"] = validate_manifest_extension(m)
m = copy.deepcopy(base); next(x for x in m["elements"] if x["id"] == "brand.purpose")["domain"] = "marketing"
cases["domain outside vocabulary"] = validate_manifest_extension(m)
m = copy.deepcopy(base); next(x for x in m["elements"] if x["id"] == "rules.no-recycled-bicycle-wording")["authority"] = "informational"
cases["rules family not binding"] = validate_manifest_extension(m)
m = copy.deepcopy(base); next(x for x in m["elements"] if x["id"] == "claim.c07-a8-range")["supersedes"] = ["claim.c06-c2-frame-recycled"]
cases["supersedes field present"] = validate_manifest(m, verify_hash=False) + validate_manifest_extension(m)
ok = True
for name, errors in cases.items():
    print(f"{'caught' if errors else 'MISSED'}: {name} -> {errors[0][:110] if errors else ''}")
    ok = ok and bool(errors)
print("negative check", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
