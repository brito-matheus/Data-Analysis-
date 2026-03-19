# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Overview

Data analysis project using R and Python.

## Repository Structure

- `codes/` — analysis scripts (R and Python)
- `Datasets/` — raw and processed data files (not tracked by git)
- `Material/` — reference materials (not tracked by git)

## Guidelines

- Keep scripts inside `codes/`
- `Datasets/` and `Material/` are gitignored — do not reference absolute paths to them in committed code
- Prefer relative paths when loading data (e.g., `../Datasets/file.csv`)