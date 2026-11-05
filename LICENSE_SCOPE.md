<!--
Project: OpenCLAW SEED — Complete Autonomous AI Ecosystem
Copyright (c) 2026 Francisco Angulo de Lafuente
Author: Francisco Angulo de Lafuente
ORCID: https://orcid.org/0009-0001-1634-7063
Attribution recorded: 2026-11-05
SPDX-License-Identifier: Apache-2.0
-->

# License Scope and Attribution

**Repository author:** Francisco Angulo de Lafuente ([ORCID](https://orcid.org/0009-0001-1634-7063)) · **Attribution recorded:** 2026-11-05

The existing root [Apache-2.0 LICENSE](LICENSE) is preserved unchanged. Native SPDX headers are added only to the 40 baseline text/code/configuration paths listed in `provenance-baseline.json` whose Git path history has the owner-only author label. This record does not amend the existing license or make separate rights claims for third-party material.

## Attribution treatment

- `.github/FUNDING.yml` retains its CAJAL Bot history and is unchanged.
- `Procfile` has no comment syntax; its baseline blob is recorded in the sidecar.
- The 19 GIF files and `seed_data/bootstrap_knowledge.jsonl` are preserved byte-for-byte and hash-recorded. Their underlying media/data authorship is not inferred from a Git commit label.
- `openclaw-agent-deploy.tar.gz` contains 22 historical files mapped by blob to this repository. Comment-compatible members receive attribution; `Procfile` is recorded by sidecar. The archive includes unmodified copies of `LICENSE` and `CITATION.cff`.
- The independent `seed-state` branch contains SEED Growth Bot-generated training outputs and data. This attribution change does not edit that branch. During review, its scheduled workflow independently advanced it to a new generated cycle; the observed bot commit and changed paths are recorded in `provenance.json`. The owner-history generator in `seed/training/engine.py` adds maintainer-only metadata to future script/notebook outputs. No individual author or SPDX claim is made for generated outputs.
- The independent `state` branch contains runtime, log and cache files and remains unchanged. No SPDX or individual authorship claim is made for its bot-generated contents.

## Evidence limits

The sidecars retain SHA-256 hashes, Git blob OIDs, path histories and selected excerpt hashes. Hashes identify exact bytes; they do not prove authorship, legal title or infringement. Git author names can be set by a committer. Third-party dependencies retain their own license terms.
