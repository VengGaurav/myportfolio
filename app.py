from flask import Flask, render_template, send_from_directory
import requests
import os

app = Flask(__name__)

def fetch_github_repos():
    """
    Fetch public, non-fork, non-archived repositories for your GitHub account.
    Uses $GITHUB_TOKEN env variable if set (needed for Render/cloud hosting!).
    """
    try:
        url = "https://api.github.com/users/VengGaurav/repos"
        headers = {}
        token = os.environ.get("GITHUB_TOKEN")
        if token:
            headers["Authorization"] = f"token {token}"
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            repos = response.json()
            filtered_repos = []
            for repo in repos:
                if not repo['fork'] and not repo['archived']:
                    filtered_repos.append({
                        'name': repo['name'],
                        'description': repo['description'] or f"{repo['name'].replace('-', ' ').title()} project",
                        'language': repo['language'],
                        'url': repo['html_url'],
                        'updated': repo['updated_at'][:10]
                    })
            return filtered_repos
        else:
            print("GitHub API Error:", response.status_code, response.json())
            return []
    except Exception as e:
        print(f"Error fetching GitHub repos: {e}")
        return []

@app.route('/')
def index():
    repos = fetch_github_repos()
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
        repo['icon'] = icon_map.get(repo['language'], 'fas fa-code')
    return render_template('index.html', repos=repos)

@app.route('/resume')
def resume():
    resume_folder = os.path.join(os.path.dirname(__file__), 'resume')
    return send_from_directory(resume_folder, 'gaurav_resume.pdf')

if __name__ == '__main__':
    # On Render, $PORT is auto-set; locally Flask defaults to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
