#!/usr/bin/env python3
"""
Basic usage examples for Lyra Prompt Optimizer

This script demonstrates common use cases for the Lyra optimizer.
"""

from lyra import LyraOptimizer


def example_1_simple_optimization():
    """Example 1: Simple prompt optimization"""
    print("=" * 70)
    print("EXAMPLE 1: Simple Optimization")
    print("=" * 70)

    optimizer = LyraOptimizer()

    # Original vague prompt
    original = "Write email"

    # Optimize it
    result = optimizer.optimize(original, platform="other", mode="basic")

    print(f"\nOriginal prompt: {original}")
    print(f"\nOptimized prompt:\n{result.optimized_prompt}")
    print(f"\nImprovements made:")
    for improvement in result.improvements:
        print(f"  • {improvement}")
    print("\n")


def example_2_technical_task():
    """Example 2: Technical task with specific platform"""
    print("=" * 70)
    print("EXAMPLE 2: Technical Task for ChatGPT")
    print("=" * 70)

    optimizer = LyraOptimizer()

    # Technical prompt
    original = "Help me fix my Python code that's not working"

    # Optimize for ChatGPT with DETAIL mode
    result = optimizer.optimize(original, platform="chatgpt", mode="detail")

    print(f"\nOriginal prompt: {original}")
    print(f"\nOptimized prompt:\n{result.optimized_prompt}")
    print(f"\nTechniques applied: {', '.join(result.techniques_applied)}")
    print(f"\nPro tip: {result.pro_tip}")
    print("\n")


def example_3_creative_task():
    """Example 3: Creative task for Claude"""
    print("=" * 70)
    print("EXAMPLE 3: Creative Task for Claude")
    print("=" * 70)

    optimizer = LyraOptimizer()

    # Creative prompt
    original = "Write a story about space"

    # Optimize for Claude
    result = optimizer.optimize(original, platform="claude", mode="detail")

    print(f"\nOriginal prompt: {original}")
    print(f"\nOptimized prompt:\n{result.optimized_prompt}")
    print(f"\nKey improvements:")
    for improvement in result.improvements:
        print(f"  • {improvement}")
    print("\n")


def example_4_analysis():
    """Example 4: Analyzing prompt complexity"""
    print("=" * 70)
    print("EXAMPLE 4: Prompt Analysis")
    print("=" * 70)

    optimizer = LyraOptimizer()

    prompts_to_analyze = [
        "Help",
        "Write a professional email to my team",
        "Create a comprehensive business plan with financial projections, market analysis, and growth strategy"
    ]

    for prompt in prompts_to_analyze:
        analysis = optimizer.deconstruct(prompt)

        print(f"\nPrompt: '{prompt}'")
        print(f"  Task Type: {analysis.task_type.value}")
        print(f"  Complexity: {analysis.complexity_score}/10")
        print(f"  Context Level: {analysis.context_level}")
        print(f"  Key Entities: {', '.join(analysis.key_entities) if analysis.key_entities else 'None'}")
        if analysis.clarity_issues:
            print(f"  Issues: {', '.join(analysis.clarity_issues)}")

    print("\n")


def example_5_clarifying_questions():
    """Example 5: Generate clarifying questions"""
    print("=" * 70)
    print("EXAMPLE 5: Clarifying Questions (DETAIL Mode)")
    print("=" * 70)

    optimizer = LyraOptimizer()

    # Vague prompt that needs clarification
    original = "Write a report"

    # Get analysis and questions
    analysis = optimizer.deconstruct(original)
    questions = optimizer.generate_clarifying_questions(analysis)

    print(f"\nOriginal prompt: '{original}'")
    print(f"\nClarifying questions that could improve this prompt:")
    for i, question in enumerate(questions, 1):
        print(f"  {i}. {question}")
    print("\n")


def example_6_comparison():
    """Example 6: Compare platforms"""
    print("=" * 70)
    print("EXAMPLE 6: Platform-Specific Optimization")
    print("=" * 70)

    optimizer = LyraOptimizer()

    original = "Explain how blockchain works"
    platforms = ["chatgpt", "claude", "gemini"]

    for platform in platforms:
        result = optimizer.optimize(original, platform=platform, mode="basic")
        print(f"\n--- Optimized for {platform.upper()} ---")
        print(result.optimized_prompt)
        print()


if __name__ == "__main__":
    # Run all examples
    example_1_simple_optimization()
    example_2_technical_task()
    example_3_creative_task()
    example_4_analysis()
    example_5_clarifying_questions()
    example_6_comparison()

    print("=" * 70)
    print("All examples completed!")
    print("=" * 70)
