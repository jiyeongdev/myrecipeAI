from openai import OpenAI
import time
from src.config.settings import GROQ_API_KEY, GROQ_BASE_URL

class TranslationService:
    def __init__(self):
        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url=GROQ_BASE_URL
        )

    def make_prompt(self, ingredient):
        """번역을 위한 프롬프트 생성"""
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

    def translate_ingredient(self, ingredient):
        """한국어 식재료명을 영어로 번역"""
        try:
            response = self.client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "user", "content": self.make_prompt(ingredient)}
                ],
                temperature=0.7,
            )
            english_name = response.choices[0].message.content.strip()
            return english_name
        except Exception as e:
            print(f"Error translating '{ingredient}': {e}")
            # time.sleep(100)  # 에러 발생 시 100초 대기
            return None
            # return self.translate_ingredient(ingredient)  # 재시도 