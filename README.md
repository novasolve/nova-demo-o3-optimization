# Nova Demo Repository - O3 Optimization

This is a demo repository for [Nova Solve](https://github.com/novasolve/nova-solve-v2) - an AI-powered test fixing tool.

## Purpose

This repository contains intentionally buggy code to demonstrate Nova Solve's capabilities:

- **sample.py**: Contains functions with deliberate bugs
- **test_sample.py**: Contains tests that fail due to the bugs

## Usage

This repository is automatically used by Nova Solve's demo mode:

```bash
nova demo
```

Or with the interactive Railway edition:

```bash
python nova_interactive_run_railway.py
```

## Bugs to Fix

1. `add()` - Subtracts instead of adding
2. `multiply()` - Adds instead of multiplying  
3. `divide()` - Returns None instead of raising ZeroDivisionError
4. `concatenate()` - Incorrectly uppercases the second string

## Reset Instructions

To reset this repository for a fresh demo:

```bash
python tools/deployment/clean_demo_repo.py
```

---

Last reset: 2025-07-16 07:19:15 UTC
