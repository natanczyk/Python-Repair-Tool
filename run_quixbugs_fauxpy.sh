#!/bin/bash
# Run FauxPy (SBFL) localization on Data_QuixBugs (40 questions).
# No model/GPU needed -- fast, single pass, model-independent.
#
# Usage:
#   bash run_quixbugs_fauxpy.sh

set -euo pipefail

QUESTIONS_ROOT="Data_QuixBugs"
QUESTIONS=$(seq 1 40)
RESULTS_ROOT="Results_QuixBugs/localization"
LOG_FILE="run_quixbugs_fauxpy_log.txt"

echo "============================================" | tee -a "$LOG_FILE"
echo "Started: $(date)"                             | tee -a "$LOG_FILE"
echo "Mode   : fauxpy"                               | tee -a "$LOG_FILE"
echo "============================================" | tee -a "$LOG_FILE"

start=$(date +%s)
PYTHONPATH=. python Faulty_Lines_and_Repair_research/faulty_lines_finder.py \
    --mode fauxpy \
    --questions-root "$QUESTIONS_ROOT" \
    --questions $QUESTIONS \
    --results-root "$RESULTS_ROOT"
elapsed=$(( $(date +%s) - start ))
echo "fauxpy: $(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s" | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "Finished: $(date)" | tee -a "$LOG_FILE"