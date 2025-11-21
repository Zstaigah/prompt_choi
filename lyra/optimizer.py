"""
Core Lyra Optimizer Module

Implements the 4-D methodology for prompt optimization:
- Deconstruct: Extract core intent and requirements
- Diagnose: Audit for clarity and completeness
- Develop: Apply optimization techniques
- Deliver: Construct and format the optimized prompt
"""

import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class AIPlatform(Enum):
    """Supported AI platforms"""
    CHATGPT = "chatgpt"
    CLAUDE = "claude"
    GEMINI = "gemini"
    OTHER = "other"


class Mode(Enum):
    """Operating modes"""
    DETAIL = "detail"
    BASIC = "basic"


class TaskType(Enum):
    """Types of tasks for optimization"""
    CREATIVE = "creative"
    TECHNICAL = "technical"
    ANALYTICAL = "analytical"
    EDUCATIONAL = "educational"
    COMPLEX = "complex"
    SIMPLE = "simple"


@dataclass
class PromptAnalysis:
    """Results from prompt analysis"""
    core_intent: str
    key_entities: List[str]
    context_level: str
    output_requirements: List[str]
    constraints: List[str]
    clarity_issues: List[str]
    task_type: TaskType
    complexity_score: int


@dataclass
class OptimizationResult:
    """Results from prompt optimization"""
    optimized_prompt: str
    improvements: List[str]
    techniques_applied: List[str]
    pro_tip: Optional[str] = None


class LyraOptimizer:
    """
    Master-level AI prompt optimization specialist.

    Transforms user input into precision-crafted prompts using the 4-D methodology.
    """

    WELCOME_MESSAGE = """Hello! I'm Lyra, your AI prompt optimizer. I transform vague requests into precise, effective prompts that deliver better results.

**What I need to know:**
• Target AI: ChatGPT, Claude, Gemini, or Other
• Prompt Style: DETAIL (I'll ask clarifying questions first) or BASIC (quick optimization)

**Examples:**
• "DETAIL using ChatGPT - Write me a marketing email"
• "BASIC using Claude - Help with my resume"

Just share your rough prompt and I'll handle the optimization!"""

    def __init__(self):
        self.platform = None
        self.mode = None

    def get_welcome_message(self) -> str:
        """Return the welcome message"""
        return self.WELCOME_MESSAGE

    # ========================
    # 1. DECONSTRUCT
    # ========================

    def deconstruct(self, prompt: str) -> PromptAnalysis:
        """
        Extract core intent, key entities, and context from the prompt.

        Args:
            prompt: The original user prompt

        Returns:
            PromptAnalysis object with extracted information
        """
        # Extract core intent (typically the main verb + object)
        core_intent = self._extract_intent(prompt)

        # Identify key entities (nouns, subjects)
        key_entities = self._extract_entities(prompt)

        # Assess context level
        context_level = self._assess_context(prompt)

        # Extract output requirements
        output_requirements = self._extract_requirements(prompt)

        # Identify constraints
        constraints = self._extract_constraints(prompt)

        # Identify clarity issues
        clarity_issues = self._identify_clarity_issues(prompt)

        # Determine task type
        task_type = self._determine_task_type(prompt, core_intent)

        # Calculate complexity score (0-10)
        complexity_score = self._calculate_complexity(prompt, clarity_issues, task_type)

        return PromptAnalysis(
            core_intent=core_intent,
            key_entities=key_entities,
            context_level=context_level,
            output_requirements=output_requirements,
            constraints=constraints,
            clarity_issues=clarity_issues,
            task_type=task_type,
            complexity_score=complexity_score
        )

    def _extract_intent(self, prompt: str) -> str:
        """Extract the core intent from the prompt"""
        prompt_lower = prompt.lower()

        # Common action verbs
        action_patterns = [
            r'\b(write|create|generate|make|build|develop|design|draft|compose)\b.*',
            r'\b(analyze|review|evaluate|assess|examine|study)\b.*',
            r'\b(explain|describe|summarize|outline|clarify)\b.*',
            r'\b(help|assist|guide|support)\b.*',
            r'\b(improve|optimize|enhance|refine|fix)\b.*',
        ]

        for pattern in action_patterns:
            match = re.search(pattern, prompt_lower)
            if match:
                return match.group(0).strip()

        # If no clear action verb, return first sentence
        sentences = prompt.split('.')
        return sentences[0].strip() if sentences else prompt[:100]

    def _extract_entities(self, prompt: str) -> List[str]:
        """Extract key entities (nouns, subjects) from the prompt"""
        # Simple noun extraction (can be enhanced with NLP)
        words = prompt.split()
        entities = []

        # Look for capitalized words (potential proper nouns)
        for word in words:
            if word[0].isupper() and word.lower() not in ['the', 'a', 'an', 'i']:
                entities.append(word.strip('.,!?;:'))

        # Common important keywords
        keywords = ['email', 'report', 'code', 'essay', 'article', 'blog', 'resume',
                   'letter', 'proposal', 'presentation', 'analysis', 'summary',
                   'review', 'plan', 'strategy', 'design', 'system']

        for keyword in keywords:
            if keyword in prompt.lower():
                entities.append(keyword)

        return list(set(entities))[:10]  # Return unique entities, max 10

    def _assess_context(self, prompt: str) -> str:
        """Assess the level of context provided"""
        word_count = len(prompt.split())
        has_details = any(word in prompt.lower() for word in ['because', 'for', 'about', 'regarding', 'context'])

        if word_count > 50 and has_details:
            return "High"
        elif word_count > 20 or has_details:
            return "Medium"
        else:
            return "Low"

    def _extract_requirements(self, prompt: str) -> List[str]:
        """Extract output requirements from the prompt"""
        requirements = []

        requirement_patterns = {
            'length': r'(\d+)\s*(words|pages|paragraphs|sentences)',
            'format': r'(format|formatted|structure|template)',
            'tone': r'(tone|formal|casual|professional|friendly|persuasive)',
            'audience': r'(audience|for|target|readers)',
            'style': r'(style|writing style|approach)',
        }

        for req_type, pattern in requirement_patterns.items():
            if re.search(pattern, prompt.lower()):
                match = re.search(pattern, prompt.lower())
                requirements.append(f"{req_type.capitalize()}: {match.group(0)}")

        return requirements

    def _extract_constraints(self, prompt: str) -> List[str]:
        """Extract constraints from the prompt"""
        constraints = []

        constraint_indicators = ['must', 'should', 'need to', 'required', 'limit', 'only',
                                'avoid', 'without', 'don\'t', 'cannot', 'restriction']

        sentences = prompt.split('.')
        for sentence in sentences:
            if any(indicator in sentence.lower() for indicator in constraint_indicators):
                constraints.append(sentence.strip())

        return constraints

    def _identify_clarity_issues(self, prompt: str) -> List[str]:
        """Identify clarity and ambiguity issues"""
        issues = []

        # Too vague
        vague_indicators = ['something', 'anything', 'stuff', 'thing', 'somehow', 'whatever']
        if any(word in prompt.lower() for word in vague_indicators):
            issues.append("Contains vague terms")

        # Too short
        if len(prompt.split()) < 5:
            issues.append("Very brief - may lack necessary context")

        # No clear output format
        format_indicators = ['format', 'structure', 'output', 'return', 'give me', 'provide']
        if not any(word in prompt.lower() for word in format_indicators):
            issues.append("Output format not specified")

        # Ambiguous pronouns
        if re.search(r'\b(it|this|that|they|them)\b', prompt.lower()):
            issues.append("Contains potentially ambiguous pronouns")

        return issues

    def _determine_task_type(self, prompt: str, intent: str) -> TaskType:
        """Determine the type of task"""
        prompt_lower = prompt.lower()

        # Creative indicators
        creative_keywords = ['story', 'creative', 'imagine', 'invent', 'design', 'brainstorm',
                           'idea', 'novel', 'poem', 'art']
        if any(word in prompt_lower for word in creative_keywords):
            return TaskType.CREATIVE

        # Technical indicators
        technical_keywords = ['code', 'program', 'debug', 'algorithm', 'function', 'api',
                            'technical', 'system', 'implementation', 'architecture']
        if any(word in prompt_lower for word in technical_keywords):
            return TaskType.TECHNICAL

        # Analytical indicators
        analytical_keywords = ['analyze', 'compare', 'evaluate', 'assess', 'research',
                             'data', 'statistics', 'metrics', 'performance']
        if any(word in prompt_lower for word in analytical_keywords):
            return TaskType.ANALYTICAL

        # Educational indicators
        educational_keywords = ['explain', 'teach', 'learn', 'understand', 'tutorial',
                              'lesson', 'guide', 'instruction', 'how to']
        if any(word in prompt_lower for word in educational_keywords):
            return TaskType.EDUCATIONAL

        # Complex vs Simple
        if len(prompt.split()) > 30 or len(prompt.split('.')) > 2:
            return TaskType.COMPLEX

        return TaskType.SIMPLE

    def _calculate_complexity(self, prompt: str, clarity_issues: List[str],
                            task_type: TaskType) -> int:
        """Calculate complexity score (0-10)"""
        score = 5  # Base score

        # Adjust based on length
        word_count = len(prompt.split())
        if word_count < 10:
            score -= 2
        elif word_count > 50:
            score += 2

        # Adjust based on clarity issues
        score += len(clarity_issues)

        # Adjust based on task type
        if task_type in [TaskType.TECHNICAL, TaskType.COMPLEX]:
            score += 2
        elif task_type == TaskType.SIMPLE:
            score -= 2

        return max(0, min(10, score))  # Clamp between 0-10

    # ========================
    # 2. DIAGNOSE
    # ========================

    def diagnose(self, analysis: PromptAnalysis) -> Dict[str, List[str]]:
        """
        Audit the prompt for issues and areas of improvement.

        Args:
            analysis: The PromptAnalysis from deconstruction

        Returns:
            Dictionary of diagnostic findings
        """
        diagnosis = {
            'critical_issues': [],
            'improvements_needed': [],
            'strengths': []
        }

        # Check clarity
        if analysis.clarity_issues:
            diagnosis['critical_issues'].extend(analysis.clarity_issues)

        # Check specificity
        if not analysis.key_entities or len(analysis.key_entities) < 2:
            diagnosis['improvements_needed'].append("Add more specific details and context")

        # Check completeness
        if not analysis.output_requirements:
            diagnosis['improvements_needed'].append("Specify desired output format")

        if analysis.context_level == "Low":
            diagnosis['improvements_needed'].append("Provide more context and background")

        # Check structure
        if analysis.complexity_score > 7 and not analysis.constraints:
            diagnosis['improvements_needed'].append("Break down into steps or add constraints")

        # Identify strengths
        if analysis.context_level == "High":
            diagnosis['strengths'].append("Good context provided")

        if analysis.constraints:
            diagnosis['strengths'].append("Clear constraints specified")

        if analysis.output_requirements:
            diagnosis['strengths'].append("Output requirements defined")

        return diagnosis

    # ========================
    # 3. DEVELOP
    # ========================

    def develop(self, prompt: str, analysis: PromptAnalysis,
                platform: AIPlatform, mode: Mode) -> str:
        """
        Develop the optimized prompt using appropriate techniques.

        Args:
            prompt: Original prompt
            analysis: PromptAnalysis from deconstruction
            platform: Target AI platform
            mode: Operating mode (DETAIL or BASIC)

        Returns:
            Optimized prompt string
        """
        techniques = self._select_techniques(analysis, mode)

        # Build the optimized prompt
        optimized_parts = []

        # 1. Add role assignment
        if 'role_assignment' in techniques:
            role = self._assign_role(analysis.task_type)
            optimized_parts.append(role)

        # 2. Add context layering
        if 'context_layering' in techniques:
            context = self._enhance_context(prompt, analysis)
            if context:
                optimized_parts.append(context)

        # 3. Add main task with clarity
        main_task = self._clarify_task(prompt, analysis)
        optimized_parts.append(main_task)

        # 4. Add output specifications
        if 'output_specs' in techniques:
            output_spec = self._create_output_spec(analysis, platform)
            optimized_parts.append(output_spec)

        # 5. Add structural elements based on task type
        if analysis.task_type == TaskType.CREATIVE and 'multi_perspective' in techniques:
            optimized_parts.append("\nConsider multiple perspectives and creative angles.")

        elif analysis.task_type == TaskType.TECHNICAL and 'constraint_based' in techniques:
            optimized_parts.append(self._add_technical_constraints(analysis))

        elif analysis.task_type == TaskType.EDUCATIONAL and 'few_shot' in techniques:
            optimized_parts.append("\nProvide clear examples and step-by-step explanations.")

        elif analysis.complexity_score > 7 and 'chain_of_thought' in techniques:
            optimized_parts.append("\nThink through this step-by-step, showing your reasoning.")

        # 6. Add constraints
        if analysis.constraints and mode == Mode.DETAIL:
            optimized_parts.append(f"\n**Constraints:**")
            for constraint in analysis.constraints:
                optimized_parts.append(f"- {constraint}")

        # 7. Platform-specific formatting
        formatted = self._apply_platform_formatting(
            "\n\n".join(optimized_parts),
            platform,
            analysis
        )

        return formatted

    def _select_techniques(self, analysis: PromptAnalysis, mode: Mode) -> List[str]:
        """Select appropriate optimization techniques"""
        techniques = ['role_assignment', 'task_decomposition']

        if mode == Mode.DETAIL:
            techniques.extend(['context_layering', 'output_specs'])

        if analysis.complexity_score > 7:
            techniques.append('chain_of_thought')

        if analysis.task_type == TaskType.CREATIVE:
            techniques.append('multi_perspective')

        if analysis.task_type == TaskType.TECHNICAL:
            techniques.append('constraint_based')

        if analysis.task_type == TaskType.EDUCATIONAL:
            techniques.append('few_shot')

        return techniques

    def _assign_role(self, task_type: TaskType) -> str:
        """Assign an appropriate AI role/persona"""
        roles = {
            TaskType.CREATIVE: "You are a creative expert with a talent for innovative thinking and storytelling.",
            TaskType.TECHNICAL: "You are an experienced technical specialist with deep expertise in software development and problem-solving.",
            TaskType.ANALYTICAL: "You are a data analyst and critical thinker skilled at breaking down complex information.",
            TaskType.EDUCATIONAL: "You are an expert educator who excels at explaining concepts clearly and effectively.",
            TaskType.COMPLEX: "You are a strategic thinker capable of handling multifaceted challenges systematically.",
            TaskType.SIMPLE: "You are a helpful assistant focused on providing clear, concise responses."
        }
        return roles.get(task_type, roles[TaskType.SIMPLE])

    def _enhance_context(self, prompt: str, analysis: PromptAnalysis) -> str:
        """Enhance context if needed"""
        if analysis.context_level == "High":
            return ""  # Already has good context

        context_prompt = "\n**Context:** "
        if analysis.key_entities:
            context_prompt += f"This task involves {', '.join(analysis.key_entities[:3])}. "

        return context_prompt

    def _clarify_task(self, prompt: str, analysis: PromptAnalysis) -> str:
        """Clarify and enhance the main task description"""
        task = f"**Task:** {analysis.core_intent}"

        if analysis.key_entities and len(analysis.key_entities) > 0:
            task += f"\n**Focus areas:** {', '.join(analysis.key_entities[:5])}"

        return task

    def _create_output_spec(self, analysis: PromptAnalysis, platform: AIPlatform) -> str:
        """Create output specifications"""
        spec = "\n**Output Requirements:**"

        if analysis.output_requirements:
            for req in analysis.output_requirements:
                spec += f"\n- {req}"
        else:
            # Add default requirements based on task type
            if analysis.task_type == TaskType.TECHNICAL:
                spec += "\n- Clear, well-commented code"
                spec += "\n- Explanation of approach"
            elif analysis.task_type == TaskType.CREATIVE:
                spec += "\n- Original and engaging content"
                spec += "\n- Appropriate tone and style"
            else:
                spec += "\n- Clear and well-structured response"
                spec += "\n- Specific and actionable information"

        return spec

    def _add_technical_constraints(self, analysis: PromptAnalysis) -> str:
        """Add technical constraints and requirements"""
        constraints = "\n**Technical Requirements:**"
        constraints += "\n- Follow best practices and coding standards"
        constraints += "\n- Consider edge cases and error handling"
        constraints += "\n- Optimize for performance and maintainability"
        return constraints

    def _apply_platform_formatting(self, prompt: str, platform: AIPlatform,
                                   analysis: PromptAnalysis) -> str:
        """Apply platform-specific formatting"""
        if platform == AIPlatform.CHATGPT:
            # ChatGPT likes structured sections
            return prompt

        elif platform == AIPlatform.CLAUDE:
            # Claude handles longer context well, can add more detail
            if analysis.complexity_score > 7:
                prompt += "\n\n**Approach:** Break this down systematically and explain your reasoning."
            return prompt

        elif platform == AIPlatform.GEMINI:
            # Gemini excels at creative and comparative tasks
            if analysis.task_type == TaskType.CREATIVE:
                prompt += "\n\nFeel free to explore creative angles and multiple possibilities."
            return prompt

        return prompt

    # ========================
    # 4. DELIVER
    # ========================

    def deliver(self, optimized_prompt: str, analysis: PromptAnalysis,
                diagnosis: Dict, techniques: List[str], mode: Mode) -> OptimizationResult:
        """
        Construct the final optimization result with metadata.

        Args:
            optimized_prompt: The developed optimized prompt
            analysis: PromptAnalysis from deconstruction
            diagnosis: Diagnostic findings
            techniques: List of techniques applied
            mode: Operating mode

        Returns:
            OptimizationResult with prompt and metadata
        """
        improvements = []

        # Document improvements made
        if diagnosis['critical_issues']:
            improvements.append(f"Fixed {len(diagnosis['critical_issues'])} clarity issues")

        if 'Add more specific details' in ' '.join(diagnosis['improvements_needed']):
            improvements.append("Enhanced specificity and detail")

        if 'Specify desired output format' in ' '.join(diagnosis['improvements_needed']):
            improvements.append("Added clear output specifications")

        if 'Provide more context' in ' '.join(diagnosis['improvements_needed']):
            improvements.append("Layered additional context")

        improvements.append(f"Optimized for {analysis.task_type.value} tasks")

        # Generate pro tip based on complexity and task type
        pro_tip = self._generate_pro_tip(analysis, mode)

        return OptimizationResult(
            optimized_prompt=optimized_prompt,
            improvements=improvements,
            techniques_applied=techniques,
            pro_tip=pro_tip
        )

    def _generate_pro_tip(self, analysis: PromptAnalysis, mode: Mode) -> str:
        """Generate a helpful pro tip"""
        tips = {
            TaskType.CREATIVE: "For creative tasks, consider asking for multiple variations to find the best fit.",
            TaskType.TECHNICAL: "When asking for code, specify your programming language, version, and any frameworks upfront.",
            TaskType.ANALYTICAL: "For analysis tasks, provide sample data or clear criteria for evaluation.",
            TaskType.EDUCATIONAL: "Learning works best when you ask follow-up questions and request examples.",
            TaskType.COMPLEX: "Break complex tasks into smaller subtasks for better results.",
        }

        if analysis.complexity_score > 7:
            return "For complex requests, consider iterating: start with a draft and refine based on the output."

        return tips.get(analysis.task_type, "Be specific about what success looks like for your request.")

    # ========================
    # PUBLIC API
    # ========================

    def optimize(self, prompt: str, platform: str = "other",
                 mode: str = "basic") -> OptimizationResult:
        """
        Main entry point for prompt optimization.

        Args:
            prompt: The original prompt to optimize
            platform: Target AI platform (chatgpt, claude, gemini, other)
            mode: Operating mode (detail, basic)

        Returns:
            OptimizationResult with optimized prompt and metadata
        """
        # Parse inputs
        platform_enum = self._parse_platform(platform)
        mode_enum = self._parse_mode(mode)

        # Auto-detect mode if not specified
        if mode == "auto":
            mode_enum = self._auto_detect_mode(prompt)

        # Execute 4-D methodology
        analysis = self.deconstruct(prompt)
        diagnosis = self.diagnose(analysis)
        techniques = self._select_techniques(analysis, mode_enum)
        optimized_prompt = self.develop(prompt, analysis, platform_enum, mode_enum)
        result = self.deliver(optimized_prompt, analysis, diagnosis, techniques, mode_enum)

        return result

    def _parse_platform(self, platform: str) -> AIPlatform:
        """Parse platform string to enum"""
        platform_lower = platform.lower()
        if 'chatgpt' in platform_lower or 'gpt' in platform_lower:
            return AIPlatform.CHATGPT
        elif 'claude' in platform_lower:
            return AIPlatform.CLAUDE
        elif 'gemini' in platform_lower:
            return AIPlatform.GEMINI
        return AIPlatform.OTHER

    def _parse_mode(self, mode: str) -> Mode:
        """Parse mode string to enum"""
        if 'detail' in mode.lower():
            return Mode.DETAIL
        return Mode.BASIC

    def _auto_detect_mode(self, prompt: str) -> Mode:
        """Auto-detect appropriate mode based on prompt"""
        word_count = len(prompt.split())

        # Simple tasks get BASIC
        simple_indicators = ['write', 'create', 'make']
        if word_count < 15 and any(word in prompt.lower() for word in simple_indicators):
            return Mode.BASIC

        # Complex or professional tasks get DETAIL
        complex_indicators = ['professional', 'business', 'technical', 'comprehensive', 'detailed']
        if word_count > 25 or any(word in prompt.lower() for word in complex_indicators):
            return Mode.DETAIL

        # Default to BASIC
        return Mode.BASIC

    def generate_clarifying_questions(self, analysis: PromptAnalysis) -> List[str]:
        """
        Generate 2-3 clarifying questions for DETAIL mode.

        Args:
            analysis: PromptAnalysis from deconstruction

        Returns:
            List of clarifying questions
        """
        questions = []

        # Ask about missing output format
        if not analysis.output_requirements:
            questions.append("What format would you like the output in? (e.g., bullet points, paragraph, code)")

        # Ask about tone/audience if not specified
        if analysis.task_type in [TaskType.CREATIVE, TaskType.EDUCATIONAL]:
            has_audience = any('audience' in req.lower() for req in analysis.output_requirements)
            if not has_audience:
                questions.append("Who is the target audience?")

        # Ask about constraints if complex
        if analysis.complexity_score > 7 and not analysis.constraints:
            questions.append("Are there any specific constraints or requirements I should know about?")

        # Ask about length if not specified
        has_length = any(req.startswith('Length:') for req in analysis.output_requirements)
        if not has_length and analysis.task_type != TaskType.TECHNICAL:
            questions.append("What length are you aiming for?")

        return questions[:3]  # Return max 3 questions
