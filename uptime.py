#!/usr/bin/env python3
"""
Bird's Uptime Robot Pro - Termux Optimized
Paid Version with 100 Devices - Owner Exclusive
"""

import requests
import time
import random
import json
import os
import re
from datetime import datetime

# ============= Configuration =============
BOT_TOKEN = "8242332978:AAGbs98UkL1UNyFVrNN1tJQQ22B6K0i1dZ0"
OWNER_ID = "6254639490"
DATA_FILE = "monitored_urls.json"
LAST_STATUS_FILE = "last_status.json"
PAID_USERS_FILE = "paid_users.json"
CONTACT_MESSAGE = "💎 This is a PAID bot! Contact @Bird_Studio to get access.\n\nPrice: Contact for pricing 💰"

# ============= 100 Device Pool =============
DEVICE_POOL = [
    # Samsung (15 devices)
    {"brand": "Samsung", "model": "SM-S908B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-S908B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-S906E", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-S906E) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-G998B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-G996B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-G996B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-G991B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-G991B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-A536B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-A536B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-A536E", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-A536E) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-A346E", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-A346E) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-A346B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-A346B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-M536B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-M536B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-G973F", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; SM-G973F) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-N986B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-N986B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-F946B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-F946B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-F731B", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-F731B) AppleWebKit/537.36"},
    {"brand": "Samsung", "model": "SM-A047F", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; SM-A047F) AppleWebKit/537.36"},
    
    # Xiaomi/Redmi/POCO (15 devices)
    {"brand": "Xiaomi", "model": "2304FPN6DG", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 2304FPN6DG) AppleWebKit/537.36"},
    {"brand": "Xiaomi", "model": "2210132G", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 2210132G) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "23013PC75G", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 23013PC75G) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "23021RAA2Y", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 23021RAA2Y) AppleWebKit/537.36"},
    {"brand": "POCO", "model": "23013PC75G", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 23013PC75G) AppleWebKit/537.36"},
    {"brand": "POCO", "model": "23049PCD8G", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 23049PCD8G) AppleWebKit/537.36"},
    {"brand": "Xiaomi", "model": "21091116AG", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; 21091116AG) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "M2012K11AG", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; M2012K11AG) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "2201116SG", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; 2201116SG) AppleWebKit/537.36"},
    {"brand": "Xiaomi", "model": "M2101K7AG", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; M2101K7AG) AppleWebKit/537.36"},
    {"brand": "Xiaomi", "model": "22041216I", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; 22041216I) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "22071212AG", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 22071212AG) AppleWebKit/537.36"},
    {"brand": "POCO", "model": "M2012K11AG", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; M2012K11AG) AppleWebKit/537.36"},
    {"brand": "Xiaomi", "model": "Mi 11 Ultra", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Mi 11 Ultra) AppleWebKit/537.36"},
    {"brand": "Redmi", "model": "Note 12 Pro+", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Note 12 Pro+) AppleWebKit/537.36"},
    
    # OnePlus (8 devices)
    {"brand": "OnePlus", "model": "LE2121", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; LE2121) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "KB2001", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; KB2001) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "NE2213", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; NE2213) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "CPH2449", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; CPH2449) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "CPH2413", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; CPH2413) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "IV2201", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; IV2201) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "DN2103", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; DN2103) AppleWebKit/537.36"},
    {"brand": "OnePlus", "model": "AC2001", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; AC2001) AppleWebKit/537.36"},
    
    # Vivo (10 devices)
    {"brand": "vivo", "model": "V2111", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; V2111) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2230", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; V2230) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2244", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; V2244) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2217", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; V2217) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2130", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; V2130) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2105", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; V2105) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "V2166", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; V2166) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "X70 Pro+", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; X70 Pro+) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "X90 Pro", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; X90 Pro) AppleWebKit/537.36"},
    {"brand": "vivo", "model": "iQOO 11", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; iQOO 11) AppleWebKit/537.36"},
    
    # OPPO (10 devices)
    {"brand": "OPPO", "model": "CPH2467", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; CPH2467) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "CPH2451", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; CPH2451) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "CPH2409", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; CPH2409) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "CPH2381", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; CPH2381) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "CPH2343", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; CPH2343) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "CPH2273", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; CPH2273) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "Reno8", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Reno8) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "Find X5", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Find X5) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "A78", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; A78) AppleWebKit/537.36"},
    {"brand": "OPPO", "model": "A58", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; A58) AppleWebKit/537.36"},
    
    # Realme (10 devices)
    {"brand": "realme", "model": "RMX3562", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; RMX3562) AppleWebKit/537.36"},
    {"brand": "realme", "model": "RMX3560", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; RMX3560) AppleWebKit/537.36"},
    {"brand": "realme", "model": "RMX3516", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; RMX3516) AppleWebKit/537.36"},
    {"brand": "realme", "model": "RMX3472", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; RMX3472) AppleWebKit/537.36"},
    {"brand": "realme", "model": "RMX3396", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; RMX3396) AppleWebKit/537.36"},
    {"brand": "realme", "model": "GT 3", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; GT 3) AppleWebKit/537.36"},
    {"brand": "realme", "model": "GT 2 Pro", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; GT 2 Pro) AppleWebKit/537.36"},
    {"brand": "realme", "model": "10 Pro+", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; 10 Pro+) AppleWebKit/537.36"},
    {"brand": "realme", "model": "C55", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; C55) AppleWebKit/537.36"},
    {"brand": "realme", "model": "C33", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; C33) AppleWebKit/537.36"},
    
    # Motorola (10 devices)
    {"brand": "Motorola", "model": "moto g73", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; moto g73) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "moto g72", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; moto g72) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "moto g62", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; moto g62) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "edge 40", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; edge 40) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "edge 30", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; edge 30) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "moto g32", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; moto g32) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "moto g22", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; moto g22) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "moto g13", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; moto g13) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "razr 40", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; razr 40) AppleWebKit/537.36"},
    {"brand": "Motorola", "model": "edge 20", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; edge 20) AppleWebKit/537.36"},
    
    # Google Pixel (8 devices)
    {"brand": "Google", "model": "Pixel 8", "android": "14", "ua": "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 8 Pro", "android": "14", "ua": "Mozilla/5.0 (Linux; Android 14; Pixel 8 Pro) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 7", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 7 Pro", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 7 Pro) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 6", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 6) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 6 Pro", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 5", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Pixel 5) AppleWebKit/537.36"},
    {"brand": "Google", "model": "Pixel 4a", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Pixel 4a) AppleWebKit/537.36"},
    
    # Huawei (8 devices)
    {"brand": "Huawei", "model": "P50 Pro", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; P50 Pro) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "Mate 50", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Mate 50) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "Nova 10", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Nova 10) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "P40 Pro", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; P40 Pro) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "Mate 40", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Mate 40) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "Y9a", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Y9a) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "P30 Pro", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; P30 Pro) AppleWebKit/537.36"},
    {"brand": "Huawei", "model": "Nova 8", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Nova 8) AppleWebKit/537.36"},
    
    # ASUS (6 devices)
    {"brand": "ASUS", "model": "ROG Phone 7", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; ROG Phone 7) AppleWebKit/537.36"},
    {"brand": "ASUS", "model": "ROG Phone 6", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; ROG Phone 6) AppleWebKit/537.36"},
    {"brand": "ASUS", "model": "Zenfone 10", "android": "13", "ua": "Mozilla/5.0 (Linux; Android 13; Zenfone 10) AppleWebKit/537.36"},
    {"brand": "ASUS", "model": "Zenfone 9", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Zenfone 9) AppleWebKit/537.36"},
    {"brand": "ASUS", "model": "Zenfone 8", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; Zenfone 8) AppleWebKit/537.36"},
    {"brand": "ASUS", "model": "ROG Phone 5", "android": "12", "ua": "Mozilla/5.0 (Linux; Android 12; ROG Phone 5) AppleWebKit/537.36"},
]

# ============= Data Management =============
def load_data():
    """Load monitored URLs"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(urls):
    """Save URL data"""
    with open(DATA_FILE, 'w') as f:
        json.dump(urls, f, indent=2)

def load_last_status():
    """Load previous status"""
    if os.path.exists(LAST_STATUS_FILE):
        with open(LAST_STATUS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_last_status(status):
    """Save current status"""
    with open(LAST_STATUS_FILE, 'w') as f:
        json.dump(status, f, indent=2)

def load_paid_users():
    """Load paid users"""
    if os.path.exists(PAID_USERS_FILE):
        with open(PAID_USERS_FILE, 'r') as f:
            return json.load(f)
    return {"users": []}

def is_paid_user(user_id):
    """Check if user is paid"""
    paid_data = load_paid_users()
    return str(user_id) in paid_data.get("users", []) or str(user_id) == OWNER_ID

def add_paid_user(user_id):
    """Add paid user (Owner only)"""
    paid_data = load_paid_users()
    if str(user_id) not in paid_data["users"]:
        paid_data["users"].append(str(user_id))
        with open(PAID_USERS_FILE, 'w') as f:
            json.dump(paid_data, f, indent=2)
        return True
    return False

def remove_paid_user(user_id):
    """Remove paid user (Owner only)"""
    paid_data = load_paid_users()
    if str(user_id) in paid_data["users"]:
        paid_data["users"].remove(str(user_id))
        with open(PAID_USERS_FILE, 'w') as f:
            json.dump(paid_data, f, indent=2)
        return True
    return False

# ============= Telegram Functions =============
def send_telegram(chat_id, text, keyboard=None):
    """Send message to Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "HTML"
    }
    
    if keyboard:
        data["reply_markup"] = json.dumps(keyboard)
    
    try:
        response = requests.post(url, data=data, timeout=10)
        return response.json()
    except Exception as e:
        print(f"Telegram error: {e}")
        return None

def get_updates(offset=None):
    """Get updates from Telegram"""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
    params = {"timeout": 30}
    if offset:
        params["offset"] = offset
    
    try:
        response = requests.get(url, params=params, timeout=35)
        return response.json().get("result", [])
    except:
        return []

# ============= Keyboards =============
def get_main_keyboard():
    """Create main keyboard"""
    return {
        "keyboard": [
            ["🕊️ Bird's Uptime Robot Pro"],
            ["📊 Status Check", "➕ Add URL"],
            ["🗑️ Delete URL", "📋 My URLs"],
            ["💎 Premium Info", "🆘 Help"]
        ],
        "resize_keyboard": True,
        "one_time_keyboard": False
    }

def get_back_keyboard():
    """Back button"""
    return {
        "keyboard": [["🔙 Main Menu"]],
        "resize_keyboard": True
    }

# ============= URL Checker =============
def check_url_status(url):
    """Check URL with random device"""
    device = random.choice(DEVICE_POOL)
    headers = {
        "User-Agent": device["ua"],
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Connection": "keep-alive",
    }
    
    try:
        start = time.time()
        response = requests.get(url, headers=headers, timeout=15, allow_redirects=True)
        response_time = int((time.time() - start) * 1000)
        
        if response.status_code == 200:
            return {
                "status": "UP",
                "emoji": "✅",
                "code": response.status_code,
                "time": response_time,
                "device": device
            }
        else:
            return {
                "status": "DOWN",
                "emoji": "❌",
                "code": response.status_code,
                "time": response_time,
                "device": device
            }
    except requests.Timeout:
        return {
            "status": "DOWN",
            "emoji": "❌",
            "code": "Timeout",
            "time": 15000,
            "device": device
        }
    except Exception as e:
        return {
            "status": "DOWN",
            "emoji": "❌",
            "code": str(e)[:30],
            "time": 0,
            "device": device
        }

# ============= Message Processing =============
def process_message(message):
    """Process user messages"""
    chat_id = str(message.get("chat", {}).get("id"))
    text = message.get("text", "")
    user_id = str(message.get("from", {}).get("id"))
    
    # Check if paid user
    if not is_paid_user(user_id):
        send_telegram(chat_id, f"⛔ {CONTACT_MESSAGE}\n\nYour ID: <code>{user_id}</code>")
        if user_id != OWNER_ID:
            send_telegram(OWNER_ID, f"🔔 New user trying to access!\n\nUser ID: <code>{user_id}</code>\nName: {message.get('from', {}).get('first_name', 'Unknown')}\n\nUse /adduser {user_id} to grant access")
        return None
    
    # Owner commands
    if user_id == OWNER_ID:
        if text.startswith("/adduser"):
            parts = text.split()
            if len(parts) == 2:
                new_user_id = parts[1]
                if add_paid_user(new_user_id):
                    send_telegram(chat_id, f"✅ User <code>{new_user_id}</code> added to premium!")
                    send_telegram(new_user_id, "🎉 Congratulations! You now have access to Bird's Uptime Robot Pro!\n\nUse /start to begin.")
                else:
                    send_telegram(chat_id, f"⚠️ User <code>{new_user_id}</code> already has access.")
            return
        
        elif text.startswith("/removeuser"):
            parts = text.split()
            if len(parts) == 2:
                user_to_remove = parts[1]
                if remove_paid_user(user_to_remove):
                    send_telegram(chat_id, f"✅ User <code>{user_to_remove}</code> removed from premium!")
                    send_telegram(user_to_remove, "⚠️ Your premium access has been revoked. Contact @Bird_Studio to renew.")
                else:
                    send_telegram(chat_id, f"⚠️ User <code>{user_to_remove}</code> not found.")
            return
        
        elif text == "/listusers":
            paid_data = load_paid_users()
            users_list = "\n".join([f"• <code>{uid}</code>" for uid in paid_data["users"]])
            send_telegram(chat_id, f"📋 <b>Premium Users:</b>\n\n{users_list}\n\nTotal: {len(paid_data['users'])}")
            return
    
    # Process commands
    if text in ["/start", "🔙 Main Menu"]:
        send_welcome(chat_id)
    
    elif text == "🕊️ Bird's Uptime Robot Pro":
        send_bird_info(chat_id)
    
    elif text == "📊 Status Check":
        send_status(chat_id)
    
    elif text == "➕ Add URL":
        send_ask_url(chat_id, "add")
    
    elif text == "🗑️ Delete URL":
        handle_delete_url(chat_id)
    
    elif text == "📋 My URLs":
        send_list_urls(chat_id)
    
    elif text == "💎 Premium Info":
        send_premium_info(chat_id)
    
    elif text == "🆘 Help":
        send_help(chat_id)
    
    elif text.startswith("http://") or text.startswith("https://"):
        add_new_url(chat_id, text, user_id)
    
    elif text.startswith("/delete"):
        url_to_delete = text.replace("/delete", "").strip()
        if url_to_delete:
            remove_url(chat_id, url_to_delete)
        else:
            send_telegram(chat_id, "❌ Please provide a URL to delete.\nExample: <code>/delete https://example.com</code>", get_back_keyboard())
    
    else:
        send_telegram(chat_id, "❓ Unknown command. Use /start for menu.", get_back_keyboard())

def send_welcome(chat_id):
    """Welcome message"""
    welcome_text = """
✨ <b>Bird's Uptime Robot Pro</b> ✨

💎 <b>Premium Uptime Monitor</b>

📱 <b>Features:</b>
• Monitor unlimited websites
• 100 Android devices pool
• Auto-check every 5 minutes
• Instant Telegram notifications
• Premium device spoofing

<b>Total Devices:</b> {} Premium devices
<b>Status:</b> 🟢 Online

Use buttons below to get started!
    """.format(len(DEVICE_POOL))
    
    send_telegram(chat_id, welcome_text, get_main_keyboard())

def send_bird_info(chat_id):
    """Bot information"""
    text = """
🕊️ <b>Bird's Uptime Robot Pro v3.0</b>

💎 <b>Premium Edition</b>

<b>How it works:</b>
1️⃣ Add your website URL
2️⃣ Bot checks every 5 minutes
3️⃣ 100 Premium Android devices spoofing
4️⃣ Instant alert on status change

<b>Device Pool:</b>
• Samsung | Xiaomi | OnePlus
• Vivo | Oppo | Realme
• Motorola | Google | Huawei | ASUS
• Total: {} premium devices

<b>Auto Wake-up:</b> Your Render sites never sleep!
<b>Status:</b> 🔒 Premium Activated
    """.format(len(DEVICE_POOL))
    
    keyboard = {
        "inline_keyboard": [
            [{"text": "📊 Check Status Now", "callback_data": "status"}],
            [{"text": "➕ Add Your Site", "callback_data": "add"}]
        ]
    }
    send_telegram(chat_id, text, keyboard)

def send_premium_info(chat_id):
    """Premium information"""
    text = """
💎 <b>Premium Status</b>

✅ <b>Your Premium is ACTIVE!</b>

<b>Benefits:</b>
• 100 Android devices
• Priority monitoring
• Faster check interval
• No ads
• 24/7 support

<b>Devices:</b> {} rotating
<b>Status:</b> 🔒 Premium
    """.format(len(DEVICE_POOL))
    send_telegram(chat_id, text, get_main_keyboard())

def send_ask_url(chat_id, action):
    """Ask for URL"""
    if action == "add":
        text = "🔗 <b>Send me the URL to monitor:</b>\n\nExample: <code>https://your-site.onrender.com</code>\n\nJust type or paste the URL."
    else:
        urls = load_data()
        if not urls:
            send_telegram(chat_id, "📭 No URLs are being monitored!", get_main_keyboard())
            return
        text = "🗑️ <b>Send me the URL to remove:</b>\n\nMonitored URLs:\n" + "\n".join([f"• <code>{url}</code>" for url in urls.keys()])
    
    send_telegram(chat_id, text, get_back_keyboard())

def handle_delete_url(chat_id):
    """Handle URL deletion"""
    urls = load_data()
    if not urls:
        send_telegram(chat_id, "📭 No URLs are being monitored!", get_main_keyboard())
        return
    
    text = "🗑️ <b>Delete URL</b>\n\nSelect URL to delete:\n\n"
    keyboard_buttons = []
    
    for url in urls.keys():
        keyboard_buttons.append([f"❌ /delete {url}"])
        text += f"• <code>{url}</code>\n"
    
    text += "\nClick the delete button below:"
    keyboard_buttons.append(["🔙 Main Menu"])
    
    keyboard = {
        "keyboard": keyboard_buttons,
        "resize_keyboard": True
    }
    
    send_telegram(chat_id, text, keyboard)

def add_new_url(chat_id, url, user_id):
    """Add new URL"""
    urls = load_data()
    
    if url in urls:
        send_telegram(chat_id, "⚠️ This URL is already being monitored!", get_main_keyboard())
        return
    
    urls[url] = {"status": "UNKNOWN", "added_by": user_id}
    save_data(urls)
    
    text = f"✅ <b>URL Added Successfully!</b>\n\nURL: <code>{url}</code>\nTotal: {len(urls)} URLs\n\n🔄 Next check in 5 minutes"
    send_telegram(chat_id, text, get_main_keyboard())
    
    # Notify owner
    if user_id != OWNER_ID:
        send_telegram(OWNER_ID, f"➕ New URL added\nUser: {user_id}\nURL: {url}")

def remove_url(chat_id, url):
    """Remove URL"""
    urls = load_data()
    
    if url not in urls:
        send_telegram(chat_id, f"❌ URL not found!\n\n<code>{url}</code> is not in monitoring list.", get_main_keyboard())
        return
    
    del urls[url]
    save_data(urls)
    
    # Remove from last status
    last_status = load_last_status()
    if url in last_status:
        del last_status[url]
        save_last_status(last_status)
    
    send_telegram(chat_id, f"🗑️ <b>URL Deleted Successfully!</b>\n\n<code>{url}</code>\nNow monitoring: {len(urls)} URLs", get_main_keyboard())
    
    # Notify owner
    if chat_id != OWNER_ID:
        send_telegram(OWNER_ID, f"🗑️ URL deleted by {chat_id}: {url}")

def send_status(chat_id):
    """Send status of all URLs"""
    urls = load_data()
    
    if not urls:
        send_telegram(chat_id, "📭 No URLs are being monitored!\n\nUse '➕ Add URL' to add one.", get_main_keyboard())
        return
    
    send_telegram(chat_id, "🔍 Checking all URLs with premium devices... Please wait.")
    
    status_report = []
    updated_status = {}
    last_status = load_last_status()
    
    for url in urls.keys():
        result = check_url_status(url)
        updated_status[url] = result["status"]
        
        status_text = f"{result['emoji']} <b>{result['status']}</b>\n"
        status_text += f"URL: <code>{url}</code>\n"
        status_text += f"Device: {result['device']['brand']} {result['device']['model']}\n"
        if result['status'] == "UP":
            status_text += f"Response: {result['time']}ms (HTTP {result['code']})\n"
        else:
            status_text += f"Error: {result['code']}\n"
        
        status_report.append(status_text)
        
        # Notify on status change
        if url in last_status and last_status[url] != result["status"]:
            notify_text = f"🔄 <b>Status Changed!</b>\n\nURL: {url}\nOld: {last_status[url]}\nNew: {result['status']}\nDevice: {result['device']['brand']} {result['device']['model']}"
            send_telegram(OWNER_ID, notify_text)
    
    save_last_status(updated_status)
    
    report = "📊 <b>Uptime Status Report</b>\n\n" + "\n".join(status_report)
    report += f"\n⏰ Last checked: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    report += f"\n💎 Premium Devices: {len(DEVICE_POOL)}"
    
    send_telegram(chat_id, report, get_main_keyboard())

def send_list_urls(chat_id):
    """List monitored URLs"""
    urls = load_data()
    last_status = load_last_status()
    
    if not urls:
        send_telegram(chat_id, "📭 No URLs are being monitored!", get_main_keyboard())
        return
    
    text = "📋 <b>Monitored URLs:</b>\n\n"
    for i, (url, info) in enumerate(urls.items(), 1):
        status = last_status.get(url, "UNKNOWN")
        emoji = "✅" if status == "UP" else "❌" if status == "DOWN" else "🔄"
        text += f"{i}. {emoji} <code>{url}</code>\n"
    
    text += f"\n📊 Total: {len(urls)} URLs\n"
    text += f"💎 Premium Devices: {len(DEVICE_POOL)}"
    
    keyboard = {
        "inline_keyboard": [
            [{"text": "📊 Check Now", "callback_data": "status"}],
            [{"text": "➕ Add URL", "callback_data": "add"}]
        ]
    }
    send_telegram(chat_id, text, keyboard)

def send_help(chat_id):
    """Help message"""
    help_text = """
🤖 <b>Bird's Uptime Robot Pro - Help Guide</b>

<b>📌 Commands:</b>
• /start - Show main menu
• 📊 Status Check - Check all URLs now
• ➕ Add URL - Add new website to monitor
• 🗑️ Delete URL - Remove website from monitoring
• 📋 My URLs - Show all monitored URLs

<b>🔧 How it works:</b>
1. Add your Render/website URL
2. Bot checks every 5 minutes
3. 100 Premium Android devices spoofing
4. Instant alert on status change

<b>💡 Tips:</b>
• Your Render site will never sleep
• Supports any HTTP/HTTPS URL
• Premium access required

<b>💎 Premium Support:</b> @Bird_Studio
    """
    
    send_telegram(chat_id, help_text, get_main_keyboard())

# ============= Auto Uptime Check =============
def auto_check():
    """Automatic check every 5 minutes"""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 🔍 Running auto uptime check...")
    
    urls = load_data()
    if not urls:
        return
    
    last_status = load_last_status()
    changed = False
    
    for url in urls.keys():
        result = check_url_status(url)
        new_status = result["status"]
        
        if url not in last_status or last_status[url] != new_status:
            last_status[url] = new_status
            changed = True
            
            # Status change notification
            emoji = "🟢" if new_status == "UP" else "🔴"
            notify_text = f"{emoji} <b>Status Changed!</b>\n\nURL: <code>{url}</code>\nNew: {new_status}\nDevice: {result['device']['brand']} {result['device']['model']}\nTime: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            send_telegram(OWNER_ID, notify_text)
            
            print(f"  → {url[:50]}... {new_status} ({result['device']['brand']})")
    
    if changed:
        save_last_status(last_status)

# ============= Main Loop =============
def main():
    print("="*50)
    print("🤖 Bird's Uptime Robot Pro Starting...")
    print(f"📱 Loaded {len(DEVICE_POOL)} Premium Android devices")
    print(f"📊 Monitoring {len(load_data())} URLs")
    print(f"👑 Owner ID: {OWNER_ID}")
    print(f"💎 Premium Users: {len(load_paid_users().get('users', []))}")
    print("="*50)
    
    # Startup notification
    send_telegram(OWNER_ID, "✅ <b>Bird's Uptime Robot Pro is ONLINE!</b>\n\nPremium Edition Active\n100 Devices Ready\n\nOwner Commands:\n/adduser [id] - Add premium user\n/removeuser [id] - Remove user\n/listusers - List all users")
    
    last_update_id = 0
    
    while True:
        try:
            # Check Telegram updates
            updates = get_updates(last_update_id + 1 if last_update_id else None)
            
            for update in updates:
                last_update_id = update.get("update_id")
                message = update.get("message")
                
                if message:
                    process_message(message)
            
            # Auto check every 5 minutes
            current_minute = datetime.now().minute
            if current_minute % 5 == 0 and datetime.now().second < 30:
                auto_check()
                time.sleep(30)
            
            time.sleep(1)
            
        except KeyboardInterrupt:
            print("\n👋 Bot stopped by user")
            send_telegram(OWNER_ID, "🛑 Bot stopped!")
            break
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)

if __name__ == "__main__":
    main()