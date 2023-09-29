import streamlit as st

st.set_page_config(page_title="CIIED Resources Page", page_icon="CIIED_Logo.png")


st.title("ACM X CIIED Student Hackathon")
st.header("Welcome to the Student Hackathon Resource Sharing Platform!")


if st.button("Access Pitching Presentation Template"):
    st.markdown("[Download Pitching Presentation Template](insert_link_to_ppt_here)")


st.subheader("Hackathon Details")
st.markdown("This student hackathon is organized by ACM and CIIED Dubai. Here are some key details:")
st.markdown("- Date: 28th September")
st.markdown("- Time: From 3 PM")
st.markdown("- Duration: 2 mins pitch + 3 mins Q&A")
st.markdown("- Location: Auditorium")
st.markdown("- Registration Deadline: 27th September")
st.markdown("- For more information, visit the [CIIED Website](https://ciied.netlify.app/)")

# Embed the content from the provided website
st.subheader("Resource: How to Design a Better Pitch Deck")
st.sidebar.markdown("**How to Design a Better Pitch Deck**")

with st.sidebar.expander("How to Design a Better Pitch Deck", expanded=True):
    st.markdown("""
        A pitch deck is a brief presentation that gives potential investors or clients an overview of your business plan, products, services, and growth traction. It is typically used to raise funding or secure new partnerships.

        A well-designed pitch deck can be a powerful tool for conveying your vision and persuading others to invest in your business. Here are some tips on how to design a better pitch deck:

        * **Start with a strong hook.** Your first slide should grab the audience's attention and make them want to learn more. This could be a bold statement, a compelling story, or a provocative question.
        * **Keep it simple.** Your pitch deck should be easy to follow and understand. Use clear and concise language, and avoid using too much jargon.
        * **Focus on the key points.** Don't try to cram too much information into your pitch deck. Focus on the most important aspects of your business, such as the problem you are solving, your solution, and your target market.
        * **Use visuals.** Visuals can help to make your pitch deck more engaging and easier to understand. Use charts, graphs, and images to illustrate your key points.
        * **Practice, practice, practice.** Before you deliver your pitch, practice it multiple times in front of a mirror or with a friend. This will help you to deliver your presentation smoothly and confidently.
    """)

# Add rules for the hackathon
st.subheader("Hackathon Rules")
st.markdown("To ensure a fair and productive hackathon experience, please adhere to the following rules:")
st.markdown("1. Teams must consist of at least 2 and at most 4 members.")
st.markdown("2. All code and project work must be done during the hackathon.")
st.markdown("3. Respect intellectual property rights. Use only authorized tools, libraries, and data.")
st.markdown("4. Plagiarism will not be tolerated. All code and content must be original.")
st.markdown("5. Be respectful and supportive of your fellow participants.")
st.markdown("6. Presentations must adhere to the time limits: 2 minutes for the pitch, followed by 5 minutes for Q&A.")
st.markdown("7. The decision of the judges is final.")

# Add prizes and awards information
st.subheader("Prizes and Awards")
st.markdown("We have exciting prizes and awards for the winners:")
st.markdown("- 1st Place: 200 AED")
st.markdown("- 2nd Place: 150 AED")
st.markdown("- 3rd Place: 100 AED")
st.markdown("- Best Pitch: 50 AED")
st.markdown("- Best Prototype: 50 AED")
st.markdown("Winners will get an exclusive chance to access the BPDC Incubation centre!")

# Add participation criteria
st.subheader("Criteria for Participation")
st.markdown("This hackathon is open to all BPDC Students.")
st.markdown("Team size should be between 2 and 4 members.")
st.markdown("Participation is free of charge.")
st.markdown("No prior coding experience is necessary for participation.")
st.markdown("ACM and CIIED will issue certificates for all participants!")

# Add a timeline
st.subheader("Timeline")
st.markdown("(All times are in GST)")

# Create a timeline slider
timeline = {
    "27th September": {
        "7th Hour (1-2 PM)": "Introduction to the Hackathon (Room G34)",
        "2:00 PM": "Hackathon Themes Are Released (Online)",
    },
    "28th September": {
        "9:00 AM - 3:00 PM": "Registration and Brainstorming Session (Auditorium)",
        "9th Hour (3 - 4 PM)": "Pitching - Workshop (Auditorium)",
        "4:00 PM - 5:30 PM": "Brainstorming Session (Auditorium)",
        "5:30 PM - 6:00 PM": "Concluding Speeches (Auditorium)",
        "6:00 PM - 7:00 PM": "Pitching Round to Judges (Room G34)",
        "7:00 PM - 7:15 PM": "Buses leave for Day Scholars (Outside Minimart)",
    },
}

selected_date = st.selectbox("Select a Date", list(timeline.keys()))
selected_events = timeline[selected_date]

st.markdown(f"**{selected_date}**")
for time, event in selected_events.items():
    st.markdown(f"- **{time}**: {event}")

# Footer
st.markdown("For any questions or assistance, please contact us at ciie@dubai.bits-pilani.ac.in.")
st.markdown("Made with ❤️ by CIIED")