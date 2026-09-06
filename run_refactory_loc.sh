#!/bin/bash
# Run all 3 LLM modes (ranking, minimal_tests, minimal_notests) for each model.
# Each model is loaded once and reused across all modes — no redundant reloads.
#
# Usage:
#   ./run_all_experiments.sh                          # run all 7 models
#   ./run_all_experiments.sh gemma4 codegemma codellama  # run specific models
#
# Results are saved as:
#   Data/question_N/llm_<model>_localization.jsonl
#   Data/question_N/llm_<model>_minimal_localization.jsonl
#   Data/question_N/llm_<model>_minimal_notests_localization.jsonl

MODELS="${@:-qwen qwen3_27b qwen3_coder gemma4 codegemma granite4 granite_code codellama}"
QUESTIONS_ROOT="Data"
QUESTIONS="1 2 3 4 5"
RESULTS_ROOT="Results/localization"
LOG_FILE="run_all_experiments_log.txt"

echo "============================================" | tee -a "$LOG_FILE"
echo "Started: $(date)"                             | tee -a "$LOG_FILE"
echo "Models : $MODELS"                             | tee -a "$LOG_FILE"
echo "============================================" | tee -a "$LOG_FILE"

for model in $MODELS; do
    echo "" | tee -a "$LOG_FILE"
    echo ">>> $model — all_llm modes" | tee -a "$LOG_FILE"
    start=$(date +%s)

    python Faulty_Lines_and_Repair_research/faulty_lines_finder.py \
        --mode all_llm \
        --model "$model" \
        --questions-root "$QUESTIONS_ROOT" \
        --questions $QUESTIONS \
        --results-root "$RESULTS_ROOT"

    elapsed=$(( $(date +%s) - start ))
    echo "$model: $(( elapsed / 3600 ))h $(( (elapsed % 3600) / 60 ))m $(( elapsed % 60 ))s" | tee -a "$LOG_FILE"
done

echo "" | tee -a "$LOG_FILE"
echo "Finished: $(date)" | tee -a "$LOG_FILE"
