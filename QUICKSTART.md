# Lyra Quick Start Guide

Get started with Lyra in under 5 minutes!

## Installation

```bash
# Clone the repository
git clone https://github.com/Zstaigah/prompt_choi.git
cd prompt_choi

# That's it! No dependencies to install
```

## First Run

### Interactive Mode (Recommended for Beginners)

```bash
python -m lyra
```

You'll see:
```
======================================================================
Hello! I'm Lyra, your AI prompt optimizer...
======================================================================

Enter your prompt (or 'quit' to exit):
>
```

Try typing:
```
BASIC using ChatGPT - Write a blog post
```

Or:
```
DETAIL using Claude - Help me create a presentation
```

### Command-Line Mode

```bash
# Basic usage
python -m lyra "Write a marketing email"

# With specific platform and mode
python -m lyra --mode detail --platform chatgpt "Write a resume"

# Short form
python -m lyra -m detail -p claude "Debug my code"
```

## Common Use Cases

### 1. Marketing & Business

```bash
python -m lyra "Create an email campaign for our product launch"
```

### 2. Software Development

```bash
python -m lyra -m detail -p chatgpt "Review my Python function for bugs"
```

### 3. Content Creation

```bash
python -m lyra -p gemini "Write a creative story about space exploration"
```

### 4. Learning & Education

```bash
python -m lyra "Explain blockchain to a beginner"
```

## Understanding the Output

When you run Lyra, you'll get:

```
YOUR OPTIMIZED PROMPT:
======================================================================
[Your improved prompt here - copy and paste this into any AI]
======================================================================

WHAT CHANGED:
• Fixed clarity issues
• Enhanced specificity and detail
• Added clear output specifications
• Optimized for [task type] tasks
```

## Tips for Best Results

1. **Specify Your Platform**: Different AIs have different strengths
   - ChatGPT: Great for conversations, coding
   - Claude: Excellent for analysis, long contexts
   - Gemini: Strong at creative, comparative tasks

2. **Choose the Right Mode**:
   - BASIC: Quick optimization (5 seconds)
   - DETAIL: Comprehensive enhancement (may ask questions)

3. **Start Simple**: Don't worry about making your prompt perfect - Lyra will fix it!

## Example Progression

### Level 1: Very Vague
```
Input: "help with code"

Output: A detailed prompt specifying:
- What kind of code help you need
- The programming language
- What you want to achieve
- Output format
```

### Level 2: Somewhat Clear
```
Input: "Write a Python function to sort data"

Output: An optimized prompt with:
- Technical role assignment
- Specific requirements
- Best practices
- Error handling needs
- Output expectations
```

### Level 3: Already Good
```
Input: "Create a Python function that sorts a list of dictionaries
        by a specific key, handles missing keys gracefully, and includes
        unit tests"

Output: A refined prompt with:
- Enhanced structure
- Platform-specific formatting
- Additional technical constraints
- Clear success criteria
```

## Python API Usage

```python
from lyra import LyraOptimizer

# Create optimizer
optimizer = LyraOptimizer()

# Optimize a prompt
result = optimizer.optimize(
    prompt="Write a blog post",
    platform="chatgpt",
    mode="detail"
)

# Use the result
print(result.optimized_prompt)
print(result.improvements)
print(result.pro_tip)
```

## What's Next?

- ✅ Read the full [README.md](README.md) for comprehensive documentation
- ✅ Explore [examples/basic_usage.py](examples/basic_usage.py) for code examples
- ✅ Try different modes and platforms
- ✅ Check out [CONTRIBUTING.md](CONTRIBUTING.md) to help improve Lyra

## Troubleshooting

### "Command not found"

Make sure you're in the project directory:
```bash
cd prompt_choi
python -m lyra
```

### "No module named 'lyra'"

Ensure you're running from the project root:
```bash
# Check your location
pwd

# Should show: .../prompt_choi

# If not, navigate there
cd /path/to/prompt_choi
```

### Python Version

Lyra requires Python 3.7 or higher:
```bash
python --version
# Should show: Python 3.7.x or higher
```

## Need Help?

- 📖 Full documentation: [README.md](README.md)
- 💬 Open an issue: [GitHub Issues](https://github.com/Zstaigah/prompt_choi/issues)
- 🔍 Check examples: [examples/](examples/)

---

**Happy optimizing! 🚀**
