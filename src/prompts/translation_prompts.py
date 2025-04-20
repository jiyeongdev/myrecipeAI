"""
번역 프롬프트 모듈
"""

def get_translation_prompt(ingredient):
    """
    번역을 위한 프롬프트 생성
    """
    return f"""
        You are an expert in culinary translation and visual ingredient classification for AI image generation.

        Your task is to translate the Korean ingredient **'{ingredient}'** into a clear, specific English ingredient name that is visually and functionally suitable for AI image generation (e.g., Stable Diffusion).

        Instructions:
        - Translate only the **edible parts** (e.g., leaf, root, stem). Exclude flowers or non-edible ornamental plants.
        - If the ingredient is rare or ambiguous, suggest a **commonly used English culinary equivalent**. If unavailable, provide a **scientific name**.
        - If necessary, replace it with a **visually and functionally similar ingredient** used in global cuisine.
        - Prioritize **visual features** (shape, color, texture) and **culinary use** to help ensure accurate image generation.

        Only output the English ingredient name. Do not include any explanation or additional text.
        """

def get_detailed_translation_prompt(ingredient):
    """
    상세한 번역을 위한 프롬프트 생성
    """
    return f"""
        You are an expert in Korean culinary translation and food ingredient classification for AI image generation.

        Your task is to translate the Korean ingredient **'{ingredient}'** into its correct English name that is suitable for AI image generation.

        Important Rules:
        1. Use the most accurate and specific English name for the Korean ingredient
        2. For grains and cereals:
        - 기장 = foxtail millet
        - 조 = sorghum
        - 수수 = sorghum
        - 메밀 = buckwheat
        - 찹쌀 = glutinous rice
        - 멥쌀 = non-glutinous rice
        3. For vegetables and fruits:
        - Use the most common English name
        - Include the specific variety if known
        4. For meats and seafood:
        - Use the standard English culinary term
        - Include the cut or part if specified
        5. For processed ingredients:
        - Use the standard English term for the processed form
        - Maintain the original meaning of the Korean term

        Additional Guidelines for Image Generation:
        1. If the ingredient is rare or ambiguous in English:
        - Suggest a visually similar ingredient commonly used in global cuisine
        - Example: "고구마" → "sweet potato" (not "Ipomoea batatas")
        2. Focus on visual features:
        - Shape, color, texture should be similar to the original ingredient
        - Example: "청경채" → "bok choy" (similar appearance)
        3. Consider culinary use:
        - If the ingredient is used similarly to another in global cuisine, use that term
        - Example: "부추" → "garlic chives" (similar culinary use)
        4. For unique Korean ingredients:
        - Use the most visually similar common ingredient
        - Add descriptive terms if needed
        - Example: "고사리" → "bracken fern" or "fern shoots"

        Only output the English ingredient name. Do not include any explanation or additional text.
        """ 