import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/recommendations"

st.set_page_config(page_title="Recommendation Engine", layout="centered")

st.title("🛒 E-Commerce Recommendation Engine")
st.write("Enter user IDs to get personalized product recommendations.")

user_input = st.text_input("User IDs (comma separated)", placeholder="e.g. 10, 25, 42")
top_n = st.number_input("Number of recommendations per user", min_value=1, max_value=20, value=5)

if st.button("Get Recommendations"):
    if not user_input.strip():
        st.error("Please enter at least one user ID.")
    else:
        try:
            user_ids = [int(uid.strip()) for uid in user_input.split(",")]

            payload = {
                "user_ids": user_ids,
                "top_n": top_n
            }

            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                results = response.json()["results"]

                st.success("Recommendations fetched successfully!")

                for user_id, recs in results.items():
                    st.subheader(f"User {user_id}")
                    if recs:
                        st.write(recs)
                    else:
                        st.write("No recommendations found.")
            else:
                st.error(f"API Error: {response.text}")

        except ValueError:
            st.error("Please enter valid integers separated by commas.")
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")
