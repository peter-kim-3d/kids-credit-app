import streamlit as st
import json
from datetime import datetime, timedelta
from pathlib import Path
import time

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="🌟 Kids Credit Tracker",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS - Simple and Fun Design
# ============================================================================
st.markdown("""
<style>
    /* Import fun font */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    /* Cheerful background */
    .stApp {
        background: linear-gradient(180deg, #FFF9C4 0%, #FFE082 100%);
        font-family: 'Fredoka', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Main title */
    .main-title {
        text-align: center;
        font-size: 3em;
        font-weight: 700;
        color: #FF6B6B;
        text-shadow: 3px 3px 0px #FFE66D;
        margin: 20px 0;
    }

    /* Balance display */
    .balance-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 25px;
        padding: 30px;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }

    .balance-emoji {
        font-size: 2.5em;
        animation: spin 4s linear infinite;
    }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .balance-label {
        color: white;
        font-size: 1.3em;
        font-weight: 600;
        margin-top: 10px;
    }

    .balance-value {
        color: #FFE66D;
        font-size: 4em;
        font-weight: 700;
        margin: 15px 0;
        font-family: 'Courier New', monospace;
    }

    /* Mode buttons */
    .mode-buttons {
        display: flex;
        gap: 20px;
        justify-content: center;
        margin: 30px 0;
    }

    /* Timer display */
    .timer-card {
        background: white;
        border-radius: 25px;
        padding: 40px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 8px 25px rgba(0,0,0,0.15);
    }

    .mode-title {
        font-size: 2.5em;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .mode-subtitle {
        font-size: 1.2em;
        color: #666;
        margin-bottom: 20px;
    }

    .timer-display {
        font-size: 5em;
        font-weight: 700;
        padding: 30px;
        margin: 25px 0;
        border-radius: 20px;
        background: #F8F9FA;
        color: #333;
        font-family: 'Courier New', monospace;
    }

    .timer-active {
        background: linear-gradient(45deg, #FF6B6B, #FFE66D, #4ECDC4, #95E1D3);
        background-size: 400% 400%;
        animation: gradient-shift 3s ease infinite, pulse 1.5s ease-in-out infinite;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* Buttons */
    div[data-testid="stButton"] button {
        font-family: 'Fredoka', sans-serif;
        font-size: 1.4em;
        font-weight: 700;
        padding: 18px 35px;
        border-radius: 20px;
        border: none;
        transition: all 0.3s ease;
        width: 100%;
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Success message */
    .success-msg {
        background: linear-gradient(135deg, #52B788 0%, #95E1D3 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        font-size: 1.4em;
        font-weight: 600;
        text-align: center;
        margin: 20px 0;
        animation: slide-in 0.5s ease;
    }

    @keyframes slide-in {
        from {
            transform: translateY(-30px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    /* History section */
    .history-section {
        background: white;
        border-radius: 20px;
        padding: 25px;
        margin: 30px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    }

    .history-title {
        font-size: 1.8em;
        font-weight: 700;
        color: #5E548E;
        margin-bottom: 15px;
    }

    .history-item {
        background: #F8F9FA;
        border-radius: 12px;
        padding: 15px;
        margin: 8px 0;
        font-size: 1.05em;
    }

    .history-earn {
        border-left: 6px solid #52B788;
    }

    .history-spend {
        border-left: 6px solid #FF6B6B;
    }

    .empty-state {
        text-align: center;
        padding: 30px;
        color: #999;
        font-size: 1.2em;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA PERSISTENCE
# ============================================================================
DATA_FILE = Path("credit_data.json")

def save_data():
    """Save app data to JSON file"""
    data = {
        'balance': st.session_state.balance,
        'history': st.session_state.history,
        'current_mode': st.session_state.current_mode,
        'earn_timer': st.session_state.earn_timer.isoformat() if st.session_state.earn_timer else None,
        'spend_timer': st.session_state.spend_timer.isoformat() if st.session_state.spend_timer else None
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def load_data():
    """Load app data from JSON file"""
    if DATA_FILE.exists():
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
            st.session_state.balance = data.get('balance', 0)
            st.session_state.history = data.get('history', [])
            st.session_state.current_mode = data.get('current_mode', 'earn')

            # Restore timers if recent (within 1 hour)
            if data.get('earn_timer'):
                timer_time = datetime.fromisoformat(data['earn_timer'])
                if datetime.now() - timer_time < timedelta(hours=1):
                    st.session_state.earn_timer = timer_time

            if data.get('spend_timer'):
                timer_time = datetime.fromisoformat(data['spend_timer'])
                if datetime.now() - timer_time < timedelta(hours=1):
                    st.session_state.spend_timer = timer_time
        except Exception as e:
            st.error(f"Error loading data: {e}")

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
def init_session_state():
    """Initialize all session state variables"""
    if 'balance' not in st.session_state:
        st.session_state.balance = 0
    if 'history' not in st.session_state:
        st.session_state.history = []
    if 'current_mode' not in st.session_state:
        st.session_state.current_mode = 'earn'  # Default mode
    if 'earn_timer' not in st.session_state:
        st.session_state.earn_timer = None
    if 'spend_timer' not in st.session_state:
        st.session_state.spend_timer = None
    if 'show_celebration' not in st.session_state:
        st.session_state.show_celebration = False
    if 'initialized' not in st.session_state:
        load_data()
        st.session_state.initialized = True

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================
def format_time(seconds):
    """Convert seconds to HH:MM:SS or MM:SS format"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def get_elapsed_time(mode):
    """Calculate elapsed time for active timer"""
    if mode == 'earn' and st.session_state.earn_timer:
        elapsed = (datetime.now() - st.session_state.earn_timer).total_seconds()
        return int(elapsed)
    elif mode == 'spend' and st.session_state.spend_timer:
        elapsed = (datetime.now() - st.session_state.spend_timer).total_seconds()
        return int(elapsed)
    return 0

def get_balance_emoji():
    """Return emoji based on balance amount"""
    balance = st.session_state.balance
    if balance == 0:
        return "😴"
    elif balance < 300:  # < 5 min
        return "😊"
    elif balance < 900:  # < 15 min
        return "😄"
    elif balance < 1800:  # < 30 min
        return "🤩"
    else:
        return "🎉"

# ============================================================================
# MODE SWITCHING
# ============================================================================
def switch_mode(mode):
    """Switch between earn and spend modes"""
    st.session_state.current_mode = mode
    save_data()

# ============================================================================
# TIMER CONTROLS
# ============================================================================
def start_timer():
    """Start timer for current mode"""
    mode = st.session_state.current_mode

    if mode == 'earn':
        if st.session_state.earn_timer:
            st.warning("⏰ Earning timer is already running!")
            return
        st.session_state.earn_timer = datetime.now()
        st.session_state.show_celebration = False

    else:  # spend mode
        if st.session_state.spend_timer:
            st.warning("⏰ Spending timer is already running!")
            return
        if st.session_state.balance <= 0:
            st.error("🚫 No credits! Earn some first!")
            return
        st.session_state.spend_timer = datetime.now()

    save_data()
    st.rerun()

def stop_timer():
    """Stop timer for current mode and update balance"""
    mode = st.session_state.current_mode

    if mode == 'earn':
        if not st.session_state.earn_timer:
            return

        elapsed = get_elapsed_time('earn')
        if elapsed < 1:
            st.warning("Timer ran for less than a second!")
            st.session_state.earn_timer = None
            save_data()
            return

        # Add to balance
        st.session_state.balance += elapsed

        # Add to history
        st.session_state.history.insert(0, {
            'type': 'earn',
            'duration': elapsed,
            'timestamp': datetime.now().isoformat()
        })

        # Show celebration
        st.session_state.show_celebration = True
        st.session_state.earn_timer = None

    else:  # spend mode
        if not st.session_state.spend_timer:
            return

        elapsed = get_elapsed_time('spend')
        if elapsed < 1:
            st.warning("Timer ran for less than a second!")
            st.session_state.spend_timer = None
            save_data()
            return

        # Deduct from balance
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

def clear_history():
    """Clear all activity history"""
    st.session_state.history = []
    save_data()
    st.rerun()

# ============================================================================
# MAIN APP
# ============================================================================
def main():
    """Main application"""

    # Initialize session state
    init_session_state()

    # ========================================================================
    # HEADER
    # ========================================================================
    st.markdown('<h1 class="main-title">🌟 Kids Credit Tracker 🌟</h1>', unsafe_allow_html=True)

    # ========================================================================
    # CELEBRATION MESSAGE
    # ========================================================================
    if st.session_state.show_celebration:
        st.markdown("""
        <div class="success-msg">
            🎉 Awesome! You Earned Time Credits! 🎉
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        st.session_state.show_celebration = False

    # ========================================================================
    # BALANCE DISPLAY - Always visible at top
    # ========================================================================
    balance_display = format_time(st.session_state.balance)
    balance_emoji = get_balance_emoji()

    st.markdown(f"""
    <div class="balance-card">
        <div class="balance-emoji">{balance_emoji}</div>
        <div class="balance-label">Your Time Credits</div>
        <div class="balance-value">{balance_display}</div>
    </div>
    """, unsafe_allow_html=True)

    # ========================================================================
    # MODE TOGGLE BUTTONS - Switch between Earn and Spend
    # ========================================================================
    col1, col2 = st.columns(2)

    with col1:
        # Earn mode button
        if st.button(
            "💪 Earn Mode",
            key="earn_mode_btn",
            type="primary" if st.session_state.current_mode == 'earn' else "secondary",
            use_container_width=True
        ):
            switch_mode('earn')
            st.rerun()

    with col2:
        # Spend mode button
        if st.button(
            "🎮 Spend Mode",
            key="spend_mode_btn",
            type="primary" if st.session_state.current_mode == 'spend' else "secondary",
            use_container_width=True
        ):
            switch_mode('spend')
            st.rerun()

    # ========================================================================
    # TIMER DISPLAY - Changes based on current mode
    # ========================================================================
    st.markdown('<div class="timer-card">', unsafe_allow_html=True)

    # Get current mode details
    mode = st.session_state.current_mode

    if mode == 'earn':
        # EARN MODE
        st.markdown('<div class="mode-title" style="color: #52B788;">💪 Earn Time Credits</div>', unsafe_allow_html=True)
        st.markdown('<div class="mode-subtitle">Study • Practice • Clean • Help • Read</div>', unsafe_allow_html=True)

        # Timer display
        is_active = st.session_state.earn_timer is not None
        elapsed = get_elapsed_time('earn') if is_active else 0
        timer_class = "timer-display timer-active" if is_active else "timer-display"

        st.markdown(f'<div class="{timer_class}">{format_time(elapsed)}</div>', unsafe_allow_html=True)

        # Control buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🚀 Start Earning", key="start_btn", disabled=is_active, use_container_width=True):
                start_timer()
        with col2:
            if st.button("⏹️ Stop & Save", key="stop_btn", disabled=not is_active, use_container_width=True):
                stop_timer()

    else:
        # SPEND MODE
        st.markdown('<div class="mode-title" style="color: #FF6B6B;">🎮 Spend Time Credits</div>', unsafe_allow_html=True)
        st.markdown('<div class="mode-subtitle">TV • Games • Tablet • Fun Time</div>', unsafe_allow_html=True)

        # Timer display
        is_active = st.session_state.spend_timer is not None
        elapsed = get_elapsed_time('spend') if is_active else 0
        timer_class = "timer-display timer-active" if is_active else "timer-display"

        st.markdown(f'<div class="{timer_class}">{format_time(elapsed)}</div>', unsafe_allow_html=True)

        # Warning if no credits
        if st.session_state.balance <= 0 and not is_active:
            st.warning("⚠️ No credits available! Switch to Earn Mode first!")

        # Control buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("▶️ Start Spending", key="start_btn",
                        disabled=is_active or st.session_state.balance <= 0,
                        use_container_width=True):
                start_timer()
        with col2:
            if st.button("⏹️ Stop", key="stop_btn", disabled=not is_active, use_container_width=True):
                stop_timer()

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # ACTIVITY HISTORY
    # ========================================================================
    st.markdown('<div class="history-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div class="history-title">📋 Activity History</div>', unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ Clear", type="secondary", use_container_width=True):
            if st.session_state.history:
                clear_history()

    # Display history
    if not st.session_state.history:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size: 2.5em;">📝</div>
            <div>No activities yet!</div>
            <div style="font-size: 0.9em;">Start earning to see your history.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show last 15 activities
        for item in st.session_state.history[:15]:
            activity_type = item['type']

            if activity_type == 'earn':
                emoji = '💪'
                label = 'Earned'
                sign = '+'
                color = '#52B788'
                css_class = 'history-earn'
            else:
                emoji = '🎮'
                label = 'Spent'
                sign = '-'
                color = '#FF6B6B'
                css_class = 'history-spend'

            timestamp = datetime.fromisoformat(item['timestamp'])
            time_str = format_time(item['duration'])

            st.markdown(f"""
            <div class="history-item {css_class}">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div style="flex: 1;">
                        <div style="font-weight: 700; font-size: 1.15em; color: {color};">
                            {emoji} {label}
                        </div>
                        <div style="color: #999; font-size: 0.85em; margin-top: 3px;">
                            {timestamp.strftime('%b %d at %I:%M %p')}
                        </div>
                    </div>
                    <div style="font-size: 1.5em; font-weight: 700; color: {color};">
                        {sign}{time_str}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # AUTO-REFRESH - Update timer every second when active
    # ========================================================================
    if st.session_state.earn_timer or st.session_state.spend_timer:
        time.sleep(1)
        st.rerun()

# ============================================================================
# RUN APP
# ============================================================================
if __name__ == "__main__":
    main()
