from Loan_Flaskapp import create_app
import os
venv_path = os.path.join(os.getcwd(), 'venv')
activate_path = os.path.join(venv_path, 'Scripts', 'activate.bat')

# Activate the virtual environment
os.system(f'call {activate_path}')

app = create_app()

if __name__=='__main__':
    app.run(debug=True)
