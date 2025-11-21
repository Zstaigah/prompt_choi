#!/usr/bin/env python3
"""
Lyra CLI - Interactive command-line interface for prompt optimization

Usage:
    python -m lyra.cli
    python -m lyra.cli --mode detail --platform chatgpt "Your prompt here"
"""

import sys
import argparse
from typing import Optional
from .optimizer import LyraOptimizer, Mode


class LyraCLI:
    """Command-line interface for Lyra prompt optimizer"""

    def __init__(self):
        self.optimizer = LyraOptimizer()
        self.platform = None
        self.mode = None

    def print_welcome(self):
        """Display welcome message"""
        print("\n" + "=" * 70)
        print(self.optimizer.get_welcome_message())
        print("=" * 70 + "\n")

    def format_result_simple(self, result, show_techniques: bool = False):
        """Format and display optimization result for simple requests"""
        print("\n" + "=" * 70)
        print("YOUR OPTIMIZED PROMPT:")
        print("=" * 70)
        print(result.optimized_prompt)
        print("\n" + "-" * 70)
        print("WHAT CHANGED:")
        for improvement in result.improvements:
            print(f"  • {improvement}")

        if show_techniques and result.techniques_applied:
            print("\n" + "-" * 70)
            print("TECHNIQUES APPLIED:")
            print(f"  {', '.join(result.techniques_applied)}")

        print("=" * 70 + "\n")

    def format_result_complex(self, result):
        """Format and display optimization result for complex requests"""
        print("\n" + "=" * 70)
        print("YOUR OPTIMIZED PROMPT:")
        print("=" * 70)
        print(result.optimized_prompt)

        print("\n" + "-" * 70)
        print("KEY IMPROVEMENTS:")
        for improvement in result.improvements:
            print(f"  • {improvement}")

        if result.techniques_applied:
            print("\n" + "-" * 70)
            print("TECHNIQUES APPLIED:")
            print(f"  {', '.join(result.techniques_applied)}")

        if result.pro_tip:
            print("\n" + "-" * 70)
            print("PRO TIP:")
            print(f"  {result.pro_tip}")

        print("=" * 70 + "\n")

    def interactive_mode(self):
        """Run in interactive mode"""
        self.print_welcome()

        while True:
            try:
                # Get user input
                print("\nEnter your prompt (or 'quit' to exit):")
                print("Format: [DETAIL/BASIC] using [Platform] - Your prompt")
                print("Example: DETAIL using ChatGPT - Write me a marketing email\n")

                user_input = input("> ").strip()

                if user_input.lower() in ['quit', 'exit', 'q']:
                    print("\nThank you for using Lyra! Goodbye.\n")
                    break

                if not user_input:
                    print("Please enter a prompt.")
                    continue

                # Parse input
                platform, mode, prompt = self.parse_input(user_input)

                if not prompt:
                    print("Could not parse prompt. Please try again.")
                    continue

                # Display processing message
                print(f"\n🔍 Analyzing your prompt... (Mode: {mode.upper()}, Platform: {platform.upper()})")

                # Run optimization
                result = self.optimizer.optimize(prompt, platform, mode)

                # Display results
                analysis = self.optimizer.deconstruct(prompt)
                if analysis.complexity_score > 6 or mode.lower() == 'detail':
                    self.format_result_complex(result)
                else:
                    self.format_result_simple(result, show_techniques=True)

                # For DETAIL mode, offer clarifying questions
                if mode.lower() == 'detail':
                    questions = self.optimizer.generate_clarifying_questions(analysis)
                    if questions:
                        print("\n" + "-" * 70)
                        print("OPTIONAL CLARIFICATIONS:")
                        print("(These could further improve your prompt)")
                        for i, question in enumerate(questions, 1):
                            print(f"  {i}. {question}")
                        print("-" * 70 + "\n")

            except KeyboardInterrupt:
                print("\n\nInterrupted. Goodbye!\n")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                print("Please try again.\n")

    def parse_input(self, user_input: str) -> tuple:
        """
        Parse user input to extract platform, mode, and prompt.

        Returns:
            Tuple of (platform, mode, prompt)
        """
        # Default values
        platform = "other"
        mode = "basic"
        prompt = user_input

        # Check for mode keyword
        input_lower = user_input.lower()
        if input_lower.startswith('detail'):
            mode = "detail"
            user_input = user_input[6:].strip()
        elif input_lower.startswith('basic'):
            mode = "basic"
            user_input = user_input[5:].strip()

        # Check for platform keyword
        if 'using' in user_input.lower():
            parts = user_input.split('using', 1)
            if len(parts) == 2:
                platform_part = parts[1].strip()

                # Extract platform
                if platform_part.lower().startswith('chatgpt'):
                    platform = "chatgpt"
                    platform_part = platform_part[7:].strip()
                elif platform_part.lower().startswith('claude'):
                    platform = "claude"
                    platform_part = platform_part[6:].strip()
                elif platform_part.lower().startswith('gemini'):
                    platform = "gemini"
                    platform_part = platform_part[6:].strip()
                elif platform_part.lower().startswith('gpt'):
                    platform = "chatgpt"
                    platform_part = platform_part[3:].strip()

                # The rest is the prompt (after removing dash if present)
                if platform_part.startswith('-'):
                    platform_part = platform_part[1:].strip()

                prompt = platform_part
        else:
            # No "using" keyword, treat everything after mode as prompt
            prompt = user_input

        return platform, mode, prompt

    def single_command_mode(self, prompt: str, platform: str = "other",
                          mode: str = "basic", verbose: bool = False):
        """Run single optimization command"""
        # Display processing message
        if verbose:
            print(f"\n🔍 Analyzing your prompt... (Mode: {mode.upper()}, Platform: {platform.upper()})")

        # Run optimization
        result = self.optimizer.optimize(prompt, platform, mode)

        # Display results
        analysis = self.optimizer.deconstruct(prompt)
        if analysis.complexity_score > 6 or mode.lower() == 'detail':
            self.format_result_complex(result)
        else:
            self.format_result_simple(result, show_techniques=verbose)


def main():
    """Main entry point for CLI"""
    parser = argparse.ArgumentParser(
        description="Lyra - AI Prompt Optimization Specialist",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Interactive mode:
    python -m lyra.cli

  Single prompt optimization:
    python -m lyra.cli "Write a marketing email"
    python -m lyra.cli --mode detail --platform chatgpt "Write a marketing email"
    python -m lyra.cli -m detail -p claude "Help me debug my Python code"

Platforms: chatgpt, claude, gemini, other
Modes: basic, detail
        """
    )

    parser.add_argument(
        'prompt',
        nargs='?',
        help='The prompt to optimize (if not provided, runs in interactive mode)'
    )

    parser.add_argument(
        '-p', '--platform',
        choices=['chatgpt', 'claude', 'gemini', 'other'],
        default='other',
        help='Target AI platform (default: other)'
    )

    parser.add_argument(
        '-m', '--mode',
        choices=['basic', 'detail'],
        default='basic',
        help='Optimization mode (default: basic)'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed information including techniques applied'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='Lyra 1.0.0'
    )

    args = parser.parse_args()

    # Create CLI instance
    cli = LyraCLI()

    # Run in appropriate mode
    if args.prompt:
        # Single command mode
        cli.single_command_mode(
            args.prompt,
            args.platform,
            args.mode,
            args.verbose
        )
    else:
        # Interactive mode
        cli.interactive_mode()


if __name__ == '__main__':
    main()
