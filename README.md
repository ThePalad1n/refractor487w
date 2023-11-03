# Refactoring and CI Integration for 487W

## Description

This repository contains the refactored codebase for the 487W assignment. The main focus of this assignment was to improve the code quality by refactoring and to ensure the robustness of the application through comprehensive test cases. Furthermore, we integrated a Continuous Integration (CI) pipeline to automate the testing process, ensuring that all new changes pass the defined tests before they can be merged into the main branch.

## Getting Started

### Dependencies

- Python 3.10.8 or higher
- Pip for managing Python packages
- Any additional packages can be installed via `pip install -r requirements.txt`

### Installing

- Clone the repository using `git clone <repo_url>`
- Install the required packages using `pip install -r requirements.txt`

### Executing Program

- To run the program, use `python app.py` (replace `app.py` with your script name)
- Make sure to activate the virtual environment if you are using one before running the script.

## Refactoring

The refactoring process involved:

- Improving code readability and maintainability
- Optimizing performance
- Reducing complexity
- Ensuring code consistency and adhering to PEP 8 style guidelines

## Testing

Tests have been written to cover a wide range of scenarios and edge cases. To manually run the tests:

```sh
poetry run pytest --cov=src tests/
```

## Continuous Integration (CI)

Continuous Integration is set up via GitHub Actions/Travis CI/GitLab CI (choose appropriate service). The CI pipeline is triggered on every push and pull request to the main branch and runs the entire suite of unit tests.

## Contributing

1. Fork it ( `https://github.com/yourname/487w-refactor-assignment/fork` )
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
