import discord
from discord import app_commands
from discord.ext import commands
import random
import json
import os
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

MENU_FILE = "menus.json"

def load_menus():
    if not os.path.exists(MENU_FILE):
        # 파일이 없으면 빈 리스트로 시작
        save_menus([])
        return []
    with open(MENU_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_menus(menu_list):
    with open(MENU_FILE, 'w', encoding='utf-8') as f:
        json.dump(menu_list, f, ensure_ascii=False, indent=2)

menus = load_menus()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

class MenuButtonView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="다시 추천", style=discord.ButtonStyle.primary)
    async def again(self, interaction: discord.Interaction, button: discord.ui.Button):
        new_menu = random.choice(menus)
        await interaction.response.edit_message(
            content=f"🍽️ 오늘의 추천 메뉴는... **{new_menu}**!",
            view=self
        )

    @discord.ui.button(label="메뉴 리스트 보기", style=discord.ButtonStyle.secondary)
    async def show_list(self, interaction: discord.Interaction, button: discord.ui.Button):
        text = '\n'.join(f"• {m}" for m in menus)
        await interaction.response.send_message(
            content=f"📋 현재 메뉴 리스트:\n{text}",
            ephemeral=False
        )

@tree.command(name="menu", description="랜덤 메뉴 추천")
async def menu_command(interaction: discord.Interaction):
    selected = random.choice(menus)
    view = MenuButtonView()
    await interaction.response.send_message(f"🍽️ 오늘의 추천 메뉴는... **{selected}**!", view=view)

@tree.command(name="menu_add", description="메뉴 추가")
@app_commands.describe(item="추가할 메뉴 이름")
async def menu_add(interaction: discord.Interaction, item: str):
    if item in menus:
        await interaction.response.send_message(f"⚠️ `{item}` 은(는) 이미 있어요.")
    else:
        menus.append(item)
        save_menus(menus)
        await interaction.response.send_message(f"✅ `{item}` 을(를) 추가했어요!")

# 자동완성 함수는 menu_remove 함수보다 위에 있어야 함
async def menu_autocomplete(interaction: discord.Interaction, current: str):
    return [
        app_commands.Choice(name=m, value=m)
        for m in menus if current.lower() in m.lower()
    ][:25]

@tree.command(name="menu_remove", description="메뉴 삭제")
@app_commands.describe(item="삭제할 메뉴 이름")
@app_commands.autocomplete(item=menu_autocomplete)
async def menu_remove(interaction: discord.Interaction, item: str):
    if item in menus:
        menus.remove(item)
        save_menus(menus)
        await interaction.response.send_message(f"🗑️ `{item}` 을(를) 삭제했어요.")
    else:
        await interaction.response.send_message(f"❌ `{item}` 은(는) 메뉴에 없어요.")

@tree.command(name="menu_list", description="메뉴 목록 보기")
async def menu_list(interaction: discord.Interaction):
    text = '\n'.join(f"• {m}" for m in menus)
    await interaction.response.send_message(f"📋 현재 메뉴 리스트:\n{text}", ephemeral=False)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ 봇 로그인 완료: {bot.user}")

# 환경변수에서 봇 토큰 가져오기
BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

if not BOT_TOKEN:
    print("❌ 오류: DISCORD_BOT_TOKEN 환경변수가 설정되지 않았습니다.")
    print("   .env 파일에 DISCORD_BOT_TOKEN=your_token_here 를 추가해주세요.")
    exit(1)

bot.run(BOT_TOKEN)
