
import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Shivarathri Karthik | AI/ML & Agentic AI Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------
# Theme / Styling
# -----------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at 15% 5%, rgba(59,130,246,.12), transparent 25%),
        radial-gradient(circle at 85% 10%, rgba(139,92,246,.12), transparent 25%),
        #070b14;
    color: #eef2ff;
}

.block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

.hero {
    padding: 3rem 2.6rem;
    border: 1px solid rgba(148,163,184,.18);
    border-radius: 28px;
    background: linear-gradient(135deg, rgba(15,23,42,.92), rgba(30,41,59,.72));
    box-shadow: 0 25px 80px rgba(0,0,0,.28);
    position: relative;
    overflow: hidden;
}
.hero:after {
    content: "";
    position: absolute;
    width: 380px;
    height: 380px;
    right: -140px;
    top: -180px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(99,102,241,.35), transparent 65%);
}
.eyebrow {
    color: #93c5fd;
    font-weight: 700;
    letter-spacing: .12em;
    text-transform: uppercase;
    font-size: .82rem;
}
.hero h1 {
    font-size: clamp(2.4rem, 6vw, 5rem);
    line-height: 1.02;
    margin: .55rem 0;
    letter-spacing: -.055em;
}
.gradient {
    background: linear-gradient(90deg,#60a5fa,#a78bfa,#22d3ee);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    color: #cbd5e1;
    font-size: 1.08rem;
    max-width: 850px;
    line-height: 1.75;
}
.pill {
    display: inline-block;
    padding: .42rem .75rem;
    margin: .25rem .25rem .25rem 0;
    border: 1px solid rgba(148,163,184,.2);
    border-radius: 999px;
    background: rgba(15,23,42,.65);
    color: #dbeafe;
    font-size: .82rem;
}
.card {
    border: 1px solid rgba(148,163,184,.16);
    border-radius: 20px;
    padding: 1.25rem;
    background: rgba(15,23,42,.68);
    height: 100%;
    box-shadow: 0 12px 40px rgba(0,0,0,.16);
}
.card h3 { margin-top: 0; }
.muted { color: #94a3b8; }
.metric {
    font-size: 2rem;
    font-weight: 800;
    color: #f8fafc;
}
.section-title {
    font-size: 1.75rem;
    font-weight: 800;
    margin: 2.4rem 0 1rem;
}
.timeline {
    border-left: 2px solid rgba(96,165,250,.35);
    padding-left: 1.25rem;
    margin-left: .4rem;
}
.timeline-item {
    margin-bottom: 1.5rem;
    position: relative;
}
.timeline-item:before {
    content: "";
    position: absolute;
    left: -1.62rem;
    top: .45rem;
    width: .7rem;
    height: .7rem;
    border-radius: 50%;
    background: #60a5fa;
    box-shadow: 0 0 20px rgba(96,165,250,.8);
}
.smallcaps {
    color:#60a5fa;
    font-size:.78rem;
    font-weight:800;
    letter-spacing:.08em;
    text-transform:uppercase;
}
a { color:#93c5fd !important; text-decoration:none; }
footer { visibility:hidden; }
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.markdown("## 🤖 Karthik AI Portfolio")
    st.caption("AI/ML • GenAI • Agentic AI • Data Science")
    st.divider()
    st.markdown("### Navigate")
    st.markdown("- 🏠 Overview")
    st.markdown("- 🧠 Expertise")
    st.markdown("- 💼 Experience")
    st.markdown("- 🚀 Projects")
    st.markdown("- 🛠️ Tech Stack")
    st.markdown("- 🎓 Education & Certifications")
    st.markdown("- 📬 Contact")
    st.divider()
    st.markdown("### Recruiter Snapshot")
    st.markdown("**Nearly 4 years** enterprise AI experience")
    st.markdown("**IBM** — Aug 2022 to Present")
    st.markdown("**Hyderabad, India**")
    st.divider()
    st.markdown("📧 shivarathhrikarthik12@gmail.com")
    st.markdown("📱 +91 9381724151")

# -----------------------------
# Hero
# -----------------------------
st.markdown("""
<div class="hero">
  <div class="eyebrow">AI/ML Engineer · Generative AI · Agentic AI</div>
  <h1>Shivarathri <span class="gradient">Karthik</span></h1>
  <p>
    I design and deploy production-grade AI systems across Machine Learning,
    Data Science, Generative AI, RAG, LLMs and Agentic AI — from business
    requirements and data pipelines to scalable deployment, evaluation,
    monitoring and production support.
  </p>
  <div>
    <span class="pill">🧠 Agentic AI</span>
    <span class="pill">🔎 RAG</span>
    <span class="pill">🤖 LLMs</span>
    <span class="pill">📊 Machine Learning</span>
    <span class="pill">☁️ Azure / AWS</span>
    <span class="pill">⚙️ MLOps / LLMOps</span>
  </div>
</div>
""", unsafe_allow_html=True)

st.write("")

c1, c2, c3, c4 = st.columns(4)
for col, value, label in [
    (c1, "4+", "Years of enterprise AI experience"),
    (c2, "3", "AI domains: ML · GenAI · Agentic"),
    (c3, "7+", "Agent / AI frameworks & platforms"),
    (c4, "3", "Major enterprise client engagements"),
]:
    with col:
        st.markdown(f'<div class="card"><div class="metric">{value}</div><div class="muted">{label}</div></div>', unsafe_allow_html=True)

# -----------------------------
# About
# -----------------------------
st.markdown('<div class="section-title">🧠 What I Build</div>', unsafe_allow_html=True)

cols = st.columns(3)
cards = [
    ("Agentic AI & Multi-Agent Systems",
     "Planner, Retrieval, Research, Validation, Reflection, Memory and Tool Execution agents using LangGraph, LangChain, CrewAI and AutoGen."),
    ("Enterprise RAG & LLM Applications",
     "Production RAG pipelines with Azure OpenAI, GPT-4o, Claude, Gemini and Llama, including semantic search, hybrid search, reranking and citations."),
    ("ML & Data Science",
     "Predictive analytics, demand forecasting, anomaly detection, recommendation systems, classification, regression, clustering and time-series forecasting."),
]
for col, (title, text) in zip(cols, cards):
    with col:
        st.markdown(f'<div class="card"><h3>{title}</h3><p class="muted">{text}</p></div>', unsafe_allow_html=True)

# -----------------------------
# Experience
# -----------------------------
st.markdown('<div class="section-title">💼 Experience</div>', unsafe_allow_html=True)
st.markdown('<div class="timeline">', unsafe_allow_html=True)

experience = [
    ("Jul 2025 – Present", "Senior Agentic AI Engineer", "Citizens Bank, Rhode Island",
     "Enterprise Agentic AI platform for intelligent document processing, enterprise knowledge retrieval, workflow orchestration and AI-driven decision support.",
     "LangGraph · LangChain · CrewAI · AutoGen · Azure OpenAI · GPT-4o · Claude · Gemini · Llama · FastAPI · FAISS · Pinecone · Azure AI Search · Docker · Kubernetes · MLflow"),
    ("Jan 2024 – Jun 2025", "GenAI Engineer", "Ford Motor Company",
     "Enterprise Generative AI and RAG applications for knowledge management, document understanding, contextual Q&A and enterprise search.",
     "Azure OpenAI · GPT-4 · LangChain · FastAPI · FAISS · Pinecone · Azure AI Search · Docker · Kubernetes · Azure DevOps · GitHub Actions · MLflow"),
    ("Aug 2022 – Dec 2023", "AI/ML Engineer – Data Scientist", "General Motors (US Remote)",
     "Predictive analytics, demand forecasting, anomaly detection and business intelligence using scalable cloud-native ML architectures.",
     "Python · Scikit-learn · Pandas · NumPy · XGBoost · Random Forest · SQL · FastAPI · Flask · MLflow · Docker · Azure · Power BI · GitHub Actions"),
]
for date, role, client, overview, tech in experience:
    st.markdown(f"""
    <div class="timeline-item">
      <div class="smallcaps">{date}</div>
      <h3>{role}</h3>
      <div><strong>{client}</strong></div>
      <p class="muted">{overview}</p>
      <p><span class="pill">{tech}</span></p>
    </div>
    """, unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)

# -----------------------------
# Architecture / capabilities
# -----------------------------
st.markdown('<div class="section-title">🚀 Engineering Capabilities</div>', unsafe_allow_html=True)
cols = st.columns(4)
capabilities = [
    ("01", "Discover", "Business requirements, use-case discovery, solution design and stakeholder collaboration."),
    ("02", "Build", "Data pipelines, ML models, RAG systems, agents, APIs and enterprise integrations."),
    ("03", "Deploy", "Docker, Kubernetes, Azure, AWS, CI/CD and cloud-native AI applications."),
    ("04", "Operate", "Evaluation, monitoring, LLMOps, MLOps, optimization, governance and production support."),
]
for col, (num, title, text) in zip(cols, capabilities):
    with col:
        st.markdown(f'<div class="card"><div class="smallcaps">{num}</div><h3>{title}</h3><p class="muted">{text}</p></div>', unsafe_allow_html=True)

# -----------------------------
# Tech stack
# -----------------------------
st.markdown('<div class="section-title">🛠️ Technology Stack</div>', unsafe_allow_html=True)

stack = {
    "Agentic AI & GenAI": "LangGraph · LangChain · CrewAI · AutoGen · RAG · Prompt Engineering · Function Calling · Tool Calling · Memory",
    "LLMs": "GPT-4o · GPT-4 · Azure OpenAI · Claude · Gemini · Llama · Hugging Face Transformers",
    "Machine Learning": "Scikit-learn · XGBoost · LightGBM · Random Forest · Decision Trees · Logistic Regression · K-Means · ARIMA · Prophet",
    "Deep Learning & NLP": "TensorFlow · PyTorch · Keras · ANN · CNN · RNN · LSTM · GRU · Transformers · NLTK · SpaCy",
    "Vector & Search": "FAISS · Pinecone · Weaviate · Azure AI Search · OpenSearch · Semantic Search · Hybrid Search · Embeddings",
    "Backend & Data": "Python · SQL · FastAPI · Flask · REST APIs · Pandas · NumPy · PySpark · Kafka · ETL",
    "MLOps / LLMOps": "MLflow · Kubeflow · GitHub Actions · Azure DevOps · AWS CodePipeline · Model Monitoring",
    "Cloud & DevOps": "Microsoft Azure · Azure OpenAI · AWS · Amazon Bedrock · SageMaker · Docker · Kubernetes",
    "Enterprise": "SAP ECC · SAP S/4HANA · SAP HANA · SAP OData · SharePoint · Confluence · Jira · SQL Server · PostgreSQL · MySQL",
}
for i, (title, items) in enumerate(stack.items()):
    if i % 2 == 0:
        a, b = st.columns(2)
    with (a if i % 2 == 0 else b):
        st.markdown(f'<div class="card" style="margin-bottom:1rem;"><h4>{title}</h4><p class="muted">{items}</p></div>', unsafe_allow_html=True)

# -----------------------------
# Education & Certifications
# -----------------------------
st.markdown('<div class="section-title">🎓 Education & Certifications</div>', unsafe_allow_html=True)
a, b = st.columns(2)
with a:
    st.markdown("""
    <div class="card">
      <div class="smallcaps">Education</div>
      <h3>B.Tech — Computer Science & Engineering</h3>
      <p class="muted">Jawaharlal Nehru Technological University Hyderabad (JNTUH) · 2022</p>
    </div>
    """, unsafe_allow_html=True)
with b:
    st.markdown("""
    <div class="card">
      <div class="smallcaps">Certifications</div>
      <p>• Microsoft Azure AI Fundamentals</p>
      <p>• AWS Machine Learning</p>
      <p>• IBM Generative AI</p>
      <p>• DeepLearning.AI Generative AI</p>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Contact CTA
# -----------------------------
st.markdown('<div class="section-title">📬 Let’s Build Production AI</div>', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
  <h2>Looking for an AI/ML Engineer who can go from idea → architecture → production?</h2>
  <p>
    I’m open to opportunities across AI/ML Engineering, Generative AI,
    Agentic AI, RAG, Data Science and applied AI engineering.
  </p>
</div>
""", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)
with c1:
    st.link_button("📧 Email Me", "mailto:shivarathhrikarthik12@gmail.com", use_container_width=True)
with c2:
    st.link_button("💻 GitHub", "https://github.com/ShivarathriKarthik", use_container_width=True)
with c3:
    st.link_button("🔗 LinkedIn", "https://www.linkedin.com/", use_container_width=True)

st.caption("© 2026 Shivarathri Karthik · AI/ML Engineer · Generative AI · Agentic AI")
