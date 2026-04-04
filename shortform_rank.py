import yt_dlp
import random
from datetime import datetime

def get_pure_korean_motion_design(mode='KR', limit=3):
    if mode == 'KR':
        display_name = "대한민국 (한국어 전용)"
        # 영문 키워드를 삭제하고 한국어 키워드 위주로 재구성
        search_query = "모션그래픽 작업물 | 키네틱 타이포그래피 포트폴리오 | 모션디자인"
        lang = 'ko-KR'
        location = 'KR'
    else:
        display_name = "전 세계 (Global)"
        search_query = "Best Motion Graphics Kinetic Typography 2026"
        lang = 'en-US'
        location = 'US'

    ydl_opts = {
        'quiet': True,
        'extract_flat': True,
        'force_generic_ext': True,
        'nocheckcertificate': True,
        # [핵심] 지역과 언어를 한국으로 완전히 고정하는 헤더
        'http_headers': {
            'Accept-Language': f'{lang},ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        },
        # 유튜브에 지역 정보를 명시적으로 전달
        'geo_bypass': True,
        'geo_bypass_country': location
    }

    print(f"\n--- 🎲 {display_name} 검색 결과 수집 중... ---")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            # 검색 표본을 100개로 설정
            result = ydl.extract_info(f"ytsearch100:{search_query}", download=False)
            
            pool = []
            for entry in result.get('entries', []):
                view_count = entry.get('view_count', 0) or 0
                uploader = entry.get('uploader', '')
                title = entry.get('title', '')

                # [한국어 판별 로직 추가] 
                # 한국 모드일 때 제목이나 채널명에 한글이 포함된 경우만 수집 (옵션)
                if mode == 'KR':
                    # 한글이 포함되어 있는지 간단히 체크
                    has_korean = any(ord('가') <= ord(char) <= ord('힣') for char in title + uploader)
                    if not has_korean:
                        continue

                if view_count >= 1000:
                    pool.append({
                        'title': title,
                        'view_count': view_count,
                        'url': f"https://www.youtube.com/watch?v={entry.get('id')}",
                        'uploader': uploader
                    })

            if not pool:
                print(f"⚠️ {display_name}: 조건에 맞는 한국 영상을 찾지 못했습니다.")
                return

            random.shuffle(pool)
            selection = pool[:limit]

            for i, video in enumerate(selection, 1):
                print(f"추천 {i}: {video['title']}")
                print(f"   - 조회수: {int(video['view_count']):,}회")
                print(f"   - 채널: {video['uploader']}")
                print(f"   - 링크: {video['url']}\n")

        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    get_pure_korean_motion_design(mode='KR')
    print("-" * 40)
    get_pure_korean_motion_design(mode='GLOBAL')