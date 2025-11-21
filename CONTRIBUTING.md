# Contributing to Lyra

Thank you for your interest in contributing to Lyra! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

If you find a bug, please open an issue on GitHub with:

1. A clear, descriptive title
2. Steps to reproduce the issue
3. Expected behavior
4. Actual behavior
5. Your environment (Python version, OS, etc.)

### Suggesting Enhancements

We love new ideas! To suggest an enhancement:

1. Open an issue with the tag "enhancement"
2. Describe the feature and its benefits
3. Provide examples of how it would be used
4. Discuss any potential drawbacks

### Pull Requests

1. **Fork the repository** and create your branch from `main`

2. **Make your changes**:
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

3. **Test your changes**:
   ```bash
   # Run the examples to ensure everything works
   python examples/basic_usage.py

   # Test the CLI
   python -m lyra "Test prompt"
   ```

4. **Commit your changes**:
   - Use clear, descriptive commit messages
   - Reference any related issues

5. **Push to your fork** and submit a pull request

6. **Wait for review**:
   - Address any feedback
   - Make requested changes
   - Engage in discussion

## Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/prompt_choi.git
cd prompt_choi

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise
- Comment complex logic

## Testing

Before submitting a PR, test your changes:

```bash
# Test CLI functionality
python -m lyra "Test prompt"

# Test with different modes
python -m lyra -m detail -p chatgpt "Test prompt"

# Run examples
python examples/basic_usage.py

# Test imports
python -c "from lyra import LyraOptimizer; print('Success!')"
```

## Documentation

When adding new features:

1. Update the README.md if needed
2. Add docstrings to new functions/classes
3. Include usage examples
4. Update the examples/ directory if applicable

## Areas for Contribution

We're particularly interested in:

### Features
- Additional optimization techniques
- Support for more AI platforms
- Enhanced task type detection
- Multilingual prompt support
- Web interface

### Improvements
- Performance optimizations
- Better error handling
- Enhanced CLI experience
- More detailed analysis

### Documentation
- More usage examples
- Video tutorials
- Translation to other languages
- API documentation

### Testing
- Unit tests
- Integration tests
- Edge case coverage

## Community Guidelines

- Be respectful and inclusive
- Provide constructive feedback
- Help others when possible
- Stay on topic in discussions
- Follow the code of conduct

## Recognition

Contributors will be acknowledged in:
- The README.md contributors section
- Release notes
- GitHub contributors page

## Questions?

- Open a discussion on GitHub
- Check existing issues and PRs
- Review the documentation

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

Thank you for helping make Lyra better! 🚀
