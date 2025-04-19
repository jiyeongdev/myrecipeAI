import pandas as pd
import time
from tqdm import tqdm
import os
from src.config.settings import (
    INGREDIENT_EXCEL_PATH,
    IMAGES_DIR,
    S3_BASE_PATH
)
from src.services.translation_service import TranslationService
from src.services.image_service import ImageService
from src.services.s3_service import S3Service

def translate_ingredients(start_row, end_row):
    """식재료 번역 함수"""
    print("🔄 번역 시작...")
    translation_service = TranslationService()
    
    # 엑셀 파일 불러오기
    df = pd.read_excel(INGREDIENT_EXCEL_PATH)
    
    # 행만 선택
    df_subset = df.iloc[start_row:end_row].copy()
    
    # 번역이 필요한 행만 처리
    for idx, row in tqdm(df_subset.iterrows(), total=len(df_subset), desc="번역 중"):
        if pd.isna(row['en_food_name2']):
            eng = translation_service.translate_ingredient(row['kor_food_name'])
            if eng is None:
                print(f"❌ 번역 실패: {row['kor_food_name']}")
                continue
            df.loc[idx, 'en_food_name2'] = eng
            print(f"번역 완료: {row['kor_food_name']} => {eng}")
            time.sleep(0.5)  # API 호출 간격 조절
    
    # 번역 결과 저장
    print("💾 번역 결과 저장 중...")
    df.to_excel(INGREDIENT_EXCEL_PATH, index=False)
    print("✅ 번역 완료!")

def generate_images(start_row, end_row):
    """이미지 생성 함수"""
    print("🔄 이미지 생성 시작...")
    image_service = ImageService()
    s3_service = S3Service()
    
    # 엑셀 파일 불러오기
    df = pd.read_excel(INGREDIENT_EXCEL_PATH)
    subset = df.iloc[start_row:end_row]
    
    # 이미지 생성
    for i, row in enumerate(tqdm(subset.itertuples(), total=len(subset), desc="이미지 생성 중")):
        prompt = image_service.generate_prompt(row.en_food_name)
        file_name = os.path.join(IMAGES_DIR, f"{row.food_id}.jpg")
        
        print(f"🚀[{i+1}/{len(subset)}] food_id: {row.food_id} / kor_food_name: {row.kor_food_name} / en_food_name: {row.en_food_name} ")
        if image_service.generate_and_process(prompt, file_name):
            # S3 업로드 (선택적)
            s3_file_path = f"{S3_BASE_PATH}/{row.food_id}.jpg"
            #s3_service.upload_file(file_name, s3_file_path)
    
    print("✅ 이미지 생성 완료!")

def main():
    """메인 실행 함수"""
    print("🚀 MyRecipe Python Project 시작!")
    start_time = time.time()

    ############################번역 & 이미지 생성할 행 지정 ################################
    start_row = 0
    end_row= 400
    ###################################################################################
  

    # 1. 번역 실행
    translate_ingredients(start_row,end_row)
    
    # 2. 이미지 생성 실행
    generate_images(start_row, end_row)  # 179-181행 처리

    # 실행 시간 계산
    end_time = time.time()
    elapsed = end_time - start_time
    minutes, seconds = divmod(elapsed, 60)
    print(f"⏱️ 전체 실행 시간: {int(minutes)}분 {int(seconds)}초")

if __name__ == "__main__":
    main() 