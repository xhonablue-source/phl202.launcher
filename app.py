import streamlit as st
import webbrowser

# Page configuration
st.set_page_config(
    page_title="PHL201 - Introduction to Philosophy",
    page_icon="🧠",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
        padding: 3rem 2rem;
        border-radius: 15px;
        color: white;
        margin-bottom: 2rem;
        text-align: center;
    }
    .week-card {
        background: white;
        padding: 2rem;
        border-radius: 12px;
        border: 2px solid #E5E7EB;
        margin-bottom: 1.5rem;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        transition: all 0.3s;
    }
    .week-card:hover {
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
        border-color: #4F46E5;
    }
    .week-title {
        color: #4F46E5;
        font-size: 1.5rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .week-description {
        color: #6B7280;
        margin-bottom: 1rem;
        line-height: 1.6;
    }
    .topic-list {
        background: #F9FAFB;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
    .resource-section {
        background: #EEF2FF;
        padding: 2rem;
        border-radius: 12px;
        margin-top: 2rem;
    }
    .highlight-box {
        background: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>🧠 PHL201: Introduction to Philosophy</h1>
    <p style="font-size: 1.2rem; margin-top: 1rem;">CognitiveCloud.ai - Xavier Honablue M.Ed</p>
    <p style="font-size: 1rem; margin-top: 0.5rem; opacity: 0.9;">A comprehensive journey through philosophical thought and critical reasoning</p>
</div>
""", unsafe_allow_html=True)

# Course Overview
st.markdown("## 📚 Course Overview")
st.markdown("""
Welcome to PHL201! This course introduces fundamental questions in philosophy including the nature of reality, 
knowledge, consciousness, and human existence. Through engaging with classical and contemporary philosophical 
texts, you'll develop critical thinking skills and explore profound questions about what it means to be human.
""")

# Weekly Structure
st.markdown("---")
st.markdown("## 📅 Weekly Schedule & Assessments")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 1-2: What is Philosophy?</div>
        <div class="week-description">
            Introduction to philosophical inquiry, Socratic method, and critical thinking fundamentals.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Socratic Method & The Crito</li>
                <li>Critical Thinking & Argument Analysis</li>
                <li>Philosophy vs. Other Disciplines</li>
                <li>Evaluating Arguments & Premises</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 3-4: Human Nature & Existence</div>
        <div class="week-description">
            Exploring existentialism and questions about human nature, freedom, and responsibility.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Sartre's Existentialism</li>
                <li>Existence Precedes Essence</li>
                <li>Freedom, Anguish, and Despair</li>
                <li>Rationalistic vs. Feminist Views</li>
            </ul>
        </div>
        <div class="highlight-box">
            <strong>⚠️ Week 4 Exam Available</strong><br>
            <small>Test your understanding of Weeks 1-4 material</small>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 5-6: Mind-Body Problem</div>
        <div class="week-description">
            Classical and contemporary theories about the relationship between mind and body.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Plato's Theory of the Soul</li>
                <li>Descartes' Dualism</li>
                <li>The Mind-Body Problem</li>
                <li>Consciousness & First-Person Experience</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 7-8: Behaviorism & Functionalism</div>
        <div class="week-description">
            Modern materialist approaches to understanding the mind through behavior and function.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Ryle's Behaviorism</li>
                <li>Ghost in the Machine Critique</li>
                <li>Functionalism Theory</li>
                <li>Mental States as Functional Roles</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 9-10: Identity Theory & AI</div>
        <div class="week-description">
            Brain-mind identity and computational theories of consciousness.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Smart's Identity Theory</li>
                <li>Computer Models of Mind</li>
                <li>Turing Test & Machine Intelligence</li>
                <li>Searle's Chinese Room Argument</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="week-card">
        <div class="week-title">Week 11-12: Contemporary Debates</div>
        <div class="week-description">
            Eliminative materialism, property dualism, and the hard problem of consciousness.
        </div>
        <div class="topic-list">
            <strong>Topics:</strong>
            <ul>
                <li>Churchland's Eliminative Materialism</li>
                <li>Chalmers' Property Dualism</li>
                <li>Philosophical Zombies</li>
                <li>The Hard Problem of Consciousness</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Assessment Links
st.markdown("---")
st.markdown("## 🎯 Course Assessments")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%); padding: 1.5rem; border-radius: 12px; color: white; text-align: center;">
        <h3 style="margin: 0;">Week 4 Exam</h3>
        <p style="margin: 0.5rem 0; opacity: 0.9;">Weeks 1-4 Coverage</p>
        <p style="font-size: 0.9rem; margin: 0.5rem 0;">Existentialism & Human Nature</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📝 Take Week 4 Exam", use_container_width=True, type="primary"):
        st.markdown("""
        <div class="highlight-box">
            <strong>Opening Week 4 Exam...</strong><br>
            <p>Click the link below to access the exam:</p>
            <a href="https://phl201-week4-exam.streamlit.app/" target="_blank" style="font-size: 1.1rem; color: #4F46E5; font-weight: 600;">
                🔗 PHL201 Week 4 Exam →
            </a>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%); padding: 1.5rem; border-radius: 12px; color: white; text-align: center;">
        <h3 style="margin: 0;">Full Assessment</h3>
        <p style="margin: 0.5rem 0; opacity: 0.9;">All 110 Questions</p>
        <p style="font-size: 0.9rem; margin: 0.5rem 0;">Complete Course Coverage</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("🧠 Take Full Assessment", use_container_width=True):
        st.info("This will launch the complete 110-question assessment covering all course topics. Make sure you have adequate time to complete it.")

with col3:
    st.markdown("""
    <div style="background: linear-gradient(135deg, #10B981 0%, #059669 100%); padding: 1.5rem; border-radius: 12px; color: white; text-align: center;">
        <h3 style="margin: 0;">Practice Mode</h3>
        <p style="margin: 0.5rem 0; opacity: 0.9;">By Category</p>
        <p style="font-size: 0.9rem; margin: 0.5rem 0;">Focused Topic Review</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("📖 Practice by Topic", use_container_width=True):
        st.success("Practice mode allows you to focus on specific philosophical topics. Use the category filter in the full assessment.")

# Resources Section
st.markdown("---")
st.markdown("""
<div class="resource-section">
    <h2 style="color: #4F46E5; margin-bottom: 1rem;">📚 Additional Resources</h2>
    
    <h3 style="color: #6B7280; margin-top: 1.5rem;">Stanford Encyclopedia of Philosophy</h3>
    <p>Peer-reviewed articles on all major philosophical topics covered in this course.</p>
    <a href="https://plato.stanford.edu/" target="_blank" style="color: #4F46E5; font-weight: 600;">Visit SEP →</a>
    
    <h3 style="color: #6B7280; margin-top: 1.5rem;">Internet Encyclopedia of Philosophy</h3>
    <p>Accessible articles on philosophy topics with clear explanations.</p>
    <a href="https://iep.utm.edu/" target="_blank" style="color: #4F46E5; font-weight: 600;">Visit IEP →</a>
    
    <h3 style="color: #6B7280; margin-top: 1.5rem;">PhilPapers</h3>
    <p>Comprehensive database of philosophy research papers and articles.</p>
    <a href="https://philpapers.org/" target="_blank" style="color: #4F46E5; font-weight: 600;">Visit PhilPapers →</a>
</div>
""", unsafe_allow_html=True)

# Study Tips
st.markdown("---")
st.markdown("## 💡 Study Tips for Success")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    **Before Each Assessment:**
    - Review your notes from the relevant weeks
    - Re-read key passages from the textbook
    - Practice reconstructing philosophical arguments
    - Test yourself on key concepts and terminology
    """)

with col2:
    st.markdown("""
    **During the Assessment:**
    - Read each question carefully
    - Consider all answer options before selecting
    - Use the category filter to focus your review
    - Take breaks if needed (your progress is saved)
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #6B7280; padding: 2rem 0;">
    <p><strong>PHL201: Introduction to Philosophy</strong></p>
    <p>CognitiveCloud.ai - Xavier Honablue M.Ed</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        For technical support or course questions, please contact your instructor.
    </p>
</div>
""", unsafe_allow_html=True)
