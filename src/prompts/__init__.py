"""
프롬프트 패키지
"""

from src.prompts.image_prompts import get_centered_img_prompt, get_cute_img_prompt, get_simple_img_prompt
from src.prompts.translation_prompts import get_translation_prompt, get_detailed_translation_prompt

__all__ = [
    'get_centered_img_prompt',
    'get_cute_img_prompt',
    'get_simple_img_prompt',
    'get_translation_prompt',
    'get_detailed_translation_prompt'
] 