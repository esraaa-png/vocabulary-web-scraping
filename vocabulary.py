import requests
from bs4 import BeautifulSoup as bs
import re
import json
import urllib.request
import time
from model import Vocabulary, Meaning, Block, Example


# =========================
# LOAD WORDS
# =========================
urls = []

with open("words.txt", "r", encoding="utf-8") as f:
    data = f.read().splitlines()
    urls = [
        f"http://5.vndic.net/index.php?word={word}&dict=en_vi"
        for word in data if word.strip()
    ]

print(urls[:10])


# =========================
# HELPERS
# =========================
def save(url, path):
    try:
        urllib.request.urlretrieve(url, path)
    except:
        pass


def trimAudio(audio):
    try:
        return re.findall(r"mp3.php\?id=\w+&dir=\d+&lang=en&", audio)[0]
    except:
        return ""


# =========================
# SESSION (IMPORTANT)
# =========================
session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})


vocabularies = []
errorURL = []


# =========================
# SCRAPER
# =========================
def CRAWL(url):

    try:
        r = session.get(url, timeout=10)
    except:
        errorURL.append(url)
        return "ERROR in requesting!"

    soup = bs(r.text, "html.parser")

    # -------------------------
    # WORD
    # -------------------------
    try:
        word = soup.select_one(".thisword").get_text(strip=True)
    except:
        return "ERROR in scraping word"

    # -------------------------
    # IMAGE
    # -------------------------
    image_api = ""
    image = ""

    try:
        img_tag = soup.find("img")
        if img_tag:
            img = img_tag.get("src", "")
            if word in img:
                image_api = "http://5.vndic.net/" + img
                image = f"./Image/{word}.png"
                save(image_api, image)
    except:
        pass

    # -------------------------
    # AUDIO
    # -------------------------
    audio_api = ""
    audio = ""

    try:
        audio_tag = soup.find("audio")
        if audio_tag:
            pass
    except:
        pass

    try:
        click_audio = soup.find_all(style="cursor:pointer;")
        if click_audio:
            ado = trimAudio(click_audio[0].get("onclick", ""))
            if ado:
                audio_api = "http://5.vndic.net/" + ado
                audio = f"./MP3/{word}.mp3"
                save(audio_api, audio)
    except:
        pass

    # -------------------------
    # MAIN CONTENT
    # -------------------------
    main = soup.select_one(".maincontent")
    if not main:
        return "ERROR in finding translation"

    trs = main.find_all("tr")

    if not trs:
        return "ERROR in finding translation"

    spelling = trs[0].get_text(strip=True)

    vocab = Vocabulary(word, image_api, image, audio_api, audio, spelling)

    block = None
    meaning = None

    # =========================
    # PARSE TABLE
    # =========================
    for i, tr in enumerate(trs):

        img = tr.find("img")
        src = img["src"] if img else ""

        content = tr.get_text(strip=True)

        # stop condition
        if src == "img/dict/809C2811.png":
            break

        # -----------------
        # NEW MEANING BLOCK
        # -----------------
        if src == "img/dict/CB1FF077.png":
            if block and meaning:
                block.addMeaning(meaning)
            meaning = Meaning(content)

        # -----------------
        # NEW GRAMMAR BLOCK
        # -----------------
        elif src == "img/dict/46E762FB.png":
            if block and meaning:
                block.addMeaning(meaning)
                meaning = None

            if block:
                vocab.addTranslation(block)

            block = Block(content)

        # -----------------
        # EXAMPLES
        # -----------------
        elif src == "img/dict/9F47DE07.png":
            if not meaning:
                continue

            try:
                next_text = trs[i + 1].get_text(strip=True)
                meaning.addExample(Example(content, next_text))
            except:
                pass

    # =========================
    # FINALIZE
    # =========================
    if block and meaning:
        block.addMeaning(meaning)

    if block:
        vocab.addTranslation(block)

    vocabularies.append(vocab.toObj())

    return "SUCCESSFULL!"


# =========================
# RUN SCRAPER
# =========================
success = 0

for i, url in enumerate(urls):
    res = CRAWL(url)

    if res == "SUCCESSFULL!":
        success += 1

    print(i, res)
    print("Rate successful:", success / max(1, len(urls)))

    time.sleep(1)  # anti-ban


# =========================
# SAVE JSON
# =========================
with open("vocabulary.json", "w", encoding="utf-8") as f:
    json.dump(vocabularies, f, ensure_ascii=False, indent=4)