"""
🌟 Kids Credit Tracker - Fancy Edition 🌟
A beautiful, modern time credit tracking app for kids

Installation:
pip install streamlit

Run:
streamlit run app.py
"""

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
# CUSTOM CSS - Modern, Clean Design with Animations
# ============================================================================
st.markdown("""
<style>
    /* Import fun fonts */
    @import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;600;700&family=Baloo+2:wght@400;600;700&display=swap');

    /* Main app styling */
    .stApp {
        background: linear-gradient(135deg, #FFF8E1 0%, #FFE0B2 50%, #FFF3E0 100%);
        font-family: 'Fredoka', 'Baloo 2', sans-serif;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Remove default padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Main title with gradient and animation */
    .app-title {
        text-align: center;
        font-size: 3.5em;
        font-weight: 700;
        background: linear-gradient(135deg, #FF6B6B 0%, #FFE66D 50%, #4ECDC4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 1.5rem;
        animation: title-glow 3s ease-in-out infinite;
    }

    @keyframes title-glow {
        0%, 100% { filter: brightness(1); transform: scale(1); }
        50% { filter: brightness(1.2); transform: scale(1.02); }
    }

    /* Balance card - floating effect */
    .balance-container {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 30px;
        padding: 2.5rem;
        text-align: center;
        margin: 1.5rem 0;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        transform: translateY(0);
        transition: all 0.3s ease;
        animation: float 3s ease-in-out infinite;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .balance-container:hover {
        box-shadow: 0 25px 80px rgba(102, 126, 234, 0.5);
        transform: translateY(-5px);
    }

    .balance-emoji {
        font-size: 3.5em;
        display: inline-block;
        animation: rotate 4s linear infinite;
    }

    @keyframes rotate {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }

    .balance-label {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.5em;
        font-weight: 600;
        margin-top: 0.5rem;
        letter-spacing: 0.5px;
    }

    .balance-value {
        color: #FFE66D;
        font-size: 5em;
        font-weight: 700;
        margin: 0.5rem 0;
        font-family: 'Courier New', monospace;
        text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.2);
    }

    /* Mode buttons container */
    .mode-toggle {
        display: flex;
        gap: 1rem;
        justify-content: center;
        margin: 2rem 0;
    }

    /* Custom button styling */
    div[data-testid="stButton"] button {
        font-family: 'Fredoka', sans-serif;
        font-size: 1.3em;
        font-weight: 700;
        padding: 1rem 2.5rem;
        border-radius: 25px;
        border: none;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
    }

    div[data-testid="stButton"] button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
    }

    div[data-testid="stButton"] button:active {
        transform: translateY(0) scale(0.98);
    }

    /* Timer section with mode-specific gradients */
    .timer-section {
        background: white;
        border-radius: 35px;
        padding: 3rem 2rem;
        margin: 2rem 0;
        box-shadow: 0 15px 50px rgba(0, 0, 0, 0.08);
        transition: all 0.4s ease;
    }

    .timer-section.earn-mode {
        border: 3px solid transparent;
        background: linear-gradient(white, white) padding-box,
                    linear-gradient(135deg, #84FAB0 0%, #8FD3F4 100%) border-box;
    }

    .timer-section.spend-mode {
        border: 3px solid transparent;
        background: linear-gradient(white, white) padding-box,
                    linear-gradient(135deg, #FA709A 0%, #FEE140 100%) border-box;
    }

    /* Mode header */
    .mode-header {
        text-align: center;
        margin-bottom: 2rem;
    }

    .mode-emoji {
        font-size: 4em;
        display: inline-block;
        animation: bounce 2s ease-in-out infinite;
    }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-15px); }
    }

    .mode-title {
        font-size: 2.8em;
        font-weight: 700;
        margin: 0.5rem 0;
    }

    .mode-title.earn {
        background: linear-gradient(135deg, #52B788 0%, #40916C 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .mode-title.spend {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .mode-subtitle {
        font-size: 1.3em;
        color: #666;
        font-weight: 500;
    }

    /* Timer display - modern glassmorphism */
    .timer-display {
        background: rgba(255, 255, 255, 0.9);
        backdrop-filter: blur(10px);
        border: 2px solid rgba(255, 255, 255, 0.3);
        border-radius: 25px;
        padding: 2rem;
        margin: 2rem 0;
        text-align: center;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
    }

    .timer-value {
        font-size: 5.5em;
        font-weight: 700;
        font-family: 'Courier New', monospace;
        color: #333;
        letter-spacing: 0.05em;
    }

    .timer-active {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        animation: timer-pulse 2s ease-in-out infinite, gradient-shift 4s ease infinite;
        color: white !important;
    }

    .timer-active .timer-value {
        color: white;
        text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.3);
    }

    @keyframes timer-pulse {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.03); }
    }

    @keyframes gradient-shift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Success celebration */
    .celebration {
        background: linear-gradient(135deg, #52B788 0%, #95E1D3 100%);
        color: white;
        padding: 1.5rem;
        border-radius: 20px;
        text-align: center;
        font-size: 1.6em;
        font-weight: 700;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(82, 183, 136, 0.3);
        animation: slide-in 0.5s ease, shake 0.5s ease 0.5s;
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

    @keyframes shake {
        0%, 100% { transform: rotate(0deg); }
        25% { transform: rotate(-3deg); }
        75% { transform: rotate(3deg); }
    }

    /* Activity history - clean cards */
    .history-container {
        background: white;
        border-radius: 25px;
        padding: 2rem;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.05);
    }

    .history-title {
        font-size: 2em;
        font-weight: 700;
        color: #5E548E;
        margin-bottom: 1.5rem;
        text-align: center;
    }

    .activity-card {
        background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
        border-radius: 18px;
        padding: 1.3rem;
        margin: 0.8rem 0;
        transition: all 0.3s ease;
        box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
    }

    .activity-card:hover {
        transform: translateX(5px);
        box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
    }

    .activity-card.earn {
        border-left: 5px solid #52B788;
    }

    .activity-card.spend {
        border-left: 5px solid #FF6B6B;
    }

    .activity-content {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .activity-info {
        flex: 1;
    }

    .activity-label {
        font-size: 1.3em;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }

    .activity-time {
        font-size: 0.95em;
        color: #999;
    }

    .activity-duration {
        font-size: 1.8em;
        font-weight: 700;
    }

    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: #aaa;
    }

    .empty-emoji {
        font-size: 4em;
        opacity: 0.5;
        margin-bottom: 1rem;
        display: block;
    }

    /* Warning message */
    .warning-box {
        background: linear-gradient(135deg, #FFF3CD 0%, #FFE5B4 100%);
        border-left: 5px solid #FFC107;
        border-radius: 15px;
        padding: 1.2rem;
        margin: 1rem 0;
        font-size: 1.2em;
        font-weight: 600;
        color: #856404;
        text-align: center;
    }

    /* Smooth transitions for mode changes */
    .fade-in {
        animation: fadeIn 0.4s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
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
        st.session_state.current_mode = 'earn'
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
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    else:
        return f"{minutes:02d}:{secs:02d}"

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
    elif balance < 300:
        return "😊"
    elif balance < 900:
        return "😄"
    elif balance < 1800:
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
    st.rerun()

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
            st.error("🚫 No credits! Switch to Earn Mode first!")
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
    # HEADER - Animated title
    # ========================================================================
    st.markdown('<h1 class="app-title">🌟 Kids Credit Tracker 🌟</h1>', unsafe_allow_html=True)

    # ========================================================================
    # CELEBRATION MESSAGE
    # ========================================================================
    if st.session_state.show_celebration:
        st.markdown('<div class="celebration">🎉 Awesome! You Earned Time Credits! 🎉</div>',
                   unsafe_allow_html=True)
        st.balloons()
        st.session_state.show_celebration = False

    # ========================================================================
    # BALANCE DISPLAY - Floating card with animation
    # ========================================================================
    balance_display = format_time(st.session_state.balance)
    balance_emoji = get_balance_emoji()

    st.markdown(f"""
    <div class="balance-container">
        <div class="balance-emoji">{balance_emoji}</div>
        <div class="balance-label">Your Time Credits</div>
        <div class="balance-value">{balance_display}</div>
    </div>
    """, unsafe_allow_html=True)

    # ========================================================================
    # MODE TOGGLE BUTTONS - Using shadcn-style buttons
    # ========================================================================
    st.markdown('<div class="mode-toggle">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "💪 Earn Mode",
            key="earn_mode_btn",
            type="primary" if st.session_state.current_mode == 'earn' else "secondary",
            use_container_width=True
        ):
            switch_mode('earn')

    with col2:
        if st.button(
            "🎮 Spend Mode",
            key="spend_mode_btn",
            type="primary" if st.session_state.current_mode == 'spend' else "secondary",
            use_container_width=True
        ):
            switch_mode('spend')

    st.markdown('</div>', unsafe_allow_html=True)

    # ========================================================================
    # TIMER SECTION - Mode-specific display with fade-in animation
    # ========================================================================
    mode = st.session_state.current_mode
    mode_class = "earn-mode" if mode == 'earn' else "spend-mode"

    st.markdown(f'<div class="timer-section {mode_class} fade-in">', unsafe_allow_html=True)

    if mode == 'earn':
        # EARN MODE
        st.markdown("""
        <div class="mode-header">
            <div class="mode-emoji">💪</div>
            <div class="mode-title earn">Earn Time Credits</div>
            <div class="mode-subtitle">Study • Practice • Clean • Help • Read</div>
        </div>
        """, unsafe_allow_html=True)

        # Timer display
        is_active = st.session_state.earn_timer is not None
        elapsed = get_elapsed_time('earn') if is_active else 0
        timer_class = "timer-display timer-active" if is_active else "timer-display"

        st.markdown(f"""
        <div class="{timer_class}">
            <div class="timer-value">{format_time(elapsed)}</div>
        </div>
        """, unsafe_allow_html=True)

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
        st.markdown("""
        <div class="mode-header">
            <div class="mode-emoji">🎮</div>
            <div class="mode-title spend">Spend Time Credits</div>
            <div class="mode-subtitle">TV • Games • Tablet • Fun Time</div>
        </div>
        """, unsafe_allow_html=True)

        # Timer display
        is_active = st.session_state.spend_timer is not None
        elapsed = get_elapsed_time('spend') if is_active else 0
        timer_class = "timer-display timer-active" if is_active else "timer-display"

        st.markdown(f"""
        <div class="{timer_class}">
            <div class="timer-value">{format_time(elapsed)}</div>
        </div>
        """, unsafe_allow_html=True)

        # Warning if no credits
        if st.session_state.balance <= 0 and not is_active:
            st.markdown("""
            <div class="warning-box">
                ⚠️ No credits available! Switch to Earn Mode to get some!
            </div>
            """, unsafe_allow_html=True)

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
    # ACTIVITY HISTORY - Clean card design
    # ========================================================================
    st.markdown('<div class="history-container fade-in">', unsafe_allow_html=True)

    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown('<div class="history-title">📋 Activity History</div>', unsafe_allow_html=True)
    with col2:
        if st.button("🗑️", key="clear_btn", help="Clear history", use_container_width=True):
            if st.session_state.history:
                clear_history()

    # Display history
    if not st.session_state.history:
        st.markdown("""
        <div class="empty-state">
            <span class="empty-emoji">📝</span>
            <div>No activities yet!</div>
            <div style="font-size: 0.9em;">Start earning to see your history.</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Show last 12 activities
        for item in st.session_state.history[:12]:
            activity_type = item['type']

            if activity_type == 'earn':
                emoji = '💪'
                label = 'Earned'
                sign = '+'
                color = '#52B788'
                css_class = 'earn'
            else:
                emoji = '🎮'
                label = 'Spent'
                sign = '-'
                color = '#FF6B6B'
                css_class = 'spend'

            timestamp = datetime.fromisoformat(item['timestamp'])
            time_str = format_time(item['duration'])

            st.markdown(f"""
            <div class="activity-card {css_class}">
                <div class="activity-content">
                    <div class="activity-info">
                        <div class="activity-label" style="color: {color};">
                            {emoji} {label}
                        </div>
                        <div class="activity-time">
                            {timestamp.strftime('%b %d at %I:%M %p')}
                        </div>
                    </div>
                    <div class="activity-duration" style="color: {color};">
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
