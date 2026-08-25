## Changyong Mun

Frontend engineer in Seoul, working on real-time, AI-facing interfaces — and on the tooling and writing that make them usable by other people.

Currently at **AhnLab**, on an EDR security platform. I build the interface for an AI threat-investigation agent: streaming agent reasoning to analysts over Server-Sent Events using the AG-UI protocol, and shipping product modules independently through Module Federation. Alongside that I automate the parts of engineering nobody enjoys — LLM-assisted code review wired through n8n, and architecture diagrams generated as editable draw.io XML rather than dead PNGs.

### Selected work

**[mcp-schema-census](https://github.com/cmun2/mcp-schema-census)** — your MCP server is valid MCP and still gets a 400 from the model provider. This tells you why, at which JSON pointer, quoting the sentence the rejection rests on. Backed by a public dataset of 617 servers and 14,804 real tool schemas. Building it surfaced a bug in the official Anthropic Python SDK, which I reported and fixed upstream ([#1876](https://github.com/anthropics/anthropic-sdk-python/issues/1876) · [#1877](https://github.com/anthropics/anthropic-sdk-python/pull/1877)).

**Debugging Arena** — frontend accessibility failures turned into playable debugging challenges. A runtime evaluator checks the rendered dialog contract while Playwright verifies that same contract independently, so the exercise cannot quietly grade itself. Built with Codex and GPT-5.6 during OpenAI Build Week. [Live demo](https://codex-web-education.vercel.app) · [Demo video](https://youtu.be/d3uML8BsAm8) · [Devpost](https://devpost.com/software/codexwebeducation)

**[Portfolio](https://changyong-portfolio.vercel.app/en)** — case studies with the reasoning behind each system, not just what shipped.

<table><tr><td valign="top" width="50%">

### Writing

<!-- blog starts -->
[An LLM in the Code Review Loop: The Parts That Aren't the Model](https://cmun2.inblog.io/272259) — 2026-08-10

[Streaming to the Browser: SSE for Telemetry and for Agents](https://cmun2.inblog.io/272256) — 2026-07-13

[Module Federation in Production: What Actually Changed](https://cmun2.inblog.io/272066) — 2026-06-15

[Next.JS 변경된 내용이 바로 반영이 안되는 문제 발생 해결](https://cmun2.inblog.io/nextjs-변경된-내용이-바로-반영이-안되는-문제-발생-해결-52894) — 2025-04-21

[RequestAnimationFrame vs SetInterval](https://cmun2.inblog.io/requestanimationframe-vs-setinterval-52712) — 2025-04-17
<!-- blog ends -->

More at [cmun2.inblog.io](https://cmun2.inblog.io) — 35+ posts in Korean on micro-frontends, SSE and hydration, CI/CD and testing practice, plus an English series. Each one starts from something that broke in production rather than from documentation.

</td><td valign="top" width="50%">

### Recent activity

<!-- activity starts -->
PR [anthropics/anthropic-sdk-typescript#1163](https://github.com/anthropics/anthropic-sdk-typescript/pull/1163) fix(schema): keep $defs when the schema root is a $ref — 2026-08-24

Issue [anthropics/anthropic-sdk-typescript#1162](https://github.com/anthropics/anthropic-sdk-typescript/issues/1162) transformJSONSchema drops $defs when the schema root is a $ref — 2026-08-24

PR [anthropics/anthropic-sdk-python#1877](https://github.com/anthropics/anthropic-sdk-python/pull/1877) fix(lib): normalise JSON Schema type arrays instead of hitting assert_never — 2026-08-23

Pushed to [cmun2/mcp-schema-census](https://github.com/cmun2/mcp-schema-census) — 2026-08-23

Issue [anthropics/anthropic-sdk-python#1876](https://github.com/anthropics/anthropic-sdk-python/issues/1876) transform_schema raises AssertionError on type arrays (e.g. type: ["string","null"]) — 2026-08-23
<!-- activity ends -->

</td></tr></table>

### Stack

**AI & real-time** — LLM application development · agent event streams (AG-UI) · Server-Sent Events · Model Context Protocol · Codex · Claude Code · n8n

**Languages & frameworks** — TypeScript · JavaScript · Python · React · Next.js · Vue · Nuxt · Node.js

**Platform & quality** — Module Federation · micro-frontends · design systems (npm) · Playwright · Vitest · CI/CD

Before frontend I did machine-learning research at [CHANGlab](https://qbio.io/), Seoul National University — nanopore RNA sequencing data, FASTQ/BAM/SAM pipelines, and distribution analysis over pandas. It is why schema and data-shape bugs are the ones I tend to notice first.

### Contact

[LinkedIn](https://www.linkedin.com/in/changyong-mun/) · dkdkdkalalal@naver.com
