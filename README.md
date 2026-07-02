# HO8 — Your Own MCP Server

> Hands-on portfolio project · **Week 4** · **Solo** · module M12. Part of the **ForgeMind AI — AI Productivity Essentials** course.

## Goal

**Done when:** A working MCP server exposing a real tool over data you actually have (ideally your HO7 capstone)

## What to ship

The server code + manifest + README on the tool it exposes + a clip of Claude calling it.

## Pick a problem statement

Choose **one** of these real use-cases — or bring your own (get it approved first):

1. You already built a solution in HO7 (your mid-course capstone) — now let Claude act on it live. Build an MCP server that exposes your HO7 project's data or actions as a real tool, so Claude can answer questions or take actions straight from it. Success: a clip of Claude calling your tool and returning a real result from your HO7 solution, not a guess — your two hands-on now connected end-to-end.

2. Your team keeps customer data in a sheet or database and you re-answer the same lookups all day. Build an MCP server that exposes it as a queryable tool so Claude can fetch 'how many orders did this client place?' directly. Success: a clip of Claude calling your tool and returning a real row from your data, not a guess.

3. You rely on a public API (weather, stocks, GitHub) but copy-pasting its output into chat is clunky. Build an MCP server that wraps that API so Claude can call it on demand inside a conversation. Success: a recording of Claude invoking your tool and answering a live question with fresh data the API returned.

4. Your tasks live in a tracker and you context-switch constantly to add or check them. Build an MCP server that can both read and write your task tracker, so Claude can list open tasks and create new ones for you. Success: a clip of Claude calling the tool to add a task and then listing it back, proving the write worked.

5. Sales reps keep pinging you for the same pricing and commission numbers. Build an MCP server exposing your company calculator (pricing, quotes, commissions) as a tool Claude can call with the inputs. Success: a recording of Claude passing real inputs to your tool and returning the correct calculated quote, with the logic running server-side.

## How to use this repo

1. Click **Use this template** to create your own copy.
2. Build your chosen project in your copy.
3. Replace this section of the README with: what you built, the problem it solves, and how to run it.

---

*HO8 · Solo · ForgeMind AI Course · module M12 (Week 4)*


## 💡 Use your Claude.ai Pro plan wisely

The Pro plan has a usage limit that resets every few hours. A few habits make it stretch — and
keep a mistake from burning your whole session:

- **Use the example prompt** in each sample's README — it's already written and tested. Don't
  reinvent it.
- **One clear prompt** beats lots of vague back-and-forth. Say what you want, with an example, in
  a single message.
- **Start a new chat when you switch tasks.** Long chats re-read every earlier message and use up
  your limit faster.
- **Don't paste big files over and over.** Paste once, then refer back to it.
- **If something works, keep it.** Tweak it rather than regenerate from scratch.
- **Using Claude Code or Cowork?** This repo's `CLAUDE.md` makes Claude follow these same rules
  automatically, and `SKILL.md` is a reusable "token-wise" skill.

If you do hit the limit, it resets after a few hours — nothing you've saved is lost.
