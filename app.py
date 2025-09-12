"""
CognitiveCloud.ai - Philosophy Module Launcher
Where Imagination Meets Science - Now Expanding to Philosophy
"""

import streamlit as st
import base64

def main():
    # Page configuration
    st.set_page_config(
        page_title="CognitiveCloud.ai - Philosophy Module",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS matching CognitiveCloud.ai branding
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #0f1419 0%, #1a2332 50%, #2d3748 100%);
        font-family: 'Inter', sans-serif;
    }
    
    .main-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 2rem;
    }
    
    .header-section {
        text-align: center;
        margin-bottom: 3rem;
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 24px;
        padding: 3rem 2rem;
    }
    
    .brand-title {
        font-size: 3.5rem;
        font-weight: 800;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1rem;
        letter-spacing: -0.02em;
    }
    
    .tagline {
        font-size: 1.2rem;
        color: #94a3b8;
        margin-bottom: 0.5rem;
        font-weight: 300;
    }
    
    .module-subtitle {
        font-size: 1.8rem;
        color: #e2e8f0;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .developer-info {
        font-size: 1rem;
        color: #64748b;
        font-style: italic;
        margin-top: 1rem;
    }
    
    .activities-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(450px, 1fr));
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    .activity-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2.5rem;
        position: relative;
        overflow: hidden;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .activity-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(135deg, rgba(59, 130, 246, 0.1), rgba(139, 92, 246, 0.1));
        opacity: 0;
        transition: opacity 0.3s ease;
        border-radius: 20px;
    }
    
    .activity-card:hover::before {
        opacity: 1;
    }
    
    .activity-card:hover {
        transform: translateY(-8px);
        border-color: rgba(59, 130, 246, 0.3);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
    }
    
    .activity-header {
        display: flex;
        align-items: center;
        margin-bottom: 1.5rem;
        position: relative;
        z-index: 1;
    }
    
    .activity-icon {
        width: 60px;
        height: 60px;
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.8rem;
        margin-right: 1rem;
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
    }
    
    .activity-meta {
        flex: 1;
    }
    
    .activity-number {
        font-size: 0.9rem;
        color: #3b82f6;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .activity-title {
        font-size: 1.5rem;
        color: #f1f5f9;
        font-weight: 700;
        margin: 0.5rem 0;
        position: relative;
        z-index: 1;
    }
    
    .activity-description {
        color: #94a3b8;
        font-size: 1rem;
        line-height: 1.6;
        margin-bottom: 2rem;
        position: relative;
        z-index: 1;
    }
    
    .launch-btn {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6);
        color: white;
        border: none;
        padding: 0.875rem 2rem;
        border-radius: 12px;
        font-weight: 600;
        font-size: 0.95rem;
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        position: relative;
        z-index: 1;
        width: 100%;
        justify-content: center;
    }
    
    .launch-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(59, 130, 246, 0.3);
    }
    
    .stats-section {
        background: rgba(255, 255, 255, 0.02);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 3rem;
    }
    
    .stats-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 2rem;
        text-align: center;
    }
    
    .stat-item {
        padding: 1rem;
    }
    
    .stat-number {
        font-size: 2.5rem;
        font-weight: 800;
        color: #3b82f6;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        color: #94a3b8;
        font-size: 0.9rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    
    .footer {
        text-align: center;
        padding: 2rem;
        color: #64748b;
        font-size: 0.9rem;
        border-top: 1px solid rgba(255, 255, 255, 0.1);
        margin-top: 3rem;
    }
    
    .status-badge {
        display: inline-block;
        background: rgba(34, 197, 94, 0.1);
        color: #22c55e;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.8rem;
        font-weight: 500;
        margin-left: 1rem;
        border: 1px solid rgba(34, 197, 94, 0.2);
    }
    
    @media (max-width: 768px) {
        .activities-grid {
            grid-template-columns: 1fr;
        }
        .brand-title {
            font-size: 2.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Main content
    st.markdown("""
    <div class="main-container">
        <div class="header-section">
            <h1 class="brand-title">CognitiveCloud.ai</h1>
            <p class="tagline">Where Imagination Meets Science</p>
            <h2 class="module-subtitle">Philosophy Module</h2>
            <p style="color: #94a3b8; font-size: 1.1rem; max-width: 600px; margin: 0 auto;">
                Expanding beyond STEM into the realm of philosophical inquiry with interactive, 
                gamified learning experiences that make complex philosophical concepts accessible and engaging.
            </p>
            <div class="developer-info">
                Philosophy Module developed by Xavier Honablue, M.Ed.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Activities section
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="activity-card">
            <div class="activity-header">
                <div class="activity-icon">🤔</div>
                <div class="activity-meta">
                    <div class="activity-number">PHL 101</div>
                    <div class="status-badge">Active</div>
                </div>
            </div>
            <h3 class="activity-title">What is Religion? What is Philosophy?</h3>
            <p class="activity-description">
                Begin your philosophical journey by exploring fundamental questions about the nature 
                of philosophy and religion. This interactive module examines core philosophical 
                thinking patterns and the relationship between faith, reason, and human understanding.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Launch PHL 101 Activity", key="phl101", help="Open Philosophy 101 module"):
            js = '''
            <script>
                window.open("https://philosophy-101-day1.streamlit.app/", "_blank");
            </script>
            '''
            st.components.v1.html(js)
            st.success("✅ Opening PHL 101: What is Religion? What is Philosophy?")
    
    with col2:
        st.markdown("""
        <div class="activity-card">
            <div class="activity-header">
                <div class="activity-icon">🧩</div>
                <div class="activity-meta">
                    <div class="activity-number">PHL 202</div>
                    <div class="status-badge">Active</div>
                </div>
            </div>
            <h3 class="activity-title">Logic & Cognitive Analysis</h3>
            <p class="activity-description">
                Advance your critical thinking skills through formal and informal logic training. 
                This interactive module uses gamified exercises to master logical reasoning, 
                argument analysis, and cognitive processing patterns essential for philosophical inquiry.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🚀 Launch PHL 202 Activity", key="phl202", help="Open Logic & Cognitive Analysis module"):
            js = '''
            <script>
                window.open("https://logic1-phl202.streamlit.app/", "_blank");
            </script>
            '''
            st.components.v1.html(js)
            st.success("✅ Opening PHL 202: Logic & Cognitive Analysis")

    # Stats section
    st.markdown("""
    <div class="stats-section">
        <div class="stats-grid">
            <div class="stat-item">
                <div class="stat-number">2</div>
                <div class="stat-label">Active Modules</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">100%</div>
                <div class="stat-label">Interactive</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">∞</div>
                <div class="stat-label">Possibilities</div>
            </div>
            <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Access</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("""
    <div class="footer">
        <p>
            <strong>CognitiveCloud.ai</strong> - Expanding the boundaries of educational technology<br>
            Philosophy Module by Xavier Honablue, M.Ed. | STEM Modules by Dr. Chet<br>
            Where Imagination Meets Science... and Philosophy
        </p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
