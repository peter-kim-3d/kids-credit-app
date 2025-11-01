import streamlit as st
import json
from datetime import datetime, timedelta
from pathlib import Path
import time

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================
st.set_page_config(
    page_title="🌟 Kids Credit Tracker 🌟",
    page_icon="🌟",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# CUSTOM CSS STYLING - Kid-Friendly Design
# ============================================================================
st.markdown("""
<style>
    /* Import fun, kid-friendly font */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&display=swap');

    /* Main background - cheerful gradient */
    .stApp {
        background: linear-gradient(135deg, #FFF9C4 0%, #FFE082 50%, #FFEB99 100%);
        font-family: 'Fredoka', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Main title styling */
    .main-title {
        text-align: center;
        font-size: 3.5em;
        font-weight: 700;
        color: #FF6B6B;
        text-shadow: 3px 3px 0px #FFE66D, 6px 6px 0px #4ECDC4;
        margin: 20px 0;
        animation: bounce 2s ease-in-out infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }

    /* Balance display - BIG and FUN! */
    .balance-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 30px;
        padding: 40px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 5px solid white;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { box-shadow: 0 10px 30px rgba(102, 126, 234, 0.5); }
        to { box-shadow: 0 10px 50px rgba(118, 75, 162, 0.8); }
    }

    .balance-label {
        color: white;
        font-size: 1.8em;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .balance-value {
        color: #FFE66D;
        font-size: 5em;
        font-weight: 700;
        text-shadow: 3px 3px 0px rgba(0,0,0,0.2);
        margin: 20px 0;
        font-family: 'Courier New', monospace;
    }

    .balance-emoji {
        font-size: 3em;
        animation: spin 3s linear infinite;
    }

    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    /* Earning section - GREEN and POSITIVE */
    .earn-section {
        background: linear-gradient(135deg, #84FAB0 0%, #8FD3F4 100%);
        border-radius: 25px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(132, 250, 176, 0.4);
        border: 4px solid #4ECDC4;
    }

    .earn-title {
        color: #2D6A4F;
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Spending section - RED/ORANGE and FUN */
    .spend-section {
        background: linear-gradient(135deg, #FA709A 0%, #FEE140 100%);
        border-radius: 25px;
        padding: 40px;
        margin: 20px 0;
        box-shadow: 0 8px 25px rgba(250, 112, 154, 0.4);
        border: 4px solid #FF6B6B;
    }

    .spend-title {
        color: #C1121F;
        font-size: 2.5em;
        font-weight: 700;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Timer display - HUGE and ANIMATED */
    .timer-display {
        font-size: 5em;
        font-weight: 700;
        text-align: center;
        padding: 30px;
        margin: 25px 0;
        border-radius: 20px;
        background: white;
        color: #333;
        font-family: 'Courier New', monospace;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .timer-active {
        background: linear-gradient(45deg, #FF6B6B, #FFE66D, #4ECDC4, #95E1D3);
        background-size: 400% 400%;
        animation: gradientShift 3s ease infinite, pulse 1.5s ease-in-out infinite;
        color: white;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.05); }
    }

    /* Buttons - BIG and COLORFUL */
    div[data-testid="stButton"] button {
        font-family: 'Fredoka', sans-serif;
        font-size: 1.5em;
        font-weight: 700;
        padding: 20px 40px;
        border-radius: 20px;
        border: none;
        box-shadow: 0 6px 20px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
        width: 100%;
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }

    div[data-testid="stButton"] button:active {
        transform: translateY(0px);
    }

    /* History section */
    .history-section {
        background: white;
        border-radius: 20px;
        padding: 30px;
        margin: 30px 0;
        box-shadow: 0 5px 20px rgba(0,0,0,0.1);
    }

    .history-title {
        color: #5E548E;
        font-size: 2em;
        font-weight: 700;
        margin-bottom: 20px;
    }

    .history-item {
        background: linear-gradient(135deg, #F8F9FA 0%, #E9ECEF 100%);
        border-radius: 15px;
        padding: 20px;
        margin: 10px 0;
        font-size: 1.1em;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
    }

    .history-earn {
        border-left: 8px solid #52B788;
    }

    .history-spend {
        border-left: 8px solid #FF6B6B;
    }

    /* Confetti animation */
    .confetti {
        position: fixed;
        width: 10px;
        height: 10px;
        background: #FFE66D;
        position: absolute;
        animation: confetti-fall 3s linear;
    }

    @keyframes confetti-fall {
        to {
            transform: translateY(100vh) rotate(360deg);
            opacity: 0;
        }
    }

    /* Success message styling */
    .success-message {
        background: linear-gradient(135deg, #52B788 0%, #95E1D3 100%);
        color: white;
        padding: 20px;
        border-radius: 15px;
        font-size: 1.5em;
        font-weight: 600;
        text-align: center;
        margin: 20px 0;
        box-shadow: 0 5px 15px rgba(82, 183, 136, 0.4);
        animation: slideIn 0.5s ease;
    }

    @keyframes slideIn {
        from {
            transform: translateY(-50px);
            opacity: 0;
        }
        to {
            transform: translateY(0);
            opacity: 1;
        }
    }

    /* Empty state message */
    .empty-state {
        text-align: center;
        padding: 40px;
        color: #6C757D;
        font-size: 1.3em;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================================
# DATA PERSISTENCE
# ============================================================================
DATA_FILE = Path("credit_data.json")

def save_data():
    """Save all app data to JSON file"""
    data = {
        'balance': st.session_state.balance,
        'history': st.session_state.history,
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

            # Restore active timers if they're recent (within 1 hour)
            if data.get('earn_timer'):
                earn_time = datetime.fromisoformat(data['earn_timer'])
                if datetime.now() - earn_time < timedelta(hours=1):
                    st.session_state.earn_timer = earn_time

            if data.get('spend_timer'):
                spend_time = datetime.fromisoformat(data['spend_timer'])
                if datetime.now() - spend_time < timedelta(hours=1):
                    st.session_state.spend_timer = spend_time
        except Exception as e:
            st.error(f"Oops! Error loading data: {e}")

# ============================================================================
# SESSION STATE INITIALIZATION
# ============================================================================
def init_session_state():
    """Initialize all session state variables"""
    if 'balance' not in st.session_state:
        st.session_state.balance = 0
    if 'history' not in st.session_state:
        st.session_state.history = []
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
    """Convert seconds to readable time format (HH:MM:SS or MM:SS)"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes}:{secs:02d}"

def get_elapsed_time(timer_type):
    """Calculate elapsed time for active timer"""
    if timer_type == 'earn' and st.session_state.earn_timer:
        elapsed = (datetime.now() - st.session_state.earn_timer).total_seconds()
        return int(elapsed)
    elif timer_type == 'spend' and st.session_state.spend_timer:
        elapsed = (datetime.now() - st.session_state.spend_timer).total_seconds()
        return int(elapsed)
    return 0

def get_balance_emoji():
    """Return emoji based on balance amount - visual feedback for kids"""
    balance = st.session_state.balance
    if balance == 0:
        return "😴"
    elif balance < 300:  # Less than 5 minutes
        return "😊"
    elif balance < 900:  # Less than 15 minutes
        return "😄"
    elif balance < 1800:  # Less than 30 minutes
        return "🤩"
    else:
        return "🎉"

# ============================================================================
# TIMER CONTROL FUNCTIONS
# ============================================================================
def start_earn():
    """Start the earning timer"""
    if st.session_state.earn_timer:
        st.warning("⏰ Earning timer is already running!")
        return

    st.session_state.earn_timer = datetime.now()
    st.session_state.show_celebration = False
    save_data()
    st.rerun()

def stop_earn():
    """Stop the earning timer and add credits"""
    if not st.session_state.earn_timer:
        return

    elapsed = get_elapsed_time('earn')

    if elapsed < 1:
        st.warning("⏱️ Timer was running for less than a second!")
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

    # Show celebration!
    st.session_state.show_celebration = True
    st.session_state.earn_timer = None

    save_data()
    st.rerun()

def start_spend():
    """Start the spending timer"""
    if st.session_state.spend_timer:
        st.warning("⏰ Spending timer is already running!")
        return

    if st.session_state.balance <= 0:
        st.error("🚫 No credits left! Earn some credits first!")
        return

    st.session_state.spend_timer = datetime.now()
    save_data()
    st.rerun()

def stop_spend():
    """Stop the spending timer and deduct credits"""
    if not st.session_state.spend_timer:
        return

    elapsed = get_elapsed_time('spend')

    if elapsed < 1:
        st.warning("⏱️ Timer was running for less than a second!")
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
    """Main application function"""

    # Initialize session state
    init_session_state()

    # ========================================================================
    # HEADER - Fun and bouncy title
    # ========================================================================
    st.markdown('<h1 class="main-title">🌟 Kids Credit Tracker 🌟</h1>', unsafe_allow_html=True)

    # ========================================================================
    # CELEBRATION MESSAGE - Shows when earning completes
    # ========================================================================
    if st.session_state.show_celebration:
        st.markdown("""
        <div class="success-message">
            🎉 Awesome Job! You Earned Credits! 🎉
        </div>
        """, unsafe_allow_html=True)
        st.balloons()  # Streamlit's built-in celebration effect!
        st.session_state.show_celebration = False

    # ========================================================================
    # BALANCE DISPLAY - Big, colorful, and fun!
    # ========================================================================
    balance_display = format_time(st.session_state.balance)
    balance_emoji = get_balance_emoji()

    st.markdown(f"""
    <div class="balance-container">
        <div class="balance-emoji">{balance_emoji}</div>
        <div class="balance-label">Your Credit Balance</div>
        <div class="balance-value">{balance_display}</div>
        <div style="color: white; font-size: 1.2em; font-weight: 600;">
            (hours:minutes:seconds)
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ========================================================================
    # EARNING SECTION - Green, positive, encouraging
    # ========================================================================
    st.markdown('<div class="earn-section">', unsafe_allow_html=True)
    st.markdown('<div class="earn-title">💪 Earn Time Credits</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #2D6A4F; margin-bottom: 20px;">
        Study • Practice • Clean • Help • Read
    </div>
    """, unsafe_allow_html=True)

    # Timer display for earning
    earn_active = st.session_state.earn_timer is not None
    earn_elapsed = get_elapsed_time('earn') if earn_active else 0
    timer_class = "timer-display timer-active" if earn_active else "timer-display"

    st.markdown(f'<div class="{timer_class}">{format_time(earn_elapsed)}</div>', unsafe_allow_html=True)

    # Earning buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 START EARNING", key="start_earn", type="primary", disabled=earn_active, use_container_width=True):
            start_earn()
    with col2:
        if st.button("⏹️ STOP & SAVE", key="stop_earn", disabled=not earn_active, use_container_width=True):
            stop_earn()

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # SPENDING SECTION - Red/orange, fun, exciting
    # ========================================================================
    st.markdown('<div class="spend-section">', unsafe_allow_html=True)
    st.markdown('<div class="spend-title">🎮 Spend Time Credits</div>', unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align: center; font-size: 1.3em; color: #C1121F; margin-bottom: 20px;">
        TV • Games • Tablet • Fun Time
    </div>
    """, unsafe_allow_html=True)

    # Timer display for spending
    spend_active = st.session_state.spend_timer is not None
    spend_elapsed = get_elapsed_time('spend') if spend_active else 0
    timer_class = "timer-display timer-active" if spend_active else "timer-display"

    st.markdown(f'<div class="{timer_class}">{format_time(spend_elapsed)}</div>', unsafe_allow_html=True)

    # Show warning if no credits
    if st.session_state.balance <= 0 and not spend_active:
        st.markdown("""
        <div style="background: #FFF3CD; padding: 15px; border-radius: 10px; text-align: center;
                    font-size: 1.2em; color: #856404; font-weight: 600; margin-bottom: 15px;">
            ⚠️ No credits available! Earn some first! ⚠️
        </div>
        """, unsafe_allow_html=True)

    # Spending buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("▶️ START SPENDING", key="start_spend", type="primary",
                     disabled=spend_active or st.session_state.balance <= 0, use_container_width=True):
            start_spend()
    with col2:
        if st.button("⏹️ STOP", key="stop_spend", disabled=not spend_active, use_container_width=True):
            stop_spend()

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # ACTIVITY HISTORY - Simple and clear
    # ========================================================================
    st.markdown('<div class="history-section">', unsafe_allow_html=True)

    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown('<div class="history-title">📋 Activity History</div>', unsafe_allow_html=True)
    with col2:
        if st.button("🗑️ Clear", type="secondary", use_container_width=True):
            if len(st.session_state.history) > 0:
                clear_history()

    # Display history or empty state
    if len(st.session_state.history) == 0:
        st.markdown("""
        <div class="empty-state">
            <div style="font-size: 3em;">📝</div>
            <div>No activities yet!</div>
            <div>Start earning credits to see your history here.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show last 15 activities
        for item in st.session_state.history[:15]:
            action_type = item['type']

            # Customize display based on type
            if action_type == 'earn':
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
                        <div style="font-weight: 700; font-size: 1.3em; color: {color};">
                            {emoji} {label}
                        </div>
                        <div style="color: #6C757D; font-size: 0.9em; margin-top: 5px;">
                            {timestamp.strftime('%b %d, %Y at %I:%M %p')}
                        </div>
                    </div>
                    <div style="font-size: 1.8em; font-weight: 700; color: {color};">
                        {sign}{time_str}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # AUTO-REFRESH - Update timers every second when active
    # ========================================================================
    if st.session_state.earn_timer or st.session_state.spend_timer:
        time.sleep(1)
        st.rerun()

# ============================================================================
# RUN THE APP
# ============================================================================
if __name__ == "__main__":
    main()
