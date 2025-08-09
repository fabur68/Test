"""In-memory data storage for the event management tool."""

# Event data keyed by event_id
events = {}

# Guest data keyed by guest_id
# Each guest is a dict with keys: name, email, category
guests = {}

# RSVP responses keyed by (event_id, guest_id)
rsvps = {}

# Seating plans keyed by event_id, values are dict seat_id -> guest_id
seating_plans = {}

# Payments keyed by guest_id
# value: dict(event_id -> status)
payments = {}

# Feedback keyed by (event_id, guest_id)
feedback = {}

# Offline cache keyed by user_id
offline_cache = {}
