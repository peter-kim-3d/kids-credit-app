import streamlit as st
import json
from datetime import datetime, timedelta
from pathlib import Path
import time

# Page configuration
st.set_page_config(
    page_title="Kids Credit Tracker",
    page_icon="🌟",
    layout="centered",
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
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        margin: 20px 0;
    }
    .balance-value {
        font-size: 4em;
        font-weight: bold;
        margin: 10px 0;
    }
    .timer-display {
        font-size: 3.5em;
        font-weight: bold;
        text-align: center;
        padding: 30px;
        border-radius: 15px;
        background: #f8f9fa;
        margin: 20px 0;
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
    .action-card {
        padding: 40px;
        border-radius: 20px;
        margin: 20px 0;
        text-align: center;
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
        border-left: 5px solid #2ecc71;
    }
    .history-spend {
        border-left: 5px solid #e74c3c;
    }
    div[data-testid="stButton"] button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        padding: 15px;
        font-size: 1.1em;
    }
</style>
""", unsafe_allow_html=True)

# Data file path
DATA_FILE = Path("credit_data.json")

# Initialize session state
def init_session_state():
    if 'balance' not in st.session_state:
        st.session_state.balance = 0
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'earn_timer' not in st.session_state:
        st.session_state.earn_timer = None
    if 'spend_timer' not in st.session_state:
        st.session_state.spend_timer = None
    if 'initialized' not in st.session_state:
        load_data()
        st.session_state.initialized = True

# Save data to JSON
def save_data():
    data = {
        'balance': st.session_state.balance,
        'history': st.session_state.history,
        'earn_timer': st.session_state.earn_timer.isoformat() if st.session_state.earn_timer else None,
        'spend_timer': st.session_state.spend_timer.isoformat() if st.session_state.spend_timer else None
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

            # Restore timers if recent (within 1 hour)
            if data.get('earn_timer'):
                earn_time = datetime.fromisoformat(data['earn_timer'])
                if datetime.now() - earn_time < timedelta(hours=1):
                    st.session_state.earn_timer = earn_time

            if data.get('spend_timer'):
                spend_time = datetime.fromisoformat(data['spend_timer'])
                if datetime.now() - spend_time < timedelta(hours=1):
                    st.session_state.spend_timer = spend_time
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

# Get elapsed time for timer
def get_elapsed_time(timer_type):
    if timer_type == 'earn' and st.session_state.earn_timer:
        elapsed = (datetime.now() - st.session_state.earn_timer).total_seconds()
        return int(elapsed)
    elif timer_type == 'spend' and st.session_state.spend_timer:
        elapsed = (datetime.now() - st.session_state.spend_timer).total_seconds()
        return int(elapsed)
    return 0

# Start timer
def start_earn():
    if st.session_state.earn_timer:
        st.warning("Earn timer is already running!")
        return
    st.session_state.earn_timer = datetime.now()
    save_data()
    st.rerun()

def start_spend():
    if st.session_state.spend_timer:
        st.warning("Spend timer is already running!")
        return
    if st.session_state.balance <= 0:
        st.error("Not enough credits! Earn credits first.")
        return
    st.session_state.spend_timer = datetime.now()
    save_data()
    st.rerun()

# Stop timer
def stop_earn():
    if not st.session_state.earn_timer:
        return

    elapsed = get_elapsed_time('earn')
    if elapsed < 1:
        st.warning("Timer was running for less than a second!")
        st.session_state.earn_timer = None
        save_data()
        return

    # Update balance
    st.session_state.balance += elapsed

    # Add to history
    st.session_state.history.insert(0, {
        'type': 'earn',
        'duration': elapsed,
        'timestamp': datetime.now().isoformat()
    })

    st.session_state.earn_timer = None
    save_data()
    st.rerun()

def stop_spend():
    if not st.session_state.spend_timer:
        return

    elapsed = get_elapsed_time('spend')
    if elapsed < 1:
        st.warning("Timer was running for less than a second!")
        st.session_state.spend_timer = None
        save_data()
        return

    # Update balance
    st.session_state.balance -= elapsed
    if st.session_state.balance < 0:
        st.session_state.balance = 0

    # Add to history
    st.session_state.history.insert(0, {
        'type': 'spend',
        'duration': elapsed,
        'timestamp': datetime.now().isoformat()
    })

    st.session_state.spend_timer = None
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
        <div style="font-size: 1.3em;">Credit Balance</div>
        <div class="balance-value">{balance_display}</div>
        <div style="font-size: 0.9em;">(hours:minutes:seconds)</div>
    </div>
    """, unsafe_allow_html=True)

    # Earn Section
    st.markdown('<div class="action-card earn-card">', unsafe_allow_html=True)
    st.markdown("## 💪 Earn Credits")

    # Timer display
    earn_active = st.session_state.earn_timer is not None
    earn_elapsed = get_elapsed_time('earn') if earn_active else 0
    timer_class = "timer-display timer-active" if earn_active else "timer-display"
    st.markdown(f'<div class="{timer_class}">{format_time(earn_elapsed)}</div>', unsafe_allow_html=True)

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start Earning", key="start_earn", type="primary", disabled=earn_active, use_container_width=True):
            start_earn()
    with col2:
        if st.button("⏹️ Stop Earning", key="stop_earn", disabled=not earn_active, use_container_width=True):
            stop_earn()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # Spend Section
    st.markdown('<div class="action-card spend-card">', unsafe_allow_html=True)
    st.markdown("## 🎮 Spend Credits")

    # Timer display
    spend_active = st.session_state.spend_timer is not None
    spend_elapsed = get_elapsed_time('spend') if spend_active else 0
    timer_class = "timer-display timer-active" if spend_active else "timer-display"
    st.markdown(f'<div class="{timer_class}">{format_time(spend_elapsed)}</div>', unsafe_allow_html=True)

    # Buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ Start Spending", key="start_spend", type="primary", disabled=spend_active or st.session_state.balance <= 0, use_container_width=True):
            start_spend()
    with col2:
        if st.button("⏹️ Stop Spending", key="stop_spend", disabled=not spend_active, use_container_width=True):
            stop_spend()

    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # History Section
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## 📋 Activity History")
    with col2:
        if st.button("🗑️ Clear", type="secondary"):
            if len(st.session_state.history) > 0:
                clear_history()

    if len(st.session_state.history) == 0:
        st.info("No activities yet. Start earning credits!")
    else:
        for item in st.session_state.history[:20]:  # Show last 20
            action_type = item['type']
            emoji = '💪' if action_type == 'earn' else '🎮'
            label = 'Earned' if action_type == 'earn' else 'Spent'
            sign = '+' if action_type == 'earn' else '-'
            color = '#2ecc71' if action_type == 'earn' else '#e74c3c'
            timestamp = datetime.fromisoformat(item['timestamp'])

            st.markdown(f"""
            <div class="history-item history-{action_type}">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <div style="font-weight: bold; font-size: 1.1em;">
                            {emoji} {label}
                        </div>
                        <div style="color: #666; font-size: 0.9em;">
                            {timestamp.strftime('%Y-%m-%d %H:%M:%S')}
                        </div>
                    </div>
                    <div style="font-size: 1.3em; font-weight: bold; color: {color};">
                        {sign}{format_time(item['duration'])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    # Auto-refresh for active timers
    if st.session_state.earn_timer or st.session_state.spend_timer:
        time.sleep(1)
        st.rerun()

if __name__ == "__main__":
    main()
