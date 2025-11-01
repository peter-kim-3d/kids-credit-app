# 🌟 Kids Credit Tracker 🌟

A **simplified, kid-friendly** time credit tracking app built with Python and Streamlit. Kids earn time credits through productive activities and spend them on fun activities!

![Kid-Friendly](https://img.shields.io/badge/Design-Kid%20Friendly-ff6b6b?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## ✨ New Simplified Design

### 🎯 Mode Switching Interface

Instead of showing two separate sections at once, the app now uses a **simple mode switcher**:

1. **Two mode buttons** at the top:
   - 💪 **Earn Mode** - for productive activities
   - 🎮 **Spend Mode** - for fun time

2. **Single timer display** that changes based on the selected mode
3. **Less clutter** - focus on one thing at a time
4. **Balance always visible** at the top
5. **Activity history** at the bottom

This makes it much **simpler and more intuitive** for kids to use!

---

## 🎨 Features

### 💪 Earn Mode
- Click "💪 Earn Mode" button to switch to earning
- Timer for tracking productive activities:
  - Study
  - Practice
  - Clean
  - Help
  - Read
- Big "🚀 Start Earning" button
- "⏹️ Stop & Save" button
- Credits automatically added when you stop
- 🎉 **Celebration with balloons!**

### 🎮 Spend Mode
- Click "🎮 Spend Mode" button to switch to spending
- Timer for tracking fun activities:
  - TV
  - Games
  - Tablet
  - Fun Time
- Big "▶️ Start Spending" button
- "⏹️ Stop" button
- Credits automatically deducted when you stop
- ⚠️ Warning if no credits available

### 🎨 Visual Design
- **Cheerful yellow gradient background**
- **Fun "Fredoka" font** (rounded, kid-friendly)
- **Purple gradient balance card** with spinning emoji
- **White timer card** with clean design
- **HUGE 5em timer** - easy to read!
- **Rainbow animated timer** when active
- **Simple, uncluttered layout**
- **No heavy rectangles or borders**

### 📊 Smart Features
- **Balance emoji** changes based on amount:
  - 😴 No credits
  - 😊 Small (< 5 min)
  - 😄 Medium (5-15 min)
  - 🤩 Good (15-30 min)
  - 🎉 Lots! (30+ min)
- **Mode remembers** your last selection
- **Timers auto-save** if you close the app
- **Activity history** with color-coded borders
- **Auto-refresh** every second when timer runs

---

## 🚀 Quick Start

### Install

```bash
pip install streamlit
```

### Run

```bash
streamlit run app.py
```

Opens at: `http://localhost:8501`

---

## ☁️ Deploy to Cloud (FREE!)

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repo: `peter-kim-3d/kids-credit-app`
5. Set file: `app.py`
6. Click "Deploy"!

Get a URL like: `https://kids-credit-tracker.streamlit.app`

Kids can access it from **any device** with internet!

---

## 🎮 How to Use

### For Kids

1. **Check your balance** at the top (big purple box with emoji)

2. **To earn credits:**
   - Click "💪 Earn Mode" button
   - Click "🚀 Start Earning"
   - Do your productive activity
   - Click "⏹️ Stop & Save"
   - Watch the balloons! 🎉

3. **To spend credits:**
   - Click "🎮 Spend Mode" button
   - Click "▶️ Start Spending"
   - Enjoy your fun time!
   - Click "⏹️ Stop" when done

4. **View history** at the bottom

### For Parents

- **Simple interface** - kids can use it independently
- **Visual feedback** - they see their balance grow
- **Teaching tool** for time management
- **No complicated options** - just earn or spend
- **Track history** to see patterns

---

## 🛠️ Technical Details

### Tech Stack
- **Python 3.7+**
- **Streamlit** - Web framework
- **JSON** - Data storage
- **CSS3** - Styling & animations

### Code Structure
```
app.py (620 lines)
├── Page Configuration
├── Custom CSS Styling
├── Data Persistence (save/load)
├── Session State Management
├── Helper Functions
├── Mode Switching
├── Timer Controls
└── Main App (UI)
```

### Session State Variables
```python
st.session_state.balance        # Total credits in seconds
st.session_state.current_mode   # 'earn' or 'spend'
st.session_state.earn_timer     # Earn timer start time
st.session_state.spend_timer    # Spend timer start time
st.session_state.history        # List of activities
st.session_state.show_celebration  # Show balloons flag
```

### Data Storage (credit_data.json)
```json
{
  "balance": 1234,
  "current_mode": "earn",
  "history": [...],
  "earn_timer": "2025-01-15T10:30:00",
  "spend_timer": null
}
```

---

## 🎯 Design Principles

### Simplicity
- ✅ Two mode buttons instead of two separate sections
- ✅ Single timer display (not two at once)
- ✅ Clean white card for timer area
- ✅ No heavy borders or rectangles
- ✅ Focus on current mode only

### Kid-Friendly
- ✅ Large, colorful buttons
- ✅ Fun emoji everywhere
- ✅ Bright, cheerful colors
- ✅ Animated elements (spinning, pulsing)
- ✅ Celebration effects
- ✅ Simple language

### Usability
- ✅ Balance always visible
- ✅ Clear visual hierarchy
- ✅ Mode buttons show active state
- ✅ Disabled buttons when appropriate
- ✅ Warning messages when needed
- ✅ Auto-refresh for real-time updates

---

## 📱 Mobile Support

Works perfectly on:
- 📱 Phones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktops

Responsive design adapts to all screen sizes!

---

## 🎓 Educational Value

Teaches kids:
- ⏰ **Time management** - tracking time spent
- 💰 **Earning & spending** - credits system
- 📊 **Cause & effect** - earn before you spend
- 🎯 **Goal setting** - work towards rewards
- 📈 **Self-tracking** - seeing their activities

---

## 🔧 Customization

### Change Colors
Edit the CSS gradients in `app.py` (lines 20-220)

### Adjust Balance Emoji
Modify `get_balance_emoji()` function (line 307-319)

### Change Activity Labels
Update subtitle text (lines 496, 517)

### Timer Refresh Rate
Adjust `time.sleep(1)` on line 610 (default: 1 second)

---

## 💡 Benefits Over Previous Versions

### Old Design ❌
- Two sections always visible (cluttered)
- Heavy colored rectangles
- Split attention between both modes
- More complex layout

### New Design ✅
- **Mode switching** - see only what you need
- **Clean white card** for timer
- **Focused** - one mode at a time
- **Simpler** - less visual clutter
- **Easier** for kids to understand

---

## 🐛 Troubleshooting

**Timer not updating?**
- It auto-refreshes every second
- Try refreshing the browser

**Mode button not changing?**
- The active mode shows as "primary" (brighter color)
- Click the other button to switch

**Can't start spending?**
- You need credits first
- Switch to Earn Mode and earn some!

**Lost my data?**
- Check if `credit_data.json` exists
- Data saves after every action

**App won't start?**
```bash
pip install --upgrade streamlit
python --version  # needs 3.7+
```

---

## 🔒 Privacy

- ✅ All data stored **locally**
- ✅ No external servers (except when deployed)
- ✅ No tracking or analytics
- ✅ Completely private
- ✅ When deployed, each user has separate data

---

## 📜 License

Free for personal use.

---

## 🎉 Start Tracking!

Help your kids learn time management with a fun, simple app they'll actually want to use! 🌟

---

**Made with ❤️ for families**
