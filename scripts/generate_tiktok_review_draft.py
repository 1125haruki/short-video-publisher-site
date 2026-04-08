from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path("/Users/takasuharuki/dev26/short-video-publisher-site")
ASSETS = ROOT / "assets"
SLIDES = ASSETS / "review_slides"
OUT_FILE = ASSETS / "tiktok-review-draft.mp4"
ICON_FILE = ASSETS / "tiktok-app-icon.png"
FONT_REG = "/System/Library/Fonts/Supplemental/Verdana.ttf"
FONT_BOLD = "/System/Library/Fonts/Supplemental/Verdana Bold.ttf"

W = 1280
H = 720


def make_slide(index: int, heading: str, body1: str, body2: str) -> Path:
    img = Image.new("RGBA", (W, H), (245, 241, 232, 255))
    draw = ImageDraw.Draw(img)

    for y in range(H):
        t = y / (H - 1)
        r = int(242 + (227 - 242) * t)
        g = int(238 + (220 - 238) * t)
        b = int(231 + (208 - 231) * t)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    draw.rounded_rectangle(
        (86, 236, 1194, 462),
        radius=26,
        fill=(255, 255, 255, 145),
        outline=(216, 208, 196, 210),
        width=2,
    )

    icon = Image.open(ICON_FILE).convert("RGBA").resize((180, 180))
    img.alpha_composite(icon, (70, 70))

    font_title = ImageFont.truetype(FONT_BOLD, 44)
    font_kicker = ImageFont.truetype(FONT_REG, 24)
    font_heading = ImageFont.truetype(FONT_BOLD, 36)
    font_body = ImageFont.truetype(FONT_REG, 24)

    draw.text((290, 86), "Short Video Publisher", font=font_title, fill=(22, 54, 51, 255))
    draw.text((292, 146), "Internal review outline only", font=font_kicker, fill=(13, 124, 102, 255))
    draw.text((92, 258), heading, font=font_heading, fill=(22, 54, 51, 255))
    draw.text((92, 320), body1, font=font_body, fill=(63, 74, 72, 255))
    draw.text((92, 370), body2, font=font_body, fill=(63, 74, 72, 255))

    out = SLIDES / f"slide_{index:02d}.png"
    img.save(out)
    return out


def build_video() -> None:
    SLIDES.mkdir(parents=True, exist_ok=True)

    slides = [
        make_slide(
            1,
            "1. Open the public website",
            "Show the public product page, Privacy Policy, and Terms.",
            "Use the same GitHub Pages domain that is registered in TikTok Developers.",
        ),
        make_slide(
            2,
            "2. Open the sandbox workspace",
            "Move to workspace.html?mode=sandbox and start Login Kit.",
            "Use a sandbox creator account for the review recording.",
        ),
        make_slide(
            3,
            "3. Load creator posting settings",
            "Show privacy options, interaction availability, and duration limit.",
            "These values come from creator_info before Direct Post.",
        ),
        make_slide(
            4,
            "4. Review privacy, disclosure, and consent",
            "Enter a public MP4 URL and title, then choose privacy manually.",
            "Show AIGC or branded content disclosure if used, then confirm consent.",
        ),
        make_slide(
            5,
            "5. Send Direct Post and check status",
            "Submit the Direct Post request and show the returned publish ID.",
            "Finish by checking publish status in the same workspace.",
        ),
    ]

    cmd = [
        "ffmpeg",
        "-y",
        "-loop",
        "1",
        "-t",
        "5",
        "-i",
        str(slides[0]),
        "-loop",
        "1",
        "-t",
        "5",
        "-i",
        str(slides[1]),
        "-loop",
        "1",
        "-t",
        "5",
        "-i",
        str(slides[2]),
        "-loop",
        "1",
        "-t",
        "5",
        "-i",
        str(slides[3]),
        "-loop",
        "1",
        "-t",
        "5",
        "-i",
        str(slides[4]),
        "-filter_complex",
        "[0:v][1:v][2:v][3:v][4:v]concat=n=5:v=1:a=0,format=yuv420p[v]",
        "-map",
        "[v]",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "24",
        "-movflags",
        "+faststart",
        str(OUT_FILE),
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    build_video()
    print(OUT_FILE)
