# IdeoMonitor

Pattern-based text scanner for compliance, audits, and internal review.

- Minimal, modular, open source.
- Single dependency: [`rich`](https://github.com/Textualize/rich)
- Patterns are plain regex—edit as needed in `scanner.py`.
- Designed and maintained by Rootflux (Nate).

---

## Quickstart

```bash
git clone https://github.com/rootflux/IdeoMonitor.git
cd IdeoMonitor
pip install -r requirements.txt
python run.py
```

Scan your own file or use the included `sample_text.txt`.

---

## Project Structure

- `run.py` – Entrypoint, no config needed.
- `ideomonitor/console_ui.py` – Handles all output, UI, and prompts.
- `ideomonitor/scanner.py` – Core scan logic; patterns live here.
- `sample_text.txt` – Example doc. Replace or extend as needed.

---

## Example Output

```
Line   Pattern           Context
----   ---------------  ------------------------------------------
1      \binternal use only\b   This document is intended for internal use only.
2      \bdo not distribute\b   Please do not distribute without proper authorization.
3      \bproprietary\b         All proprietary information must remain confidential.
3      \bconfidential\b        All proprietary information must remain confidential.
2      \bauthorization\b       Please do not distribute without proper authorization.
```

---

## License

MIT. No catch.

---

_Built and maintained by Nate / Rootflux. Because text never audits itself._
