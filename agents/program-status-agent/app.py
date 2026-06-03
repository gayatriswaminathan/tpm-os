"""
Program Status Agent — a tiny Streamlit app that turns raw program notes into
a clean, audience-tuned status update.

It's the TPM OS `status-update` skill wrapped in a web UI. Model-agnostic:
it uses Claude or OpenAI if a key is set, and falls back to an offline mode so
it runs for anyone with no key.

Run:
    pip install -r requirements.txt
    streamlit run app.py
"""

import os
from pathlib import Path

import streamlit as st

# --- skill instructions -------------------------------------------------------

FALLBACK_SYSTEM = """You are a senior technical program manager writing a status update.
Lead with the overall status and the single most important headline. Tune the
depth to the audience. Give every Amber/Red a cause, an action, an owner, and a
date. Separate decisions/asks from FYIs. Be honest, not rosy. Keep it to one
screen for executives. Output:
Overall: RAG + one-line headline
✅ Progress · 🚧 In flight · ⚠️ Risks & blockers (with owner + date) ·
🙋 Decisions/help needed · 🔜 Next."""


def load_skill() -> str:
    """Use the repo's status-update SKILL.md if present; else a fallback prompt."""
    skill = Path(__file__).resolve().parents[2] / "skills" / "status-update" / "SKILL.md"
    if skill.exists():
        text = skill.read_text()
        if text.startswith("---"):
            parts = text.split("---", 2)
            if len(parts) == 3:
                return parts[2].strip()
        return text.strip()
    return FALLBACK_SYSTEM


# --- model-agnostic provider --------------------------------------------------

def offline_status(program: str, period: str, audience: str, notes: str) -> str:
    """Render a real, structured status update from notes — no model needed.

    Light keyword heuristics sort each note into progress / in-flight / risk /
    next, then format it in the status-update structure.
    """
    lines = [l.strip("-•* \t") for l in notes.splitlines() if l.strip()]
    risk_kw = ("block", "waiting", "slip", "delay", "risk", "issue", "down",
               "fail", "overrun", "pending", "stuck", "escalat")
    done_kw = ("finish", "done", "complete", "migrat", "resolved", "fixed",
               "went well", "shipped", "signed off", "launched", "closed")
    next_kw = ("next", "will ", "plan", "upcoming", "tomorrow", "then ", "going to")
    prog, inflight, risks, nexts = [], [], [], []
    for l in lines:
        low = l.lower()
        if any(k in low for k in risk_kw):
            risks.append(l)
        elif any(k in low for k in done_kw):
            prog.append(l)
        elif any(k in low for k in next_kw):
            nexts.append(l.split(":", 1)[-1].strip() if low.startswith("next") else l)
        else:
            inflight.append(l)
    overall = "🔴 Red" if len(risks) >= 3 else ("🟡 Amber" if risks else "🟢 Green")
    headline = risks[0] if risks else (prog[0] if prog else "On track.")
    out = [f"**{program} — Status Update | {period}**",
           f"**Overall: {overall} — {headline}**", ""]
    if prog:
        out.append("**✅ Progress this period**")
        out += [f"- {p}" for p in prog]
        out.append("")
    if inflight:
        out.append("**🚧 In flight**")
        out += [f"- {p}" for p in inflight]
        out.append("")
    if risks:
        out.append("**⚠️ Risks & blockers**")
        out += [f"- {r}  _→ assign an owner + date_" for r in risks]
        out.append("")
    if nexts:
        out.append("**🔜 Next**")
        out += [f"- {n}" for n in nexts]
        out.append("")
    out.append("_Drafted by the Program Status Agent (offline). Connect a model "
               "(Gemini / Claude / OpenAI) for richer phrasing._")
    return "\n".join(out)


def generate(system: str, user: str, program: str, period: str,
             audience: str, notes: str) -> tuple[str, str]:
    """Resolve Gemini → Claude → OpenAI → offline. Any provider error falls
    back to the offline formatter, so the app always produces a result."""
    try:
        if os.getenv("GEMINI_API_KEY"):
            import google.generativeai as genai
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=system)
            return model.generate_content(user).text, "Gemini"
        if os.getenv("ANTHROPIC_API_KEY"):
            import anthropic
            client = anthropic.Anthropic()
            msg = client.messages.create(
                model="claude-sonnet-4-6", max_tokens=1200,
                system=system, messages=[{"role": "user", "content": user}],
            )
            return msg.content[0].text, "Claude"
        if os.getenv("OPENAI_API_KEY"):
            from openai import OpenAI
            client = OpenAI()
            resp = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "system", "content": system},
                          {"role": "user", "content": user}],
            )
            return resp.choices[0].message.content, "OpenAI"
    except Exception:
        pass  # any provider error (404/429/auth) → offline formatter
    return offline_status(program, period, audience, notes), "offline"


# --- UI -----------------------------------------------------------------------

st.set_page_config(page_title="Program Status Agent · TPM OS", page_icon="📊", layout="centered")

BRAND_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

.stApp {
  background-color: #0a0a09;
  background-image:
    linear-gradient(#1a1916 1px, transparent 1px),
    linear-gradient(90deg, #1a1916 1px, transparent 1px);
  background-size: 48px 48px;
}
.block-container { max-width: 760px; padding-top: 2.5rem; }
html, body, [class*="css"], .stMarkdown, p, label, input, textarea { font-family: 'Inter', sans-serif !important; }

/* branded header */
.gs-brand { display:flex; align-items:center; gap:10px; margin-bottom:6px; }
.gs-brand .dot { width:24px; height:24px; border-radius:6px; background:#e9b949; color:#0a0a09; display:inline-flex; align-items:center; justify-content:center; font-weight:700; font-size:14px; }
.gs-brand .nm { font-weight:600; font-size:16px; color:#f4f1e9; }
.gs-brand .tag { font-family:'JetBrains Mono', monospace; font-size:12px; color:#9b9488; }
.gs-hero { font-size:40px; font-weight:700; letter-spacing:-.02em; line-height:1.05; margin:18px 0 8px; color:#f4f1e9; }
.gs-hero .g { color:#e9b949; }
.gs-sub { font-size:17px; color:#9b9488; margin-bottom:8px; }

/* inputs */
.stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] > div {
  background:#15140f !important; border:1px solid #211f1a !important; color:#f4f1e9 !important; border-radius:9px !important;
}
.stTextArea textarea { font-family:'JetBrains Mono', monospace !important; font-size:13px !important; }
label { color:#9b9488 !important; font-size:13px !important; font-weight:500 !important; }

/* primary button */
.stButton > button {
  background:#e9b949 !important; color:#0a0a09 !important; font-weight:600 !important;
  border:none !important; border-radius:9px !important; padding:.55rem 1.4rem !important;
}
.stButton > button:hover { background:#f3c75c !important; }
.stDownloadButton > button {
  background:transparent !important; color:#f4f1e9 !important; border:1px solid #211f1a !important; border-radius:9px !important;
}

/* output card */
.gs-out { background:#100f0d; border:1px solid #211f1a; border-radius:14px; padding:8px 22px; }

hr { border-color:#1a1916 !important; }
[data-testid="stSidebar"] { background:#100f0d; border-right:1px solid #1a1916; }
.gs-foot { font-family:'JetBrains Mono', monospace; font-size:12px; color:#615b51; }
.gs-foot a { color:#9b9488; text-decoration:none; }
</style>
"""
st.markdown(BRAND_CSS, unsafe_allow_html=True)

st.markdown(
    '<div class="gs-brand"><span class="dot">T</span>'
    '<span class="nm">TPM OS</span>'
    '<span class="tag">// program status agent</span></div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="gs-hero">Raw notes in.<br/>A <span class="g">clean status update</span> out.</div>',
            unsafe_allow_html=True)
st.markdown('<div class="gs-sub">Paste your messy program notes, pick an audience, '
            'and get an exec-ready update — every risk with an owner and a date.</div>',
            unsafe_allow_html=True)
st.write("")

with st.sidebar:
    st.header("Setup")
    st.write("Set an API key as an environment variable for live generation:")
    st.code("# free — no billing needed:\nexport GEMINI_API_KEY=...\n\n# or paid:\nexport ANTHROPIC_API_KEY=...\nexport OPENAI_API_KEY=...")
    st.write("Free key: [aistudio.google.com](https://aistudio.google.com) → Get API key.")
    st.write("No key? It runs in offline mode and shows the assembled context.")

col1, col2 = st.columns(2)
with col1:
    program = st.text_input("Program name", "Payments Migration")
with col2:
    audience = st.selectbox("Audience", ["exec", "stakeholder", "engineering"])

period = st.text_input("Reporting period", "Week ending May 29")

notes = st.text_area(
    "Raw notes",
    height=220,
    placeholder="Paste your messy notes here — what got done, what's blocked, "
                "risks, asks, dates...",
    value=(
        "- finished 3 more team migrations, now 12 of 18\n"
        "- API latency incident Tuesday, fixed Wednesday (config)\n"
        "- still waiting on security sign-off for SSO, blocking go-live\n"
        "- routing-engine vendor slipped delivery by a week\n"
        "- demo to business went well\n"
        "- next: finish remaining migrations, get security sign-off"
    ),
)

if st.button("Generate status update", type="primary"):
    if not notes.strip():
        st.warning("Add some notes first.")
    else:
        system = load_skill()
        user = (f"audience: {audience}\nprogram: {program}\nperiod: {period}\n\n"
                f"raw notes:\n{notes}")
        with st.spinner("Writing the update..."):
            output, provider = generate(system, user, program, period, audience, notes)
        st.success(f"Generated with: {provider}")
        st.markdown("---")
        st.markdown(output)
        st.download_button("Download as Markdown", output,
                           file_name="status-update.md")

st.markdown("---")
st.markdown(
    '<div class="gs-foot">built by '
    '<a href="https://github.com/gayatriswaminathan">Gayatri Swaminathan</a> · '
    '<a href="https://gayatriswaminathan.github.io/tpm-os">TPM OS</a> · '
    '<a href="https://notesbygs.substack.com">Notes by GS</a></div>',
    unsafe_allow_html=True,
)
