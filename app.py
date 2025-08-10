from flask import Flask, request, jsonify, send_from_directory
from events import create_event, update_event, delete_event, get_all_events
from guests import manage_guest, get_all_guests
from database import SessionLocal
from models import Event, Guest
from db_setup import init_db

app = Flask(__name__, static_url_path='', static_folder='.')

# Ensure database tables exist on startup
init_db()


@app.route('/')
def index():
    """Serve the main HTML page."""
    return send_from_directory('.', 'index.html')


@app.route('/api/events', methods=['GET'])
def list_events():
    """Return all events."""
    return jsonify(get_all_events())


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
    updated = update_event(event_id, **request.get_json(force=True))
    if not updated:
        return jsonify({'error': 'not found'}), 404
    return jsonify(updated)


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
def remove_event(event_id: int):
    """Delete the specified event."""
    if not delete_event(event_id):
        return jsonify({'error': 'not found'}), 404
    return '', 204


@app.route('/api/guests', methods=['GET'])
def list_guests():
    """Return all guests."""
    return jsonify(get_all_guests())


@app.route('/api/guests', methods=['POST'])
def add_guest():
    """Add a guest."""
    data = request.get_json(force=True)
    gid = manage_guest(action='add',
                       name=data.get('name', ''),
                       email=data.get('email', ''),
                       category=data.get('category', ''))
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
    session = SessionLocal()
    event_count = session.query(Event).count()
    guest_count = session.query(Guest).count()
    session.close()
    return jsonify({'events': event_count, 'guests': guest_count})


if __name__ == '__main__':
    app.run(debug=True)
