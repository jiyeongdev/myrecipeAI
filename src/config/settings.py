import os
from pathlib import Path

# 프로젝트 루트 디렉토리
ROOT_DIR = Path(__file__).parent.parent.parent

# 데이터 디렉토리
DATA_DIR = ROOT_DIR / "data"
INGREDIENT_EXCEL_PATH = DATA_DIR / "ingredient_name_info.xlsx"

# 이미지 생성 실패하는 파일 저장 경로
ERROR_SAVE_FILE_PATH = DATA_DIR / "error_saveimg_filename.txt"

# 출력 디렉토리
IMAGES_DIR = DATA_DIR / "images"

# 번역 API 설정
GROQ_API_KEY = "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"
GROQ_BASE_URL = "https://api.groq.com/openai/v1"

# AWS S3 설정
S3_BUCKET_NAME = "myrecipe-bucket"
S3_BASE_PATH = "ingredient"



# 이미지 생성 설정
IMAGE_SIZE = (512, 512)
IMAGE_QUALITY = 70
NUM_INFERENCE_STEPS = 30
GUIDANCE_SCALE = 7.5

# 디렉토리 생성
for directory in [DATA_DIR, IMAGES_DIR]:
    directory.mkdir(parents=True, exist_ok=True) 