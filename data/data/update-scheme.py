import json
from datetime import datetime
from pathlib import Path

p = Path(".")
for filename in p.glob("**/*.json"):
    print(filename)
    with open(filename) as f:
        content = json.load(f)

    now = datetime.utcnow()
    now = now.replace(microsecond=0)
    content = {
        "title": content["title"],
        "name": content["tag"],
        "creator": content["creator"],
        "license": content["license"],
        "data source": content["data source"],
        "last updated": now.isoformat(),
        "data": content["data"],
    }

    with open(filename, "w") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)
