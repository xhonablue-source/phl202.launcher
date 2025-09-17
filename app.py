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
            <div class="detail-badge">Tue/Thu 11:00 AM-12:44 PM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Progress Summary
    st.markdown("""
    <div class="progress-summary">
        <div class="progress-stats">
            <div>
                <div class="stat-number">5</div>
                <div class="stat-label">Active Lessons</div>
            </div>
            <div>
                <div class="stat-number">27</div>
                <div class="stat-label">Coming Soon</div>
            </div>
            <div>
                <div class="stat-number">13</div>
                <div class="stat-label">Assignments</div>
            </div>
            <div>
                <div class="stat-number">12</div>
                <div class="stat-label">Hours Available</div>
            </div>
        </div>
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
                <p class="lesson-type">Tuesday • Interactive Exploration</p>
            </a>
            <a href="https://phl201-branches.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🌳</div>
                <h4 class="lesson-title">Three Branches of Philosophy</h4>
                <p class="lesson-type">Thursday • Conceptual Framework</p>
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
                <p class="lesson-type">Tuesday • Historical Context</p>
            </div>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">💡</div>
                <h4 class="lesson-title">Plato's Theory of Forms</h4>
                <p class="lesson-type">Thursday • Metaphysics</p>
            </div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 1: Plato's Cave Video Reflection (4.6%)</div>
            <div class="assignment-desc">300-400 word reflection on Plato's Allegory of the Cave - Due Thursday</div>
        </div>
        <div class="assignment-info" style="background: #e6fffa; border-left: 3px solid #319795;">
            <a href="https://logic1-phl202.streamlit.app/" target="_blank" style="text-decoration: none; display: block;">
                <div style="background: #319795; color: white; padding: 0.8rem 1.2rem; border-radius: 8px; text-align: center; transition: all 0.2s ease; cursor: pointer;" onmouseover="this.style.background='#2c7a7b'" onmouseout="this.style.background='#319795'">
                    <div style="font-weight: 600; margin-bottom: 0.2rem;">🎮 Optional Logic Exercises (No Grade)</div>
                    <div style="font-size: 0.85rem; opacity: 0.9;">Logic Games & Exercises - Practice critical thinking skills</div>
                </div>
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 3: Ancient Philosophy - ACTIVE
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">3</div>
            Week 3: Ancient Philosophy (3 hours)
        </div>
        <div class="lesson-grid">
            <a href="https://phl201-week3.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">✏️</div>
                <h4 class="lesson-title">Revision Workshop</h4>
                <p class="lesson-type">Tuesday • Writing Improvement</p>
            </a>
            <a href="https://phl201-week3.streamlit.app/" target="_blank" class="lesson-card active">
                <div class="lesson-icon">🏛️</div>
                <h4 class="lesson-title">Plato's Theory of Forms</h4>
                <p class="lesson-type">Thursday • Ancient Philosophy</p>
            </a>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 2: Rewritten Video Reflection (4.6%)</div>
            <div class="assignment-desc">Revised Cave reflection incorporating Theory of Forms - Due Tuesday</div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 3: Aristotelian Ethics Reading Response (4.6%)</div>
            <div class="assignment-desc">350-400 word analysis of virtue ethics - Due Thursday</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 4: Medieval Philosophy
    st.markdown("""
    <div class="week-section">
        <div class="week-title">
            <div class="week-number">4</div>
            Week 4: Medieval Philosophy
        </div>
        <div class="lesson-grid">
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🏰</div>
                <h4 class="lesson-title">Medieval Philosophy - Augustine & Aquinas</h4>
                <p class="lesson-type">Tuesday</p>
            </div>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">🕉️</div>
                <h4 class="lesson-title">Eastern Philosophy Introduction</h4>
                <p class="lesson-type">Thursday</p>
            </div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 4: Comparative Philosophy Journal Entry (4.6%)</div>
            <div class="assignment-desc">Weekly philosophical writing and reflection assignment</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Week 5: Eastern Philosophy - ACTIVE
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
                <p class="lesson-type">Tuesday • Eastern Wisdom</p>
            </a>
            <div class="lesson-card coming-soon">
                <div class="lesson-icon">📜</div>
                <h4 class="lesson-title">Confucian Thought</h4>
                <p class="lesson-type">Thursday • Social Philosophy</p>
            </div>
        </div>
        <div class="assignment-info">
            <div class="assignment-title">Assignment 5: Eastern Philosophy Reflection Paper (4.6%)</div>
            <div class="assignment-desc">350-400 word reflection on Buddhist philosophy and its relevance - Due Thursday</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Continue with remaining weeks...
    weeks_data = [
        {
            "week": 6, "title": "African & Indigenous Philosophy", 
            "lessons": [("African Philosophy Traditions", "🌍", "Tuesday"), ("Indigenous Philosophical Perspectives", "🪶", "Thursday")],
            "assignment": "Assignment 6: Cultural Philosophy Comparison Chart (4.6%)"
        },
        {
            "week": 7, "title": "Modern Philosophy", 
            "lessons": [("Descartes & Rationalism", "🧠", "Tuesday"), ("Empiricism - Locke & Hume", "👁️", "Thursday")],
            "assignment": "Assignment 7: Rationalism vs. Empiricism Debate Preparation (4.6%)"
        },
        {
            "week": 8, "title": "Midterm Week", 
            "lessons": [("Midterm Review", "📚", "Tuesday"), ("MIDTERM EXAM", "📝", "Thursday")],
            "assignment": "Midterm Examination (20%)",
            "exam": True
        },
        {
            "week": 9, "title": "Kant & Utilitarianism", 
            "lessons": [("Kant's Critical Philosophy", "⚖️", "Tuesday"), ("Ethics - Utilitarianism", "🎯", "Thursday")],
            "assignment": "Assignment 8: Ethical Theory Application Exercise (4.6%)"
        },
        {
            "week": 10, "title": "Ethical Theories", 
            "lessons": [("Deontological Ethics", "📋", "Tuesday"), ("Virtue Ethics", "🌟", "Thursday")],
            "assignment": "Assignment 9: Personal Ethics Philosophy Paper (4.6%)"
        },
        {
            "week": 11, "title": "Political Philosophy", 
            "lessons": [("Social Contract Theory", "🤝", "Tuesday"), ("Justice and Rights", "⚖️", "Thursday")],
            "assignment": "Assignment 10: Political Philosophy Case Study Analysis (4.6%)"
        },
        {
            "week": 12, "title": "Philosophy of Science", 
            "lessons": [("Philosophy of Science", "🔬", "Tuesday"), ("Thanksgiving Break", "🦃", "Thursday")],
            "assignment": "Assignment 11: Science and Philosophy Reflection (4.6%)"
        },
        {
            "week": 13, "title": "Existentialism", 
            "lessons": [("Existentialism", "🎭", "Tuesday"), ("Phenomenology and Consciousness", "🧘", "Thursday")],
            "assignment": "Assignment 12: Existentialist Life Reflection (4.6%)"
        },
        {
            "week": 14, "title": "Contemporary Philosophy", 
            "lessons": [("Contemporary Philosophy Issues", "🌐", "Tuesday"), ("Student Philosopher Presentations", "🎤", "Thursday")],
            "assignment": "Assignment 13: Philosopher Research Presentation (4.8%)"
        },
        {
            "week": 15, "title": "Philosophy & Technology", 
            "lessons": [("Philosophy and Technology", "💻", "Tuesday"), ("Final Review Session", "📖", "Thursday")],
            "assignment": "Final Exam Preparation"
        },
        {
            "week": 16, "title": "Final Examination", 
            "lessons": [("FINAL EXAM", "📝", "Tuesday")],
            "assignment": "Final Examination (20%)",
            "exam": True
        }
    ]

    for week_info in weeks_data:
        section_class = "week-section exam-week" if week_info.get("exam") else "week-section"
        st.markdown(f"""
        <div class="{section_class}">
            <div class="week-title">
                <div class="week-number">{week_info['week']}</div>
                Week {week_info['week']}: {week_info['title']}
            </div>
            <div class="lesson-grid">
        """, unsafe_allow_html=True)
        
        for lesson_title, icon, day in week_info["lessons"]:
            card_class = "lesson-card exam-card" if week_info.get("exam") else "lesson-card coming-soon"
            st.markdown(f"""
                <div class="{card_class}">
                    <div class="lesson-icon">{icon}</div>
                    <h4 class="lesson-title">{lesson_title}</h4>
                    <p class="lesson-type">{day}</p>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("""
            </div>
            <div class="assignment-info">
        """, unsafe_allow_html=True)
        
        if week_info.get("exam"):
            st.markdown(f"""
                <div class="assignment-title">{week_info['assignment']}</div>
                <div class="assignment-desc">Comprehensive examination covering course materials</div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="assignment-title">{week_info['assignment']}</div>
                <div class="assignment-desc">Weekly philosophical writing and reflection assignment</div>
            """, unsafe_allow_html=True)
        
        st.markdown("</div></div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
