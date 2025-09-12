"""
CognitiveCloud.ai Philosophy Module Launcher
Matching the design of the math standards launcher
"""

import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="CognitiveCloud.ai Philosophy Module",
        page_icon="🧠",
        layout="wide",
        initial_sidebar_state="collapsed"
    )

    # Custom CSS matching the CognitiveCloud.ai launcher design
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    .stApp {
        background: #f8f9fa;
        font-family: 'Inter', sans-serif;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 3rem 0;
        background: white;
        margin-bottom: 2rem;
    }
    
    .brand-title {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .brand-emoji {
        color: #e91e63;
        margin-right: 0.5rem;
    }
    
    .subtitle {
        font-size: 0.9rem;
        color: #718096;
        font-weight: 400;
    }
    
    .section-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d3748;
        margin: 2rem 0 1rem 1rem;
    }
    
    .app-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 1.5rem;
        padding: 0 1rem;
        margin-bottom: 2rem;
    }
    
    .app-card {
        background: white;
        border-radius: 12px;
        padding: 2rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
        text-align: center;
        transition: all 0.2s ease;
        min-height: 200px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    
    .app-card:hover {
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
        transform: translateY(-2px);
    }
    
    .app-card.phl101 {
        background: linear-gradient(135deg, #e8f5e8 0%, #f0fff0 100%);
        border-color: #68d391;
    }
    
    .app-card.phl202 {
        background: linear-gradient(135deg, #fef5e7 0%, #fffbf0 100%);
        border-color: #f6ad55;
    }
    
    .app-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }
    
    .phl101 .app-icon {
        color: #38a169;
    }
    
    .phl202 .app-icon {
        color: #dd6b20;
    }
    
    .app-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.5rem;
        line-height: 1.3;
    }
    
    .app-description {
        font-size: 0.85rem;
        color: #4a5568;
        line-height: 1.4;
        margin-bottom: 1.5rem;
        flex-grow: 1;
    }
    
    .launch-button {
        display: inline-block;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        text-decoration: none;
        border: none;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .phl101 .launch-button {
        background: #38a169;
        color: white;
    }
    
    .phl101 .launch-button:hover {
        background: #2f855a;
    }
    
    .phl202 .launch-button {
        background: #dd6b20;
        color: white;
    }
    
    .phl202 .launch-button:hover {
        background: #c05621;
    }
    
    .stButton > button {
        width: 100%;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        padding: 0.5rem 1.5rem !important;
        border-radius: 20px !important;
        font-size: 0.85rem !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
    }
    
    .phl101-btn > div > button {
        background: #38a169 !important;
        color: white !important;
    }
    
    .phl101-btn > div > button:hover {
        background: #2f855a !important;
    }
    
    .phl202-btn > div > button {
        background: #dd6b20 !important;
        color: white !important;
    }
    
    .phl202-btn > div > button:hover {
        background: #c05621 !important;
    }
    
    .divider {
        height: 1px;
        background: #e2e8f0;
        margin: 2rem 0;
    }
    
    @media (max-width: 768px) {
        .app-grid {
            grid-template-columns: 1fr;
            padding: 0 0.5rem;
        }
        
        .main-header {
            padding: 1rem 0 2rem 0;
        }
        
        .brand-title {
            font-size: 1.3rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Main header matching the original design
    st.markdown("""
    <div class="main-header">
        <h1 class="brand-title">
            <span class="brand-emoji">🧠</span>CognitiveCloud.ai Philosophy Module
        </h1>
        <p class="subtitle">Interactive Philosophy Learning Activities • Developed by Xavier Honablue M.Ed.</p>
    </div>
    """, unsafe_allow_html=True)

    # Philosophy section title
    st.markdown('<h2 class="section-title">Philosophy & Critical Thinking</h2>', unsafe_allow_html=True)

    # Apps grid
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="app-card phl101">
            <div>
                <div class="app-icon">🤔</div>
                <h3 class="app-title">What is Religion? What is Philosophy?</h3>
                <p class="app-description">
                    Explore fundamental questions about the nature of philosophy and religion through interactive dialogue and critical examination.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="phl101-btn">', unsafe_allow_html=True)
        if st.button("Launch App", key="phl101"):
            st.link_button("🚀 Open PHL 101", "https://philosophy-101-day1.streamlit.app/", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="app-card phl202">
            <div>
                <div class="app-icon">🧩</div>
                <h3 class="app-title">Logic & Cognitive Analysis</h3>
                <p class="app-description">
                    Master formal and informal logic through structured reasoning exercises and cognitive analysis tools.
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="phl202-btn">', unsafe_allow_html=True)
        if st.button("Launch App", key="phl202"):
            st.link_button("🚀 Open PHL 202", "https://logic1-phl202.streamlit.app/", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Divider
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Additional philosophy modules coming soon section
    st.markdown('<h2 class="section-title">Coming Soon</h2>', unsafe_allow_html=True)
    
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.markdown("""
        <div class="app-card" style="opacity: 0.6;">
            <div>
                <div class="app-icon">⚖️</div>
                <h3 class="app-title">Ethics & Moral Reasoning</h3>
                <p class="app-description">
                    Navigate complex ethical dilemmas through guided moral reasoning frameworks.
                </p>
            </div>
            <div style="padding: 0.5rem 1.5rem; border-radius: 20px; font-size: 0.85rem; background: #e2e8f0; color: #4a5568;">
                Coming Soon
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="app-card" style="opacity: 0.6;">
            <div>
                <div class="app-icon">🌍</div>
                <h3 class="app-title">Political Philosophy</h3>
                <p class="app-description">
                    Examine different systems of governance and theories of social organization.
                </p>
            </div>
            <div style="padding: 0.5rem 1.5rem; border-radius: 20px; font-size: 0.85rem; background: #e2e8f0; color: #4a5568;">
                Coming Soon
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col5:
        st.markdown("""
        <div class="app-card" style="opacity: 0.6;">
            <div>
                <div class="app-icon">🧠</div>
                <h3 class="app-title">Philosophy of Mind</h3>
                <p class="app-description">
                    Explore consciousness, identity, and the nature of mental states through interactive scenarios.
                </p>
            </div>
            <div style="padding: 0.5rem 1.5rem; border-radius: 20px; font-size: 0.85rem; background: #e2e8f0; color: #4a5568;">
                Coming Soon
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
