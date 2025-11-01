# Kids Credit Tracker

A simple Python/Streamlit web app to help kids track time credits. Kids earn credits by doing productive activities and spend them on entertainment.

## Features

- **💪 Earn Credits**: Start a timer when doing productive activities (study, practice, chores, etc.)
- **🎮 Spend Credits**: Use earned credits for fun activities (TV, tablet, games, etc.)
- **⏱️ Automatic Tracking**: Built-in timers that update in real-time
- **💾 Auto-Save**: All data saves automatically to a JSON file
- **📋 Activity History**: View all past earning and spending with timestamps
- **Simple Interface**: Just two options - Earn or Spend!

## How to Use

### Earning Credits

1. Click **▶️ Start Earning** when your child starts a productive activity
2. Let them do their activity (studying, practicing, cleaning, etc.)
3. Click **⏹️ Stop Earning** when done
4. Credits are automatically added to their balance!

### Spending Credits

1. Click **▶️ Start Spending** when they want screen time or fun activities
2. Let them enjoy their earned time (TV, tablet, games, etc.)
3. Click **⏹️ Stop Spending** when done
4. Credits are automatically deducted from their balance!

### Important Notes

- Kids must have credits in their balance before they can spend
- Timers update automatically every second
- All data is saved automatically
- Can't start spending if balance is zero

## Running Locally

### Requirements

- Python 3.7 or higher

### Installation

1. Clone this repository or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deploy to Streamlit Cloud (FREE)

Deploy this app for free so kids can access it from anywhere on the internet!

### Step-by-Step Deployment

1. **Push your code to GitHub**
   - Make sure your repository is public or you have Streamlit Cloud access to private repos

2. **Go to Streamlit Cloud**
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

3. **Deploy the App**
   - Click "New app"
   - Select your repository: `peter-kim-3d/kids-credit-app`
   - Branch: Your main branch
   - Main file path: `app.py`
   - Click "Deploy"!

4. **Share the URL**
   - Once deployed, you'll get a URL like: `https://your-app-name.streamlit.app`
   - Kids can access it from any device with internet!

### Deployment Notes

- Streamlit Cloud is **completely free** for public apps
- The app will auto-save data to `credit_data.json`
- Data persists between sessions
- The app auto-refreshes when timers are running

## Technical Details

### Files

- `app.py` - Main Streamlit application (300+ lines)
- `requirements.txt` - Python dependencies
- `credit_data.json` - Auto-generated data storage (not in git)
- `.gitignore` - Excludes data file from version control

### Technologies Used

- Python 3.7+
- Streamlit - Web app framework
- JSON - Data persistence

### Data Storage

- All data stored in `credit_data.json` locally
- Includes: balance, history, and active timers
- Auto-saves after every action

## Tips for Parents

1. **Keep it Simple**: Just two buttons - Earn and Spend
2. **Fair Exchange**: The app uses a 1:1 ratio (1 second earned = 1 second spent)
3. **Set Expectations**: Explain what activities count as "earning" vs "spending"
4. **Review Together**: Check the activity history to discuss time management
5. **Multi-Device**: Once deployed to Streamlit Cloud, accessible from any device

## Benefits Over Manual System

Your old manual system required:
- Turning timer on/off
- Writing down times on paper
- Calculating balance manually

This app automatically:
- Tracks all timers
- Calculates balance instantly
- Saves history permanently
- Shows everything in one view

## Troubleshooting

**Timers not updating?**
- The app auto-refreshes every second when a timer is active
- If it seems stuck, refresh the page

**Lost data?**
- Check if `credit_data.json` exists in the app directory
- Data is saved after every Start/Stop action

**Can't start spending timer?**
- Make sure there are credits in the balance
- Earn credits first by using the Earn timer

**App won't start?**
- Make sure Streamlit is installed: `pip install streamlit`
- Check Python version: `python --version` (needs 3.7+)

## Privacy

- Data is stored locally in `credit_data.json`
- When deployed, each deployment has its own data storage
- No personal information is collected or transmitted
- Completely private and secure

## License

Free to use and modify for personal use.
