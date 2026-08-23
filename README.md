## Changyong Mun

Frontend engineer in Seoul, working on real-time, AI-facing interfaces — and on the tooling
and writing that make them usable by other people.

Currently at **AhnLab**, on an EDR security platform. I build the interface for an AI
threat-investigation agent: streaming agent reasoning to analysts over Server-Sent Events
using the AG-UI protocol, and shipping product modules independently through Module
Federation. Alongside that I automate the parts of engineering nobody enjoys — LLM-assisted
code review wired through n8n, and architecture diagrams generated as editable draw.io XML
rather than dead PNGs.

### Selected work

**[mcp-schema-census](https://github.com/cmun2/mcp-schema-census)** — your MCP server is
valid MCP and still gets a 400 from the model provider. This tells you why, at which JSON
pointer, quoting the sentence the rejection rests on. Backed by a public dataset of 617
servers and 14,804 real tool schemas. Building it surfaced a bug in the official Anthropic
Python SDK, which I reported and fixed upstream
([#1876](https://github.com/anthropics/anthropic-sdk-python/issues/1876) ·
[#1877](https://github.com/anthropics/anthropic-sdk-python/pull/1877)).

**Debugging Arena** — frontend accessibility failures turned into playable debugging
challenges. A runtime evaluator checks the rendered dialog contract while Playwright
verifies that same contract independently, so the exercise cannot quietly grade itself.
Built with Codex and GPT-5.6 during OpenAI Build Week.
[Live demo](https://codex-web-education.vercel.app) ·
[Demo video](https://youtu.be/d3uML8BsAm8) ·
[Devpost](https://devpost.com/software/codexwebeducation)

**[Portfolio](https://changyong-portfolio.vercel.app/en)** — case studies with the reasoning
behind each system, not just what shipped.

### Writing

[cmun2.inblog.io](https://cmun2.inblog.io) — 35+ posts in Korean on micro-frontends, SSE and
hydration, CI/CD and testing practice, plus an English series:

- [Module Federation in Production: What Actually Changed](https://cmun2.inblog.io/272066)
- [Streaming to the Browser: SSE for Telemetry and for Agents](https://cmun2.inblog.io/272256)
- [An LLM in the Code Review Loop: The Parts That Aren't the Model](https://cmun2.inblog.io/272259)

Each one starts from something that broke in production rather than from documentation.

### Stack

TypeScript · React · Next.js · Vue · Nuxt · Node.js · Python
Server-Sent Events · agent event streams · AG-UI · Module Federation · Playwright · n8n

### Contact

[LinkedIn](https://www.linkedin.com/in/changyong-mun/) · dkdkdkalalal@naver.com
