import json
from datetime import datetime

class LuizNogueira:
    def __init__(self):
        self.username = "LuiizNogueira"
        self.role = "Fullstack & Mobile Engineer"
        self.languages = ["Python", "TypeScript", "JavaScript", "SQL"]
        self.frameworks = ["React Native", "Node.js", "Express", "FastAPI"]
        self.databases = ["MySQL", "PostgreSQL"]
        self.tools = ["Git", "Docker", "Linux", "VS Code"]
        self.philosophy = "Clean Code & apps mobile escaláveis"

    def get_status(self):
        now = datetime.now().strftime("%d/%m/%Y às %H:%M")
        return {
            "status": "Online & Coding 🚀",
            "coffee_level": "100%",
            "current_focus": "Performance mobile & integrações de backend",
            "last_updated": now
        }

def update_readme():
    me = LuizNogueira()
    status = me.get_status()
    
    output_markdown = f"""```json
{json.dumps(status, indent=4, ensure_ascii=False)}
```"""

    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()

    start_tag = "<!--PYTHON_STATUS_START-->"
    end_tag = "<!--PYTHON_STATUS_END-->"
    
    start_pos = content.find(start_tag) + len(start_tag)
    end_pos = content.find(end_tag)

    if start_pos != -1 and end_pos != -1:
        new_content = content[:start_pos] + "\n" + output_markdown + "\n" + content[end_pos:]
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new_content)
        print("README atualizado com sucesso via Python!")

if __name__ == "__main__":
    update_readme()
