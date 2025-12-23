import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from agent.travel_agent import run_travel_agent


st.set_page_config(
    page_title="Agentic AI Travel Planner",
    page_icon="🧭",
    layout="centered"
)

st.title("🧭 Agentic AI Travel Planner")
st.divider()

user_query = st.text_input(
    "✍️ Describe your trip",
    placeholder="Plan a 4 day trip from Bangalore to Goa under 20000"
)


if st.button("🚀 Plan My Trip"):
    if not user_query.strip():
        st.warning("Please describe your trip.")
    else:
        with st.spinner("Thinking like a travel expert..."):
            result = run_travel_agent(user_query)

        if "error" in result:
            st.error(result["error"])
        else:
            st.success("✅ Trip Planned Successfully!")
            st.divider()


            # SUMMARY
            st.subheader(" Trip Summary")
            col1, col2, col3 = st.columns(3)
            col1.metric("From", result["source"])
            col2.metric("To", result["destination"])
            col3.metric(
                "Duration",
                f"{result['days']} Days / {result['nights']} Nights"
            )

            # FLIGHT
            st.subheader("✈️ Flight Details")
            flight = result["flight"]
            st.markdown(
                f"""
                **{flight['airline']}**  
                🛫 {flight.get('from')} → {flight.get('to')}  
                ⏰ {flight.get('departure_time')} → {flight.get('arrival_time')}  
                💸 ₹{flight['price']}
                """
            )

            # HOTEL
            st.subheader("🏨 Hotel Recommendation")
            hotel = result["hotel"]
            st.markdown(
                f"""
                **{hotel['hotel_name']}**  
                ⭐ Rating: {hotel['rating']} / 5  
                💰 ₹{hotel['price_per_night']} per night  
                🛏️ {result['nights']} Nights → ₹{hotel['price_per_night'] * result['nights']}
                """
            )

            # PLACES
            st.subheader("📍 Places to Visit")
            for p in result["places"]:
                st.markdown(
                    f"""
                    • **{p['name']}**  
                      🏷️ {p['type'].title()} | ⭐ {p['rating']}
                    """
                )

            # WEATHER
            st.subheader("🌦️ Weather Forecast")
            weather = result["weather"]
            cols = st.columns(len(weather))
            for i, (day, temp) in enumerate(weather.items()):
                cols[i].metric(day.replace("_", " ").title(), temp)

            # BUDGET
            st.subheader("💰 Estimated Budget")
            budget = result["budget"]
            col1, col2, col3 = st.columns(3)
            col1.metric("✈️ Flight", f"₹{budget['flight']}")
            col2.metric("🏨 Hotel", f"₹{budget['hotel']}")
            col3.metric("🍽️ Food & Local", f"₹{budget['food_and_local']}")

            st.success(f"💸 **Total Trip Cost: ₹{budget['total_cost']}**")
