import streamlit as st
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
import time

# Page configuration
st.set_page_config(
    page_title="Kids Credit Tracker",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        text-align: center;
        color: #667eea;
        font-size: 3em;
        margin-bottom: 10px;
    }
    .balance-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 30px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
    }
    .balance-value {
        font-size: 3em;
        font-weight: bold;
        margin: 10px 0;
    }
    .timer-display {
        font-size: 2.5em;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        border-radius: 10px;
        background: #f8f9fa;
        margin: 10px 0;
        font-family: 'Courier New', monospace;
    }
    .timer-active {
        background: #ffe6e6;
        color: #e74c3c;
        animation: pulse 1s infinite;
    }
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    .activity-card {
        padding: 20px;
        border-radius: 15px;
        margin: 10px 0;
    }
    .earn-card {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
    }
    .spend-card {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
    }
    .history-item {
        padding: 15px;
        margin: 5px 0;
        border-radius: 10px;
        background: #f8f9fa;
    }
    .history-earn {
        border-left: 4px solid #2ecc71;
    }
    .history-spend {
        border-left: 4px solid #e74c3c;
    }
    div[data-testid="stButton"] button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Data file path
DATA_FILE = Path("credit_data.json")

# Activity definitions
ACTIVITIES = {
    'study': {'type': 'earn', 'label': 'Study', 'emoji': '📚'},
    'practice': {'type': 'earn', 'label': 'Practice', 'emoji': '🎵'},
    'cleaning': {'type': 'earn', 'label': 'Cleaning', 'emoji': '🧹'},
    'tv': {'type': 'spend', 'label': 'TV/Tablet', 'emoji': '📺'},
    'game': {'type': 'spend', 'label': 'Game', 'emoji': '🎮'}
}

# Initialize session state
def init_session_state():
    if 'balance' not in st.session_state:
        st.session_state.balance = 0
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'active_timers' not in st.session_state:
        st.session_state.active_timers = {}
    if 'initialized' not in st.session_state:
        load_data()
        st.session_state.initialized = True

# Save data to JSON
def save_data():
    data = {
        'balance': st.session_state.balance,
        'history': st.session_state.history,
        'active_timers': {
            activity: {
                'start_time': timer['start_time'].isoformat(),
                'type': timer['type']
            }
            for activity, timer in st.session_state.active_timers.items()
        }
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Load data from JSON
def load_data():
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            st.session_state.balance = data.get('balance', 0)
            st.session_state.history = data.get('history', [])

            # Restore active timers (only if recent - within 1 hour)
            active_timers = data.get('active_timers', {})
            for activity, timer_data in active_timers.items():
                start_time = datetime.fromisoformat(timer_data['start_time'])
                if datetime.now() - start_time < timedelta(hours=1):
                    st.session_state.active_timers[activity] = {
                        'start_time': start_time,
                        'type': timer_data['type']
                    }
        except Exception as e:
            st.error(f"Error loading data: {e}")

# Format seconds to HH:MM:SS or MM:SS
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

# Calculate elapsed time for active timer
def get_elapsed_time(activity):
    if activity in st.session_state.active_timers:
        start_time = st.session_state.active_timers[activity]['start_time']
        elapsed = (datetime.now() - start_time).total_seconds()
        return int(elapsed)
    return 0

# Start timer
def start_timer(activity):
    activity_type = ACTIVITIES[activity]['type']

    # Check if already running
    if activity in st.session_state.active_timers:
        st.warning(f"{ACTIVITIES[activity]['label']} timer is already running!")
        return

    # For spend activities, check balance
    if activity_type == 'spend' and st.session_state.balance <= 0:
        st.error("Not enough credits! Earn more credits first.")
        return

    # Start timer
    st.session_state.active_timers[activity] = {
        'start_time': datetime.now(),
        'type': activity_type
    }
    save_data()
    st.rerun()

# Stop timer
def stop_timer(activity):
    if activity not in st.session_state.active_timers:
        return

    # Calculate elapsed time
    elapsed = get_elapsed_time(activity)

    if elapsed < 1:
        st.warning("Timer was running for less than a second!")
        del st.session_state.active_timers[activity]
        save_data()
        return

    activity_type = st.session_state.active_timers[activity]['type']

    # Update balance
    if activity_type == 'earn':
        st.session_state.balance += elapsed
    else:
        st.session_state.balance -= elapsed
        if st.session_state.balance < 0:
            st.session_state.balance = 0

    # Add to history
    st.session_state.history.insert(0, {
        'activity': activity,
        'duration': elapsed,
        'type': activity_type,
        'timestamp': datetime.now().isoformat()
    })

    # Remove from active timers
    del st.session_state.active_timers[activity]

    save_data()
    st.rerun()

# Clear history
def clear_history():
    st.session_state.history = []
    save_data()
    st.rerun()

# Main app
def main():
    init_session_state()

    # Header
    st.markdown('<h1 class="main-header">🌟 Kids Credit Tracker 🌟</h1>', unsafe_allow_html=True)

    # Balance display
    balance_display = format_time(st.session_state.balance)
    st.markdown(f"""
    <div class="balance-box">
        <div style="font-size: 1.2em;">Credit Balance</div>
        <div class="balance-value">{balance_display}</div>
        <div style="font-size: 0.9em;">(hours:minutes:seconds)</div>
    </div>
    """, unsafe_allow_html=True)

    # Earn Credits Section
    st.markdown("## 💪 Earn Credits")
    earn_cols = st.columns(3)

    for idx, (activity, info) in enumerate([item for item in ACTIVITIES.items() if item[1]['type'] == 'earn']):
        with earn_cols[idx]:
            st.markdown(f'<div class="activity-card earn-card">', unsafe_allow_html=True)
            st.markdown(f"### {info['emoji']} {info['label']}")

            # Timer display
            is_active = activity in st.session_state.active_timers
            elapsed = get_elapsed_time(activity) if is_active else 0
            timer_class = "timer-display timer-active" if is_active else "timer-display"
            st.markdown(f'<div class="{timer_class}">{format_time(elapsed)}</div>', unsafe_allow_html=True)

            # Buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("▶️ Start", key=f"start_{activity}", type="primary", disabled=is_active):
                    start_timer(activity)
            with col2:
                if st.button("⏹️ Stop", key=f"stop_{activity}", disabled=not is_active):
                    stop_timer(activity)

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Spend Credits Section
    st.markdown("## 🎮 Spend Credits")
    spend_cols = st.columns(2)

    for idx, (activity, info) in enumerate([item for item in ACTIVITIES.items() if item[1]['type'] == 'spend']):
        with spend_cols[idx]:
            st.markdown(f'<div class="activity-card spend-card">', unsafe_allow_html=True)
            st.markdown(f"### {info['emoji']} {info['label']}")

            # Timer display
            is_active = activity in st.session_state.active_timers
            elapsed = get_elapsed_time(activity) if is_active else 0
            timer_class = "timer-display timer-active" if is_active else "timer-display"
            st.markdown(f'<div class="{timer_class}">{format_time(elapsed)}</div>', unsafe_allow_html=True)

            # Buttons
            col1, col2 = st.columns(2)
            with col1:
                if st.button("▶️ Start", key=f"start_{activity}", type="primary", disabled=is_active or st.session_state.balance <= 0):
                    start_timer(activity)
            with col2:
                if st.button("⏹️ Stop", key=f"stop_{activity}", disabled=not is_active):
                    stop_timer(activity)

            st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # History Section
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## 📋 Activity History")
    with col2:
        if st.button("🗑️ Clear History", type="secondary"):
            if len(st.session_state.history) > 0:
                clear_history()

    if len(st.session_state.history) == 0:
        st.info("No activities yet. Start earning credits!")
    else:
        for item in st.session_state.history[:20]:  # Show last 20
            activity = ACTIVITIES[item['activity']]
            sign = '+' if item['type'] == 'earn' else '-'
            color = '#2ecc71' if item['type'] == 'earn' else '#e74c3c'
            timestamp = datetime.fromisoformat(item['timestamp'])

            st.markdown(f"""
            <div class="history-item history-{item['type']}">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: bold; font-size: 1.1em;">
                            {activity['emoji']} {activity['label']}
                        </div>
                        <div style="color: #666; font-size: 0.9em;">
                            {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
                        </div>
                    </div>
                    <div style="font-size: 1.2em; font-weight: bold; color: {color};">
                        {sign}{format_time(item['duration'])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Auto-refresh for active timers
    if len(st.session_state.active_timers) > 0:
        time.sleep(1)
        st.rerun()

if __name__ == "__main__":
    main()
