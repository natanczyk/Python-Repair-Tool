
# I think that assignment-path is redundant, based on submission path name we can choose right test suite from the test_suite folder.
python -m main_pipeline_alfa `
  --submission-path Data\students\lab5ex1_sub.py `
  --test-suite-path Data\test_suites\lab5ex1.py `
  --description-path Data\Descriptions\lab5ex1_description.txt `
  --output-file Data\repaired\lab5ex1_repaired.py `
  --feedback-file Data\results\feedback.txt `
  --analysis-file Data\results\analysis.jsonl `
  --feedback-type 5