import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import os
from src.config.settings import (
    IMAGE_SIZE,
    IMAGE_QUALITY,
    NUM_INFERENCE_STEPS,
    GUIDANCE_SCALE,
    ERROR_SAVE_FILE_PATH
)
from src.utils.image_utils import (
    is_black_image,
    is_white_background,
    auto_crop_image,
    fix_white_background,
    get_unique_filename
)
from src.prompts import get_centered_img_prompt, get_cute_img_prompt, get_simple_img_prompt

class ImageService:
    def __init__(self):
        self.pipe = self._initialize_pipeline()
       

    def _initialize_pipeline(self):
        """Stable Diffusion 파이프라인 초기화"""
        pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            safety_checker=None,
            torch_dtype=torch.float32
        )

        # 디바이스 설정
        if torch.backends.mps.is_available():
            device = "mps"
        elif torch.cuda.is_available():
            device = "cuda"
        else:
            device = "cpu"

        return pipe.to(device)

    def generate_prompt(self, ingredient_name):
        """이미지 생성을 위한 프롬프트 생성"""
        # 중앙 배치 프롬프트 사용
        return get_centered_img_prompt(ingredient_name)
        
        # 귀여운 스타일 프롬프트 사용
        # return get_cute_img_prompt(ingredient_name)
        
        # 심플 프롬프트 사용
        # return get_simple_img_prompt(ingredient_name)

    def _save_error_filename(self, filename):
        """실패한 파일명을 error_save_file.txt에 추가"""
        # error_save_file.txt가 있는 디렉토리 생성
        os.makedirs(os.path.dirname(ERROR_SAVE_FILE_PATH), exist_ok=True)
        
        # 파일명을 error_save_file.txt에 추가
        with open(self.error_file, 'a', encoding='utf-8') as f:
            f.write(f"{filename}\n")

    def generate_and_process(self, prompt, filename, retries=3):
        """이미지 생성 및 후처리"""
        # 저장할 디렉토리 확인 및 생성
        dir_name = os.path.dirname(filename)
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
            
        # 파일명이 이미 존재하면 고유 이름으로 변경
        filename = get_unique_filename(filename)
            
        for attempt in range(retries):
            image = self.pipe(
                prompt,
                num_inference_steps=NUM_INFERENCE_STEPS,
                guidance_scale=GUIDANCE_SCALE
            ).images[0]
            
            # 이미지 리사이즈 및 저장
            image = image.resize(IMAGE_SIZE)
            image.save(filename, format="JPEG", quality=IMAGE_QUALITY, optimize=True)

            # NSFW 검은 이미지 감지
            if is_black_image(filename):
                print(f"⚫ NSFW 감지됨 → 재시도 ({attempt+1}/{retries})")
                continue

            # 흰 배경 아닌 경우 수정
            # if not is_white_background(filename):
                # print(f"⚠️ 흰 배경 아님 → {filename}")
                # fix_white_background(filename, filename)

            # 크롭 후 저장
            auto_crop_image(filename, filename)
            
            print(f"✅ 최종 이미지 저장: {filename} \n")
            return True

        print(f"❌ {filename} 생성 실패 \n")
        self._save_error_filename(filename)  # 실패한 파일명 저장
        return False 