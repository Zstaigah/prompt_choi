# Lyra - AI Prompt Optimization Framework

> Transform vague requests into precision-crafted prompts that unlock AI's full potential

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Lyra is a master-level AI prompt optimization specialist that uses a proven 4-D methodology to transform any user input into highly effective prompts across all AI platforms (ChatGPT, Claude, Gemini, and more).

## 🌟 Features

- **4-D Methodology**: Deconstruct → Diagnose → Develop → Deliver
- **Platform-Optimized**: Tailored formatting for ChatGPT, Claude, Gemini
- **Dual Operating Modes**: BASIC (quick fixes) and DETAIL (comprehensive optimization)
- **Intelligent Analysis**: Automatic task type detection and complexity scoring
- **Interactive CLI**: User-friendly command-line interface
- **Python API**: Programmatic access for integration

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Zstaigah/prompt_choi.git
cd prompt_choi

# No external dependencies required - uses Python standard library only
```

### Interactive Mode

```bash
# Launch interactive CLI
python -m lyra

# Or use the convenience script
python lyra_app.py
```

### Command-Line Usage

```bash
# Basic optimization
python -m lyra "Write a marketing email"

# Specify platform and mode
python -m lyra --mode detail --platform chatgpt "Write a marketing email"

# Short form
python -m lyra -m detail -p claude "Help debug my code"
```

### Python API

```python
from lyra import LyraOptimizer

# Create optimizer instance
optimizer = LyraOptimizer()

# Optimize a prompt
result = optimizer.optimize(
    prompt="Write me a blog post",
    platform="chatgpt",
    mode="detail"
)

# Access the results
print(result.optimized_prompt)
print(result.improvements)
print(result.pro_tip)
```

## 📚 The 4-D Methodology

### 1. **DECONSTRUCT**
Extract core intent, key entities, context, requirements, and constraints from your prompt.

### 2. **DIAGNOSE**
Audit for clarity gaps, ambiguity, specificity issues, and completeness.

### 3. **DEVELOP**
Apply advanced techniques:
- **Creative tasks**: Multi-perspective analysis
- **Technical tasks**: Constraint-based optimization
- **Educational tasks**: Few-shot examples + clear structure
- **Complex tasks**: Chain-of-thought + systematic frameworks

### 4. **DELIVER**
Construct optimized prompt with platform-specific formatting and implementation guidance.

## 🎯 Operating Modes

### BASIC Mode
- Quick optimization of primary issues
- Core techniques only
- Ready-to-use prompt in seconds

### DETAIL Mode
- Comprehensive context gathering
- 2-3 targeted clarifying questions
- Advanced optimization techniques
- Platform-specific enhancements

## 💡 Usage Examples

### Example 1: Simple Request (BASIC Mode)

**Input:**
```
Write email
```

**Output:**
```
You are a professional communication specialist with expertise in email writing.

**Task:** Write a professional email

**Output Requirements:**
- Clear and well-structured response
- Specific and actionable information
- Appropriate tone for the context
```

### Example 2: Complex Request (DETAIL Mode)

**Input:**
```
DETAIL using ChatGPT - Create a technical documentation guide for our API
```

**Output:**
```
You are an experienced technical specialist with deep expertise in
software development and problem-solving.

**Task:** Create a comprehensive technical documentation guide for an API

**Focus areas:** API, technical, documentation, guide

**Output Requirements:**
- Clear structure with sections for authentication, endpoints, examples
- Code snippets with multiple language implementations
- Error handling and status codes documentation
- Best practices and rate limiting information

**Technical Requirements:**
- Follow best practices and coding standards
- Consider edge cases and error handling
- Optimize for performance and maintainability

**Approach:** Break this down systematically and explain your reasoning.
```

### Example 3: Interactive Mode

```
$ python -m lyra

======================================================================
Hello! I'm Lyra, your AI prompt optimizer. I transform vague requests
into precise, effective prompts that deliver better results.

**What I need to know:**
• Target AI: ChatGPT, Claude, Gemini, or Other
• Prompt Style: DETAIL (I'll ask clarifying questions first) or BASIC
  (quick optimization)

**Examples:**
• "DETAIL using ChatGPT - Write me a marketing email"
• "BASIC using Claude - Help with my resume"
======================================================================

Enter your prompt (or 'quit' to exit):
> DETAIL using Claude - Help me write a blog post about AI

🔍 Analyzing your prompt... (Mode: DETAIL, Platform: CLAUDE)

======================================================================
YOUR OPTIMIZED PROMPT:
======================================================================
[Optimized prompt displayed here]
...
```

## 🏗️ Project Structure

```
prompt_choi/
├── lyra/
│   ├── __init__.py          # Package initialization
│   ├── optimizer.py         # Core optimization engine
│   ├── cli.py              # Command-line interface
│   └── __main__.py         # Module entry point
├── lyra_app.py             # Convenience script
├── examples/               # Usage examples
├── tests/                  # Unit tests
├── README.md              # This file
└── LICENSE                # MIT License
```

## 🔧 Advanced Features

### Custom Platform Configuration

```python
from lyra import LyraOptimizer
from lyra.optimizer import AIPlatform

optimizer = LyraOptimizer()

# Optimize for specific platform
result = optimizer.optimize(
    prompt="Explain quantum computing",
    platform="claude",  # Optimized for Claude's longer context
    mode="detail"
)
```

### Complexity Analysis

```python
# Get detailed analysis of your prompt
analysis = optimizer.deconstruct("Your prompt here")

print(f"Task Type: {analysis.task_type}")
print(f"Complexity Score: {analysis.complexity_score}/10")
print(f"Key Entities: {analysis.key_entities}")
print(f"Clarity Issues: {analysis.clarity_issues}")
```

### Clarifying Questions (DETAIL Mode)

```python
analysis = optimizer.deconstruct("Write a report")
questions = optimizer.generate_clarifying_questions(analysis)

for question in questions:
    print(f"- {question}")
# Output:
# - What format would you like the output in?
# - Who is the target audience?
# - What length are you aiming for?
```

## 📊 Optimization Techniques

Lyra automatically selects and applies appropriate techniques:

- **Role Assignment**: Assigns expert persona based on task type
- **Context Layering**: Enhances insufficient context
- **Output Specifications**: Defines clear deliverables
- **Task Decomposition**: Breaks complex tasks into steps
- **Chain-of-Thought**: Encourages systematic reasoning
- **Few-Shot Learning**: Provides examples for clarity
- **Multi-Perspective**: Explores creative angles
- **Constraint Optimization**: Applies technical requirements

## 🎓 Supported Task Types

Lyra recognizes and optimizes for:

- **Creative**: Stories, content, brainstorming
- **Technical**: Code, debugging, architecture
- **Analytical**: Data analysis, comparisons, research
- **Educational**: Explanations, tutorials, learning
- **Complex**: Multi-step, systematic challenges
- **Simple**: Quick, straightforward requests

## 🌐 Platform Support

### ChatGPT / GPT-4
- Structured sections
- Clear conversation starters
- Concise formatting

### Claude
- Longer context windows
- Reasoning frameworks
- Detailed explanations

### Gemini
- Creative task optimization
- Comparative analysis
- Multi-perspective approaches

### Other Platforms
- Universal best practices
- Flexible formatting
- Core optimization techniques

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Inspired by best practices in prompt engineering
- Built with insights from the AI research community
- Designed for developers, writers, researchers, and AI enthusiasts

## 📞 Contact

- **Project**: [prompt_choi](https://github.com/Zstaigah/prompt_choi)
- **Issues**: [GitHub Issues](https://github.com/Zstaigah/prompt_choi/issues)

---

**Made with ❤️ by the Lyra team**

*Transform your prompts. Unlock AI's potential.*