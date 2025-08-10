<<<<<<< HEAD
from flask import Flask, request, jsonify, send_from_directory, session
=======
from flask import Flask, request, jsonify, send_from_directory
>>>>>>> main
from events import create_event, update_event, delete_event, get_all_events
from guests import manage_guest, get_all_guests
from database import SessionLocal
from models import Event, Guest
from db_setup import init_db
<<<<<<< HEAD
from auth import create_user, authenticate_user, request_password_reset, verify_two_factor
from security import require_roles

app = Flask(__name__, static_url_path='', static_folder='.')
app.secret_key = "dev-secret"
=======

app = Flask(__name__, static_url_path='', static_folder='.')
>>>>>>> main

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
<<<<<<< HEAD
@require_roles('admin', 'co-organizer')
=======
>>>>>>> main
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
<<<<<<< HEAD
@require_roles('admin', 'co-organizer')
=======
>>>>>>> main
def edit_event(event_id: int):
    """Update an existing event."""
    updated = update_event(event_id, **request.get_json(force=True))
    if not updated:
        return jsonify({'error': 'not found'}), 404
    return jsonify(updated)


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
<<<<<<< HEAD
@require_roles('admin')
=======
>>>>>>> main
def remove_event(event_id: int):
    """Delete the specified event."""
    if not delete_event(event_id):
        return jsonify({'error': 'not found'}), 404
    return '', 204


@app.route('/api/guests', methods=['GET'])
<<<<<<< HEAD
@require_roles('admin', 'co-organizer')
=======
>>>>>>> main
def list_guests():
    """Return all guests."""
    return jsonify(get_all_guests())


@app.route('/api/guests', methods=['POST'])
<<<<<<< HEAD
@require_roles('admin', 'co-organizer')
=======
>>>>>>> main
def add_guest():
    """Add a guest."""
    data = request.get_json(force=True)
    gid = manage_guest(action='add',
                       name=data.get('name', ''),
                       email=data.get('email', ''),
<<<<<<< HEAD
                       category=data.get('category', ''),
                       event_id=data.get('event_id'))
=======
                       category=data.get('category', ''))
>>>>>>> main
    return jsonify({'id': gid}), 201


@app.route('/api/guests/<int:guest_id>', methods=['DELETE'])
<<<<<<< HEAD
@require_roles('admin')
=======
>>>>>>> main
def delete_guest(guest_id: int):
    """Delete a guest."""
    try:
        manage_guest(guest_id, action='delete')
        return '', 204
    except ValueError:
        return jsonify({'error': 'not found'}), 404


@app.route('/api/analytics', methods=['GET'])
<<<<<<< HEAD
@require_roles('admin', 'co-organizer')
=======
>>>>>>> main
def analytics_summary():
    """Simple analytics overview."""
    session = SessionLocal()
    event_count = session.query(Event).count()
    guest_count = session.query(Guest).count()
    session.close()
    return jsonify({'events': event_count, 'guests': guest_count})


<<<<<<< HEAD
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json(force=True)
    uid = create_user(data['email'], data['password'], data.get('role', 'guest'))
    return jsonify({'id': uid}), 201


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    user = authenticate_user(data['email'], data['password'])
    if not user:
        return jsonify({'error': 'invalid credentials'}), 401
    if user.role == 'admin':
        otp = data.get('otp')
        if not otp or not verify_two_factor(otp):
            return jsonify({'error': '2fa required'}), 401
    session['user_id'] = user.id
    session['role'] = user.role
    return jsonify({'message': 'logged in'})


@app.route('/api/password-reset', methods=['POST'])
def password_reset():
    data = request.get_json(force=True)
    if request_password_reset(data['email']):
        return jsonify({'message': 'reset sent'})
    return jsonify({'error': 'not found'}), 404


@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'message': 'logged out'})


=======
>>>>>>> main
if __name__ == '__main__':
    app.run(debug=True)
