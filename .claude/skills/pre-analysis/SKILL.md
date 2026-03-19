---
name: pre-analysis
description: Perform a structured exploratory pre-analysis of a dataset (variable overview, descriptives, visualizations, correlation) and generate a Quarto document.
argument-hint: "[path/to/dataset.csv]"
---

# Pre-Analysis Skill

Perform a structured exploratory pre-analysis of a dataset and generate a Quarto document with the results.

## Instructions

The user will provide a dataset (file path or a dataframe already loaded in context). Follow these steps:

### 1. Identify the language and data

- Detect whether the project uses **R** or **Python** and adapt the code accordingly.
- Identify the dataset: file path, variable name, or ask the user if unclear.
- Identify the output file name for the Quarto document (default: `pre_analysis_<dataset_name>.qmd`).

### 2. Create the output folder

- Check if a `pre_analysis/` folder exists in the project root. If not, create it.

### 3. Generate a Quarto document

Create a `.qmd` file inside `pre_analysis/` with the following sections:

#### Section 1 — Variable overview
- List all variables (columns) with their data types.
- Classify each as: numeric continuous, numeric discrete, categorical (nominal/ordinal), datetime, or other.

#### Section 2 — Descriptive statistics
- For **numeric** variables: n, mean, median, std, min, max, q1, q3, number of NAs.
- For **categorical** variables: n, number of unique levels, mode, frequency table (top 10), number of NAs.
- Present as a formatted table.

#### Section 3 — Visualizations
- If the dataset has **more than 10 variables**, ask the user to select a subset before generating plots. List the available variables and wait for confirmation.
- For **numeric** variables: histogram + boxplot (use a combined layout).
- For **categorical** variables: bar chart of frequencies.
- For **datetime** variables: line plot of counts over time.
- Label axes clearly, use a clean theme.

#### Section 4 — Correlation analysis
- Compute a correlation matrix for all **numeric** variables.
- Render it as a heatmap with correlation values annotated.
- Highlight pairs with |correlation| > 0.7.
- If there are fewer than 2 numeric variables, note that correlation is not applicable.

### 4. Tracking and log

- Add a **YAML header** to the Quarto document with:
  - `title`, `author` (ask if unknown), `date` (today's date), `format: html`
  - `execute: echo: true` so all code is shown
- Add a **log chunk** at the top of the document that prints:
  - Session/environment info (R: `sessionInfo()` / Python: `sys.version`, library versions)
  - Timestamp of when the document was rendered
- At the end of the document, add a **Session Info** section that captures the full environment.

### 5. Render (optional)

- Ask the user if they want to render the document immediately after creation.
- If yes, run `quarto render <file>` and report success or errors.

## Code style

- **R**: use `tidyverse` (dplyr, ggplot2, tidyr), `skimr` for descriptives, `corrplot` or `ggcorrplot` for correlations, `knitr::kable` or `gt` for tables.
- **Python**: use `pandas`, `matplotlib`/`seaborn` for plots, `pandas-profiling` or manual stats, `seaborn.heatmap` for correlation.
- Keep chunks labeled and organized (`#| label: ...`).
- Use `#| warning: false` and `#| message: false` on setup chunks.

## Output

Tell the user:
- The path to the created `.qmd` file.
- How to render it (`quarto render <path>`).
- A summary of what was found (number of variables, types breakdown, any notable correlations or missing data).