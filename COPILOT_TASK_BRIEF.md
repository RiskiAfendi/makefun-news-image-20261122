# Copilot Task Brief — Make.fun News Image

**Bounty:** https://make.fun/bounty/news-image-20261122  
**Target news date:** Sunday, 22 November 2026  
**Repository:** https://github.com/RiskiAfendi/makefun-news-image-20261122  
**Required runtime:** Python 3.13  
**Entry point:** `main.py` at repository root

## Mission

Build an original, editorial-quality one-image summary of the world's news on 22 November 2026, plus a deterministic offline program that writes it to `/output/entry.png`.

## Mandatory bounty gates

1. Keep this repository public and under the entrant's own GitHub account. The existing MIT license is the OSI-approved project license.
2. Put the executable entry point at root as `main.py` for Python 3.13.
3. The program runs without network access.
4. Both executions must write exactly the same bytes to `/output/entry.png`.
5. The image must be a complete PNG or JPEG, at most 1 MiB (1,048,576 bytes), and at most 1024 × 1024 pixels.
6. AI coding-agent transcripts for the sessions that build the entry must be included with the make.fun submission.
7. The session that builds the entry must begin after this bounty opened. Keep all implementation work and its evidence in the eligible session.
8. For entries received from 23 November 2026 00:00 UTC onward, do not execute code obtained from environment secrets. Do not use `eval`, `Function`, `vm`, dynamic imports, or shells/interpreters fed with environment-secret values to run program code.
9. Do not copy another entrant's submitted code or image. Do not use downloaded code as the deliverable. Write the implementation in this Copilot session and keep provenance clear.

## Implementation approach

- Prefer a simple, auditable Python 3.13 entry point using only the standard library.
- Store the finished, original image at `assets/entry.png`.
- Have `main.py` copy those exact bytes to `/output/entry.png`; create the output directory if needed.
- Do not make HTTP requests, access external services, install packages at runtime, or depend on machine-specific fonts/assets.
- Keep `main.py` small and deterministic. It must not generate timestamps, random values, or other run-dependent output.
- Add a local validation script or tests only if useful; keep the actual required entry point at repository root.

## Editorial and factual standards

- Use the owner's verified research and approved concept documents as the source of news selection and visual direction.
- Do not invent events, dates, casualty figures, quotes, statistics, or causal claims.
- Prioritize a clear hierarchy: a small number of dominant lead stories, concise supporting stories, restrained data points, legible labels, and an original visual system.
- The image itself must communicate the target date and a coherent global-news picture without relying on a caption outside the image.
- Do not copy, trace, or imitate another entrant's image. Public entries may be studied only as high-level reference; create an original composition and artwork.
- If the verified research files or final approved visual concept are unavailable in this session, stop and ask the owner to provide them rather than guessing.

## Required verification before any submission

- Confirm the PNG/JPEG signature and complete file structure.
- Confirm dimensions are no greater than 1024 × 1024.
- Confirm image size is no greater than 1,048,576 bytes.
- Run `main.py` twice in the actual target-compatible environment.
- Compare the two output files byte-for-byte.
- Confirm there are no network calls or runtime dependencies.
- Confirm the transcript(s) for the session that authored the deliverable are ready to upload.
- Do not submit until every check passes and the owner approves.

## Current state

Repository setup is complete; implementation has not started. No `main.py`, final image, tests, or make.fun submission have been created yet.
