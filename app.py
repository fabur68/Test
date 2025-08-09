from flask import Flask, request, jsonify, send_from_directory

from data_store import init_db
from events import create_event, update_event, delete_event, list_events
from guests import manage_guest, list_guests

app = Flask(__name__, static_url_path='', static_folder='.')


@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')


@app.route('/api/events', methods=['GET'])
def list_events_route():
    """Return all events."""
    return jsonify(list_events())


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
        data.get('program', []),
    )
    return jsonify({'id': event_id}), 201


@app.route('/api/events/<int:event_id>', methods=['PUT'])
def edit_event(event_id: int):
    """Update an existing event."""
    if not update_event(event_id, **request.get_json(force=True)):
        return jsonify({'error': 'not found'}), 404
    return jsonify(list_events().get(event_id))


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def remove_event(event_id: int):
    """Delete the specified event."""
    if not delete_event(event_id):
        return jsonify({'error': 'not found'}), 404
    return '', 204


@app.route('/api/guests', methods=['GET'])
def list_guests_route():
    """Return all guests."""
    return jsonify(list_guests())


@app.route('/api/guests', methods=['POST'])
def add_guest():
    """Add a guest."""
    data = request.get_json(force=True)
    gid = manage_guest(
        action='add',
        name=data.get('name', ''),
        email=data.get('email', ''),
        category=data.get('category', ''),
    )
    return jsonify({'id': gid}), 201


@app.route('/api/guests/<int:guest_id>', methods=['DELETE'])
def delete_guest(guest_id: int):
    """Delete a guest."""
    try:
        manage_guest(guest_id, action='delete')
        return '', 204
    except ValueError:
        return jsonify({'error': 'not found'}), 404


@app.route('/api/analytics', methods=['GET'])
def analytics_summary():
    """Simple analytics overview."""
    return jsonify({'events': len(list_events()), 'guests': len(list_guests())})


if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=8080)

