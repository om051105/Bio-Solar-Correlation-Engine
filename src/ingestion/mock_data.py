import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

def generate_synthetic_data(days=60):
    """
    Generates realistic synthetic data for the Bio-Solar Correlation Engine.
    Creates two CSVs: one for Solar weather data, one for Bio-wearable data.
    """
    
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)
    date_range = pd.date_range(start=start_date, end=end_date, freq='D')
    
    # --- 1. Generate Solar Data (Weather API simulation) ---
    solar_data = []
    
    # Season simulation: Let's pretend it's transitioning into Winter (SAD context)
    # Sunlight decreases over time
    for i, date in enumerate(date_range):
        # Base sunlight hours drops from 12 to 8 over 60 days
        base_sunlight = 12 - (i / days * 4) 
        
        # specific weather events
        is_cloudy = random.random() < 0.3 # 30% chance of cloudy day
        cloud_pct = random.uniform(60, 100) if is_cloudy else random.uniform(0, 30)
        
        # Real sunlight is affected by clouds
        actual_sunlight = base_sunlight * (1 - (cloud_pct / 100 * 0.7))
        
        uv_index = int((actual_sunlight / 12) * 10) # UV index correlated with clear sun
        
        solar_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "location": "New York, USA",
            "sunrise_time": "06:30", # Simplified
            "sunset_time": "18:00",  # Simplified
            "cloud_cover_pct": round(cloud_pct, 2),
            "uv_index": uv_index,
            "sunlight_hours": round(actual_sunlight, 2)
        })
        
    df_solar = pd.DataFrame(solar_data)
    df_solar.to_csv("data/raw/solar_history.csv", index=False)
    print(f"✅ Generated {len(df_solar)} days of Solar Data")

    # --- 2. Generate Bio Data (Wearable simulation) ---
    bio_data = []
    
    # User profile: Someone sensitive to weather
    current_mood = 8.0 # Starting happy
    
    for i, date in enumerate(date_range):
        solar_day = df_solar.iloc[i]
        
        # Logic: If yesterday was dark, mood drops today
        if i > 0:
            prev_sun = df_solar.iloc[i-1]["sunlight_hours"]
            if prev_sun < 5:
                current_mood -= random.uniform(0.5, 1.5) # Depressive slide
            elif prev_sun > 8:
                current_mood += random.uniform(0.1, 0.8) # Recovery
        
        # Clamp mood 1-10
        current_mood = max(1, min(10, current_mood))
        
        # Sleep correlates with mood (Lower mood = often worse sleep or oversleeping)
        # Let's say: Good mood = 7-8 hours. Bad mood = erratic (4h or 10h)
        if current_mood > 6:
            sleep_hours = random.uniform(6.5, 8.5)
        else:
            sleep_hours = random.choice([random.uniform(4, 5.5), random.uniform(9, 11)])
            
        # Steps
        steps = int(random.uniform(3000, 12000) * (current_mood / 10)) # Less active when sad
        
        bio_data.append({
            "date": date.strftime("%Y-%m-%d"),
            "user_id": "usr_001",
            "sleep_hours": round(sleep_hours, 2),
            "step_count": steps,
            "mood_score": round(current_mood, 2), # Self-reported metric
            "energy_level": int(current_mood) # 1-10 scale
        })
        
    df_bio = pd.DataFrame(bio_data)
    df_bio.to_csv("data/raw/bio_history.csv", index=False)
    print(f"✅ Generated {len(df_bio)} days of Bio Data")

if __name__ == "__main__":
    generate_synthetic_data()
