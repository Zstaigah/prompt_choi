"""
Setup script for Lyra - AI Prompt Optimization Framework
"""

from setuptools import setup, find_packages

# Read the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="lyra-prompt-optimizer",
    version="1.0.0",
    author="Lyra Team",
    author_email="",
    description="Transform vague requests into precision-crafted prompts that unlock AI's full potential",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zstaigah/prompt_choi",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - uses Python standard library only
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    entry_points={
        "console_scripts": [
            "lyra=lyra.cli:main",
        ],
    },
    keywords="ai prompt optimization gpt chatgpt claude gemini prompt-engineering",
    project_urls={
        "Bug Reports": "https://github.com/Zstaigah/prompt_choi/issues",
        "Source": "https://github.com/Zstaigah/prompt_choi",
        "Documentation": "https://github.com/Zstaigah/prompt_choi#readme",
    },
)
