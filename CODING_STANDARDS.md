# Coding Standards

This document outlines the coding standards used in the MCP Weather project for both Python and TypeScript.

## Python Standards

Python code follows [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/). We use `flake8` to enforce these standards.

### Key Standards

- Use 4 spaces for indentation
- Maximum line length of 88 characters
- Use blank lines to separate functions and classes
- Use docstrings for all public modules, functions, classes, and methods
- Import statements should be on separate lines
- Use explicit variable names that describe the purpose
- Add 2 blank lines before top-level functions and classes

### Enforcement

We use `flake8` to enforce these standards. The configuration is in `.flake8` file:

```bash
# Install development dependencies
uv add --dev flake8

# To check for PEP 8 compliance
flake8 weather.py
```

## TypeScript Standards

TypeScript code follows the [Airbnb JavaScript/TypeScript Style Guide](https://github.com/airbnb/javascript). We use ESLint with Airbnb TypeScript configuration to enforce these standards.

### Key Standards

- Use single quotes for strings
- Use camelCase for variables and functions
- Use PascalCase for types and interfaces
- Use semicolons at the end of statements
- Use 2 spaces for indentation
- Avoid using `any` type when possible
- Prefer explicit return types

### Enforcement

We use ESLint with Airbnb TypeScript configuration to enforce these standards:

```bash
# Install ESLint and dependencies
npm install --save-dev eslint @typescript-eslint/parser @typescript-eslint/eslint-plugin eslint-config-airbnb-typescript eslint-plugin-import

# To check for ESLint compliance
npm run lint
```

## Pre-commit Checks

Before committing code, please ensure:

1. All linting checks pass
2. The code builds successfully
3. All tests pass

For Python:
```bash
flake8 weather.py
```

For TypeScript:
```bash
npm run lint
npm run build
```