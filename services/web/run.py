from main_python_files import app
import os
# mozliwe ze bedzie mozna biblioteke os usunac

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
# usunalem, mam nadzieje ze nic nie zmieni: debug=os.environ.get('DEBUG') == 1
