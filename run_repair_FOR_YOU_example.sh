#!/usr/bin/env bash
# Example: run the repair loop on your own submission, independent of the
# question_N/ dataset layout. Edit the paths below, then run:
#
#   ./run_repair_FOR_YOU_example.sh fauxpy qwen
#   ./run_repair_FOR_YOU_example.sh none granite4
#   ./run_repair_FOR_YOU_example.sh best_loc codegemma   # also loads Gemma4
#
# repair-type: none | fauxpy | best_loc | self_llm
# repair-model: qwen | qwen3_27b | qwen3_coder | gemma4 | granite4 |
#               codegemma | granite_code | codellama

set -euo pipefail

REPAIR_TYPE=${1:?Usage: $0 <repair-type> <repair-model>}
REPAIR_MODEL=${2:?Usage: $0 <repair-type> <repair-model>}

# ── EDIT THESE ────────────────────────────────────────────────────────────
SUBMISSION=my_data/buggy_submission.py
TEST_SUITE=my_data/test_suite.py
DESCRIPTION=my_data/description.txt      # optional -- comment out the --description line below if unused
OUTPUT_DIR=my_results/${REPAIR_TYPE}_${REPAIR_MODEL}
# ──────────────────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

python repair_research/run_repair_FOR_YOU.py \
    --repair-type "$REPAIR_TYPE" \
    --repair-model "$REPAIR_MODEL" \
    --submission "$SUBMISSION" \
    --test-suite "$TEST_SUITE" \
    --description "$DESCRIPTION" \
    --output-dir "$OUTPUT_DIR"

echo ""
echo "=== Done. Result in $OUTPUT_DIR/result.json ==="
