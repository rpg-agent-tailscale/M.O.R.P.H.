# MORPH 1.0
**Minimum Original Reconstruction, Maximum Practical Harvest**

MORPH helps developers deliver a *usable capability* without rebuilding the world. Separate software's **soul** (observable behavior, rules and acceptance criteria) from its **body** (interface, assets, runtime and interoperability). Then choose the shortest safe path to a working result.

## The MORPH ladder
1. **CONFIGURE** an existing tool.
2. **EXTEND** it with a script, plugin, or adapter.
3. **FORK / MORPH** a legitimately reusable open-source base.
4. **RECONSTRUCT** one authorized, observable behavior.
5. **BUILD NEW** only when the others do not meet the need.

Explore alternatives for roughly 30 minutes, choose one bounded working experiment, verify it and ship. Record nonblocking issues as Improvement Debt.

## Use now
Requires Python 3.10+ with no dependencies:

```bash
python morph.py init my-feature
python morph.py check my-feature
python -m unittest discover -s tests -v
```

The CLI generates editable soul/body briefs. `check` only detects unfinished placeholders; it is **not** a factual or legal validator. This release does **not** bundle REA/Reversa, analyze binaries, execute agents, or contact external services.

See [method](docs/METHOD.md), [architecture](docs/ARCHITECTURE.md), [responsible use](docs/LEGAL-ETHICS.md), and the [Treasure Seekers pilot](docs/TREASURE-SEEKERS-PILOT.md).

## Inspiration and acknowledgements
- [sandeco/reversa](https://github.com/sandeco/reversa): transform legacy code into traceable operational specifications.
- [morluto/rea](https://github.com/morluto/rea): evidence-backed investigation of application behavior.

MORPH is an original independent method, **not a fork or integration** of either project. All implementation and templates in this initial repository are original.

License: MIT. Contributions welcome: see CONTRIBUTING.md.
