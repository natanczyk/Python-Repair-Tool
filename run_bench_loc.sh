#!/bin/bash
# Run LLM localization mode(s) on Data_Bench for one model. Does NOT re-run
# fauxpy (model-independent, assumed already done).
#
# Usage:
#   bash run_bench_all_llm.sh gemma4                     # all 3 modes (default)
#   bash run_bench_all_llm.sh granite4 minimal_notests    # single mode
#   bash run_bench_all_llm.sh granite4 "ranking minimal_tests"

set -euo pipefail

MODEL=${1:?Usage: $0 <model> [mode(s), default: all_llm]}
MODES=${2:-all_llm}
QUESTIONS_ROOT="Data_Bench"
QUESTIONS="easy medium hard"
DESCRIPTIONS_ROOT="Data_Bench/Descriptions"
RESULTS_ROOT="Results_Bench/localization"
LOG_FILE="run_bench_all_llm_log.txt"

echo "============================================" | tee -a "$LOG_FILE"
echo "Started: $(date)"                             | tee -a "$LOG_FILE"
echo "Model  : $MODEL"                               | tee -a "$LOG_FILE"
echo "Mode(s): $MODES"                               | tee -a "$LOG_FILE"
echo "============================================" | tee -a "$LOG_FILE"

start=$(date +%s)
python Faulty_Lines_and_Repair_research/faulty_lines_finder_bench.py \
    --mode $MODES \
    --model "$MODEL" \
    --questions-root "$QUESTIONS_ROOT" \
    --questions $QUESTIONS \
    --descriptions-root "$DESCRIPTIONS_ROOT" \
    --results-root "$RESULTS_ROOT"
elapsed=$(( $(date +%s) - start ))
echo "$MODEL: $(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s" | tee -a "$LOG_FILE"

echo "" | tee -a "$LOG_FILE"
echo "Finished: $(date)" | tee -a "$LOG_FILE"