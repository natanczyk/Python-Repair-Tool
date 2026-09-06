#!/bin/bash
# Run all 3 LLM localization modes (ranking, minimal_tests, minimal_notests)
# on Data_QuixBugs (40 questions) for one or more models, one at a time
# (each model loaded once, reused across all 3 modes and 40 questions).
# Does NOT run fauxpy.
#
# Usage:
#   bash run_quixbugs_all_llm.sh gemma4
#   bash run_quixbugs_all_llm.sh gemma4 granite_code qwen
#   HF_HUB_DISABLE_XET=1 bash run_quixbugs_all_llm.sh gemma4 granite_code qwen

set -euo pipefail

if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <model> [model2] [model3] ..."
    exit 1
fi

QUESTIONS_ROOT="Data_QuixBugs"
QUESTIONS=$(seq 1 40)
RESULTS_ROOT="Results_QuixBugs/localization"
LOG_FILE="run_quixbugs_all_llm_log.txt"

for MODEL in "$@"; do
    echo "============================================" | tee -a "$LOG_FILE"
    echo "Started: $(date)"                             | tee -a "$LOG_FILE"
    echo "Model  : $MODEL"                               | tee -a "$LOG_FILE"
    echo "============================================" | tee -a "$LOG_FILE"

    start=$(date +%s)
    python Faulty_Lines_and_Repair_research/faulty_lines_finder.py \
        --mode all_llm \
        --model "$MODEL" \
        --questions-root "$QUESTIONS_ROOT" \
        --questions $QUESTIONS \
        --results-root "$RESULTS_ROOT"
    elapsed=$(( $(date +%s) - start ))
    echo "$MODEL: $(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s" | tee -a "$LOG_FILE"

    echo "" | tee -a "$LOG_FILE"
    echo "Finished $MODEL: $(date)" | tee -a "$LOG_FILE"
done

echo "All models done." | tee -a "$LOG_FILE"