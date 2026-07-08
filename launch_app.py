import os
import subprocess
import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / 'network status.html'

if not HTML_FILE.exists():
    raise SystemExit(f'The dashboard file was not found: {HTML_FILE}')

try:
    if sys.platform.startswith('win'):
        os.startfile(str(HTML_FILE))
    elif sys.platform.startswith('darwin'):
        subprocess.Popen(['open', str(HTML_FILE)])
    else:
        subprocess.Popen(['xdg-open', str(HTML_FILE)])
except Exception as exc:
    raise SystemExit(f'Could not open the dashboard: {exc}')
