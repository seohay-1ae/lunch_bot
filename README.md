# 🍽️ Discord 점심추천 봇

Discord에서 랜덤하게 점심 메뉴를 추천해주는 봇입니다. 슬래시 커맨드와 인터랙티브 버튼을 통해 쉽게 메뉴를 관리하고 추천받을 수 있습니다.

## ✨ 주요 기능

- 🎲 **랜덤 메뉴 추천**: 저장된 메뉴 중에서 랜덤하게 선택
- ➕ **메뉴 추가**: 새로운 메뉴를 리스트에 추가
- 🗑️ **메뉴 삭제**: 자동완성 기능이 있는 메뉴 삭제
- 📋 **메뉴 목록 보기**: 현재 저장된 모든 메뉴 확인
- 🔄 **인터랙티브 버튼**: "다시 추천" 및 "메뉴 리스트 보기" 버튼

## 🚀 설치 및 실행

### 1. 저장소 클론
```bash
git clone https://github.com/seohay-1ae/lunch_bot.git
cd lunch_bot
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경변수 설정
`.env` 파일을 생성하고 Discord 봇 토큰을 추가하세요:
```
DISCORD_BOT_TOKEN=your_discord_bot_token_here
```

### 4. 봇 실행
```bash
python bot.py
```

## 📝 사용법

### 슬래시 커맨드

- `/menu` - 랜덤 메뉴 추천
- `/menu_add <메뉴명>` - 메뉴 추가
- `/menu_remove <메뉴명>` - 메뉴 삭제 (자동완성 지원)
- `/menu_list` - 메뉴 목록 보기

### 인터랙티브 버튼

메뉴 추천 후 나타나는 버튼들:
- **다시 추천**: 새로운 메뉴로 다시 추천
- **메뉴 리스트 보기**: 현재 저장된 모든 메뉴 표시

## 🔧 기술 스택

- **Python 3.8+**
- **discord.py** - Discord API 라이브러리
- **python-dotenv** - 환경변수 관리
- **JSON** - 메뉴 데이터 저장

## 📁 프로젝트 구조

```
lunch_bot/
├── bot.py              # 메인 봇 코드
├── menus.json          # 메뉴 데이터
├── requirements.txt    # 의존성 목록
├── .env               # 환경변수 (봇 토큰)
├── .gitignore         # Git 제외 파일
└── README.md          # 프로젝트 설명
```

## 🔒 보안

- 봇 토큰은 `.env` 파일에 저장되며 Git에 업로드되지 않습니다
- `.gitignore`에 의해 민감한 정보가 보호됩니다

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.

## 📞 문의

프로젝트에 대한 문의사항이 있으시면 [Issues](https://github.com/seohay-1ae/lunch_bot/issues)를 통해 연락해주세요.

---

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!
