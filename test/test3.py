from pathlib import Path
script_path = Path(__file__).resolve()
script_dir = script_path.parent
path = str(script_dir)+ "/jeudupendufb.jpg"
f = open(path)