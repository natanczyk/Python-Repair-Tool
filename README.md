# Localization-Aware LLM Debugging - Thesis Project

In this thesis We want to find the most efficient repairing mode for Introductory Python Submissions. We are comparing FauxPy (spectrum-based fault localization) against 8 LLMs for fault
localization and automated program repair, across three datasets of
increasing structural difference from each other: **Refactory** (real
student submissions to introductory Python assignments), **Bench**
(DebugBench submissions with synthetically injected bugs), and **QuixBugs**
(40 classic algorithms, each with a single seeded bug). We want to find the best repairing configuration achieving highest solve rate. It is also desired to see if Fauxpy outperforms

## Repository structure

```
LLMs/                              Model wrapper classes (one per LLM)
Localization/                      Program + FauxPyRunner (SBFL via FauxPy)
Faulty_Lines_and_Repair_research/  Fault localization pipeline (fauxpy / ranking /
                                    minimal-set-with-tests / minimal-set-without-tests)
repair_research/                   Repair-loop pipeline (none / fauxpy / best_loc / self_llm)
data_tools/                        Dataset construction & ground-truth scripts
analysis/                          Tables + figures for every result in the thesis
  quix_loc/, quix_repair/            QuixBugs localization / repair analysis
  refactory_repair/                  Refactory repair analysis
  bench_loc/                         Bench localization analysis
  (top-level table*.py)              Refactory localization analysis

Data/            Refactory dataset (committed as-is)
Data_Bench/      Bench dataset (built via data_tools/build_bench_dataset.py)
Data_QuixBugs/   QuixBugs adapted into the same question_N/ layout as Data/
                 (built via data_tools/prepare_quixbugs_data.py)
QuixBugs/        Upstream QuixBugs benchmark clone (not committed here -- see below)

results_v2/          Localization + repair result JSONL files, by dataset
repaired_versions/   Saved repaired-code snapshots for solved submissions

run_{refactory,bench,quixbugs}_{loc,fauxpy,repair}.sh   Entry-point scripts
```

## Setup

**Requirements:** Python 3.10 or 3.11. A CUDA-capable GPU is required for
every LLM mode -- `bitsandbytes` 4-bit quantization has no CPU fallback.
Models range from 7B to 34B parameters; the larger ones expect roughly
20-30GB of VRAM even at 4-bit, and several `LLMs/*.py` wrappers use
`device_map="auto"` across two GPUs. Only `fauxpy` mode and the
`data_tools/` dataset-prep scripts run without a GPU.

```bash
python -m venv venv
source venv/bin/activate        # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Several models (e.g. the Gemma family) are gated on HuggingFace and require
being logged in first:

```bash
huggingface-cli login
```

## Dataset setup

**Refactory** (`Data/`) ships as-is in this repo -- no build step.

**Bench** (`Data_Bench/`): built from the DebugBench HuggingFace dataset
(requires internet access):

```bash
python data_tools/build_bench_dataset.py
```

**QuixBugs** (`Data_QuixBugs/`): requires the upstream QuixBugs repo cloned
alongside this project first (it's gitignored here since it carries its own
`.git`):

```bash
git clone https://github.com/jkoppel/QuixBugs.git QuixBugs
python data_tools/prepare_quixbugs_data.py
```

## Running experiments

Each dataset has matching entry-point scripts at the repo root. All accept
a model key from: `qwen`, `qwen3_27b`, `qwen3_coder`, `gemma4`, `granite4`,
`codegemma`, `granite_code`, `codellama`.

**Localization** (produces `fauxpy_localization.jsonl` and
`llm_<model>_*.jsonl` under `results_v2/`):

```bash
bash run_refactory_loc.sh <model>       # or run_quixbugs_loc.sh / run_bench_loc.sh
bash run_refactory_fauxpy.sh            # FauxPy only, no model needed
```

**Repair** (produces `repair_<type>_<model>_results.jsonl`, and saves
solved submissions' repaired code):

```bash
bash run_refactory_repair.sh <model>              # all 4 repair types
TYPES="best_loc self_llm" bash run_quixbugs_repair.sh <model>   # only these types
```

> **Note:** `run_refactory_repair.sh` currently has hardcoded absolute
> paths from the cluster this project was developed on
> (`QUESTIONS_ROOT=/home/guests3/nkg/MASTER_PROJECT/Data`) -- update these
> to your own paths (or switch to relative paths, as the other run scripts
> already do) before running it elsewhere.

## Reproducing the analysis

Every table and figure in the thesis is regenerable from the downloaded
`results_v2/` data. Each analysis package is self-contained; run scripts
from inside their own folder (they resolve paths relative to the repo
root via `Path(__file__).parent.parent[.parent]`):

```bash
cd analysis/quix_repair
python table1_solve_rate.py    # ... through table9_invasiveness.py
```

Tables are saved as CSV to `tables/`, figures as PNG to `figures/`, within
each analysis package's own folder.

