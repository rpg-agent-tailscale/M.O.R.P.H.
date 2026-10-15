"""MORPH 1.0: dependency-free soul/body contract templates."""
from pathlib import Path
import argparse

TEMPLATES = {
 'brief.md': '# Capability brief\n\nProblem: TODO\nDesired outcome: TODO\nExisting alternatives: TODO\nAuthorization and rights: TODO\nSelected path (CONFIGURE/EXTEND/FORK/RECONSTRUCT/BUILD): TODO\nWhy: TODO\n',
 'soul.md': '# Soul: behavioral contract\n\nObservable input: TODO\nExpected output: TODO\nEdge case: TODO\nAcceptance example: TODO\nSource evidence: TODO\nUnknowns: TODO\n',
 'body.md': '# Body: implementation contract\n\nTarget platform: TODO\nReusable components: TODO\nVisual baseline: TODO\nFrozen invariants: TODO\nAssets and licenses: TODO\n',
 'proof.md': '# Proof and decision\n\nOne bounded test: TODO\nBefore: TODO\nAfter: TODO\nChecker result: TODO\nImprovement Debt: TODO\nShip/adapt/discard: TODO\n',
}

def init(folder):
    folder = Path(folder)
    if folder.exists() and any((folder/name).exists() for name in TEMPLATES):
        raise ValueError('Refusing to overwrite existing contracts')
    folder.mkdir(parents=True, exist_ok=True)
    for name, content in TEMPLATES.items():
        (folder/name).write_text(content, encoding='utf-8')
    return folder

def check(folder):
    folder = Path(folder)
    missing = [name for name in TEMPLATES if not (folder/name).is_file()]
    if missing:
        return 'MISSING: ' + ', '.join(missing)
    count = sum((folder/name).read_text(encoding='utf-8').count('TODO') for name in TEMPLATES)
    return f'INCOMPLETE: {count} TODO values' if count else 'READY FOR HUMAN REVIEW (not fact-verified)'

def main():
    p = argparse.ArgumentParser(description='MORPH: minimum reconstruction, maximum practical harvest')
    p.add_argument('action', choices=['init','check'])
    p.add_argument('folder')
    args = p.parse_args()
    print(init(args.folder) if args.action == 'init' else check(args.folder))

if __name__ == '__main__':
    main()
