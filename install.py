import os
import subprocess
import sys
from pathlib import Path

def create_venv():
    print("📦 Creating virtual environment...")
    subprocess.run([sys.executable, "-m", "venv", "venv"])

def activate_venv_command():
    if os.name == "nt":
        return ".\\venv\\Scripts\\activate"
    else:
        return "source venv/bin/activate"

def install_requirements():
    print("⬇️ Installing dependencies...")
    pip = Path("venv") / ("Scripts" if os.name == "nt" else "bin") / "pip"
    subprocess.run([str(pip), "install", "--upgrade", "pip"])
    subprocess.run([str(pip), "install", "-r", "requirements.txt"])

def create_env_file():
    if not Path(".env").exists():
        print("⚙️ Creating .env file...")
        with open(".env", "w") as f:
            f.write("DB_NAME=default_db\n")
            f.write("DB_USER=admin\n")
            f.write("DB_PASSWORD=admin123\n")

def main():
    create_venv()
    install_requirements()
    create_env_file()
    print("✅ Setup complete!")
    print(f"🔧 To activate the virtual environment, run: {activate_venv_command()}")

if __name__ == "__main__":
    main()
