from openai import OpenAI
import time
from src.config.settings import GROQ_API_KEY, GROQ_BASE_URL
from src.prompts import get_translation_prompt, get_detailed_translation_prompt

class TranslationService:
    def __init__(self):
        self.client = OpenAI(
            api_key=GROQ_API_KEY,
            base_url=GROQ_BASE_URL
        )

    def make_prompt(self, ingredient):
        """번역을 위한 프롬프트 생성"""
        # 기본 번역 프롬프트 사용
        return get_translation_prompt(ingredient)
        
        # 상세 번역 프롬프트 사용
        # return get_detailed_translation_prompt(ingredient)

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