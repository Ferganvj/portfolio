from pathlib import Path

from content import OWNER, ABOUT, EXPERIENCE, PROJECTS, SKILLS
from renderer import build_portfolio_html

Path("dist").mkdir(exist_ok=True)
Path("dist/index.html").write_text(
    build_portfolio_html(OWNER, ABOUT, EXPERIENCE, PROJECTS, SKILLS),
    encoding="utf-8",
)
print("built → dist/index.html")
