#!/usr/bin/env bash
# Run repair types for one model (default: all 4 -- none, fauxpy, best_loc, self_llm).
#
# Usage:
#   ./repair_research/run_all.sh qwen
#   ./repair_research/run_all.sh qwen3_27b
#   ./repair_research/run_all.sh qwen3_27b 1 3 4 5              # skip question 2
#   TYPES="best_loc self_llm" ./repair_research/run_all.sh granite4       # only these types
#   TYPES="best_loc self_llm" ./repair_research/run_all.sh granite4 3 4 5 # + only these questions
#
# best_loc requires Gemma4 cache to exist. Run once before any best_loc experiments:
#   python repair_research/precompute_loc.py \
#     --questions-root /home/guests3/nkg/MASTER_PROJECT/Data \
#     --results-root /media/generalstorage4/nkgstorage/Results/repair

set -euo pipefail

TYPES=(${TYPES:-none fauxpy best_loc self_llm})

REPAIR_MODEL=${1:?Usage: $0 <repair-model> [question-numbers...]}
shift
if [ "$#" -eq 0 ]; then
    QUESTIONS=(1 3 4 5)
else
    QUESTIONS=("$@")
fi
QUESTIONS_ROOT=/home/guests3/nkg/MASTER_PROJECT/Data
RESULTS_ROOT=/media/generalstorage4/nkgstorage/Results/repair
PYTHON=python
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"

cd "$SCRIPT_DIR"

run_type() {
    local TYPE=$1
    echo ""
    echo "======================================================="
    echo "  TYPE: $TYPE   MODEL: $REPAIR_MODEL   QUESTIONS: ${QUESTIONS[*]}"
    echo "======================================================="
    $PYTHON repair_research/run_repair.py \
        --repair-type "$TYPE" \
        --repair-model "$REPAIR_MODEL" \
        --questions-root "$QUESTIONS_ROOT" \
        --results-root "$RESULTS_ROOT" \
        --questions "${QUESTIONS[@]}" \
        --resume
}

for TYPE in "${TYPES[@]}"; do
    run_type "$TYPE"
done

echo ""
echo "=== All done: $REPAIR_MODEL ==="
