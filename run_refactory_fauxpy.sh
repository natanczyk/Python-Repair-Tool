#!/bin/bash
LOG_FILE="run_all_models_log.txt"

start=$(date +%s)
python Faulty_Lines_and_Repair_research/faulty_lines_finder.py \
    --mode fauxpy --questions-root Data --questions 1 2 3 4 5 \
    --results-root Results/localization
elapsed=$(( $(date +%s) - start ))
echo "fauxpy: $(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s" | tee -a $LOG_FILE
