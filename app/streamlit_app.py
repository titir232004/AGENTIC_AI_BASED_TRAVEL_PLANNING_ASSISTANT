import streamlit as st
import sys
import os
import re

# --------------------------------------------------
# Fix imports (so Streamlit can find agent module)
# --------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.travel_agent import run_travel_agent

# --------------------------------------------------
# Helper: extract days from query
# --------------------------------------------------
def extract_days(query: str) -> int:
    """
    Extract number of days from user query.
    Defaults to 3 if not found.
    """
    match = re.search(r"(\d+)\s*(day|days)", query.lower())
    if match:
        return int(match.group(1))
    return 3

# --------------------------------------------------
# UI Header
# --------------------------------------------------
st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 Agentic AI Travel Planner")
st.divider()

# --------------------------------------------------
# User input
# --------------------------------------------------
user_query = st.text_input(
    "✍️ Describe your trip",
    placeholder="Plan a 5 day trip from Hyderabad to Goa under 15000"
)

# --------------------------------------------------
# Run agent
# --------------------------------------------------
if st.button("🚀 Plan My Trip"):
    if not user_query.strip():
        st.warning("Please describe your trip.")
    else:
        days = extract_days(user_query)
        nights = max(days - 1, 1)

        with st.spinner("🧠 Thinking like a travel expert..."):
            result = run_travel_agent(user_query, nights=nights)

        # ------------------------
        # Check for errors
        # ------------------------
        if isinstance(result, str):
            st.error(result)
        else:
            st.success("✅ Trip Planned Successfully!")
            st.divider()

            # --------------------------------------------------
            # Trip Summary
            # --------------------------------------------------
            st.subheader("📍 Trip Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("From", result["source"])
            col2.metric("To", result["destination"])
            col3.metric("Duration", f"{result['days']} Days / {result['nights']} Nights")

            # --------------------------------------------------
            # Flight Details
            # --------------------------------------------------
            st.subheader("✈️ Flight Details")
            flight = result["flight"]
            st.markdown(
                f"""
                **✈️ {flight['airline']}**  
                🛫 **{flight['from']} → {flight['to']}**  
                ⏰ {flight['departure_time']} → {flight['arrival_time']}  
                💸 **₹{flight['price']}**
                """
            )

            # --------------------------------------------------
            # Hotel Recommendation
            # --------------------------------------------------
            st.subheader("🏨 Hotel Recommendation")
            hotel = result["hotel"]
            st.markdown(
                f"""
                **🏨 {hotel['hotel_name']}**  
                ⭐ Rating: {hotel['rating']} / 5  
                💰 ₹{hotel['price_per_night']} per night  
                🛏️ {result['nights']} Nights → **₹{hotel['price_per_night'] * result['nights']}**
                """
            )

            # --------------------------------------------------
            # Places to Visit
            # --------------------------------------------------
            st.subheader("📍 Places to Visit")
            for p in result["places"]:
                st.markdown(
                    f"""
                    • **{p['name']}**  
                      🏷️ {p['type'].title()} | ⭐ {p['rating']}
                    """
                )

            # --------------------------------------------------
            # Weather
            # --------------------------------------------------
            st.subheader("🌦️ Weather Forecast")
            weather = result["weather"]
            cols = st.columns(len(weather))
            for i, (day, temp) in enumerate(weather.items()):
                cols[i].metric(day.replace("_", " ").title(), temp)

            # --------------------------------------------------
            # Budget Breakdown
            # --------------------------------------------------
            st.subheader("💰 Estimated Budget")
            budget = result["budget"]
            col1, col2, col3 = st.columns(3)
            col1.metric("✈️ Flight", f"₹{budget['flight']}")
            col2.metric("🏨 Hotel", f"₹{budget['hotel']}")
            col3.metric("🍽️ Food & Local", f"₹{budget['food_and_local']}")
            st.success(f"💸 **Total Trip Cost: ₹{budget['total_cost']}**")
