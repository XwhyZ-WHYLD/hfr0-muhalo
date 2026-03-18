---
name: Release checklist
about: Checklist for production release issue tracking
---

- [ ] Update `pyproject.toml` version
- [ ] Update `CHANGELOG.md` (if maintained)
- [ ] Run `ruff check .` and `pytest`
- [ ] Validate `Dockerfile` and `docker-compose.yml`
- [ ] Confirm results artifacts are committed (`results/*.json`)
- [ ] Tag release in GitHub
- [ ] Merge to main and verify CI passes
