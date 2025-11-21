# Lyra Examples

This directory contains example scripts demonstrating various use cases for the Lyra prompt optimizer.

## Running the Examples

```bash
# Make sure you're in the project root directory
cd prompt_choi

# Run the basic usage examples
python examples/basic_usage.py
```

## Available Examples

### basic_usage.py

Comprehensive examples covering:

1. **Simple Optimization** - Quick optimization of a vague prompt
2. **Technical Task** - Optimizing technical prompts for specific platforms
3. **Creative Task** - Enhancing creative writing prompts
4. **Prompt Analysis** - Analyzing complexity and task types
5. **Clarifying Questions** - Generating questions for DETAIL mode
6. **Platform Comparison** - Comparing optimization across platforms

## Example Use Cases

### Marketing & Communications

```python
from lyra import LyraOptimizer

optimizer = LyraOptimizer()

# Marketing email
result = optimizer.optimize(
    "Write a promotional email for our new product launch",
    platform="chatgpt",
    mode="detail"
)
print(result.optimized_prompt)
```

### Software Development

```python
# Code review request
result = optimizer.optimize(
    "Review my Python function for performance issues",
    platform="claude",
    mode="detail"
)
print(result.optimized_prompt)
```

### Content Creation

```python
# Blog post creation
result = optimizer.optimize(
    "Create a blog post about AI trends",
    platform="gemini",
    mode="detail"
)
print(result.optimized_prompt)
```

### Education & Learning

```python
# Tutorial request
result = optimizer.optimize(
    "Explain machine learning to beginners",
    platform="chatgpt",
    mode="detail"
)
print(result.optimized_prompt)
```

## Interactive Testing

You can also test interactively:

```bash
python -m lyra
```

Then try these prompts:

- `BASIC using ChatGPT - Write a resume`
- `DETAIL using Claude - Create a business plan`
- `BASIC using Gemini - Explain quantum computing`

## Advanced Usage

### Custom Analysis

```python
from lyra import LyraOptimizer

optimizer = LyraOptimizer()

# Get detailed analysis
analysis = optimizer.deconstruct("Your prompt here")

print(f"Core Intent: {analysis.core_intent}")
print(f"Task Type: {analysis.task_type}")
print(f"Complexity: {analysis.complexity_score}/10")
print(f"Key Entities: {analysis.key_entities}")
print(f"Clarity Issues: {analysis.clarity_issues}")
```

### Batch Processing

```python
prompts = [
    "Write email",
    "Create presentation",
    "Debug code"
]

for prompt in prompts:
    result = optimizer.optimize(prompt)
    print(f"Original: {prompt}")
    print(f"Optimized: {result.optimized_prompt}\n")
```

## Tips for Best Results

1. **Be Specific About Your Goal**: Even vague prompts get optimized, but starting with some context helps
2. **Choose the Right Mode**: Use BASIC for quick tasks, DETAIL for important/complex work
3. **Specify the Platform**: Different AI platforms have different strengths
4. **Iterate**: Use the optimized prompt, then refine based on results
5. **Answer Clarifying Questions**: In DETAIL mode, addressing the suggested questions can further improve results

## Need Help?

- Check the main [README](../README.md) for comprehensive documentation
- Review the [optimizer.py](../lyra/optimizer.py) source code for implementation details
- Open an issue on GitHub for questions or suggestions
