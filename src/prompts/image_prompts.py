"""
이미지 생성 프롬프트 모듈
"""

def get_centered_img_prompt(ingredient_name):
    """
    중앙 배치된 이미지 생성을 위한 프롬프트
    """
    return f"""A food ingredient {ingredient_name} that you can find in a refrigerator or grocery store, 
            a perfectly centered {ingredient_name}, (centered composition:1.5), (symmetrical composition:1.3), 
            professional food photography of a single {ingredient_name} on pure white background (255, 255, 255).
            (centered:1.4), (dead center:1.3), (perfect symmetry:1.2), (top-down view:1.2).
            The {ingredient_name} must be exactly in the middle of the frame.
            Crystal clear focus, even studio lighting, no shadows.
            (isolated object:1.3), (floating:1.2), (commercial product photography:1.2).
            Absolutely no text, no watermarks, no additional objects.
            High-end product photography, 8k, ultra sharp, professional lighting.
            (white background:1.4), (minimalist:1.2), (clean:1.2).""".replace('\n', ' ').replace('  ', ' ')

def get_cute_img_prompt(ingredient_name):
    """
    귀여운 스타일의 이미지 생성을 위한 프롬프트
    """
    return f"""A food ingredient {ingredient_name} that you can find in a refrigerator or grocery store, 
            a super cute and adorable {ingredient_name}, (kawaii style:1.5), (cartoon-like:1.4), (anime style:1.3), 
            (chibi style:1.3), (character design:1.3), (mascot style:1.3),
            professional food photography of a single {ingredient_name} on pure white background (255, 255, 255).
            (centered:1.4), (dead center:1.3), (perfect symmetry:1.2), (top-down view:1.2).
            The {ingredient_name} must be exactly in the middle of the frame.
            Crystal clear focus, even studio lighting, no shadows.
            (isolated object:1.3), (floating:1.2), (commercial product photography:1.2).
            (cute eyes:1.4), (friendly expression:1.4), (adorable:1.5), (sweet smile:1.3), (chibi face:1.3).
            (no realistic texture:1.3), (flat cartoon style:1.3), (simple shapes:1.3).
            Absolutely no text, no watermarks, no additional objects.
            High-end product photography, 8k, ultra sharp, professional lighting.
            (white background:1.4), (minimalist:1.2), (clean:1.2).""".replace('\n', ' ').replace(' ', ' ')

def get_simple_img_prompt(ingredient_name):
    """
    심플한 스타일의 이미지 생성을 위한 프롬프트
    """
    return f"""A food ingredient {ingredient_name} that you can find in a refrigerator or grocery store, 
            a single centered {ingredient_name}, which is an edible food ingredient, exactly in the middle of the image, 
            on a seamless pure white background. Perfect symmetry. 
            Centered object. No cropping. No border touching. Full object in view. 
            No other objects. No text. No shadow. No reflection. Even lighting. 
            Top-down minimalist product photo. Sharp focus.""".replace('\n', ' ').replace(' ', ' ') 