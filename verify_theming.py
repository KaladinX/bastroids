import sys
import os

# Add the project directory to sys.path so we can import the modules
project_dir = "/home/kieran/projects/personal/learning/boots/bastroids"
sys.path.append(project_dir)

try:
    print("Attempting to import constants...")
    import constants
    print(f"TWILIGHT_BG: {constants.TWILIGHT_BG}")
    print(f"SILVER_GLAMOUR: {constants.SILVER_GLAMOUR}")
    print(f"ASTEROID_GREY: {constants.ASTEROID_GREY}")
    
    print("Attempting to import player...")
    import player
    
    print("Attempting to import asteroid...")
    import asteroid
    
    print("Attempting to import main...")
    import main
    
    print("All imports successful. Syntax check passed.")
except Exception as e:
    print(f"Verification failed: {e}")
    sys.exit(1)
