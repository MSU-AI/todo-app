from flask import Flask, render_template, request, redirect, url_for
from main import AIIntegratedTODO

app = Flask(__name__)
todo = AIIntegratedTODO()

@app.route('/', methods=['GET', 'POST'])
def home():
    actions = ['add', 'begin', 'end', 'pause', 'resume', 'suggest', 'exit']
    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add':
            new_task = request.form.get('new_task')
            todo.add_task(new_task)
        elif action in ['begin', 'end', 'pause', 'resume', 'suggest']:
            # Call the corresponding function in main.py
            getattr(todo, action)()
        elif action == 'exit':
            return redirect(url_for('exit'))  # Assuming you have an 'exit' route
        return redirect(url_for('home'))

    tasks = todo.get_tasks()
    return render_template('todo.html', tasks=tasks, actions=actions)

@app.route('/exit', methods=['GET'])
def exit():
    return "Thank you for using our application. Goodbye!"

if __name__ == '__main__':
    app.run(debug=True)