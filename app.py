import streamlit as st

st.set_page_config(
    page_title="College Enquiry Chatbot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI-Based College Enquiry Chatbot")
st.write("Welcome to BVC Engineering College!")
st.write("Ask me about courses, fees, admissions, hostel and more.")

# Sample college information for project demonstration
college_data = {
    "name": "BVC Engineering College",
    "location": "Odalarevu, Andhra Pradesh, India",

    "courses": [
        "Computer Science and Engineering (CSE)",
        "Artificial Intelligence and Machine Learning (AIML)",
        "Electronics and Communication Engineering (ECE)",
        "Electrical and Electronics Engineering (EEE)",
        "Civil Engineering",
        "Mechanical Engineering"
    ],

    "admission": """
    1. Complete 10+2 with the required subjects.
    2. Apply through the applicable entrance exam and counselling process.
    3. Submit academic certificates and required documents.
    4. Complete admission formalities.
    Eligibility and admission rules depend on the course and admission category.
    """,

    "fees": """
    Tuition Fee: Rs. 75,000 per year
    Hostel Fee: Rs. 60,000 per year
    Bus Fee: Rs. 20,000 per year
    Other Charges: Rs. 5,000 per year
    These are DEMO VALUES for testing only, not verified college fees.
    """,

    "timings": """
    College Working Hours: 9:00 AM to 4:00 PM
    Lunch Break: 12:30 PM to 1:15 PM
    Working Days: Monday to Saturday
    These are sample timings for demonstration.
    """,

    "scholarships": """
    1. Government Post-Matric Scholarship
    2. Eligible state scholarship schemes
    3. Eligible fee reimbursement schemes
    Students must meet the applicable eligibility rules.
    """,

    "hostel": """
    Hostel Facilities:
    - Separate accommodation arrangements, subject to availability
    - Food and dining facilities
    - Common study areas
    - Basic accommodation facilities
    Hostel details shown here are sample information.
    """,

    "transport": """
    Transport Facilities:
    - College bus service
    - Routes covering selected nearby areas
    - Morning pickup and afternoon drop
    Sample transport information. Routes and fees need verification.
    """,

    "placements": """
    Placement Support:
    - Resume preparation
    - Aptitude and communication training
    - Technical interview practice
    - Campus recruitment opportunities
    Placement statistics and recruiter names must be verified.
    """,

    "contact": """
    College: BVC Engineering College
    Location: Odalarevu, Andhra Pradesh
    Phone: +91-9876543210 (DEMO NUMBER - NOT REAL)
    Email: admissions@example.com (DEMO EMAIL - NOT REAL)
    Office Hours: 9:00 AM to 4:00 PM (sample)
    """
}

# Question matching
question = st.text_input(
    "Ask your question:",
    placeholder="Example: What is the fee structure?"
)

if st.button("Get Answer"):
    q = question.lower().strip()

    if not q:
        st.warning("Please enter a question.")

    elif any(x in q for x in [
        "location", "address", "where is", "college name",
        "which college", "college situated"
    ]):
        st.subheader("🏫 College Name and Location")
        st.write("College Name:", college_data["name"])
        st.write("Location:", college_data["location"])

    elif any(x in q for x in [
        "course", "courses", "branch", "branches",
        "available course", "which course", "what course"
    ]):
        st.subheader("📚 Available Courses and Branches")
        for course in college_data["courses"]:
            st.write("•", course)

    elif any(x in q for x in [
        "admission", "admissions", "eligibility", "documents"
    ]):
        st.subheader("📝 Admission Procedure")
        st.write(college_data["admission"])

    elif any(x in q for x in [
        "fee", "fees", "tuition", "cost", "how much"
    ]):
        st.subheader("💰 Fee Structure")
        st.write(college_data["fees"])

    elif any(x in q for x in [
        "timing", "timings", "working hours", "college time"
    ]):
        st.subheader("🕒 College Timings")
        st.write(college_data["timings"])

    elif any(x in q for x in [
        "scholarship", "scholarships", "fee reimbursement"
    ]):
        st.subheader("🎓 Scholarship Details")
        st.write(college_data["scholarships"])

    elif any(x in q for x in [
        "hostel", "accommodation", "room", "food facility"
    ]):
        st.subheader("🏠 Hostel Facilities")
        st.write(college_data["hostel"])

    elif any(x in q for x in [
        "transport", "transportation", "bus", "bus route"
    ]):
        st.subheader("🚌 Transport Facilities")
        st.write(college_data["transport"])

    elif any(x in q for x in [
        "placement", "placements", "recruiter",
        "job opportunity", "companies"
    ]):
        st.subheader("💼 Placement Information")
        st.write(college_data["placements"])

    elif any(x in q for x in [
        "contact", "phone", "mobile", "email",
        "telephone", "office number"
    ]):
        st.subheader("☎️ College Office Contact Details")
        st.write(college_data["contact"])

    else:
        st.info(
            "Sorry, I could not understand your question. "
            "Please ask about college location, courses, "
            "admissions, fees, timings, scholarships, hostel, "
            "transport, placements or contact details."
        )

st.divider()
st.caption("College Enquiry Chatbot | Project Demonstration")