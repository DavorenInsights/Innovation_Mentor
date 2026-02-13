# Innovation_Mentor.py
import streamlit as st
import textwrap
from datetime import datetime
from streamlit_extras.switch_page_button import switch_page
from app_config import PUBLIC

st.set_page_config(
    page_title="Innovation Instrument",
    page_icon="◼",
    layout="wide"
)

def local_css(file_name: str):
    with open(file_name, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# ---------- Console Header ----------
now = datetime.now().strftime("%Y-%m-%d %H:%M")

header = textwrap.dedent(f"""
<div class="hero sub-hero">
  <div class="hero-glow"></div>
  <div class="hero-content">
    <h1 class="hero-title">Innovation Intelligence Instrument</h1>
    <p class="hero-sub">
      Diagnostic lenses for readiness, constraints, and execution risk.
      <span class="muted">Public diagnostic layer.</span>
    </p>
    <p class="muted" style="margin-top:10px; font-size:13px;">
      Run timestamp: {now}
    </p>
  </div>
</div>
""")
st.markdown(header, unsafe_allow_html=True)

# ---------- Sidebar Nav ----------
st.sidebar.markdown("### Lenses")
if st.sidebar.button("TRL & Readiness", use_container_width=True):
    switch_page("trl_calculator")
if st.sidebar.button("Business Model Logic", use_container_width=True):
    switch_page("business_model_selector")
if st.sidebar.button("Commercialisation Logic", use_container_width=True):
    switch_page("commercialisation_strategy")
if st.sidebar.button("IP & Protectability", use_container_width=True):
    switch_page("ip_management")
if st.sidebar.button("Risk Framing", use_container_width=True):
    switch_page("risk_dashboard")

st.sidebar.markdown("---")
st.sidebar.markdown("### Outputs")
if PUBLIC:
    st.sidebar.caption("Public export: diagnostic summary only.")
else:
    st.sidebar.caption("Institutional export enabled.")

# ---------- Console Body ----------
left, right = st.columns([1.35, 1])

with left:
    st.markdown("## Project Context")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.text_input("Project / Venture name", key="proj_name")
    with c2:
        st.selectbox("Sector", ["Energy", "Mobility", "Health", "Manufacturing", "Other"], key="sector")
    with c3:
        st.selectbox("Stage", ["Idea", "Prototype", "Pilot", "Early commercial", "Scaling"], key="stage")

    st.markdown("## Start a Diagnostic Run")
    st.caption("Choose a lens in the sidebar. Your state accumulates across lenses.")
    st.markdown("""
<div class="section-block">
  <div class="section-title">How to use this instrument</div>
  <div class="section-text">
    Run one lens at a time. Each lens updates your diagnostic state.
    The public layer shows signals and constraints, not a full execution plan.
  </div>
</div>
""", unsafe_allow_html=True)

with right:
    st.markdown("## Diagnostic State")
    # placeholder metrics: wire these to your actual scoring/state once you confirm where it's stored
    m1, m2 = st.columns(2)
    with m1:
        st.metric("Readiness", "—")
    with m2:
        st.metric("Constraint Load", "—")

    st.markdown("### Flags")
    st.markdown("""
<div class="section-block">
  <div class="section-title">Current signals</div>
  <div class="section-text">
    No run data yet. Begin with TRL or Business Model Logic.
  </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>© Davoren Insights — Public Diagnostic Layer</div>", unsafe_allow_html=True)
