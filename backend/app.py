from flask import Flask, render_template, send_from_directory, jsonify
import requests
import os

# Set template_folder and static_folder to parent directories
app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '../templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '../static')
)

def fetch_github_repos():
    """Fetch repositories from GitHub API"""
    try:
        url = "https://api.github.com/users/VengGaurav/repos"
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()
            formatted_repos = []
            for repo in repos:
                if not repo['fork'] and not repo['archived']:
                    formatted_repos.append({
                        'name': repo['name'],
                        'description': repo['description'] or f"{repo['name'].replace('-', ' ').title()} project",
                        'language': repo['language'],
                        'url': repo['html_url'],
                        'updated': repo['updated_at'][:10]
                    })
            return formatted_repos
        else:
            return []
    except Exception as e:
        print(f"Error fetching GitHub repos: {e}")
        return []

@app.route('/')
def index():
    repos = fetch_github_repos()
    # Read the template and inject dynamic projects
    with open(os.path.join(app.template_folder, 'index.html'), 'r', encoding='utf-8') as f:
        template = f.read()
    projects_html = ""
    icon_map = {
        'Python': 'fab fa-python',
        'JavaScript': 'fab fa-js-square',
        'HTML': 'fab fa-html5',
        'CSS': 'fab fa-css3-alt',
        'Java': 'fab fa-java',
        'C++': 'fas fa-code',
        'C': 'fas fa-code',
        'C#': 'fas fa-code',
        'PHP': 'fab fa-php',
        'Ruby': 'fas fa-gem',
        'Go': 'fas fa-code',
        'Rust': 'fas fa-code',
        'Swift': 'fab fa-swift',
        'Kotlin': 'fas fa-code',
        'TypeScript': 'fab fa-js-square',
        'Vue': 'fab fa-vuejs',
        'React': 'fab fa-react',
        'Angular': 'fab fa-angular'
    }
    for repo in repos:
        icon = icon_map.get(repo['language'], 'fas fa-code')
        projects_html += f'''
            <li>
                <i class="{icon}"></i> 
                <a href="{repo['url']}" target="_blank" class="project-link">
                    {repo['name'].replace('-', ' ').title()} - {repo['description']}
                </a>
                <span class="project-lang">{repo['language']}</span>
            </li>
        '''
    template = template.replace(
        '<ul>\n            <li><i class="fas fa-film"></i> Movie Recommender - AI-powered movie recommendation system with Netflix-style UI (Flask, TMDB API)</li>\n            <li><i class="fas fa-gavel"></i> Court Case Fetcher - Flask web app to fetch & store court case info with SQLite</li>\n            <li><i class="fas fa-clock"></i> Pomodoro Timer - Productivity timer application built with JavaScript</li>\n            <li><i class="fas fa-globe"></i> Portfolio Website - This responsive portfolio built with Flask and modern CSS</li>\n        </ul>',
        f'<ul id="dynamic-projects">\n            {projects_html}\n        </ul>'
    )
    return template

@app.route('/resume')
def get_resume():
    # Serve the resume PDF from the resume directory
    resume_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../resume'))
    return send_from_directory(resume_dir, 'gaurav_resume.pdf')

@app.route('/api/repos')
def api_repos():
    repos = fetch_github_repos()
    return jsonify(repos)

if __name__ == '__main__':
    app.run(debug=True)
