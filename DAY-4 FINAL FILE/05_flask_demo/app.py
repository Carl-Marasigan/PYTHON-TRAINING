from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret"

# In-memory task list (for demonstration purposes)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.post('/add')
def add_task():
    task_content = request.form.get('task_content')
    if task_content:
        tasks.append(task_content)
        flash('Task added successfully!', 'success')
    else:
        flash('Task cannot be empty_package!', 'danger')
    return redirect(url_for('index'))

@app.post('/delete/<int:task_id>')
def delete_task(task_id):
    try:
        tasks.pop(task_id)
        flash('Task deleted successfully!', 'success')
    except IndexError:
        flash('Task not found!', 'danger')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
