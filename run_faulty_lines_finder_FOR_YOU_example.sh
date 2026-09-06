#!/usr/bin/env bash
# Example: run fault localization on your own submission, independent of the
# question_N/ dataset layout. Edit the paths below, then run:
#
#   ./run_faulty_lines_finder_FOR_YOU_example.sh fauxpy
#   ./run_faulty_lines_finder_FOR_YOU_example.sh minimal_notests qwen
#   ./run_faulty_lines_finder_FOR_YOU_example.sh ranking gemma4
#   ./run_faulty_lines_finder_FOR_YOU_example.sh minimal_tests granite4
#
# mode: fauxpy | ranking | minimal_tests | minimal_notests
#   fauxpy          needs TEST_SUITE, no model
#   ranking         needs TEST_PAIRS_DIR + model
#   minimal_tests   needs TEST_PAIRS_DIR + model
#   minimal_notests needs DESCRIPTION + model
# model (all modes except fauxpy): qwen | qwen3_27b | qwen3_coder | gemma4 |
#                                  granite4 | codegemma | granite_code | codellama

set -euo pipefail

MODE=${1:?Usage: $0 <mode> [model]}
MODEL=${2:-}

# ── EDIT THESE ────────────────────────────────────────────────────────────
SUBMISSION=my_data/buggy_submission.py
TEST_SUITE=my_data/test_suite.py             # fauxpy only
TEST_PAIRS_DIR=my_data/test_io               # ranking / minimal_tests only -- dir of input_*.txt / output_*.txt
DESCRIPTION=my_data/description.txt          # minimal_notests (required) / optional elsewhere
OUTPUT_FILE=my_results/loc_${MODE}${MODEL:+_$MODEL}.jsonl
# ──────────────────────────────────────────────────────────────────────────

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

ARGS=(--mode "$MODE" --submission "$SUBMISSION" --output-file "$OUTPUT_FILE")

case "$MODE" in
    fauxpy)
        ARGS+=(--test-suite "$TEST_SUITE")
        ;;
    ranking|minimal_tests)
        ARGS+=(--test-pairs-dir "$TEST_PAIRS_DIR" --model "${MODEL:?model required for $MODE}")
        ;;
    minimal_notests)
        ARGS+=(--description "$DESCRIPTION" --model "${MODEL:?model required for $MODE}")
        ;;
esac

python Faulty_Lines_and_Repair_research/faulty_lines_finder_FOR_YOU.py "${ARGS[@]}"

echo ""
echo "=== Done. Result in $OUTPUT_FILE ==="