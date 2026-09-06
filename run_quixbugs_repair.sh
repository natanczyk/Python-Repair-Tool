#!/usr/bin/env bash
# Run repair types on Data_QuixBugs for one model (default: all 4 -- none,
# fauxpy, best_loc, self_llm). Mirrors repair_research/run_all.sh, but
# pointed at QuixBugs (40 questions, none skipped -- the Refactory
# question-2 skip in run_all.sh doesn't apply here).
#
# Usage:
#   bash run_quixbugs_repair.sh qwen
#   bash run_quixbugs_repair.sh qwen3_27b 1 5 12          # only these questions
#   TYPES="best_loc self_llm" bash run_quixbugs_repair.sh granite4   # only these types

set -euo pipefail

TYPES=(${TYPES:-none fauxpy best_loc self_llm})

REPAIR_MODEL=${1:?Usage: $0 <repair-model> [question-numbers...]}
shift
if [ "$#" -eq 0 ]; then
    QUESTIONS=($(seq 1 40))
else
    QUESTIONS=("$@")
fi
QUESTIONS_ROOT="Data_QuixBugs"
RESULTS_ROOT="Results_QuixBugs/repair"
PYTHON=python

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