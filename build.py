import os
import shutil
from pathlib import Path

os.environ["STATIC_BUILD"] = "1"

from app import app

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
STATIC_SRC = ROOT / "static"
STATIC_DST = DOCS / "static"

ROUTES = [("/", "index.html")] + [(f"/modulo{i}", f"modulo{i}.html") for i in range(1, 5)]


def main():
    if DOCS.exists():
        shutil.rmtree(DOCS)
    DOCS.mkdir()
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")

    with app.test_client() as client:
        for path, filename in ROUTES:
            resp = client.get(path)
            if resp.status_code != 200:
                raise RuntimeError(f"{path} -> {resp.status_code}")
            (DOCS / filename).write_bytes(resp.data)

    if STATIC_DST.exists():
        shutil.rmtree(STATIC_DST)
    shutil.copytree(STATIC_SRC, STATIC_DST)

    import json
    from app import module_records
    (DOCS / "modules.json").write_text(
        json.dumps(module_records(), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"Built {len(ROUTES)} pages into {DOCS}")


if __name__ == "__main__":
    main()
