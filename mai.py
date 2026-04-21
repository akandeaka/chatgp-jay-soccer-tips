# ==========================================
# FORTRESS AI v4 - RENDER VERSION
# ==========================================

from datetime import datetime, timedelta
import random


# ==========================================
# 1. FETCH MATCHES (MOCK DATA FOR NOW)
# ==========================================

def fetch_matches():
    now = datetime.now()

    leagues = ["EPL", "Bundesliga", "La Liga", "Random League"]

    matches = []

    for i in range(20):
        match = {
            "teams": f"Team{i} vs Team{i+1}",
            "league": random.choice(leagues),
            "kickoff": now + timedelta(hours=random.randint(1, 12)),
            "home_odds": round(random.uniform(1.2, 2.5), 2),
            "draw_odds": round(random.uniform(3.0, 4.5), 2),
            "away_odds": round(random.uniform(3.5, 8.0), 2),
            "form_score": round(random.uniform(0.4, 0.9), 2),
            "over25": random.randint(40, 80),
            "btts": random.randint(40, 80)
        }

        matches.append(match)

    return matches


# ==========================================
# 2. TIME FILTER (1–3 HOURS WINDOW)
# ==========================================

def is_within_time_window(kickoff):
    now = datetime.now()
    diff = (kickoff - now).total_seconds() / 3600
    return 1 <= diff <= 3


# ==========================================
# 3. MATCH QUALITY FILTER
# ==========================================

def is_good_match(match):

    if not (1.25 <= match["home_odds"] <= 1.70):
        return False

    if match["form_score"] < 0.6:
        return False

    if match["over25"] < 55:
        return False

    if match["league"] not in ["EPL", "Bundesliga", "La Liga"]:
        return False

    return True


# ==========================================
# 4. SCORING ENGINE
# ==========================================

def calculate_score(match):

    score = (
        match["form_score"] * 0.4 +
        (match["over25"] / 100) * 0.3 +
        (match["btts"] / 100) * 0.2 +
        0.1
    )

    return round(score, 2)


# ==========================================
# 5. ANALYSIS ENGINE
# ==========================================

def analyze_matches(matches):

    best_picks = []

    for match in matches:

        if not is_within_time_window(match["kickoff"]):
            continue

        if not is_good_match(match):
            continue

        score = calculate_score(match)

        if score >= 0.70:
            best_picks.append((match, score))

    best_picks.sort(key=lambda x: x[1], reverse=True)

    return best_picks[:5]


# ==========================================
# 6. OUTPUT SYSTEM
# ==========================================

def display_picks(picks):

    print("\n==============================")
    print("🔥 FORTRESS AI PICKS")
    print("==============================")

    if not picks:
        print("❌ No strong matches found\n")
        return

    for match, score in picks:
        print(f"Match: {match['teams']}")
        print(f"League: {match['league']}")
        print(f"Kickoff: {match['kickoff'].strftime('%H:%M')}")
        print(f"Odds: {match['home_odds']}")
        print(f"Form: {match['form_score']}")
        print(f"Over2.5: {match['over25']}%")
        print(f"BTTS: {match['btts']}%")
        print(f"Confidence: {int(score * 100)}%")
        print("------------------------------")


# ==========================================
# 7. MAIN EXECUTION (IMPORTANT FOR RENDER)
# ==========================================

def run_system():

    print(f"\n⏰ Running Fortress AI at {datetime.now()}")

    matches = fetch_matches()

    picks = analyze_matches(matches)

    display_picks(picks)


# ==========================================
# ENTRY POINT
# ==========================================

if __name__ == "__main__":
    run_system()
