import streamlit as st
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Shivarathri Karthik | AI/ML Engineer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# PROFILE INFORMATION
# ============================================================

NAME = "Shivarathri Karthik"

EMAIL = "shivarathhrikarthik12@gmail.com"

PHONE = "+91 9381724151"

GITHUB_URL = "https://github.com/ShivarathriKarthik"

LINKEDIN_URL = "https://www.linkedin.com/in/shivarathri-karthik-900095278/"

# ============================================================
# PHOTO PATH
#
# Put your photo in the SAME folder as app.py
#
# Example:
#
# portfolio/
# ├── app.py
# └── Karthik.jpg
#
# If your file has a different name, change this line.
# ============================================================

PHOTO_PATH = r"Passport Photo Karthik.jpg"

# ============================================================
# RESUME
# ============================================================
# Put your PDF in the same folder as app.py.
#
# Example:
#
# portfolio/
# ├── app.py
# ├── Karthik.jpg
# └── Shivarathri Karthik IBM Resume.pdf
#
# If your resume has another filename, change this line.
# ============================================================

RESUME_PATH = "Shivarathri Karthik IBM Resume.pdf"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 0%,
                rgba(37, 99, 235, 0.12),
                transparent 30%
            ),
            radial-gradient(
                circle at 90% 0%,
                rgba(124, 58, 237, 0.10),
                transparent 30%
            ),
            #070b14;
    }


    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }


    /* ========================================================
       HEADINGS
       ======================================================== */

    h1 {
        font-weight: 800 !important;
        letter-spacing: -0.04em !important;
    }

    h2 {
        font-weight: 750 !important;
        letter-spacing: -0.025em !important;
    }

    h3 {
        font-weight: 700 !important;
    }


    /* ========================================================
       CONTAINERS
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 18px;
        border: 1px solid rgba(148, 163, 184, 0.14);
        background: rgba(15, 23, 42, 0.65);
    }


    /* ========================================================
       PROFILE IMAGE
       ======================================================== */

    div[data-testid="stImage"] img {
        border-radius: 20px;
        border: 1px solid rgba(148, 163, 184, 0.16);
        box-shadow:
            0 20px 50px rgba(0, 0, 0, 0.35);
    }


    /* ========================================================
       METRICS
       ======================================================== */

    div[data-testid="stMetric"] {
        background:
            rgba(15, 23, 42, 0.80);

        border:
            1px solid rgba(148, 163, 184, 0.14);

        border-radius: 16px;

        padding: 1rem;

        min-height: 115px;
    }

    div[data-testid="stMetricLabel"] {
        color: #94a3b8 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #f8fafc !important;
        font-weight: 800 !important;
    }


    /* ========================================================
       BUTTONS
       ======================================================== */

    div.stButton > button,
    div[data-testid="stLinkButton"] a {
        border-radius: 10px !important;
        min-height: 42px !important;
        font-weight: 600 !important;
    }


    /* ========================================================
       SKILL TAGS
       ======================================================== */

    .skill-tag {
        display: inline-block;

        padding: 7px 12px;

        margin: 4px 3px;

        border-radius: 999px;

        background:
            rgba(30, 41, 59, 0.9);

        border:
            1px solid rgba(96, 165, 250, 0.18);

        color: #dbeafe;

        font-size: 0.78rem;

        font-weight: 500;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer-text {
        text-align: center;

        color: #64748b;

        line-height: 1.8;

        padding-top: 1rem;

        padding-bottom: 1rem;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🤖 Karthik")

    st.caption("AI/ML Engineer")

    st.caption("Generative AI • Agentic AI")

    st.divider()

    st.markdown("### Portfolio")

    st.markdown("🏠 Introduction")

    st.markdown("🧠 Core Expertise")

    st.markdown("💼 Experience")

    st.markdown("🚀 Projects")

    st.markdown("🛠️ Technology")

    st.markdown("🎓 Education")

    st.markdown("📜 Certifications")

    st.markdown("📄 Resume")

    st.markdown("📬 Contact")

    st.divider()

    st.markdown("### Contact")

    st.write(EMAIL)

    st.write(PHONE)


# ============================================================
# INTRODUCTION
# ============================================================

st.title("Introduction")

st.caption(
    "AI/ML Engineer • Generative AI • Agentic AI"
)

st.write("")


# ============================================================
# HERO SECTION
# ============================================================

photo_col, profile_col = st.columns(
    [1.0, 2.2],
    gap="large"
)


# ============================================================
# LEFT — PROFILE PHOTO
# ============================================================

with photo_col:

    photo_file = Path(PHOTO_PATH)

    if photo_file.exists():

        st.image(
            str(photo_file),
            use_container_width=True
        )

    else:

        st.error(
            "Profile photo not found."
        )

        st.info(
            f"""
            Put your profile photo in the same folder as
            `app.py`.

            Current path:

            `{PHOTO_PATH}`
            """
        )


# ============================================================
# RIGHT — PROFILE
# ============================================================

with profile_col:

    # --------------------------------------------------------
    # ROLE BOX
    # --------------------------------------------------------

    with st.container(border=True):

        st.markdown(
            "## 🔵 AI/ML ENGINEER"
        )

        st.markdown(
            "**GENERATIVE AI  •  AGENTIC AI**"
        )


    st.write("")


    # --------------------------------------------------------
    # NAME
    # --------------------------------------------------------

    st.title(
        "Shivarathri Karthik"
    )


    # --------------------------------------------------------
    # PROFESSIONAL TITLE
    # --------------------------------------------------------

    st.subheader(
        "AI/ML Engineer | Generative AI | Agentic AI"
    )


    # --------------------------------------------------------
    # INTRODUCTION
    # --------------------------------------------------------

    st.write(
        """
        AI/ML Engineer with **4+ years of professional
        experience** building enterprise Machine Learning,
        Generative AI, RAG and Agentic AI solutions.
        """
    )

    st.write(
        """
        I specialize in designing production-ready AI systems,
        multi-agent architectures, LLM applications,
        enterprise retrieval pipelines and scalable
        machine-learning solutions.
        """
    )

    st.write(
        """
        My focus is on taking AI from
        **prototype → production**.
        """
    )


    # --------------------------------------------------------
    # SOCIAL + RESUME BUTTONS
    # --------------------------------------------------------

    github_col, linkedin_col, email_col, resume_col = st.columns(
        4
    )


    with github_col:

        st.link_button(
            "💻 GitHub",
            GITHUB_URL,
            use_container_width=True
        )


    with linkedin_col:

        st.link_button(
            "🔗 LinkedIn",
            LINKEDIN_URL,
            use_container_width=True
        )


    with email_col:

        st.link_button(
            "📧 Email",
            f"mailto:{EMAIL}",
            use_container_width=True
        )


    with resume_col:

        resume_file = Path(RESUME_PATH)

        if resume_file.exists():

            with open(
                resume_file,
                "rb"
            ) as file:

                resume_data = file.read()

            st.download_button(
                label="📄 Resume",
                data=resume_data,
                file_name=resume_file.name,
                mime="application/pdf",
                use_container_width=True
            )

        else:

            st.warning(
                "Resume not found"
            )


# ============================================================
# RECRUITER SNAPSHOT
# ============================================================

st.divider()

st.header(
    "Recruiter Snapshot"
)

st.caption(
    "A quick overview of my professional profile."
)


metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:

    st.metric(
        label="Experience",
        value="4+ Years"
    )


with metric2:

    st.metric(
        label="Organization",
        value="IBM"
    )


with metric3:

    st.metric(
        label="Specialization",
        value="GenAI"
    )


with metric4:

    st.metric(
        label="Focus",
        value="AI → Production"
    )


# ============================================================
# CORE EXPERTISE
# ============================================================

st.divider()

st.header(
    "Core Expertise"
)

st.caption(
    "Technologies and engineering capabilities."
)


skills = [

    "Python",
    "Machine Learning",
    "Deep Learning",
    "Data Science",
    "Generative AI",
    "Agentic AI",
    "LLMs",
    "RAG",
    "LangChain",
    "LangGraph",
    "CrewAI",
    "AutoGen",
    "Azure OpenAI",
    "GPT-4o",
    "Claude",
    "Gemini",
    "Llama",
    "FAISS",
    "Pinecone",
    "OpenSearch",
    "MLflow",
    "Docker",
    "Kubernetes",
    "Azure",
    "AWS",
    "GCP",
    "Vertex AI",

]


skill_html = ""


for skill in skills:

    skill_html += (
        f'<span class="skill-tag">{skill}</span>'
    )


st.markdown(
    skill_html,
    unsafe_allow_html=True
)


# ============================================================
# WHAT I BUILD
# ============================================================

st.divider()

st.header(
    "What I Build"
)

st.caption(
    "End-to-end AI engineering capabilities."
)


build1, build2, build3 = st.columns(
    3,
    gap="large"
)


# ------------------------------------------------------------
# AGENTIC AI
# ------------------------------------------------------------

with build1:

    with st.container(border=True):

        st.subheader(
            "🤖 Agentic AI"
        )

        st.write(
            """
            Multi-agent systems using LangGraph,
            LangChain, CrewAI and AutoGen.

            Planning, orchestration, tool calling,
            memory, reflection, validation and
            autonomous workflows.
            """
        )


# ------------------------------------------------------------
# RAG
# ------------------------------------------------------------

with build2:

    with st.container(border=True):

        st.subheader(
            "🔎 Enterprise RAG"
        )

        st.write(
            """
            Production RAG systems using LLMs,
            embeddings, vector databases,
            semantic search, hybrid retrieval,
            reranking and enterprise data.
            """
        )


# ------------------------------------------------------------
# MACHINE LEARNING
# ------------------------------------------------------------

with build3:

    with st.container(border=True):

        st.subheader(
            "📊 ML & Data Science"
        )

        st.write(
            """
            Predictive modelling, classification,
            regression, clustering, forecasting,
            NLP, anomaly detection and
            data-driven solutions.
            """
        )


# ============================================================
# PROFESSIONAL EXPERIENCE
# ============================================================

st.divider()

st.header(
    "Professional Experience"
)

st.caption(
    "Selected enterprise AI/ML experience."
)


# ============================================================
# EXPERIENCE 1
# ============================================================

with st.container(border=True):

    st.caption(
        "JUL 2025 — PRESENT"
    )

    st.subheader(
        "Senior Agentic AI Engineer"
    )

    st.write(
        "**Enterprise Multi-Agent AI Platform — General Motors (GM)**"
    )

    st.write(
        """
        Designed and developed multi-agent AI architectures
        using LangGraph, LangChain, CrewAI and AutoGen.

        Built specialized Planner, Orchestrator, Retrieval,
        Research, Validation, Reflection, Memory and
        Tool Execution agents.

        Developed enterprise RAG pipelines integrating
        SharePoint, Confluence, Jira, SAP and SQL Server.
        """
    )

    st.markdown(
        """
        **Core Technologies**

        `LangGraph` `LangChain` `CrewAI` `AutoGen`
        `Azure OpenAI` `GPT-5o` `Claude` `Gemini`
        `Llama` `RAG`
        """
    )


# ============================================================
# EXPERIENCE 2
# ============================================================

with st.container(border=True):

    st.caption(
        "GENERATIVE AI / RAG"
    )

    st.subheader(
        "Generative AI Engineer"
    )

    st.write(
        "**Enterprise AI Solutions — Citizens Bank**"
    )

    st.write(
        """
        Developed enterprise Generative AI and RAG
        applications for knowledge retrieval,
        document intelligence, contextual question
        answering and AI-assisted workflows.

        Designed retrieval pipelines, prompt strategies,
        LLM integrations and production-oriented
        AI services.
        """
    )

    st.markdown(
        """
        **Core Technologies**

        `Python` `LangChain` `RAG` `Azure OpenAI`
        `Embeddings` `Vector Databases` `Docker`
        """
    )


# ============================================================
# EXPERIENCE 3
# ============================================================

with st.container(border=True):

    st.caption(
        "AI / ML ENGINEERING"
    )

    st.subheader(
        "AI/ML Engineer & Data Scientist"
    )

    st.write(
        """
        Developed Machine Learning and Data Science
        solutions covering predictive analytics,
        classification, regression, NLP, anomaly
        detection and business intelligence.

        Worked across the ML lifecycle from data
        preparation and feature engineering to
        model evaluation and deployment.
        """
    )

    st.markdown(
        """
        **Core Technologies**

        `Python` `Pandas` `NumPy` `Scikit-learn`
        `XGBoost` `MLflow` `SQL` `Power BI`
        """
    )


# ============================================================
# FEATURED PROJECTS
# ============================================================

st.divider()

st.header(
    "Featured Projects"
)

st.caption(
    "Selected AI engineering projects."
)


project1, project2 = st.columns(
    2,
    gap="large"
)


# ------------------------------------------------------------
# PROJECT 1
# ------------------------------------------------------------

with project1:

    with st.container(border=True):

        st.subheader(
            "🚀 Enterprise Multi-Agent AI Platform"
        )

        st.caption(
            "Agentic AI • LangGraph • LangChain"
        )

        st.write(
            """
            Production-oriented multi-agent platform
            designed to break complex enterprise tasks
            into specialized AI workflows.

            Architecture includes planning,
            orchestration, retrieval, research,
            validation, reflection, memory and
            tool execution.
            """
        )

        st.markdown(
            """
            **Stack**

            `LangGraph` `LangChain` `CrewAI`
            `AutoGen` `Azure OpenAI`
            `GPT-4o` `Claude` `Gemini`
            """
        )


# ------------------------------------------------------------
# PROJECT 2
# ------------------------------------------------------------

with project2:

    with st.container(border=True):

        st.subheader(
            "🔍 Enterprise RAG Platform"
        )

        st.caption(
            "RAG • LLM • Document Intelligence"
        )

        st.write(
            """
            Enterprise retrieval platform supporting
            ingestion, chunking, embeddings, retrieval,
            context construction and grounded
            LLM responses.
            """
        )

        st.markdown(
            """
            **Stack**

            `Python` `LangChain` `Azure OpenAI`
            `FAISS` `Pinecone` `OpenSearch`
            `Embeddings` `Reranking`
            """
        )


# ============================================================
# ENGINEERING CAPABILITIES
# ============================================================

st.divider()

st.header(
    "Engineering Capabilities"
)


cap1, cap2, cap3, cap4 = st.columns(
    4,
    gap="medium"
)


with cap1:

    with st.container(border=True):

        st.subheader("01")

        st.write("**Architecture**")

        st.caption(
            "AI solution architecture, system design, "
            "agent architecture and RAG design."
        )


with cap2:

    with st.container(border=True):

        st.subheader("02")

        st.write("**Development**")

        st.caption(
            "Python, APIs, AI agents, ML models, "
            "LLM applications and data pipelines."
        )


with cap3:

    with st.container(border=True):

        st.subheader("03")

        st.write("**Deployment**")

        st.caption(
            "Docker, Kubernetes, cloud platforms, "
            "CI/CD and production deployment."
        )


with cap4:

    with st.container(border=True):

        st.subheader("04")

        st.write("**Optimization**")

        st.caption(
            "Evaluation, observability, performance, "
            "cost optimization and LLMOps."
        )


# ============================================================
# TECHNOLOGY STACK
# ============================================================

st.divider()

st.header(
    "Technology Stack"
)


tech1, tech2 = st.columns(
    2,
    gap="large"
)


with tech1:

    with st.container(border=True):

        st.subheader(
            "🤖 Generative AI & Agentic AI"
        )

        st.write(
            """
            LangGraph

            LangChain

            CrewAI

            AutoGen

            RAG

            Prompt Engineering

            Function Calling

            Tool Calling

            Memory

            Multi-Agent Systems
            """
        )


with tech2:

    with st.container(border=True):

        st.subheader(
            "🧠 Large Language Models"
        )

        st.write(
            """
            Azure OpenAI

            GPT-4o

            Claude

            Gemini

            Llama

            Hugging Face Transformers
            """
        )


tech3, tech4 = st.columns(
    2,
    gap="large"
)


with tech3:

    with st.container(border=True):

        st.subheader(
            "📊 Machine Learning & Data Science"
        )

        st.write(
            """
            Python

            Pandas

            NumPy

            Scikit-learn

            XGBoost

            TensorFlow

            PyTorch

            NLP

            Feature Engineering

            Model Evaluation
            """
        )


with tech4:

    with st.container(border=True):

        st.subheader(
            "🔎 Vector Search & RAG"
        )

        st.write(
            """
            FAISS

            Pinecone

            Weaviate

            OpenSearch

            Azure AI Search

            Embeddings

            Semantic Search

            Hybrid Search

            Reranking
            """
        )


tech5, tech6 = st.columns(
    2,
    gap="large"
)


with tech5:

    with st.container(border=True):

        st.subheader(
            "☁️ Cloud & MLOps"
        )

        st.write(
            """
            Microsoft Azure

            AWS

            GCP

            Vertex AI

            AWS SageMaker

            MLflow

            Kubeflow

            Docker

            Kubernetes

            GitHub Actions
            """
        )


with tech6:

    with st.container(border=True):

        st.subheader(
            "⚙️ Backend & Data"
        )

        st.write(
            """
            FastAPI

            Flask

            REST APIs

            SQL

            MySQL

            SQL Server

            PostgreSQL

            ETL

            Power BI

            Git / GitHub
            """
        )


# ============================================================
# ENTERPRISE INTEGRATIONS
# ============================================================

st.divider()

st.header(
    "Enterprise Integrations"
)


integration1, integration2, integration3, integration4 = st.columns(4)


with integration1:

    st.info("📁 SharePoint")


with integration2:

    st.info("📚 Confluence")


with integration3:

    st.info("🎫 Jira")


with integration4:

    st.info("🗄️ SQL / SAP")


# ============================================================
# EDUCATION
# ============================================================

st.divider()

st.header(
    "Education"
)


with st.container(border=True):

    st.subheader(
        "B.Tech — Computer Science & Engineering"
    )

    st.write(
        "Jawaharlal Nehru Technological University Hyderabad"
    )

    st.caption(
        "2018 — 2022"
    )


# ============================================================
# CERTIFICATIONS
# ============================================================

st.header(
    "Certifications"
)


cert1, cert2, cert3, cert4 = st.columns(4)


with cert1:

    st.info("Azure AI Engineer")


with cert2:

    st.info("AI-900")


with cert3:

    st.info("AWS AI Practitioner")


with cert4:

    st.info("IBM Generative AI")


# ============================================================
# RESUME SECTION
# ============================================================

st.divider()

st.header(
    "📄 Resume"
)

st.caption(
    "Download my latest resume for a detailed overview "
    "of my experience, projects and technical skills."
)


resume_file = Path(RESUME_PATH)


if resume_file.exists():

    resume_col1, resume_col2, resume_col3 = st.columns(
        [1, 1.5, 1]
    )

    with resume_col2:

        with open(
            resume_file,
            "rb"
        ) as file:

            resume_data = file.read()


        st.download_button(
            label="📥 Download Resume",
            data=resume_data,
            file_name=resume_file.name,
            mime="application/pdf",
            use_container_width=True
        )

else:

    st.error(
        f"Resume file not found: {RESUME_PATH}"
    )

    st.info(
        """
        Put your resume PDF in the same folder as
        `app.py` and make sure the filename matches
        `RESUME_PATH`.
        """
    )


# ============================================================
# CONTACT
# ============================================================

st.divider()

st.header(
    "Let's Build Production AI"
)

st.write(
    """
    Open to opportunities involving AI/ML Engineering,
    Generative AI, Agentic AI, RAG, Machine Learning,
    Data Science and AI Engineering.
    """
)


contact1, contact2, contact3 = st.columns(3)


with contact1:

    st.link_button(
        "📧 Contact Me",
        f"mailto:{EMAIL}",
        use_container_width=True
    )


with contact2:

    st.link_button(
        "💻 GitHub",
        GITHUB_URL,
        use_container_width=True
    )


with contact3:

    st.link_button(
        "🔗 LinkedIn",
        LINKEDIN_URL,
        use_container_width=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    """
    <div class="footer-text">

    <strong>Shivarathri Karthik</strong>

    <br>

    AI/ML Engineer • Generative AI • Agentic AI

    <br>

    Python • Machine Learning • RAG • LLMs •
    LangGraph • LangChain • MLOps

    <br><br>

    © 2026 Shivarathri Karthik

    </div>
    """,
    unsafe_allow_html=True
)
