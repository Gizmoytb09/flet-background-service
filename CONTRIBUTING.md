# Contributing to flet-background-service

<div align="center">

<img src="https://img.shields.io/badge/PRs-welcome-brightgreen?style=for-the-badge&logo=github" alt="PRs Welcome"/>
&nbsp;
<img src="https://img.shields.io/badge/status-Beta-orange?style=for-the-badge" alt="Beta"/>
&nbsp;
<img src="https://img.shields.io/badge/code%20style-ruff-5e81f4?style=for-the-badge" alt="Ruff"/>

</div>

---

Thank you for your interest in contributing to **flet-background-service**! 🎉  
This library is in **Beta development**, so your feedback and pull requests are especially valuable during this phase.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Code Style](#code-style)
- [Testing](#testing)
- [Commit Conventions](#commit-conventions)
- [Submitting a Pull Request](#submitting-a-pull-request)
- [Reporting Issues](#reporting-issues)

---

## Code of Conduct

Please be respectful and constructive in all interactions. We follow the [Contributor Covenant](https://www.contributor-covenant.org/) Code of Conduct.

---

## Getting Started

### Prerequisites

- Python **3.12+**
- Flet **≥ 0.83.0**
- A working Android or iOS build environment if testing on device

### Fork & Clone

```bash
# 1. Fork the repo on GitHub, then clone your fork:
git clone https://github.com/<your-username>/flet-background-service.git
cd flet-background-service

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux / macOS
.venv\Scripts\activate           # Windows

# 3. Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

---

## Development Workflow

```bash
# Create a feature branch
git checkout -b feat/my-feature

# Make your changes …

# Lint
ruff check src/ examples/
ruff format src/ examples/

# Type-check
mypy src/

# Commit and push
git add .
git commit -m "feat: describe your change"
git push origin feat/my-feature

# Open a Pull Request on GitHub
```

---

## Code Style

This project uses **Ruff** for linting and formatting, and **Mypy** with `strict = true` for type checking.

| Tool | Config |
|------|--------|
| `ruff` | `pyproject.toml` → `[tool.ruff]` |
| `mypy` | `pyproject.toml` → `[tool.mypy]` |

Ruff will automatically catch:
- Import ordering (`isort` equivalent)
- Unused imports, variables
- Bugbear rules
- Type annotation issues

Run before every commit:

```bash
ruff check src/ && ruff format --check src/ && mypy src/
```

---

## Testing

Tests live in `tests/` (not yet created — **contributions for test coverage are highly welcome!**).

```bash
pytest tests/ -v
```

---

## Commit Conventions

We use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | When to use |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation changes |
| `refactor:` | Code refactoring |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance tasks |
| `ci:` | CI/CD changes |

Example: `feat: add update_notification overload for custom icon`

---

## Submitting a Pull Request

1. Ensure all linting and type checks pass.
2. Add or update docstrings where applicable.
3. Update `CHANGELOG.md` with a brief description under `[Unreleased]`.
4. Reference any related issues with `Closes #<issue-number>`.
5. Open a PR with a clear title and description of the change.

---

## Reporting Issues

Use the [GitHub Issues](https://github.com/Gizmoytb09/flet-background-service/issues) tracker.

Please include:
- **Platform**: Android version / iOS version
- **Flet version**: `pip show flet`
- **Package version**: `pip show flet-background-service`
- **Minimal reproducible example**
- **Expected vs actual behavior**

---

<div align="center">
<sub>Thank you for helping make <strong>flet-background-service</strong> better! 💙</sub>
</div>
