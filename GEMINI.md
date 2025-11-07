# Gemini Review Context

## Project goals
- Training repo with small algorithmic tasks (CheckiO style).

## Code style
- Prefer readable, simple solutions over micro-optimizations.
- Python: ruff + black, mypy with basic typing.
- Keep functions small and pure where possible.
- Add minimal tests under `tests/`.

## Review expectations
- Point out unclear names, missing edge cases, and complexity.
- Suggest unit tests for corner cases if missing.
- Prefer typing hints on public functions.