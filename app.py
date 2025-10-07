"""
PHL 201 Introduction to Philosophy - CognitiveCloud.ai Launcher
Wayne County Community College District • Xavier Honablue, M.Ed.
"""

import streamlit as st

def main():
    # Page configuration
    st.set_page_config(
        page_title="PHL 201 - Introduction to Philosophy",
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
        padding: 2rem 0 2rem 0;
        background: white;
        margin-bottom: 2rem;
        border-bottom: 3px solid #e91e63;
    }
    
    .course-title {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a202c;
        margin-bottom: 0.3rem;
    }
    
    .college-info {
        font-size: 1rem;
        color: #718096;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    .instructor-info {
        font-size: 0.9rem;
        color: #4a5568;
        margin-bottom: 1rem;
    }
    
    .course-details {
        display: flex;
        justify-content: center;
        gap: 2rem;
        flex-wrap: wrap;
        margin-top: 1rem;
    }
    
    .detail-badge {
        font-size: 0.8rem;
        color: #e91e63;
        font-weight: 600;
        background: #fdf2f8;
        padding: 0.4rem 0.8rem;
        border-radius: 16px;
        border: 1px solid #f3e8ff;
    }
    
    .progress-summary {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #e91e63;
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
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .latest-feature {
        margin: 2rem 1rem;
        background: linear-gradient(135deg, #e53e3e 0%, #c53030 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        color: white;
        text-align: center;
        border: 3px solid #ffd700;
        animation: pulse-glow 2s infinite;
    }

    @keyframes pulse-glow {
        0% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12), 0 0 0 0 rgba(255, 215, 0, 0.7); }
        50% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12), 0 0 20px 10px rgba(255, 215, 0, 0.3); }
        100% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12), 0 0 0 0 rgba(255, 215, 0, 0.7); }
    }

    .special-section {
        margin: 2rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        color: white;
        text-align: center;
    }

    .special-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.8rem;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }

    .special-subtitle {
        font-size: 1rem;
        opacity: 0.9;
        margin-bottom: 1.5rem;
        font-weight: 400;
    }

    .special-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 12px;
        padding: 1.5rem;
        max-width: 600px;
        margin: 0 auto;
        transition: all 0.3s ease;
        cursor: pointer;
        text-decoration: none;
        color: white;
        display: block;
    }

    .special-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.2);
        background: rgba(255, 255, 255, 0.2);
        text-decoration: none;
        color: white;
    }

    .special-icon {
        font-size: 2.5rem;
        margin-bottom: 1rem;
    }

    .special-card-title {
        font-size: 1.1rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .special-card-desc {
        font-size: 0.9rem;
        opacity: 0.9;
        line-height: 1.4;
    }

    .featured-section {
        margin: 2rem 1rem;
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
        color: white;
        text-align: center;
    }
    
    .week-section {
        margin: 1.5rem 1rem;
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #e91e63;
    }
    
    .week-title {
        font-size: 1rem;
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
        flex-shrink: 0;
    }
    
    .lesson-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 1rem;
        margin-bottom: 1rem;
    }
    
    .lesson-card {
        background: #f7fafc;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 1rem;
        text-decoration: none;
        color: inherit;
        transition: all 0.2s ease;
        cursor: pointer;
        display: block;
    }
    
    .lesson-card:hover {
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        transform: translateY(-2px);
        text-decoration: none;
        color: inherit;
    }
    
    .lesson-card.active {
        border-color: #68d391;
        background: linear-gradient(135deg, #f0fff4 0%, #f7fafc 100%);
    }

    .lesson-card.advanced {
        border-color: #9f7aea;
        background: linear-gradient(135deg, #faf5ff 0%, #f7fafc 100%);
    }

    .lesson-card.quiz {
        border-color: #ffd700;
        background: linear-gradient(135deg, #fffbf0 0%, #f7fafc 100%);
        border-width: 2px;
    }

    .quiz .lesson-icon {
        color: #d69e2e;
    }

    .advanced .lesson-icon {
        color: #805ad5;
    }
    
    .lesson-card.coming-soon {
        opacity: 0.6;
        cursor: not-allowed;
    }
    
    .lesson-icon {
        font-size: 1.5rem;
        margin-bottom: 0.5rem;
        text-align: center;
    }
    
    .active .lesson-icon {
        color: #38a169;
    }
    
    .coming-soon .lesson-icon {
        color: #a0aec0;
    }
    
    .lesson-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.3rem;
        text-align: center;
        line-height: 1.2;
    }
    
    .lesson-type {
        font-size: 0.7rem;
        color: #718096;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    
    .assignment-info {
        background: #edf2f7;
        border-radius: 6px;
        padding: 0.8rem;
        margin-top: 1rem;
        border-left: 3px solid #4299e1;
    }
    
    .assignment-title {
        font-size: 0.8rem;
        font-weight: 600;
        color: #2d3748;
        margin-bottom: 0.3rem;
    }
    
    .assignment-desc {
        font-size: 0.75rem;
        color: #4a5568;
        line-height: 1.3;
    }
    
    .exam-week {
        background: linear-gradient(135deg, #fed7e2 0%, #fbb6ce 100%);
        border-left: 4px solid #e91e63;
    }
    
    .exam-card {
        background: linear-gradient(135deg, #fed7e2 0%, #fbb6ce 100%);
        border-color: #e91e63;
    }
    
    @media (max-width: 768px) {
        .lesson-grid {
            grid-template-columns: 1fr;
        }
        
        .course-details {
            flex-direction: column;
            align-items: center;
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
        <h1 class="course-title">🧠 PHL 201: Introduction to Philosophy</h1>
        <p class="college-info">Wayne County Community College District</p>
        <p class="instructor-info">Instructor: Xavier Honablue, M.Ed. | Room 204 | honablue@umich.edu</p>
        <div class="course-details">
            <div class="detail-badge">3 Credit Hours</div>
            <div class="detail-badge">45 Contact Hours</div>
            <div class="detail-badge">16 Weeks</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress Summary
    st.markdown("""
    <div class="progress-summary">
        <div class="progress-stats">
            <div>
                <div class="stat-number">10</div>
                <div class="stat-label">Active Lessons</div>
            </div>
            <div>
                <div class="stat-number">22</div>
                <div class="stat-label">Coming Soon</div>
            </div>
            <div>
                <div class="stat-number">13</div>
                <div class="stat-label">Assignments</div>
            </div>
            <div>
                <div class="stat-number">27</div>
                <div class="stat-label">Hours Available</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Latest Feature - EXAM 1 (120 Questions)
    st.markdown("""
    <div class="latest-feature">
        <div class="special-title">🆕 Latest Feature: EXAM 1 - Comprehensive Philosophy Assessment</div>
        <div class="special-subtitle">120 Questions • All 5 Sections • Tutorial Mode with Instant Feedback</div>
        <a href="https://phl201-exam1.streamlit.app/" target="_blank" class="special-card">
            <div class="special-icon">📝🎓✨</div>
            <div class="special-card-title">EXAM 1: Complete Philosophy Exam (120 Questions)</div>
            <div class="special-card-desc">
                Master all core philosophical concepts with this comprehensive exam covering Epistemology (30Q), 
                Plato's Theory of Forms (20Q), Socrates & Ancient Philosophy (20Q), Human Nature & Darwin (20Q), 
                and Logic & Argumentation (30Q). Features tutorial mode with instant feedback, detailed explanations 
                for every question, real-time scoring, and section-by-section performance analysis. Perfect for 
                comprehensive review and exam preparation!
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Featured Research Paper Section
    st.markdown("""
    <div class="featured-section">
        <div class="special-title">📄 Featured Research Paper</div>
        <div class="special-subtitle">Xavier Honablue, M.Ed. - Academic Publication</div>
        <a href="https://xavier-honablue-paper3.streamlit.app/" target="_blank" class="special-card">
            <div class="special-icon">📚✨</div>
            <div class="special-card-title">Academic Research: Philosophy in Practice</div>
            <div class="special-card-desc">
                Explore cutting-edge philosophical research by your instructor. This academic paper 
                demonstrates the practical application of philosophical principles in contemporary 
                educational and intellectual contexts.
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Special Advanced Section - Metaphysics CognitiveCloud
    st.markdown("""
    <div class="special-section">
        <div class="special-title">🌟 Advanced Metaphysics Module</div>
        <div class="special-subtitle">CognitiveCloud.ai - Logic Symbol Geometry & Infinitesimal Reality</div>
        <a href="https://phl201-metaphysics1.streamlit.app/" target="_blank" class="special-card">
            <div class="special-icon">∧∨¬→ε</div>
            <div class="special-card-title">Metaphysics CognitiveCloud: Logic Symbols & Geometric Meaning</div>
            <div class="special-card-desc">
                Explore how logic symbols encode geometric intuitions about reality's structure. 
                Discover the epsilon (ε) principle, string theory foundations, and dimensional transcendence. 
                Interactive 3D visualizations reveal how linearity collapses into wave-interdependence.
            </div>
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Week 1: Course Introduction
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">1</div>
            Week 1: Course Introduction
        </div>
        <div class="lesson-grid">
            <a href="https://philosophy-101-day1.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🤔</div>
                <h4 class="lesson-title">What is Philosophy?</h4>
                <p class="lesson-type">Interactive Exploration</p>
            </a>
            <a href="https://phl201-branches.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🌳</div>
                <h4 class="lesson-title">Three Branches of Philosophy</h4>
                <p class="lesson-type">Conceptual Framework</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Welcome Activity</div>
            <div class="assignment-desc">Full credit for all students - Course introduction and expectations</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 2: Ancient Philosophy
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">2</div>
            Week 2: Ancient Philosophy
        </div>
        <div class="lesson-grid">
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🏛️</div>
                <h4 class="lesson-title">Introduction to Ancient Philosophy</h4>
                <p class="lesson-type">Historical Context</p>
            </div>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🎭</div>
                <h4 class="lesson-title">Socratic Method & Dialogue</h4>
                <p class="lesson-type">Critical Thinking</p>
            </div>
            <a href="https://phl201-metaphysics1.streamlit.app/" target="_blank" class="lesson-card advanced">
                <div class="lesson-icon">∧∨¬</div>
                <h4 class="lesson-title">Advanced: Logic Symbol Geometry</h4>
                <p class="lesson-type">Optional • Metaphysical Foundations</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 1: Plato's Cave Video Reflection (4.6%)</div>
            <div class="assignment-desc">300-400 word reflection on Plato's Allegory of the Cave</div>
        </div>
        <div class="assignment-info" style="background: #e6fffa; border-left: 3px solid #319795;">
            <a href="https://logic1-phl202.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #319795; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#2c7a7b'" onmouseout="this.style.background='#319795'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🎮 Optional Logic Exercises (No Grade)</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Logic Games & Exercises - Practice critical thinking skills</div>
                </div>
            </a>
        </div>
        <div class="assignment-info" style="background: #faf5ff; border-left: 3px solid #9f7aea;">
            <a href="https://phl201-metaphysics1.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #9f7aea; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#805ad5'" onmouseout="this.style.background='#9f7aea'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🌟 Advanced: Metaphysics CognitiveCloud (No Grade)</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Explore logic symbol geometry & epsilon principle - 3D interactive visualizations</div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 3: Plato's Philosophy
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">3</div>
            Week 3: Plato's Philosophy (3 hours)
        </div>
        <div class="lesson-grid">
            <a href="https://phl201-week3.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">✏️</div>
                <h4 class="lesson-title">Writing Revision Workshop</h4>
                <p class="lesson-type">Writing Improvement</p>
            </a>
            <a href="https://phl201-week3.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">💡</div>
                <h4 class="lesson-title">Plato's Theory of Forms</h4>
                <p class="lesson-type">Metaphysics & Reality</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 2: Rewritten Video Reflection (4.6%)</div>
            <div class="assignment-desc">Revised Cave reflection incorporating Theory of Forms</div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 3: Aristotelian Ethics Reading Response (4.6%)</div>
            <div class="assignment-desc">350-400 word analysis of virtue ethics</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 4: Medieval Philosophy & Epistemology
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">4</div>
            Week 4: Medieval Philosophy & Epistemology (3 hours)
        </div>
        <div class="lesson-grid">
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🏰</div>
                <h4 class="lesson-title">Medieval Philosophy - Augustine & Aquinas</h4>
                <p class="lesson-type">Medieval Thought</p>
            </div>
            <a href="https://phl201-epistemology.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🔍</div>
                <h4 class="lesson-title">Epistemology: Theory of Knowledge</h4>
                <p class="lesson-type">Knowledge & Belief</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 4: Comparative Philosophy Journal Entry (4.6%)</div>
            <div class="assignment-desc">Weekly philosophical writing and reflection assignment</div>
        </div>
        <div class="assignment-info" style="background: #f0fff4; border-left: 3px solid #38a169;">
            <a href="https://phl201-epistemology.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #38a169; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#2f855a'" onmouseout="this.style.background='#38a169'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🔍 Epistemology Interactive Module</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Explore knowledge, belief, and skepticism through interactive exercises</div>
                </div>
            </a>
        </div>
        <div class="assignment-info" style="background: #fffbf0; border-left: 3px solid #d69e2e;">
            <a href="https://phl201-week4-quiz.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #d69e2e; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#b7791f'" onmouseout="this.style.background='#d69e2e'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🧠 Week 4 Philosophy Quiz (Optional)</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">85-question comprehensive quiz - Test your knowledge of ancient philosophy</div>
                </div>
            </a>
        </div>
        <div class="assignment-info" style="background: #fff5f5; border-left: 3px solid #e53e3e;">
            <a href="https://phl201-week4-exam.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #e53e3e; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#c53030'" onmouseout="this.style.background='#e53e3e'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">📝 Week 4 Philosophy Exam</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Comprehensive exam - Ancient Philosophy & Human Nature</div>
                </div>
            </a>
        </div>
        <div class="assignment-info" style="background: #f0fff4; border-left: 3px solid #38a169;">
            <a href="https://phl201-critique.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #38a169; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#2f855a'" onmouseout="this.style.background='#38a169'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🔍 Gettier Problem Critique</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Advanced epistemology - Challenge JTB through critical analysis of the fake barn scenario</div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 5: Eastern Philosophy - NOW WITH EXAM 1
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">5</div>
            Week 5: Eastern Philosophy (3 hours)
        </div>
        <div class="lesson-grid">
            <a href="https://phl202-buddhism.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">☸️</div>
                <h4 class="lesson-title">Buddhist Philosophy</h4>
                <p class="lesson-type">Eastern Wisdom</p>
            </a>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">📜</div>
                <h4 class="lesson-title">Confucian Thought</h4>
                <p class="lesson-type">Social Philosophy</p>
            </div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 5: Eastern Philosophy Reflection Paper (4.6%)</div>
            <div class="assignment-desc">350-400 word reflection on Buddhist philosophy and its relevance</div>
        </div>
        <div class="assignment-info" style="background: #fff5f5; border-left: 3px solid #e53e3e;">
            <a href="https://phl201-exam1.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: linear-gradient(135deg, #e53e3e 0%, #c53030 100%); color: white; padding: 1rem 1.5rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer; border: 2px solid #ffd700;" onmouseover="this.style.transform='scale(1.02)'" onmouseout="this.style.transform='scale(1)'">
                    <div style="font-weight: 700; margin-bottom: 0.3rem; font-size: 1.1rem;">📝🎓 EXAM 1: Comprehensive Philosophy Assessment</div>
                    <div style="font-size: 0.9rem; opacity: 0.95; margin-bottom: 0.5rem;">120 Questions • Tutorial Mode • Instant Feedback</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">
