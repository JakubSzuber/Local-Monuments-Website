# This file is used to start the application by importing the app variable from main_python_files and running it on host 0.0.0.0 and port 5000.
# It uses the if __name__ == "__main__": guard to ensure the code within the block only runs when the script is run directly.

from main_python_files import app

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
