# 🌟 Kids Credit Tracker 🌟

A **fun, colorful, and interactive** Python/Streamlit web app designed for kids to track time credits! Kids earn credits by doing productive activities and spend them on entertainment.

![Kid-Friendly Design](https://img.shields.io/badge/Design-Kid%20Friendly-ff6b6b?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

---

## ✨ Features

### 🎨 Kid-Friendly Design
- **Cheerful gradient background** (yellow and orange tones)
- **Fun "Fredoka" font** (imported from Google Fonts)
- **Animated elements**: bouncing title, glowing balance display, spinning emoji
- **Color-coded sections**:
  - 🟩 **Green** for earning credits (positive, encouraging)
  - 🟥 **Red/Orange** for spending credits (fun, exciting)
- **HUGE animated timers** that pulse and change colors when active
- **Celebration effects** with balloons when earning completes!

### 💪 Earn Credits
- Start timer when doing productive activities
- Activities include: Study, Practice, Clean, Help, Read
- Big "🚀 START EARNING" and "⏹️ STOP & SAVE" buttons
- Credits automatically added to balance
- Celebration message and balloons when you stop!

### 🎮 Spend Credits
- Start timer for fun activities (TV, Games, Tablet)
- Can only spend if you have credits
- Warning message if no credits available
- Credits automatically deducted from balance

### 📊 Visual Feedback
- **Balance emoji changes** based on credit amount:
  - 😴 No credits
  - 😊 Small amount (< 5 min)
  - 😄 Medium (5-15 min)
  - 🤩 Good amount (15-30 min)
  - 🎉 Lots of credits! (30+ min)
- **Animated timers** with gradient shifting colors
- **Glowing effects** on balance display
- **Smooth animations** throughout

### 📋 Activity History
- Clean, card-based history display
- Color-coded borders (green for earned, red for spent)
- Shows last 15 activities
- Timestamps in friendly format
- Clear button to reset history

### 💾 Data Persistence
- Auto-saves to `credit_data.json`
- Saves balance, history, and active timers
- Restores state when you return
- Works offline!

---

## 🚀 Running Locally

### Requirements
- Python 3.7 or higher
- Streamlit

### Installation

1. **Clone the repository:**
```bash
git clone https://github.com/peter-kim-3d/kids-credit-app.git
cd kids-credit-app
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run app.py
```

4. **Open in browser:**
The app will automatically open at `http://localhost:8501`

---

## ☁️ Deploy to Streamlit Cloud (FREE!)

Make the app accessible from anywhere on the internet!

### Step-by-Step Deployment

1. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Deploy the App**
   - Click "New app"
   - Repository: `peter-kim-3d/kids-credit-app`
   - Branch: Your main branch
   - Main file path: `app.py`
   - Click "Deploy"!

3. **Share the URL**
   - You'll get a URL like: `https://kids-credit-tracker.streamlit.app`
   - Kids can access it from any device!

### Deployment Benefits
- ✅ **Completely FREE** for public apps
- ✅ **Always accessible** via URL
- ✅ **Auto-updates** when you push changes
- ✅ **Mobile-friendly** design
- ✅ **No server maintenance** required

---

## 🎨 Design Highlights

### Visual Elements
- **Bouncing animated title** with colorful text shadow
- **Glowing purple balance card** with spinning emoji
- **Gradient backgrounds** on earn (green/blue) and spend (pink/yellow) sections
- **Huge 5em timers** that are easy to read from across the room
- **Animated active timers** with shifting rainbow gradients
- **Big, tactile buttons** with hover effects
- **Smooth transitions** and animations throughout

### UX/UI Principles
- **Simple and intuitive** - just two main actions
- **High contrast colors** for visibility
- **Large text and buttons** perfect for kids
- **Visual feedback** for every action
- **Encouraging messages** and celebrations
- **No clutter** - clean, focused design

### Accessibility
- **High readability** with large fonts
- **Clear visual hierarchy**
- **Color-coded sections** for easy navigation
- **Emoji icons** for visual communication
- **Responsive design** works on all screen sizes

---

## 🎯 How to Use

### For Kids

1. **Look at your balance** at the top (the big colorful box)
2. **To earn credits:**
   - Do something productive (study, practice, clean, help, read)
   - Click "🚀 START EARNING"
   - Do your activity
   - Click "⏹️ STOP & SAVE"
   - Watch the balloons! 🎉

3. **To spend credits:**
   - Check you have credits first
   - Click "▶️ START SPENDING"
   - Enjoy your fun time (TV, games, tablet)
   - Click "⏹️ STOP" when done

4. **Check your history** at the bottom to see all your activities!

### For Parents

1. **Set clear expectations** about what counts as earning vs spending
2. **Monitor the history** to see activity patterns
3. **Adjust the rules** as needed (1:1 ratio is default)
4. **Celebrate achievements** when kids earn credits
5. **Use it as a teaching tool** for time management

---

## 🛠️ Technical Details

### Tech Stack
- **Python 3.7+**
- **Streamlit** - Web app framework
- **JSON** - Data persistence
- **Google Fonts** - Fredoka font
- **CSS3** - Animations and styling

### File Structure
```
kids-credit-app/
├── app.py              # Main Streamlit application (650+ lines)
├── requirements.txt    # Python dependencies
├── credit_data.json    # Auto-generated data storage
├── .gitignore         # Git ignore rules
└── README.md          # This file
```

### Key Code Features
- **Modular functions** with clear docstrings
- **Session state management** for persistent data
- **Auto-refresh mechanism** for real-time timer updates
- **Celebration triggers** for positive reinforcement
- **Extensive CSS** for custom styling
- **Comprehensive comments** explaining logic

### Data Storage
```json
{
  "balance": 1234,           // Total credits in seconds
  "history": [...],          // Array of activity objects
  "earn_timer": "ISO-8601",  // Active earn timer timestamp
  "spend_timer": "ISO-8601"  // Active spend timer timestamp
}
```

---

## 🎁 Benefits Over Manual System

### Old Manual System ❌
- Turn timer on/off manually
- Write times on paper
- Calculate balance by hand
- Easy to make mistakes
- Paper gets lost
- No history tracking
- Boring and tedious

### This App ✅
- **Automatic timers** with one click
- **Auto-calculation** of balance
- **Never lose data** (saved to file)
- **Beautiful visual design** kids love
- **Complete history** always available
- **Celebration effects** for motivation
- **Fun and engaging!**

---

## 🔧 Customization

### Change Colors
Edit the CSS gradients in `app.py` around lines 20-270

### Adjust Balance Emoji Thresholds
Modify the `get_balance_emoji()` function around line 351

### Change Activity Suggestions
Update the text in the earn/spend sections around lines 507-540

### Modify Timer Update Frequency
Adjust the `time.sleep(1)` value on line 639 (currently 1 second)

---

## 🐛 Troubleshooting

**Timers not updating?**
- The app auto-refreshes every second when a timer is active
- Refresh the browser page if it seems stuck

**Lost data?**
- Check if `credit_data.json` exists
- Data saves after every action

**Can't start spending?**
- You need credits in your balance first
- Earn some credits by using the earn timer

**Animations not smooth?**
- Check your browser supports CSS animations
- Try a modern browser (Chrome, Firefox, Safari, Edge)

**App won't start?**
- Ensure Streamlit is installed: `pip install streamlit`
- Check Python version: `python --version` (needs 3.7+)

---

## 📱 Mobile Support

The app is fully responsive and works great on:
- 📱 Phones
- 📱 Tablets
- 💻 Laptops
- 🖥️ Desktops

All animations and interactions work on touch devices!

---

## 🎓 Educational Value

This app teaches kids:
- ⏰ **Time management** - understanding time spent on activities
- 💰 **Resource management** - credits as a limited resource
- 📊 **Cause and effect** - earn before you spend
- 🎯 **Goal setting** - working towards a reward
- 📈 **Self-awareness** - tracking their own activities

---

## 🔒 Privacy & Security

- ✅ All data stored **locally** in `credit_data.json`
- ✅ **No external servers** (except when deployed)
- ✅ **No personal information** collected
- ✅ **No tracking or analytics**
- ✅ **Completely private** and secure
- ✅ When deployed, each instance has **isolated data**

---

## 📜 License

Free to use and modify for **personal use**.

---

## 🙏 Credits

- **Streamlit** - Amazing Python web framework
- **Google Fonts** - Fredoka font family
- **Emoji** - For making everything more fun!

---

## 🎉 Have Fun!

Enjoy using the Kids Credit Tracker! Make learning and time management fun and rewarding! 🌟

---

**Made with ❤️ for kids everywhere**
