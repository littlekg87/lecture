"""Generate legacy website URLs in the deployment output, never in the repo root."""
import html
import json
import shutil
import sys
from pathlib import Path


def build(site):
    site = site.resolve()
    config = json.loads(Path(__file__).with_name('legacy-urls.json').read_text())

    def path(relative):
        result = (site / relative).resolve()
        if not result.is_relative_to(site):
            raise ValueError(relative)
        return result

    for old, target in config['redirects'].items():
        expected = path(target + 'index.html' if target.endswith('/') else target)
        if not expected.is_file():
            raise FileNotFoundError(expected)
        # Relative to the site root, including installations under /lecture/.
        relative = '../' * (len(Path(old).parts) - 1) + target
        canonical = 'https://littlekg87.github.io/lecture/' + target
        output = path(old)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(
            '<!doctype html><html lang="ko"><head><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Ask Sillok 발표자료</title><link rel="canonical" href="'
            + html.escape(canonical, quote=True) + '"></head><body>'
            '<p>Ask Sillok 통합 폴더로 이동했습니다. <a id="destination" href="'
            + html.escape(relative, quote=True) + '">발표자료 열기</a></p><script>'
            'const destination=new URL(' + json.dumps(relative) + ',location.href);'
            'destination.search=location.search;destination.hash=location.hash;'
            'document.getElementById("destination").href=destination.href;'
            'location.replace(destination.href);</script></body></html>\n',
            encoding='utf-8',
        )
    for old, target in config['copies'].items():
        source, output = path(target), path(old)
        if not source.is_file():
            raise FileNotFoundError(source)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, output)
    print(f"Generated {len(config['redirects'])} redirects and {len(config['copies'])} copies")


if __name__ == '__main__':
    build(Path(sys.argv[1]))
