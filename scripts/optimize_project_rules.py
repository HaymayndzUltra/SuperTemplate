#!/usr/bin/env python3
import re
import sys
from pathlib import Path
import yaml

ROOT = Path('/home/haymayndz/Labs-test2/.cursor/rules/project-rules')

CATEGORIES = {
    'languages': [
        'python','typescript','javascript','golang','java','cpp','rust','php','swift','kotlin','lua','julia'
    ],
    'frameworks': [
        'nextjs','react','react-native','angular','vue','svelte','sveltekit','nuxt','gatsby','remix','astro',
        'fastapi','django','nestjs','rails','flask','laravel','spring','expo','flutter','ionic','android'
    ],
    'compliance': ['pci-compliance','sox-compliance','accessibility','cybersecurity'],
    'infrastructure': ['azure','terraform','docker','kubernetes','aws','gcp','vercel','heroku'],
    'utilities': [
        'global','best-practices','performance','testing','security','clean-architecture','observability'
    ],
}

DUPLICATES = {
    'web-development.mdc': None,
    'backend-development.mdc': None,
}

STD_ALWAYS_APPLY = False
STD_SCOPE = 'project-rules'
STD_DESC_FMT = (
    'TAGS: [{tags}] | TRIGGERS: [{triggers}] | SCOPE: {scope} | DESCRIPTION: {desc}'
)

TAG_HINTS = {
    'python': ('language,backend', 'python,py,fastapi'),
    'typescript': ('language,frontend', 'ts,typescript,react,nextjs'),
    'javascript': ('language,frontend', 'js,javascript,react'),
    'golang': ('language,backend', 'go,golang,nethttp'),
    'java': ('language,backend', 'java,spring'),
    'cpp': ('language,systems', 'cpp,c++'),
    'rust': ('language,systems', 'rust,performance'),
    'php': ('language,backend', 'php,laravel'),
    'swift': ('language,mobile', 'swift,ios'),
    'kotlin': ('language,mobile', 'kotlin,android'),
    'lua': ('language,scripting', 'lua'),
    'julia': ('language,ml', 'julia'),
    'nextjs': ('framework,frontend', 'nextjs,react'),
    'react': ('framework,frontend', 'react,spa'),
    'react-native': ('framework,mobile', 'react-native,expo'),
    'angular': ('framework,frontend', 'angular'),
    'vue': ('framework,frontend', 'vue'),
    'svelte': ('framework,frontend', 'svelte'),
    'sveltekit': ('framework,frontend', 'sveltekit'),
    'nuxt': ('framework,frontend', 'nuxt,vue'),
    'gatsby': ('framework,frontend', 'gatsby,react'),
    'remix': ('framework,frontend', 'remix,react'),
    'astro': ('framework,frontend', 'astro'),
    'fastapi': ('framework,backend', 'fastapi,python'),
    'django': ('framework,backend', 'django,python'),
    'nestjs': ('framework,backend', 'nestjs,node'),
    'rails': ('framework,backend', 'rails,ruby'),
    'flask': ('framework,backend', 'flask,python'),
    'laravel': ('framework,backend', 'laravel,php'),
    'spring': ('framework,backend', 'spring,java'),
    'expo': ('framework,mobile', 'expo,react-native'),
    'flutter': ('framework,mobile', 'flutter,dart'),
    'ionic': ('framework,mobile', 'ionic,angular'),
    'android': ('framework,mobile', 'android,kotlin'),
    'pci-compliance': ('compliance,security', 'pci,payment,cardholder'),
    'sox-compliance': ('compliance,security', 'sox,finance,controls'),
    'accessibility': ('a11y,ui', 'accessibility,aria'),
    'cybersecurity': ('security', 'owasp,security'),
    'azure': ('cloud,iac', 'azure,terraform'),
    'terraform': ('iac,cloud', 'terraform,aws,azure,gcp'),
    'docker': ('container,devops', 'docker,containers'),
    'kubernetes': ('orchestration,devops', 'k8s,kubernetes'),
    'aws': ('cloud', 'aws,iam'),
    'gcp': ('cloud', 'gcp,iam'),
    'vercel': ('hosting', 'vercel,edge'),
    'heroku': ('hosting', 'heroku'),
    'global': ('global', 'global,all'),
    'best-practices': ('quality', 'best,practice'),
    'performance': ('performance', 'perf,latency'),
    'testing': ('testing', 'test,qa'),
    'security': ('security', 'security,owasp'),
    'clean-architecture': ('architecture', 'clean,architecture'),
    'observability': ('observability', 'logs,traces,metrics'),
}

GLOB_HINTS = {
    'languages': 'src/**/*.{ext}',
    'frameworks': '**/*{name}*/**',
    'compliance': '**/*',
    'infrastructure': 'infra/**/*',
    'utilities': '**/*',
}

DEFAULT_BODY = """
## Purpose
Provide actionable, production-ready guidance.

## AI Persona
- Role: Expert in this domain
- Style: Concise, prescriptive, secure-by-default

## Protocols
1. Apply rules deterministically
2. Enforce security/compliance gates
3. Document key decisions succinctly

## Checks
- Lint/tests/coverage thresholds
- Security/Compliance validations
""".strip()

FM_START = re.compile(r'^---\s*$')
FM_END = re.compile(r'^---\s*$')


def parse_frontmatter(text: str):
    lines = text.splitlines()
    if not lines or not FM_START.match(lines[0]):
        return None, text
    for i in range(1, min(len(lines), 200)):
        if FM_END.match(lines[i]):
            fm = '\n'.join(lines[1:i])
            body = '\n'.join(lines[i+1:])
            try:
                data = yaml.safe_load(fm) or {}
            except Exception:
                data = {}
            return data, body
    return None, text


def build_frontmatter(name: str, category: str, existing: dict):
    base = existing.copy() if existing else {}
    base['alwaysApply'] = False
    base['scope'] = STD_SCOPE
    stem = name.replace('.mdc', '')
    tags, triggers = TAG_HINTS.get(stem, ('general', stem))
    desc = base.get('description') or f'Guidance for {stem}'
    base['description'] = STD_DESC_FMT.format(
        tags=tags,
        triggers=triggers,
        scope=STD_SCOPE,
        desc=desc,
    )
    if 'globs' not in base or not base['globs']:
        if category in ('languages', 'frameworks'):
            if category == 'languages':
                ext = {
                    'python': 'py',
                    'typescript': '{ts,tsx}',
                    'javascript': '{js,jsx}',
                    'golang': 'go',
                    'java': 'java',
                    'cpp': '{cpp,hpp,c,h}',
                    'rust': 'rs',
                    'php': 'php',
                    'swift': 'swift',
                    'kotlin': 'kt',
                    'lua': 'lua',
                    'julia': 'jl',
                }.get(stem, '*')
                base['globs'] = [GLOB_HINTS['languages'].format(ext=ext)]
            else:
                base['globs'] = [GLOB_HINTS['frameworks'].format(name=stem)]
        else:
            base['globs'] = [GLOB_HINTS.get(category, '**/*')]
    return base


def categorize(name: str) -> str:
    stem = name.replace('.mdc', '')
    for cat, items in CATEGORIES.items():
        if stem in items or any(stem.startswith(i) for i in items):
            return cat
    return 'utilities'


def ensure_frontmatter(text: str, name: str, category: str):
    fm, body = parse_frontmatter(text)
    newfm = build_frontmatter(name, category, fm or {})
    fm_yaml = yaml.safe_dump(newfm, sort_keys=False).strip()
    body = (body or '').strip()
    if not body:
        body = DEFAULT_BODY
    if not body.endswith('\n'):
        body += '\n'
    return f"---\n{fm_yaml}\n---\n{body}"


def process_file(path: Path, dry_run=False):
    name = path.name
    if name in DUPLICATES:
        if not dry_run:
            path.unlink(missing_ok=True)
        return 'duplicate', str(path), None
    category = categorize(name)
    content = path.read_text(encoding='utf-8', errors='ignore')
    updated = ensure_frontmatter(content, name, category)
    dest_dir = ROOT / category
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / name
    if not dry_run:
        dest.write_text(updated, encoding='utf-8')
        path.unlink(missing_ok=True)
    return 'moved', str(path), str(dest)


def write_indexes_and_report(report):
    for cat in CATEGORIES.keys():
        cat_dir = ROOT / cat
        idx = cat_dir / 'INDEX.mdc'
        files = [p.name for p in sorted(cat_dir.glob('*.mdc'))]
        idx.write_text('\n'.join(['# Index', '', *files])+'\n', encoding='utf-8')
    global_idx = ROOT / 'INDEX.mdc'
    lines = ['# Project Rules Index', '']
    for cat in CATEGORIES.keys():
        lines.append(f'## {cat}')
        for p in sorted((ROOT / cat).glob('*.mdc')):
            lines.append(f'- {p.name}')
        lines.append('')
    global_idx.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    vr = ROOT / 'VALIDATION_REPORT.md'
    vr.write_text('# Validation Report\n\n' + yaml.safe_dump(report, sort_keys=False), encoding='utf-8')


def main():
    dry_run = '--dry-run' in sys.argv
    report = {'moved': [], 'duplicates': [], 'errors': []}
    for item in sorted(ROOT.glob('*.mdc')):
        try:
            status, src, dst = process_file(item, dry_run=dry_run)
            if status == 'duplicate':
                report['duplicates'].append(Path(src).name)
            elif status == 'moved':
                report['moved'].append({'from': src, 'to': dst})
        except Exception as e:
            report['errors'].append({'file': str(item), 'error': str(e)})
    if not dry_run:
        write_indexes_and_report(report)
    print(yaml.safe_dump(report, sort_keys=False))


if __name__ == '__main__':
    main()

