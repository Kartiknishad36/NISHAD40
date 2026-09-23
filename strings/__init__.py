import os
from typing import List

import yaml

languages = {}
languages_present = {}


def get_string(lang: str):
    return languages.get(lang) or languages["en"]


_LANG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "langs")

# always load English first
with open(os.path.join(_LANG_DIR, "en.yml"), encoding="utf8") as f:
    languages["en"] = yaml.safe_load(f)
languages_present["en"] = languages["en"].get("name", "English")

for filename in os.listdir(_LANG_DIR):
    if not filename.endswith(".yml") or filename == "en.yml":
        continue
    language_name = filename[:-4]
    path = os.path.join(_LANG_DIR, filename)
    try:
        with open(path, encoding="utf8") as f:
            data = yaml.safe_load(f) or {}
        # fill missing keys from English
        for item in languages["en"]:
            if item not in data:
                data[item] = languages["en"][item]
        languages[language_name] = data
        languages_present[language_name] = data.get("name", language_name)
    except Exception as e:
        print(f"Language skip {filename}: {e}")
        # exit() mat karo — en se chalega
