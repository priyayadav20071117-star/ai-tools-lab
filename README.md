# ai-tools-lab
# AI Tools Lab

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)

A beginner-friendly Python project that brings together classic **sorting algorithms** and handy **utility functions**. Every function is written to be simple, well documented, and easy to read, so it works equally well as a learning resource or as a small toolkit for your own projects.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Contributors](#contributors)
- [License](#license)

## Features

- **Sorting algorithms** implemented in plain Python with clear comments
- **Utility functions** for common everyday tasks
- Docstrings on every function
- No external dependencies required
- Easy to read, run, and extend

## Project Structure

```
ai-tools-lab/
├── sorting.py      # Sorting algorithms
├── utils.py        # Utility functions
├── README.md
└── LICENSE
```

## Installation

**Requirements:** Python 3.8 or newer. You can check your version with `python --version`.

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/ai-tools-lab.git
   ```

2. **Move into the project folder**

   ```bash
   cd ai-tools-lab
   ```

3. **(Optional) Create a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate      # On Windows: venv\Scripts\activate
   ```

That's it. The project has no dependencies, so there is nothing else to install.

## Usage

Import the functions you need directly from the modules.

### Utility functions

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

# Check if text reads the same forwards and backwards
print(is_palindrome("Racecar"))                          # True
print(is_palindrome("A man, a plan, a canal: Panama"))   # True
print(is_palindrome("Hello"))                            # False

# Count the words in a piece of text
print(count_words("The quick brown fox"))                # 4

# Convert a temperature from Celsius to Fahrenheit
print(celsius_to_fahrenheit(100))                        # 212.0
```

### Sorting algorithms

```python
from sorting import bubble_sort

numbers = [5, 2, 9, 1, 7]
print(bubble_sort(numbers))                              # [1, 2, 5, 7, 9]
```

### Try the built-in examples

Each module includes a small demo that runs when you execute the file directly:

```bash
python utils.py
```

## Contributing

Contributions are welcome, and beginners are encouraged to join in!

1. Fork this repository
2. Create a new branch: `git checkout -b feature/my-new-feature`
3. Make your changes and add a docstring to any new function
4. Commit your work: `git commit -m "Add my new feature"`
5. Push to your branch: `git push origin feature/my-new-feature`
6. Open a Pull Request

Please keep the code simple and readable, in keeping with the spirit of the project.

## Contributors

Thanks to everyone who has helped make this project better.

| Name | GitHub | Role |
| ---- | ------ | ---- |
| **priya yadav** | [@priyayadav20071117-star](https://github.com/priyayadav20071117-star) | Creator & Maintainer |

Want to see your name here? See the [Contributing](#contributing) section.

## License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2026 Your Name

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```