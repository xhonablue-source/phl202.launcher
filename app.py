"""
CognitiveCloud.ai PHL 202 Course Launcher
3 Credit Hours • 39 Contact Hours • Xavier Honablue M.Ed.
"""

import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="PHL 202 - Logic & Philosophy",
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
        border-bottom: 3px solid #e91e63;
    }
    
    .course-title {
        font-size: 2rem;
        font-weight: 700;
        color: #2d3748;
        margin-bottom: 0.5rem;
    }
    
    .brand-emoji {
        color: #e91e63;
        margin-right: 0.5rem;
    }
    
    .course-info {
        font-size: 1rem;
        color: #718096;
        font-weight: 400;
        margin-bottom: 1rem;
    }
    
    .credit-info {
        font-size: 0.9rem;
        color: #e91e63;
        font-weight: 600;
        background: #fdf2f8;
        padding: 0.5rem 1rem;
        border-radius: 20px;
        display: inline-block;
        margin: 0.5rem;
    }
    
    .week-section {
        margin: 2rem 1rem;
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #e91e63;
    }
    
    .week-title {
        font-size: 1.1rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 1rem;
        display: flex;
        align-items: center;
    }
    
    .week-number {
        background: #e91e63;
        color: white;
        border-radius: 50%;
        width: 24px;
        height: 24px;
        font-size: 0.8rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 0.8rem;
    }
    
    .activity-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
    }
    
    .activity-card {
        background: #f7fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        transition: all 0.2s ease;
        cursor: pointer;
    }
    
    .activity-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
    }
    
    .activity-card.active {
        border-color: #68d391;
        background: linear-gradient(135deg, #f0fff4 0%, #f7fafc 100%);
    }
    
    .activity-card.coming-soon {
        opacity: 0.6;
    }
    
    .activity-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
    }
    
    .active .activity-icon {
        color: #38a169;
    }
    
    .coming-soon .activity-icon {
        color: #a0aec0;
    }
    
    .activity-title {
        font-size: 0.9rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.3rem;
    }
    
    .activity-duration {
        font-size: 0.7rem;
        color: #718096;
        margin-bottom: 0.8rem;
    }
    
    .stButton > button {
        width: 100% !important;
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
        padding: 0.4rem 1rem !important;
        border-radius: 16px !important;
        font-size: 0.8rem !important;
        font-weight: 500 !important;
        transition: all 0.2s ease !important;
        font-family: 'Inter', sans-serif !important;
        background: #38a169 !important;
        color: white !important;
    }
    
    .stButton > button:hover {
        background: #2f855a !important;
    }
    
    .coming-soon-btn {
        width: 100%;
        padding: 0.4rem 1rem;
        border-radius: 16px;
        font-size: 0.8rem;
        font-weight: 500;
        background: #e2e8f0;
        color: #4a5568;
        border: none;
        cursor: not-allowed;
    }
    
    .progress-summary {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border: 1px solid #e2e8f0;
    }
    
    .progress-stats {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(120px, 1fr));
        gap: 1rem;
        text-align: center;
    }
    
    .stat-number {
        font-size: 1.5rem;
        font-weight: 700;
        color: #e91e63;
    }
    
    .stat-label {
        font-size: 0.8rem;
        color: #4a5568;
    }
    
    @media (max-width: 768px) {
        .activity-grid {
            grid-template-columns: 1fr;
        }
        
        .course-title {
            font-size: 1.5rem;
        }
    }
    </style>
    """, unsafe_allow_html=True)

    # Course Header
    st.markdown("""
    <div class="main-header">
        <h1 class="course-title">
            <span class="brand-emoji">🧠</span>PHL 202: Logic & Philosophy
        </h1>
        <p class="course-info">Interactive Philosophy Course • Xavier Honablue, M.Ed.</p>
        <div class="credit-info">3 Credit Hours</div>
        <div class="credit-info">39 Contact Hours</div>
        <div class="credit-info">13 Weeks</div>
    </div>
    """, unsafe_allow_html=True)

    # Progress Summary
    st.markdown("""
    <div class="progress-summary">
        <div class="progress-stats">
            <div>
                <div class="stat-number">2</div>
                <div class="stat-label">Active Modules</div>
            </div>
            <div>
                <div class="stat-number">24</div>
                <div class="stat-label">Coming Soon</div>
            </div>
            <div>
                <div class="stat-number">26</div>
                <div class="stat-label">Total Activities</div>
            </div>
            <div>
                <div class="stat-number">6</div>
                <div class="stat-label">Hours Available</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 1: Introduction to Philosophy
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">1</div>
            Week 1: Introduction to Philosophy (3 hours)
        </div>
        <div class="activity-grid">
            <div class="activity-card active">
                <div class="activity-icon">🤔</div>
                <h4 class="activity-title">What is Philosophy?</h4>
                <p class="activity-duration">90 minutes</p>
            </div>
            <div class="activity-card active">
                <div class="activity-icon">⛪</div>
                <h4 class="activity-title">Philosophy vs Religion</h4>
                <p class="activity-duration">90 minutes</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button("Launch: What is Philosophy?", "https://philosophy-101-day1.streamlit.app/", use_container_width=True)
    with col2:
        st.link_button("Launch: Philosophy vs Religion", "https://philosophy-101-day1.streamlit.app/", use_container_width=True)

    # Week 2: Logic Fundamentals
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">2</div>
            Week 2: Logic Fundamentals (3 hours)
        </div>
        <div class="activity-grid">
            <div class="activity-card active">
                <div class="activity-icon">🧩</div>
                <h4 class="activity-title">Formal Logic</h4>
                <p class="activity-duration">90 minutes</p>
            </div>
            <div class="activity-card active">
                <div class="activity-icon">🎯</div>
                <h4 class="activity-title">Cognitive Analysis</h4>
                <p class="activity-duration">90 minutes</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    with col3:
        st.link_button("Launch: Formal Logic", "https://logic1-phl202.streamlit.app/", use_container_width=True)
    with col4:
        st.link_button("Launch: Cognitive Analysis", "https://logic1-phl202.streamlit.app/", use_container_width=True)

    # Weeks 3-13 (Coming Soon)
    weeks_data = [
        {"week": 3, "title": "Arguments & Reasoning", "activities": ["Valid Arguments", "Logical Fallacies"]},
        {"week": 4, "title": "Critical Thinking", "activities": ["Assumption Analysis", "Evidence Evaluation"]},
        {"week": 5, "title": "Ethics Introduction", "activities": ["Moral Theory", "Ethical Dilemmas"]},
        {"week": 6, "title": "Metaphysics", "activities": ["Reality & Existence", "Free Will vs Determinism"]},
        {"week": 7, "title": "Epistemology", "activities": ["Knowledge & Belief", "Sources of Knowledge"]},
        {"week": 8, "title": "Philosophy of Mind", "activities": ["Consciousness", "Mind-Body Problem"]},
        {"week": 9, "title": "Political Philosophy", "activities": ["Justice & Rights", "Government & Authority"]},
        {"week": 10, "title": "Aesthetics", "activities": ["Philosophy of Art", "Beauty & Taste"]},
        {"week": 11, "title": "Philosophy of Science", "activities": ["Scientific Method", "Explanation & Causation"]},
        {"week": 12, "title": "Applied Philosophy", "activities": ["Business Ethics", "Environmental Ethics"]},
        {"week": 13, "title": "Integration & Review", "activities": ["Synthesis Project", "Final Reflection"]}
    ]

    for week_data in weeks_data:
        st.markdown(f"""
        <div class="week-section">
            <div class="week-title">
                <div class="week-number">{week_data['week']}</div>
                Week {week_data['week']}: {week_data['title']} (3 hours)
            </div>
            <div class="activity-grid">
                <div class="activity-card coming-soon">
                    <div class="activity-icon">📚</div>
                    <h4 class="activity-title">{week_data['activities'][0]}</h4>
                    <p class="activity-duration">90 minutes</p>
                    <button class="coming-soon-btn">Coming Soon</button>
                </div>
                <div class="activity-card coming-soon">
                    <div class="activity-icon">💭</div>
                    <h4 class="activity-title">{week_data['activities'][1]}</h4>
                    <p class="activity-duration">90 minutes</p>
                    <button class="coming-soon-btn">Coming Soon</button>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
