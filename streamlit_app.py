import streamlit as st

# Define the title and description for your app
st.title("ACM X CIIED Student Hackathon")
st.header("Welcome to the Student Hackathon Resource Sharing Platform!")

# Create a button to access the PPT
if st.button("Access Pitching Presentation Template"):
    st.markdown("[Download Pitching Presentation Template](insert_link_to_ppt_here)")

# Provide information about the hackathon
st.subheader("Hackathon Details")
st.markdown("This student hackathon is organized by ACM and CIIED Dubai. Here are some key details:")
st.markdown("- Date: 28th September")
st.markdown("- Time: From 3PM")
st.markdown("- Duration: 2 mins pitch + 5 mins Q&A")
st.markdown("- Location: Auditorium")
st.markdown("- Registration Deadline: [Insert Deadline]")
st.markdown("- For more information, visit the [CIIED Website](insert_website_link_here)")

# Embed the content from the provided website
st.subheader("Resource: How to Design a Better Pitch Deck")
st.markdown("Here is a resource that can help you design a better pitch deck for the hackathon:")
st.markdown("[How to Design a Better Pitch Deck](https://www.ycombinator.com/library/4T-how-to-design-a-better-pitch-deck)")

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
st.markdown("- 1st Place: [Prize Details]")
st.markdown("- 2nd Place: [Prize Details]")
st.markdown("- 3rd Place: [Prize Details]")

# You can add more sections, resources, or information as needed

# Footer
st.markdown("For any questions or assistance, please contact us at [email@example.com].")

# Run the app
if __name__ == "__main__":
    st.run()
