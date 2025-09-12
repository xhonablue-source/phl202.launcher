#!/usr/bin/env python3
"""
Philosophy Cognitive Cloud Launcher Generator
Developed for Xavier Honablue M.Ed.
"""

def generate_launcher_html():
    """Generate the HTML content for the Philosophy Cognitive Cloud launcher page."""
    
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Philosophy Cognitive Cloud - Xavier Honablue M.Ed.</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
            min-height: 100vh;
            color: #333;
            overflow-x: hidden;
        }

        .background-pattern {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            opacity: 0.1;
            background-image: radial-gradient(circle at 25% 25%, #ffffff 2px, transparent 2px);
            background-size: 50px 50px;
            pointer-events: none;
        }

        .container {
            position: relative;
            z-index: 1;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 2rem;
        }

        .main-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 25px;
            padding: 3rem;
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
            max-width: 1000px;
            width: 100%;
            backdrop-filter: blur(15px);
            border: 1px solid rgba(255, 255, 255, 0.3);
            animation: fadeInUp 0.8s ease-out;
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header {
            text-align: center;
            margin-bottom: 3rem;
        }

        .main-title {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(135deg, #1e3c72, #2a5298, #667eea);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
            text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .subtitle {
            font-size: 1.4rem;
            color: #666;
            margin-bottom: 1rem;
            font-weight: 300;
        }

        .developer-credit {
            font-size: 1.1rem;
            color: #888;
            font-style: italic;
            font-weight: 500;
        }

        .description {
            text-align: center;
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 3rem;
            line-height: 1.7;
            max-width: 800px;
            margin-left: auto;
            margin-right: auto;
        }

        .activities-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2rem;
            margin-bottom: 3rem;
        }

        .activity-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 20px;
            padding: 2.5rem;
            text-decoration: none;
            color: white;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
            position: relative;
            overflow: hidden;
        }

        .activity-card.phl101 {
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        }

        .activity-card.phl202 {
            background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        }

        .activity-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(255, 255, 255, 0.1);
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .activity-card:hover {
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.25);
        }

        .activity-card:hover::before {
            opacity: 1;
        }

        .activity-number {
            font-size: 1.1rem;
            font-weight: 600;
            opacity: 0.9;
            margin-bottom: 0.5rem;
            position: relative;
            z-index: 1;
        }

        .activity-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
            position: relative;
            z-index: 1;
            line-height: 1.3;
        }

        .activity-description {
            font-size: 1rem;
            opacity: 0.95;
            line-height: 1.6;
            margin-bottom: 1.5rem;
            position: relative;
            z-index: 1;
        }

        .launch-button {
            display: inline-flex;
            align-items: center;
            background: rgba(255, 255, 255, 0.2);
            padding: 0.8rem 1.5rem;
            border-radius: 30px;
            font-size: 0.95rem;
            font-weight: 600;
            text-decoration: none;
            color: white;
            transition: all 0.3s ease;
            position: relative;
            z-index: 1;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        .launch-button:hover {
            background: rgba(255, 255, 255, 0.3);
            transform: translateX(5px);
        }

        .launch-button::after {
            content: '→';
            margin-left: 0.5rem;
            transition: transform 0.3s ease;
        }

        .launch-button:hover::after {
            transform: translateX(3px);
        }

        .features-section {
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
        }

        .features-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 600;
            color: #444;
            margin-bottom: 2rem;
        }

        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .feature-item {
            text-align: center;
            padding: 1.5rem;
            background: rgba(102, 126, 234, 0.05);
            border-radius: 15px;
            border: 1px solid rgba(102, 126, 234, 0.1);
        }

        .feature-icon {
            font-size: 2rem;
            margin-bottom: 1rem;
        }

        .feature-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #444;
            margin-bottom: 0.5rem;
        }

        .feature-description {
            font-size: 0.95rem;
            color: #666;
            line-height: 1.4;
        }

        .footer {
            text-align: center;
            margin-top: 3rem;
            padding-top: 2rem;
            border-top: 1px solid rgba(0, 0, 0, 0.1);
            color: #888;
            font-size: 0.9rem;
        }

        @media (max-width: 768px) {
            .main-card {
                padding: 2rem;
                margin: 1rem;
            }
            
            .main-title {
                font-size: 2.2rem;
            }
            
            .activities-grid {
                grid-template-columns: 1fr;
            }
            
            .activity-card {
                padding: 2rem;
            }
            
            .features-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <div class="background-pattern"></div>
    
    <div class="container">
        <div class="main-card">
            <div class="header">
                <h1 class="main-title">Philosophy Cognitive Cloud</h1>
                <p class="subtitle">Interactive Philosophy Education Platform</p>
                <p class="developer-credit">Developed by Xavier Honablue, M.Ed.</p>
            </div>

            <div class="description">
                Welcome to an innovative approach to philosophical learning. Our cognitive cloud platform combines traditional philosophical inquiry with modern interactive technology to create engaging, thought-provoking educational experiences.
            </div>

            <div class="activities-grid">
                <a href="https://philosophy-101-day1.streamlit.app/" class="activity-card phl101" target="_blank">
                    <div class="activity-number">PHL 101</div>
                    <h2 class="activity-title">What is Religion? What is Philosophy?</h2>
                    <p class="activity-description">
                        Explore fundamental questions about the nature of philosophy and religion. This interactive activity examines the foundations of philosophical thinking and the relationship between faith and reason.
                    </p>
                    <div class="launch-button">Launch Activity</div>
                </a>

                <a href="https://logic1-phl202.streamlit.app/" class="activity-card phl202" target="_blank">
                    <div class="activity-number">PHL 202</div>
                    <h2 class="activity-title">Logic & Cognitive Analysis</h2>
                    <p class="activity-description">
                        Dive deep into logical reasoning, critical thinking, and cognitive processes. This advanced activity uses interactive tools to help students master formal and informal logic principles.
                    </p>
                    <div class="launch-button">Launch Activity</div>
                </a>
            </div>

            <div class="features-section">
                <h3 class="features-title">Platform Features</h3>
                <div class="features-grid">
                    <div class="feature-item">
                        <div class="feature-icon">🎯</div>
                        <h4 class="feature-title">Interactive Learning</h4>
                        <p class="feature-description">Engage with philosophical concepts through dynamic, hands-on exercises and simulations</p>
                    </div>
                    <div class="feature-item">
                        <div class="feature-icon">🧠</div>
                        <h4 class="feature-title">Cognitive Enhancement</h4>
                        <p class="feature-description">Develop critical thinking skills through structured philosophical analysis</p>
                    </div>
                    <div class="feature-item">
                        <div class="feature-icon">🌐</div>
                        <h4 class="feature-title">Cloud-Based Access</h4>
                        <p class="feature-description">Learn anywhere, anytime with our accessible web-based platform</p>
                    </div>
                    <div class="feature-item">
                        <div class="feature-icon">📚</div>
                        <h4 class="feature-title">Comprehensive Curriculum</h4>
                        <p class="feature-description">From introductory concepts to advanced logical analysis</p>
                    </div>
                </div>
            </div>

            <div class="footer">
                <p>&copy; 2025 Philosophy Cognitive Cloud | Xavier Honablue, M.Ed. | Educational Innovation in Philosophy</p>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    return html_content

def save_launcher_page(filename="philosophy_launcher.html"):
    """Save the launcher page to an HTML file."""
    html_content = generate_launcher_html()
    
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        print(f"✅ Launcher page saved successfully as '{filename}'")
        print(f"🚀 Open the file in your web browser to view the launcher")
        return True
    except Exception as e:
        print(f"❌ Error saving file: {e}")
        return False

def add_activity(activity_data):
    """
    Add a new activity to the launcher.
    
    Args:
        activity_data (dict): Dictionary containing:
            - 'code': Activity code (e.g., 'PHL301')
            - 'title': Activity title
            - 'description': Activity description
            - 'url': Streamlit app URL
            - 'gradient': CSS gradient colors (optional)
    """
    # This function can be extended to dynamically add new activities
    # For now, it serves as a template for future expansion
    pass

def main():
    """Main function to generate and save the launcher page."""
    print("🎓 Philosophy Cognitive Cloud Launcher Generator")
    print("=" * 50)
    print("Developed for Xavier Honablue M.Ed.")
    print()
    
    # Generate and save the launcher page
    success = save_launcher_page()
    
    if success:
        print()
        print("📋 Current Activities:")
        print("• PHL 101: What is Religion? What is Philosophy?")
        print("• PHL 202: Logic & Cognitive Analysis")
        print()
        print("🔧 To customize:")
        print("• Edit the HTML content in generate_launcher_html()")
        print("• Modify URLs, titles, or descriptions as needed")
        print("• Add new activities using the activity template")

if __name__ == "__main__":
    main()
