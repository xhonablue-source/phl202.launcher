{
            "week": 7,
            "title": "Modern Philosophy",
            "lessons": [("Descartes & Rationalism", "🧠", "Tuesday"), ("Empiricism - Locke & Hume", "👁️", "Thursday")],
            "assignment": "Assignment 7: Rationalism vs. Empiricism Debate Preparation (4.6%)"
        },
        {
            "week": 8,
            "title": "Midterm Week",
            "lessons": [("Midterm Review", "📚", "Tuesday"), ("MIDTERM EXAM", "📝", "Thursday")],
            "assignment": "Midterm Examination (20%)",
            "exam": True
        },
        {
            "week": 9,
            "title": "Kant & Utilitarianism",
            "lessons": [("Kant's Critical Philosophy", "⚖️", "Tuesday"), ("Ethics - Utilitarianism", "🎯", "Thursday")],
            "assignment": "Assignment 8: Ethical Theory Application Exercise (4.6%)"
        },
        {
            "week": 10,
            "title": "Ethical Theories",
            "lessons": [("Deontological Ethics", "📋", "Tuesday"), ("Virtue Ethics", "🌟", "Thursday")],
            "assignment": "Assignment 9: Personal Ethics Philosophy Paper (4.6%)"
        },
        {
            "week": 11,
            "title": "Political Philosophy",
            "lessons": [("Social Contract Theory", "🤝", "Tuesday"), ("Justice and Rights", "⚖️", "Thursday")],
            "assignment": "Assignment 10: Political Philosophy Case Study Analysis (4.6%)"
        },
        {
            "week": 12,
            "title": "Philosophy of Science",
            "lessons": [("Philosophy of Science", "🔬", "Tuesday"), ("Thanksgiving Break", "🦃", "Thursday")],
            "assignment": "Assignment 11: Science and Philosophy Reflection (4.6%)"
        },
        {
            "week": 13,
            "title": "Epistemology - Advanced Topics",
            "lessons": [("Gettier Problem Critique", "🔍", "Tuesday"), ("Knowledge & Justification", "📖", "Thursday")],
            "assignment": "Assignment 12: Philosophical Critique Essay (4.6%)",
            "active_links": ["https://phl201-critique.streamlit.app/"]
        },
        {
            "week": 14,
            "title": "Contemporary Philosophy",
            "lessons": [("Contemporary Philosophy Issues", "🌐", "Tuesday"), ("Student Philosopher Presentations", "🎤", "Thursday")],
            "assignment": "Assignment 13: Philosopher Research Presentation (4.8%)"
        },
        {
            "week": 15,
            "title": "Philosophy & Technology",
            "lessons": [("Philosophy and Technology", "💻", "Tuesday"), ("Final Review Session", "📖", "Thursday")],
            "assignment": "Final Exam Preparation"
        },
        {
            "week": 16,
            "title": "Final Examination",
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
        
        active_links = week_info.get("active_links", [])
        for idx, lesson_data in enumerate(week_info["lessons"]):
            lesson_title, icon, day = lesson_data
            
            if week_info.get("exam"):
                card_class = "lesson-card exam-card"
                link_html = f'<div class="{card_class}">'
                close_tag = "</div>"
            elif idx < len(active_links):
                card_class = "lesson-card active"
                link_html = f'<a href="{active_links[idx]}" target="_blank" class="{card_class}">'
                close_tag = "</a>"
            else:
                card_class = "lesson-card coming-soon"
                link_html = f'<div class="{card_class}">'
                close_tag = "</div>"
            
            st.markdown(f"""
                {link_html}
                    <div class="lesson-icon">{icon}</div>
                    <h4 class="lesson-title">{lesson_title}</h4>
                    <p class="lesson-type">{day}</p>
                {close_tag}
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
