import streamlit as st

st.title('About Us')

st.header("Project Scope")
st.write("""
This web-based assistant helps foreign nationals who have recently become Permanent Residents (PR) in Singapore
navigate the various administrative, financial, and legal changes that come with PR status.
It consolidates official information from multiple government agencies into a single,
searchable knowledge base, delivering personalised guidance using Retrieval-Augmented Generation (RAG).
""")

st.header("Objectives")
st.markdown("""
- **Consolidate dispersed official information** from ICA, IRAS, CPF, MOM, HDB, and MOH.
- **Provide personalised guidance** based on user inputs such as current employment pass, age, and employment sector.
- **Implement RAG-enabled Q&A** using a local vector store and OpenAI GPT for accurate, grounded answers.
- **Simplify complex government processes** into clear, actionable steps for new PRs.
""")

st.header("Data Sources")
st.markdown("""
The app uses static official documents including:
- **ICA**: PR obligations, Re-entry Permit renewal, NRIC registration.
- **IRAS**: Tax residency rules, relief eligibility, filing requirements.
- **CPF**: CPF contribution rates, phased contribution schemes for PRs.
- **MOM**: Work pass cancellation procedures post-PR.
- **HDB**: Housing eligibility and CPF grants for PRs.
- **MOH**: MediShield Life premiums and healthcare changes.
""")

st.header("Features")
st.markdown("""
1. **Hardcoded Login**: Secure access with a fixed username and password.
2. **Document Upload**: Static upload of government PDFs and text guides.
3. **RAG Q&A**: Users ask questions; the system retrieves relevant info and generates grounded answers.
4. **User Personalisation**: Onboarding form collects user profile data to tailor responses.
""")
