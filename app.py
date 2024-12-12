from flask import Flask, render_template, request, redirect, url_for
from src.reactor_manager import ReactorManager
from src.reactor import Reactor

app = Flask(__name__)

reactor_manager = ReactorManager()


@app.route('/')
def index():
    reactors = reactor_manager.get_all_reactors_with_recommendations()
    return render_template('index.html', reactors=reactors)


@app.route('/add_reactor', methods=['GET', 'POST'])
def add_reactor():
    if request.method == 'POST':
        name = request.form['name']
        power_output = float(request.form['power_output'])
        temperature = float(request.form['temperature'])
        pressure = float(request.form['pressure'])
        new_reactor = Reactor(name, power_output, temperature, pressure)
        reactor_manager.add_reactor(new_reactor)
        return redirect(url_for('index'))
    return render_template('add_reactor.html')


@app.route('/update_reactor/<name>', methods=['GET', 'POST'])
def update_reactor(name):
    reactor = reactor_manager.find_reactor_by_name(name)
    if reactor is None:
        return "Reactor not found", 404
    if request.method == 'POST':
        reactor.update_status(
            power_output=float(request.form['power_output']),
            temperature=float(request.form['temperature']),
            pressure=float(request.form['pressure'])
        )
        return redirect(url_for('index'))
    return render_template('update_reactor.html', reactor=reactor)


if __name__ == '__main__':
    app.run(debug=True)
