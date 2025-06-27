# Ativa a venv Poetry no Bash
VENV_PATH=$(poetry env info --path)
source "$VENV_PATH/bin/activate"
