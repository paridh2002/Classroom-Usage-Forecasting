import pandas as pd
import numpy as np   # ✅ Add this line

def load_data():
    # Create fake daily data
    rng = pd.date_range(start="2025-01-01", periods=200, freq="D")

    usage = (50 + 10 * np.sin(rng.dayofyear / 20)) + np.random.normal(0, 5, len(rng))

    df = pd.DataFrame({
        "date": rng,
        "usage": usage
    })

    df.to_csv("classroom_usage.csv", index=False)
    return df
