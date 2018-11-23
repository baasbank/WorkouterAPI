from flask import Flask, jsonify

app = Flask(__name__)

workout_history = [
  {
    'Exercise': 'Dumbbell Row',
    'Weight': '50kg',
    'Reps': 10,
    'Rest': 2
  },
  {
    'Exercise': 'Deadlift',
    'Weight': '100kg',
    'Reps': 10,
    'Rest': 2
  }
]

@app.route('/history')
def get_history():
  return jsonify({'history': workout_history})

app.run(port=8000)