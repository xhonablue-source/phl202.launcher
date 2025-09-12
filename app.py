"""
Philosophy Cognitive Cloud Launcher - Streamlit App
Developed for Xavier Honablue M.Ed.
"""

import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="Philosophy Cognitive Cloud - Xavier Honablue M.Ed.",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS for styling
    st.markdown("""
    <style>
    .main {
        padding-top: 2rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0;
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }
    
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #1e3c72, #2a5298, #667eea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 0.5rem;
    }
    
    .subtitle {
        font-size: 1.4rem;
        color: #666;
        margin-bottom: 1rem;
    }
    
    .developer-credit {
        font-size: 1.1rem;
        color: #888;
        font-style: italic;
    }
    
    .activity-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem 0;
        color: white;
        text-align: center;
    }
    
    .activity-card.phl101 {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .activity-card.phl202 {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .activity-title {
        font-size: 1.8rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    
    .activity-description {
        font-size: 1rem;
        margin-bottom: 1.5rem;
        opacity: 0.95;
    }
    
    .stButton > button {
        background: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 25px !important;
        padding: 0.8rem 2rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background: rgba(255, 255, 255, 0.3) !important;
        transform: translateY(-2px) !important;
    }
    
    .features-section {
        background: rgba(255, 255, 255, 0.95);
        padding: 2rem;
        border-radius: 20px;
        margin-top: 2rem;
    }
    
    .feature-item {
        text-align: center;
        padding: 1.5rem;
        background: rgba(102, 126, 234, 0.05);
        border-radius: 15px;
        margin: 1rem;
        border: 1px solid rgba(102, 126, 234, 0.1);
    }
    </style>
    """, unsafe_allow_html=True)

    # Main header
    st.markdown("""
    <div class="main-header">
        <h1 class="main-title">Philosophy Cognitive Cloud</h1>
        <p class="subtitle">Interactive Philosophy Education Platform</p>
        <p class="developer-credit">Developed by Xavier Honablue, M.Ed.</p>
    </div>
    """, unsafe_allow_html=True)

    # Description
    st.markdown("""
    <div style="text-align: center; font-size: 1.2rem; color: white; margin-bottom: 3rem; 
                background: rgba(255, 255, 255, 0.1); padding: 2rem; border-radius: 15px;">
        Welcome to an innovative approach to philosophical learning. Our cognitive cloud platform 
        combines traditional philosophical inquiry with modern interactive technology to create 
        engaging, thought-provoking educational experiences.
    </div>
    """, unsafe_allow_html=True)

    # Activities section
    st.markdown("## 🎯 Available Activities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="activity-card phl101">
            <div style="font-size: 1.1rem; font-weight: 600; opacity: 0.9; margin-bottom: 0.5rem;">PHL 101</div>
            <h2 class="activity-title">What is Religion? What is Philosophy?</h2>
            <p class="activity-description">
                Explore fundamental questions about the nature of philosophy and religion. 
                This interactive activity examines the foundations of philosophical thinking 
                and the relationship between faith and reason.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Launch PHL 101 Activity", key="phl101"):
            st.markdown("""
            <script>
            window.open('https://philosophy-101-day1.streamlit.app/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("Opening PHL 101: What is Religion? What is Philosophy?")
            st.markdown("[Click here if the page doesn't open automatically](https://philosophy-101-day1.streamlit.app/)")
    
    with col2:
        st.markdown("""
        <div class="activity-card phl202">
            <div style="font-size: 1.1rem; font-weight: 600; opacity: 0.9; margin-bottom: 0.5rem;">PHL 202</div>
            <h2 class="activity-title">Logic & Cognitive Analysis</h2>
            <p class="activity-description">
                Dive deep into logical reasoning, critical thinking, and cognitive processes. 
                This advanced activity uses interactive tools to help students master 
                formal and informal logic principles.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Launch PHL 202 Activity", key="phl202"):
            st.markdown("""
            <script>
            window.open('https://logic1-phl202.streamlit.app/', '_blank');
            </script>
            """, unsafe_allow_html=True)
            st.success("Opening PHL 202: Logic & Cognitive Analysis")
            st.markdown("[Click here if the page doesn't open automatically](https://logic1-phl202.streamlit.app/)")

    # Features section
    st.markdown("""
    <div class="features-section">
        <h3 style="text-align: center; font-size: 1.5rem; margin-bottom: 2rem; color: #444;">Platform Features</h3>
    </div>
    """, unsafe_allow_html=True)
    
    feat_col1, feat_col2, feat_col3, feat_col4 = st.columns(4)
    
    with feat_col1:
        st.markdown("""
        <div class="feature-item">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🎯</div>
            <h4 style="color: #444; margin-bottom: 0.5rem;">Interactive Learning</h4>
            <p style="color: #666; font-size: 0.9rem;">Engage with philosophical concepts through dynamic exercises</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col2:
        st.markdown("""
        <div class="feature-item">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🧠</div>
            <h4 style="color: #444; margin-bottom: 0.5rem;">Cognitive Enhancement</h4>
            <p style="color: #666; font-size: 0.9rem;">Develop critical thinking through structured analysis</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col3:
        st.markdown("""
        <div class="feature-item">
            <div style="font-size: 2rem; margin-bottom: 1rem;">🌐</div>
            <h4 style="color: #444; margin-bottom: 0.5rem;">Cloud-Based Access</h4>
            <p style="color: #666; font-size: 0.9rem;">Learn anywhere, anytime with web-based platform</p>
        </div>
        """, unsafe_allow_html=True)
    
    with feat_col4:
        st.markdown("""
        <div class="feature-item">
            <div style="font-size: 2rem; margin-bottom: 1rem;">📚</div>
            <h4 style="color: #444; margin-bottom: 0.5rem;">Comprehensive Curriculum</h4>
            <p style="color: #666; font-size: 0.9rem;">From introductory concepts to advanced logic</p>
        </div>
        """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div style="text-align: center; margin-top: 3rem; padding: 2rem; 
                background: rgba(255, 255, 255, 0.1); border-radius: 15px; color: white;">
        <p>&copy; 2025 Philosophy Cognitive Cloud | Xavier Honablue, M.Ed. | Educational Innovation in Philosophy</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
