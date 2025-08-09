from flask import Flask, request, jsonify, send_from_directory
from events import create_event, update_event, delete_event
from data_store import events

app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')


@app.route('/api/events', methods=['GET'])
def list_events():
    """Return all events."""
    return jsonify(events)


@app.route('/api/events', methods=['POST'])
def add_event():
    """Create an event from posted JSON."""
    data = request.get_json(force=True)
    event_id = create_event(
        data.get('name', ''),
        data.get('date', ''),
        data.get('time', ''),
        data.get('location', ''),
        float(data.get('price', 0)),
        data.get('program', [])
    )
    return jsonify({'id': event_id}), 201


@app.route('/api/events/<int:event_id>', methods=['PUT'])
def edit_event(event_id: int):
    """Update an existing event."""
    if not update_event(event_id, **request.get_json(force=True)):
        return jsonify({'error': 'not found'}), 404
    return jsonify(events[event_id])


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def remove_event(event_id: int):
    """Delete the specified event."""
    if not delete_event(event_id):
        return jsonify({'error': 'not found'}), 404
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
