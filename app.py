"""
Three Branches of Philosophy - Interactive Educational App
A comprehensive lesson on Metaphysics, Epistemology, and Ethics
"""

import streamlit as st
import time
import json
from datetime import datetime
from typing import List, Dict, Optional

# Configure page
st.set_page_config(
    page_title="Three Branches of Philosophy",
    page_icon="🌳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'current_slide' not in st.session_state:
    st.session_state.current_slide = 0
if 'student_responses' not in st.session_state:
    st.session_state.student_responses = {}
if 'quiz_scores' not in st.session_state:
    st.session_state.quiz_scores = {}
if 'reflection_notes' not in st.session_state:
    st.session_state.reflection_notes = {"metaphysics": "", "epistemology": "", "ethics": ""}

# Slide content for Three Branches of Philosophy
SLIDES = [
    {
        "id": "welcome",
        "title": "Three Branches of Philosophy",
        "content": """
        # 🌳 Three Branches of Philosophy
        
        ## Thursday • Conceptual Framework
        
        ### Today's Learning Objectives:
        - **Understand** the three main branches of philosophical inquiry
        - **Explore** fundamental questions in each branch
        - **Connect** philosophical concepts to everyday life
        - **Practice** philosophical thinking and reasoning
        
        > *"Philosophy begins in wonder."* — Aristotle
        
        **The Three Branches We'll Explore:**
        1. 🤔 **Metaphysics** - What exists?
        2. 🧠 **Epistemology** - How do we know?
        3. ⚖️ **Ethics** - How should we live?
        """,
        "presenter_notes": "Welcome students and set the stage for understanding philosophy's systematic approach to fundamental questions."
    },
    {
        "id": "philosophy_tree",
        "title": "The Philosophy Tree",
        "content": """
        # 🌳 Visualizing Philosophy as a Tree
        
        ## The Metaphor:
        Think of philosophy as a great tree with three main branches, each reaching toward different fundamental questions about existence, knowledge, and values.
        
        ### 🌿 Branch 1: Metaphysics
        **The Nature of Reality**
        - What exists?
        - What is real vs. illusion?
        - Do abstract things (numbers, ideas) exist?
        - Is there a God or ultimate reality?
        
        ### 🌿 Branch 2: Epistemology  
        **The Nature of Knowledge**
        - How do we know things?
        - What makes beliefs justified?
        - Can we have certain knowledge?
        - What are the limits of human understanding?
        
        ### 🌿 Branch 3: Ethics
        **The Nature of Right and Wrong**
        - What makes actions right or wrong?
        - How should we live?
        - What is the good life?
        - What do we owe to others?
        
        ## 🔗 How They Connect:
        These branches intertwine - your view of reality affects how you think we can know things, which affects how you think we should act.
        """,
        "presenter_notes": "Use the tree metaphor to help students see philosophy as an organized system of inquiry, not random questions."
    },
    {
        "id": "metaphysics_deep_dive",
        "title": "Branch 1: Metaphysics",
        "content": """
        # 🤔 Metaphysics: What Exists?
        
        ## Core Question: *"What is the nature of reality?"*
        
        ### Key Areas of Investigation:
        
        **🌌 Existence & Being**
        - What does it mean for something to exist?
        - Why is there something rather than nothing?
        
        **🧩 Substance & Properties**
        - What are things made of ultimately?
        - Are minds and bodies different substances?
        
        **⏰ Time & Space**
        - Is time real or an illusion?
        - Does the past still exist?
        
        **🔢 Abstract Objects**
        - Do numbers exist independently of human minds?
        - What about concepts like justice or beauty?
        
        ## 💭 Famous Metaphysical Questions:
        - If you replace every part of a ship, is it still the same ship?
        - Do you remain the same person throughout your life?
        - Could there be multiple universes?
        - Is everything predetermined or do we have free will?
        
        ### 🎯 Reflection Question:
        What do you think is the most fundamental thing that exists?
        """,
        "presenter_notes": "Give concrete examples to make abstract metaphysical concepts accessible. The ship of Theseus is particularly good for engaging students.",
        "interactive": True,
        "discussion_prompt": "What do you think is the most fundamental thing that exists? Matter? Mind? Energy? Something else?"
    },
    {
        "id": "epistemology_deep_dive",
        "title": "Branch 2: Epistemology",
        "content": """
        # 🧠 Epistemology: How Do We Know?
        
        ## Core Question: *"What can we know and how can we know it?"*
        
        ### Key Areas of Investigation:
        
        **🎯 Sources of Knowledge**
        - Experience (empiricism)
        - Reason (rationalism)  
        - Intuition
        - Testimony from others
        
        **✅ Justification**
        - What makes a belief justified?
        - How much evidence is enough?
        - Can we know anything with certainty?
        
        **🧩 The Nature of Truth**
        - What makes statements true or false?
        - Is truth relative or absolute?
        
        **🤷 Skepticism**
        - How do we know we're not dreaming?
        - Could we be deceived about everything?
        
        ## 💭 Famous Epistemological Puzzles:
        - How do you know you're not in a simulation like The Matrix?
        - Can you know something without being able to prove it?
        - If everyone believes something false, does that make it true?
        - Is seeing always believing?
        
        ### 🎯 Reflection Question:
        What's something you're absolutely certain you know? How do you know it?
        """,
        "presenter_notes": "Connect to students' experience with social media, fake news, and information reliability. The Matrix example works well.",
        "interactive": True,
        "discussion_prompt": "What's something you're absolutely certain you know? How do you know it? What would it take to make you doubt it?"
    },
    {
        "id": "ethics_deep_dive",
        "title": "Branch 3: Ethics",
        "content": """
        # ⚖️ Ethics: How Should We Live?
        
        ## Core Question: *"What is right and wrong, and how should we act?"*
        
        ### Key Areas of Investigation:
        
        **⚖️ Normative Ethics**
        - What makes actions right or wrong?
        - Should we focus on consequences or intentions?
        - What virtues should we cultivate?
        
        **🎯 Applied Ethics**
        - Medical ethics: When is it okay to end life support?
        - Environmental ethics: What do we owe future generations?
        - Technology ethics: Should AI have rights?
        
        **🤔 Meta-Ethics**
        - Are moral facts objective or subjective?
        - Where do moral obligations come from?
        
        **💫 The Good Life**
        - What makes life meaningful?
        - Is happiness the ultimate goal?
        - How do we balance individual and social good?
        
        ## 💭 Famous Ethical Dilemmas:
        - Trolley Problem: Save five lives by sacrificing one?
        - If you could prevent suffering by telling a lie, should you?
        - Do animals have rights equal to humans?
        - Is it wrong to be wealthy while others are poor?
        
        ### 🎯 Reflection Question:
        What's the most important moral principle that guides your decisions?
        """,
        "presenter_notes": "Use contemporary examples like social media ethics, climate change, AI. Students relate well to everyday moral choices.",
        "interactive": True,
        "discussion_prompt": "What's the most important moral principle that guides your decisions? Where do you think this principle comes from?"
    },
    {
        "id": "connections_activity",
        "title": "How the Branches Connect",
        "content": """
        # 🔗 Activity: Tracing the Connections
        
        ## See How Your Philosophical Views Connect!
        
        ### Example: The Question of Punishment
        
        **🤔 Metaphysical Question:**
        Do humans have free will, or are our actions determined by prior causes?
        
        **🧠 Epistemological Question:**  
        How can we know whether someone truly intended to commit a crime?
        
        **⚖️ Ethical Question:**
        If someone's actions were determined by their genetics and environment, is it just to punish them?
        
        ---
        
        ## 🎯 Your Turn: Pick a Current Issue
        
        **Choose one:**
        - Artificial Intelligence
        - Climate Change  
        - Social Media
        - Medical Treatment
        - Economic Inequality
        
        **Then ask:**
        1. **Metaphysical:** What exists here? (minds, rights, nature, etc.)
        2. **Epistemological:** How do we know what's true about this issue?
        3. **Ethical:** What should we do?
        
        ### 💭 Discussion Prompt:
        Notice how you can't fully answer the ethical question without first considering the metaphysical and epistemological dimensions!
        """,
        "presenter_notes": "This activity shows students that philosophical thinking is systematic and interconnected. Walk around and help groups see the connections.",
        "interactive": True,
        "timer_minutes": 15,
        "activity_type": "group_work"
    },
    {
        "id": "everyday_philosophy",
        "title": "Philosophy in Everyday Life",
        "content": """
        # 🏠 Philosophy in Your Daily Life
        
        ## You're Already a Philosopher!
        
        ### 🌅 Morning Questions (Metaphysics)
        - *"Who am I really?"* (personal identity)
        - *"Is this dream real?"* (reality vs. appearance)
        - *"Do I have free will today?"* (determinism vs. freedom)
        
        ### 📱 Throughout the Day (Epistemology)
        - *"Should I believe this news story?"* (evidence and truth)
        - *"How do I know what my friend meant?"* (interpretation)
        - *"Can I trust my memory?"* (sources of knowledge)
        
        ### 🌙 Evening Reflection (Ethics)
        - *"Did I do the right thing today?"* (moral evaluation)
        - *"What kind of person am I becoming?"* (virtue)
        - *"How can I live better tomorrow?"* (the good life)
        
        ## 🎯 Philosophy as a Life Skill
        
        **Critical Thinking:** Questioning assumptions, evaluating evidence
        **Clear Communication:** Defining terms, making logical arguments  
        **Ethical Reasoning:** Considering multiple perspectives, weighing values
        **Wonder & Curiosity:** Staying open to new ideas and possibilities
        
        ### 💫 The Philosophical Mindset:
        *"I know that I know nothing"* - Socrates
        
        Philosophy isn't about having all the answers - it's about asking better questions and thinking more carefully about the big issues that matter most.
        """,
        "presenter_notes": "Help students see philosophy as practical, not just academic. Emphasize that philosophical thinking improves decision-making and self-understanding."
    },
    {
        "id": "wrap_up",
        "title": "Synthesis & Next Steps",
        "content": """
        # 🎯 Bringing It All Together
        
        ## What We've Discovered:
        
        ### 🌳 The Three Branches:
        - **Metaphysics:** Investigates the fundamental nature of reality
        - **Epistemology:** Examines how we acquire knowledge and what we can know
        - **Ethics:** Explores how we should live and what makes actions right or wrong
        
        ### 🔗 Key Insights:
        1. **Interconnection:** The branches influence each other
        2. **Relevance:** These questions matter for daily life
        3. **Ongoing:** Philosophy is a process, not a destination
        4. **Personal:** Your philosophical views shape how you see everything
        
        ## 📝 Reflection Assignment:
        
        **Choose ONE branch that interests you most and write 2-3 paragraphs:**
        
        1. **Explain** the branch in your own words
        2. **Identify** a specific question from that branch that intrigues you
        3. **Connect** it to something in your own life or current events
        4. **Explore** different possible answers (you don't need to solve it!)
        
        ## 🚀 Looking Ahead:
        
        **Next Class:** We'll dive deeper into one specific philosophical method - logical argumentation and critical thinking skills.
        
        **Coming Up:** Applications to religion, ethics, politics, science, and art.
        
        ### 🌟 Remember:
        Philosophy isn't about memorizing what ancient Greeks thought - it's about learning to think more clearly and deeply about the questions that matter most to human life.
        """,
        "presenter_notes": "Wrap up by emphasizing the practical value of philosophical thinking. Collect reflections to gauge student understanding and interests."
    }
]

# Quiz data for each branch
QUIZ_DATA = {
    "metaphysics_quiz": {
        "title": "Metaphysics: Understanding Reality",
        "questions": [
            {
                "question": "Which question is primarily metaphysical?",
                "options": [
                    "How do we know if God exists?",
                    "Does God exist?", 
                    "Should we believe in God?",
                    "What evidence supports God's existence?"
                ],
                "correct": 1,
                "explanation": "Metaphysics asks about what exists, not how we know it (epistemology) or what we should do (ethics). The question 'Does God exist?' is asking about the nature of reality itself."
            },
            {
                "question": "The Ship of Theseus paradox primarily deals with:",
                "options": [
                    "How we know things",
                    "Personal identity and persistence",
                    "Moral responsibility",
                    "The existence of abstract objects"
                ],
                "correct": 1,
                "explanation": "This famous paradox asks whether an object remains the same if all its parts are replaced - a question about identity and what makes something the same thing over time."
            },
            {
                "question": "Free will vs. determinism is a debate about:",
                "options": [
                    "Whether we can know the future",
                    "Whether our actions are morally right",
                    "Whether our choices are truly free or predetermined",
                    "Whether we can trust our senses"
                ],
                "correct": 2,
                "explanation": "This metaphysical debate asks about the fundamental nature of human action and choice - whether we truly have freedom or if everything is determined by prior causes."
            }
        ]
    },
    "epistemology_quiz": {
        "title": "Epistemology: Understanding Knowledge",
        "questions": [
            {
                "question": "Epistemology is primarily concerned with:",
                "options": [
                    "What exists in reality",
                    "How we should act morally",
                    "How we acquire and justify knowledge",
                    "What makes life meaningful"
                ],
                "correct": 2,
                "explanation": "Epistemology studies the nature, sources, and limits of knowledge - how we know things and what counts as justified belief."
            },
            {
                "question": "The question 'How do you know you're not dreaming right now?' illustrates:",
                "options": [
                    "Metaphysical doubt about reality",
                    "Epistemological skepticism about knowledge",
                    "Ethical concerns about deception",
                    "Logical fallacies in reasoning"
                ],
                "correct": 1,
                "explanation": "This is a classic epistemological challenge that questions whether we can have certain knowledge about the external world - it's about the limits and reliability of our knowledge, not about what's real."
            },
            {
                "question": "Which is an epistemological question?",
                "options": [
                    "Do numbers exist independently of minds?",
                    "Is it wrong to lie?",
                    "Can we know anything with absolute certainty?",
                    "What is the meaning of life?"
                ],
                "correct": 2,
                "explanation": "This question asks about the nature and limits of knowledge itself - whether certain knowledge is possible for humans."
            }
        ]
    },
    "ethics_quiz": {
        "title": "Ethics: Understanding Right and Wrong",
        "questions": [
            {
                "question": "Which question belongs primarily to ethics?",
                "options": [
                    "Do moral facts exist objectively?",
                    "How do we know what's right and wrong?",
                    "What should I do in this situation?",
                    "What is the nature of goodness?"
                ],
                "correct": 2,
                "explanation": "While the others touch on ethics, 'What should I do?' is the central practical question of ethics - how to act rightly in specific situations."
            },
            {
                "question": "The trolley problem is designed to explore:",
                "options": [
                    "Whether we can know the consequences of our actions",
                    "Whether numbers and abstract objects exist",
                    "Whether intentions matter more than consequences",
                    "Whether free will exists"
                ],
                "correct": 2,
                "explanation": "The trolley problem tests whether we judge actions by their consequences (saving five lives) or by the nature of the action itself (actively causing one death)."
            },
            {
                "question": "Applied ethics focuses on:",
                "options": [
                    "Abstract theories about the nature of morality",
                    "Specific moral issues in real-world contexts",
                    "Whether moral truths exist",
                    "How we can know right from wrong"
                ],
                "correct": 1,
                "explanation": "Applied ethics takes ethical theories and applies them to concrete issues like medical ethics, environmental ethics, or business ethics."
            }
        ]
    }
}

# Learning resources
RESOURCES = {
    "videos": [
        {
            "title": "Crash Course Philosophy #1 - What is Philosophy?",
            "url": "https://www.youtube.com/watch?v=1A_CAkYt3GY",
            "description": "Introduction to philosophical thinking and the main branches",
            "duration": "8 minutes"
        },
        {
            "title": "The Three Branches of Philosophy Explained",
            "url": "https://www.youtube.com/watch?v=YxBShkU_83o",
            "description": "Clear overview of metaphysics, epistemology, and ethics",
            "duration": "12 minutes"
        },
        {
            "title": "Philosophy: Metaphysics",
            "url": "https://www.youtube.com/watch?v=YY_VRhS8JCY",
            "description": "Deeper dive into metaphysical questions and problems",
            "duration": "10 minutes"
        }
    ],
    "readings": [
        {
            "title": "Stanford Encyclopedia: Metaphysics",
            "url": "https://plato.stanford.edu/entries/metaphysics/",
            "description": "Comprehensive academic overview of metaphysics"
        },
        {
            "title": "Internet Encyclopedia: Epistemology",
            "url": "https://iep.utm.edu/epistemo/",
            "description": "Accessible introduction to epistemological questions"
        },
        {
            "title": "Ethics: A Brief Introduction",
            "url": "https://iep.utm.edu/ethics/",
            "description": "Overview of ethical theories and applied ethics"
        }
    ]
}

def display_slide(slide_data: dict) -> None:
    """Display a slide with enhanced formatting and interactivity"""
    
    # Main content
    st.markdown(slide_data["content"])
    
    # Interactive elements
    if slide_data.get("interactive"):
        st.markdown("---")
        
        if "discussion_prompt" in slide_data:
            st.markdown("### 💭 Think & Discuss:")
            st.info(slide_data["discussion_prompt"])
            
            # Response area
            response_key = f"response_{slide_data['id']}"
            response = st.text_area(
                "Share your thoughts:",
                key=response_key,
                placeholder="What do you think? Write your response here...",
                height=100
            )
            
            if response and st.button(f"Save Response", key=f"save_{slide_data['id']}"):
                st.session_state.student_responses[response_key] = {
                    'response': response,
                    'timestamp': datetime.now().isoformat(),
                    'slide': slide_data['title']
                }
                st.success("Response saved!")
        
        # Timer for activities
        if slide_data.get("timer_minutes"):
            st.markdown("---")
            col1, col2 = st.columns([1, 3])
            with col1:
                if st.button(f"⏰ Start {slide_data['timer_minutes']} min timer"):
                    st.session_state.timer_start = time.time()
                    st.session_state.timer_duration = slide_data['timer_minutes'] * 60
                    st.rerun()
            
            with col2:
                if hasattr(st.session_state, 'timer_start'):
                    elapsed = time.time() - st.session_state.timer_start
                    remaining = max(0, st.session_state.timer_duration - elapsed)
                    
                    if remaining > 0:
                        mins, secs = divmod(int(remaining), 60)
                        st.markdown(f"**Time remaining: {mins:02d}:{secs:02d}**")
                        time.sleep(1)
                        st.rerun()
                    else:
                        st.success("⏰ Time's up!")

def display_quiz(quiz_id: str) -> None:
    """Display an interactive quiz for each branch"""
    
    if quiz_id not in QUIZ_DATA:
        st.error("Quiz not found!")
        return
    
    quiz = QUIZ_DATA[quiz_id]
    st.markdown(f"## 📝 {quiz['title']}")
    st.markdown("Test your understanding of this philosophical branch!")
    
    with st.form(f"quiz_{quiz_id}"):
        answers = {}
        
        for i, q in enumerate(quiz["questions"]):
            st.markdown(f"**Question {i+1}:** {q['question']}")
            
            answer = st.radio(
                "Choose your answer:",
                options=q["options"],
                key=f"q_{quiz_id}_{i}",
                index=None
            )
            
            if answer is not None:
                answers[i] = q["options"].index(answer)
        
        submitted = st.form_submit_button("Submit Quiz")
        
        if submitted and len(answers) == len(quiz["questions"]):
            # Grade the quiz
            correct_count = 0
            total_questions = len(quiz["questions"])
            
            st.markdown("---")
            st.markdown("### 📊 Quiz Results:")
            
            for i, q in enumerate(quiz["questions"]):
                if i in answers:
                    is_correct = answers[i] == q["correct"]
                    if is_correct:
                        correct_count += 1
                        st.success(f"✅ Question {i+1}: Correct!")
                    else:
                        st.error(f"❌ Question {i+1}: Incorrect")
                        st.info(f"**Correct answer:** {q['options'][q['correct']]}")
                    
                    with st.expander(f"Explanation for Question {i+1}"):
                        st.markdown(q['explanation'])
            
            # Overall score
            score_pct = (correct_count / total_questions) * 100
            st.session_state.quiz_scores[quiz_id] = score_pct
            
            if score_pct >= 80:
                st.balloons()
                st.success(f"Outstanding! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            elif score_pct >= 60:
                st.success(f"Good work! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")
            else:
                st.warning(f"Keep studying! Score: {correct_count}/{total_questions} ({score_pct:.0f}%)")

def display_reflection_journal():
    """Display reflection journal for students to explore each branch"""
    
    st.markdown("# 📔 Philosophical Reflection Journal")
    st.markdown("Deepen your understanding by reflecting on each branch of philosophy.")
    
    tabs = st.tabs(["🤔 Metaphysics", "🧠 Epistemology", "⚖️ Ethics"])
    
    branches = ["metaphysics", "epistemology", "ethics"]
    prompts = {
        "metaphysics": [
            "What do you think is the most fundamental aspect of reality?",
            "Do you believe you have free will? Why or why not?",
            "What's your take on the mind-body problem?"
        ],
        "epistemology": [
            "How do you decide what to believe?", 
            "What's something you're absolutely certain about?",
            "How do you handle conflicting information?"
        ],
        "ethics": [
            "What's your most important moral principle?",
            "Describe a difficult ethical decision you've faced.",
            "How do you think we should treat future generations?"
        ]
    }
    
    for i, (tab, branch) in enumerate(zip(tabs, branches)):
        with tab:
            st.markdown(f"## Reflection on {branch.title()}")
            
            # Random prompt selector
            selected_prompt = st.selectbox(
                "Choose a reflection prompt:",
                prompts[branch],
                key=f"prompt_{branch}"
            )
            
            # Reflection text area
            reflection = st.text_area(
                f"Your thoughts on {branch}:",
                value=st.session_state.reflection_notes[branch],
                height=200,
                placeholder=f"Reflect on the prompt: {selected_prompt}",
                key=f"reflection_{branch}"
            )
            
            if st.button(f"Save Reflection", key=f"save_reflection_{branch}"):
                st.session_state.reflection_notes[branch] = reflection
                st.success("Reflection saved!")
            
            # Word count
            word_count = len(reflection.split()) if reflection else 0
            st.caption(f"Word count: {word_count}")

def sidebar_navigation() -> str:
    """Enhanced sidebar navigation"""
    
    st.sidebar.markdown("# 🌳 Three Branches of Philosophy")
    
    # Mode selection
    mode = st.sidebar.radio(
        "Choose Mode:",
        ["📚 Lesson Slides", "📝 Quizzes", "📔 Reflection Journal", "📖 Resources"]
    )
    
    if mode == "📚 Lesson Slides":
        st.sidebar.markdown("## Slide Navigation")
        
        # Slide selector
        slide_titles = [f"{i+1}. {slide['title']}" for i, slide in enumerate(SLIDES)]
        selected_slide = st.sidebar.selectbox(
            "Jump to slide:",
            options=range(len(SLIDES)),
            format_func=lambda x: slide_titles[x],
            index=st.session_state.current_slide
        )
        
        if selected_slide != st.session_state.current_slide:
            st.session_state.current_slide = selected_slide
        
        # Navigation buttons
        col1, col2 = st.sidebar.columns(2)
        with col1:
            if st.button("⬅️ Previous") and st.session_state.current_slide > 0:
                st.session_state.current_slide -= 1
                st.rerun()
        
        with col2:
            if st.button("Next ➡️") and st.session_state.current_slide < len(SLIDES) - 1:
                st.session_state.current_slide += 1
                st.rerun()
        
        # Progress
        progress = (st.session_state.current_slide + 1) / len(SLIDES)
        st.sidebar.progress(progress)
        st.sidebar.caption(f"Slide {st.session_state.current_slide + 1} of {len(SLIDES)}")
        
        # Presenter notes
        if st.sidebar.checkbox("📋 Show Presenter Notes"):
            current_slide = SLIDES[st.session_state.current_slide]
            st.sidebar.markdown("**Notes:**")
            st.sidebar.info(current_slide.get("presenter_notes", "No notes available."))
    
    elif mode == "📝 Quizzes":
        st.sidebar.markdown("## Quiz Selection")
        st.sidebar.markdown("Test your understanding of each branch:")
        
        for quiz_id, quiz in QUIZ_DATA.items():
            if quiz_id in st.session_state.quiz_scores:
                score = st.session_state.quiz_scores[quiz_id]
                st.sidebar.markdown(f"✅ {quiz['title']}: {score:.0f}%")
            else:
                st.sidebar.markdown(f"⏳ {quiz['title']}: Not taken")
    
    elif mode == "📔 Reflection Journal":
        st.sidebar.markdown("## Reflection Progress")
        
        for branch in ["metaphysics", "epistemology", "ethics"]:
            word_count = len(st.session_state.reflection_notes[branch].split()) if st.session_state.reflection_notes[branch] else 0
            if word_count > 0:
                st.sidebar.markdown(f"✅ {branch.title()}: {word_count} words")
            else:
                st.sidebar.markdown(f"⏳ {branch.title()}: Not started")
    
    return mode.split()[1].lower()

def display_resources():
    """Display learning resources"""
    
    st.markdown("# 📖 Learning Resources")
    st.markdown("Explore these resources to deepen your understanding of philosophy's three branches.")
    
    # Videos
    st.markdown("## 🎥 Videos")
    
    col1, col2 = st.columns(2)
    for i, video in enumerate(RESOURCES["videos"]):
        with col1 if i % 2 == 0 else col2:
            with st.container():
                st.markdown(f"### {video['title']}")
                st.markdown(f"{video['description']}")
                st.markdown(f"**Duration:** {video['duration']}")
                st.markdown(f"[Watch Now]({video['url']})")
                st.markdown("---")
    
    # Readings
    st.markdown("## 📚 Readings")
    
    for reading in RESOURCES["readings"]:
        st.markdown(f"- **[{reading['title']}]({reading['url']})** - {reading['description']}")
    
    # Additional practice
    st.markdown("## 🧠 Practice Activities")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Philosophical Scenarios")
        st.markdown("Try applying the three branches to these scenarios:")
        st.markdown("- The trolley problem")
        st.markdown("- Artificial intelligence consciousness")  
        st.markdown("- Time travel paradoxes")
        st.markdown("- Virtual reality ethics")
    
    with col2:
        st.markdown("### Discussion Questions")
        st.markdown("Great for group discussions:")
        st.markdown("- Can machines think?")
        st.markdown("- Is reality what we perceive?")
        st.markdown("- Do we have moral obligations to future people?")
        st.markdown("- What makes you 'you'?")

def main():
    """Main application function"""
    
    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main > div {
        padding-top: 2rem;
    }
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        border: none;
        background: linear-gradient(45deg, #4CAF50, #45a049);
        color: white;
        font-weight: bold;
    }
    .stButton > button:hover {
        background: linear-gradient(45deg, #45a049, #4CAF50);
        transform: translateY(-2px);
    }
    .philosophy-branch {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Determine current mode
    current_mode = sidebar_navigation()
    
    if current_mode == "lesson":
        # Display current slide
        current_slide = SLIDES[st.session_state.current_slide]
        display_slide(current_slide)
        
        # Navigation controls at bottom
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            if st.session_state.current_slide > 0:
                if st.button("⬅️ Previous Slide"):
                    st.session_state.current_slide -= 1
                    st.rerun()
        
        with col3:
            if st.session_state.current_slide < len(SLIDES) - 1:
                if st.button("Next Slide ➡️"):
                    st.session_state.current_slide += 1
                    st.rerun()
        
        with col2:
            # Progress indicator
            progress = (st.session_state.current_slide + 1) / len(SLIDES)
            st.progress(progress)
            st.caption(f"Slide {st.session_state.current_slide + 1} of {len(SLIDES)}")
    
    elif current_mode == "quizzes":
        st.markdown("# 📝 Test Your Knowledge")
        st.markdown("Take these quizzes to check your understanding of each philosophical branch.")
        
        # Quiz selection
        quiz_choice = st.selectbox(
            "Select a quiz:",
            list(QUIZ_DATA.keys()),
            format_func=lambda x: QUIZ_DATA[x]["title"]
        )
        
        display_quiz(quiz_choice)
        
        # Overall progress
        if st.session_state.quiz_scores:
            st.markdown("---")
            st.markdown("## Your Quiz Progress")
            
            for quiz_id, score in st.session_state.quiz_scores.items():
                quiz_title = QUIZ_DATA[quiz_id]["title"]
                if score >= 80:
                    st.success(f"✅ {quiz_title}: {score:.0f}% - Excellent!")
                elif score >= 60:
                    st.info(f"📚 {quiz_title}: {score:.0f}% - Good work!")
                else:
                    st.warning(f"📖 {quiz_title}: {score:.0f}% - Keep studying!")
    
    elif current_mode == "reflection":
        display_reflection_journal()
        
        # Export reflections
        if any(st.session_state.reflection_notes.values()):
            st.markdown("---")
            if st.button("💾 Export All Reflections"):
                export_data = {
                    'philosophical_reflections': st.session_state.reflection_notes,
                    'student_responses': st.session_state.student_responses,
                    'quiz_scores': st.session_state.quiz_scores,
                    'export_date': datetime.now().isoformat()
                }
                
                json_str = json.dumps(export_data, indent=2)
                st.download_button(
                    "Download Reflections",
                    json_str,
                    file_name=f"philosophy_reflections_{datetime.now().strftime('%Y%m%d')}.json",
                    mime="application/json"
                )
    
    elif current_mode == "resources":
        display_resources()

if __name__ == "__main__":
    main()
