# Copilot Instructions for Game Stability Analyzer (GSA)

## 1. Big picture
- Single-package Python library (`gsa`) with a core `GameStabilityAnalyzer` class in `gsa/core.py`.
- Purpose: collect rolling metrics (`fps`, `memory`), compute instability score and status (`STABLE`, `WARNING`, `CRITICAL`).
- `README.md` shows usage pattern: instantiate `GameStabilityAnalyzer`, call `observe(...)`, then `analyze()`.

## 2. Key files and data flows
- `gsa/core.py`: stateful analyzer with 30-point sliding window in `self.history`.
- `observe(metrics)`: append metric dictionary, clamp history size to 30.
- `analyze()`: require at least 5 points then derive `fps_drop`, `memory_spike`, `score`, `status`, `reasons`, and a message.
- `_generate_message(status)`: maps status to human-readable message.

## 3. Project-specific conventions
- No external dependencies in `requirements.txt`.
- Minimal API surface: `GameStabilityAnalyzer` only; avoid introducing unrelated modules unless adding explicit new feature area.
- Numeric thresholds are currently hard-coded: fps drop 10/25, memory spike 300/700, crisp boundary status logic (30,70).
- Comment language includes mixed English/Arabic in one place (`# تحديد الحالة`), maintain this context if you need to adjust logic while preserving intent.

## 4. Development workflow
- No tests currently shipped. Prefer adding unit tests in a `tests/` folder with `pytest` conventions.
- Build/install: `pip install -e .` from project root (if `setup.py`/`pyproject.toml` added later).
- Quick manual smoke:
  - `python -c "from gsa import GameStabilityAnalyzer; g=GameStabilityAnalyzer(); g.observe({'fps':60,'memory':1200}); ..."`

## 5. Feature extensions to keep consistent
- New metrics should follow dictionary-based metric ingestion and be optional (`get('metric',0)` style).
- Maintain fixed history window behavior and the 5-observations minimum for analysis.
- Status classification should remain deterministic and stateless other than history.

## 6. Agent behavior hints
- Avoid large refactors without tests; if adding logic, add focused tests for boundary cases (`fps_drop` exactly 10/25, `memory_spike` exactly 300/700).
- Preserve output schema from `analyze()`: `status`, `crash_score`, `reasons`, `message`.
- Document any change in this file; keep it lean and specific to this repository.

> Feedback request: If any parts of the behavior are unclear (e.g., intended tolerance window, future metric plans), please tell me so I can refine this guide.