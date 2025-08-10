from flask import Flask, request, jsonify, send_from_directory, session
from events import create_event, update_event, delete_event, get_all_events
from guests import manage_guest, get_all_guests
from invitations import send_invitation, record_rsvp
from seating import create_seating_plan, select_seat, assign_seat_manually
from payments import process_payment, payment_status
from analytics import dashboard_overview, generate_report
from feedback import submit_feedback
from database import SessionLocal
from models import Event, Guest
from db_setup import init_db
from auth import create_user, authenticate_user, request_password_reset, verify_two_factor
from security import require_roles

app = Flask(__name__, static_url_path='', static_folder='.')
app.secret_key = "dev-secret"

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
@require_roles('admin', 'co-organizer')
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
@require_roles('admin', 'co-organizer')
def edit_event(event_id: int):
    """Update an existing event."""
    updated = update_event(event_id, **request.get_json(force=True))
    if not updated:
        return jsonify({'error': 'not found'}), 404
    return jsonify(updated)


@app.route('/api/events/<int:event_id>', methods=['DELETE'])
@require_roles('admin')
def remove_event(event_id: int):
    """Delete the specified event."""
    if not delete_event(event_id):
        return jsonify({'error': 'not found'}), 404
    return '', 204


@app.route('/api/guests', methods=['GET'])
@require_roles('admin', 'co-organizer')
def list_guests():
    """Return all guests."""
    return jsonify(get_all_guests())


@app.route('/api/guests', methods=['POST'])
@require_roles('admin', 'co-organizer')
def add_guest():
    """Add a guest."""
    data = request.get_json(force=True)
    gid = manage_guest(action='add',
                       name=data.get('name', ''),
                       email=data.get('email', ''),
                       category=data.get('category', ''),
                       event_id=data.get('event_id'))
    return jsonify({'id': gid}), 201


@app.route('/api/guests/<int:guest_id>', methods=['DELETE'])
@require_roles('admin')
def delete_guest(guest_id: int):
    """Delete a guest."""
    try:
        manage_guest(guest_id, action='delete')
        return '', 204
    except ValueError:
        return jsonify({'error': 'not found'}), 404


@app.route('/api/analytics', methods=['GET'])
@require_roles('admin', 'co-organizer')
def analytics_summary():
    """Simple analytics overview."""
    session = SessionLocal()
    event_count = session.query(Event).count()
    guest_count = session.query(Guest).count()
    session.close()
    return jsonify({'events': event_count, 'guests': guest_count})


@app.route('/api/invitations', methods=['POST'])
@require_roles('admin', 'co-organizer')
def api_send_invitation():
    data = request.get_json(force=True)
    if send_invitation(data['event_id'], data['email']):
        return jsonify({'status': 'sent'})
    return jsonify({'error': 'event not found'}), 404


@app.route('/api/rsvp', methods=['POST'])
def api_record_rsvp():
    data = request.get_json(force=True)
    record_rsvp(data['event_id'], data['guest_id'], data['response'])
    return jsonify({'status': 'recorded'})


@app.route('/api/seating/plan', methods=['POST'])
@require_roles('admin', 'co-organizer')
def api_create_plan():
    data = request.get_json(force=True)
    create_seating_plan(data['event_id'], data['seats'])
    return jsonify({'status': 'created'})


@app.route('/api/seating/select', methods=['POST'])
def api_select_seat():
    data = request.get_json(force=True)
    if select_seat(data['event_id'], data['guest_id'], data['seat_id']):
        return jsonify({'status': 'selected'})
    return jsonify({'error': 'unavailable'}), 400


@app.route('/api/seating/assign', methods=['POST'])
@require_roles('admin', 'co-organizer')
def api_assign_seat():
    data = request.get_json(force=True)
    if assign_seat_manually(data['event_id'], data['guest_id'], data['seat_id']):
        return jsonify({'status': 'assigned'})
    return jsonify({'error': 'invalid seat'}), 400


@app.route('/api/payments', methods=['POST'])
def api_process_payment():
    data = request.get_json(force=True)
    process_payment(data['guest_id'], data['event_id'], data['amount'], data.get('method', 'card'))
    return jsonify({'status': 'paid'})


@app.route('/api/payments/<int:guest_id>/<int:event_id>', methods=['GET'])
def api_payment_status(guest_id: int, event_id: int):
    return jsonify({'status': payment_status(guest_id, event_id)})


@app.route('/api/analytics/<int:event_id>', methods=['GET'])
@require_roles('admin', 'co-organizer')
def api_event_report(event_id: int):
    return jsonify(generate_report(event_id))


@app.route('/api/feedback', methods=['POST'])
def api_feedback():
    data = request.get_json(force=True)
    submit_feedback(data['event_id'], data['guest_id'], data['rating'], data.get('comment', ''))
    return jsonify({'status': 'received'})


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
        if otp and not verify_two_factor(otp):
            return jsonify({'error': 'invalid otp'}), 401
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
