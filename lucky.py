
import os
from dotenv import load_dotenv
import openai 
from datetime import datetime

load_dotenv()
# OpenWeather API 키
openai_api_key = os.getenv('OPENAI_API_KEY')

client = openai.OpenAI(api_key=openai_api_key)  # 수정
# README 파일 경로
README_PATH = "README.md"

def get_openai():
    """OpenAI API를 사용하여 운세를 가져옴"""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "너는 한줄로 말하는 운세전문가."},
            {"role": "user", "content": "오늘의 운세를 한줄로 말해줘"}
        ]
    )
    return response.choices[0].message.content

def update_readme():
    """README.md 파일을 업데이트"""
    luck_info = get_openai()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    readme_content = f"""
# Weather API Status

이 리포지토리는 운세를 알려줍니다.

현재 시간: {now} (UTC)

## 올해의 운세
> {luck_info}



---
자동 업데이트 봇에 의해 관리됩니다.
"""

    with open(README_PATH, "w", encoding="utf-8") as file:
        file.write(readme_content)

if __name__ == "__main__":
    update_readme()

