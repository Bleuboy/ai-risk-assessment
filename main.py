import streamlit as st
import use_cases
import risks

def display_use_cases_selection():
    # Center the header with custom styling
    st.markdown("<h2 style='text-align: center;'>Step 1: Select Use Cases</h2>", unsafe_allow_html=True)
    
    # Create a centered container using columns
    _, col_center, _ = st.columns([1, 2, 1])
    
    with col_center:
        st.markdown("""
        <style>
        .use-case-container {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown("<div class='use-case-container'>", unsafe_allow_html=True)
        
        st.markdown("**Please select the use cases that apply to your application:**")
        
        selected_cases = []
        for i, use_case in enumerate(use_cases.USE_CASES):
            if st.checkbox(f"{use_case['title']}", key=f"use_case_{i}"):
                selected_cases.append(use_case)
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # Button to proceed
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            continue_button = st.button("Continue", use_container_width=True)
            
        if continue_button:
            if not selected_cases:
                st.error("Please select at least one use case to continue.")
            else:
                st.session_state.selected_use_cases = selected_cases
                st.session_state.page = "risk_assessment"
                # Initialize risk assessment data
                st.session_state.current_question_index = 0
                st.session_state.answers = {}
                
                # Get all unique risks from selected use cases
                unique_risks = set()
                for case in selected_cases:
                    for risk in case['risks']:
                        unique_risks.add(risk)
                
                # Create a list of risk objects that match the unique risk titles
                st.session_state.questions = []
                for risk in risks.all_risks:
                    if risk['title'] in unique_risks:
                        st.session_state.questions.append(risk)
                
                st.rerun()

def display_risk_assessment():
    st.subheader("Step 2: Risk Assessment")
    
    # Calculate progress
    total_questions = len(st.session_state.questions)
    current_index = st.session_state.current_question_index
    progress = current_index / total_questions if total_questions > 0 else 0
    
    # Display progress bar
    st.progress(progress)
    st.write(f"Question {current_index + 1} of {total_questions}")
    
    # Display current question
    if total_questions > 0 and current_index < total_questions:
        current_question = st.session_state.questions[current_index]
        st.markdown(f"### {current_question['title']}")
        st.write(current_question['question'])
        
        # Display radio buttons for options
        option_value = st.radio(
            "Select your answer:",
            options=range(5),
            format_func=lambda i: current_question['options'][i],
            key=f"question_{current_index}",
            index=st.session_state.answers.get(current_question['title'], 0)
        )
        
        # Store answer when user selects an option
        st.session_state.answers[current_question['title']] = option_value
        
        # Navigation buttons
        col1, col2, col3 = st.columns([1, 1, 1])
    
        with col1:
            if current_index > 0:
                if st.button("Previous"):
                    st.session_state.current_question_index -= 1
                    st.rerun()
            else:
                if st.button("Back to Use Cases"):
                    st.session_state.page = "use_cases"
                    st.rerun()
                
        with col2:
            if current_index < total_questions - 1:
                if st.button("Next"):
                    st.session_state.current_question_index += 1
                    st.rerun()
            else:
                if st.button("Finish Assessment"):
                    st.session_state.page = "results"
                    st.rerun()

def display_results():
    st.subheader("Results")
    
    # Calculate the weighted score
    if len(st.session_state.answers) > 0:
        weighted_score = 0
        max_weighted_score = 0
        
        # Calculate weighted scores
        for question_title, answer_value in st.session_state.answers.items():
            # Find the risk to get its weight
            for risk in risks.all_risks:
                if risk['title'] == question_title:
                    # Default weight to 1 if not specified
                    weight = risk.get('weight', 1) 
                    weighted_score += answer_value * weight
                    max_weighted_score += 4 * weight  # 4 is max score per question
                    break
        
        # Calculate percentage
        percentage = (weighted_score / max_weighted_score * 100) if max_weighted_score > 0 else 0
        
        # Create columns for layout
        col1, col2 = st.columns([3, 1])
        
        with col1:
            # Generate color based on percentage (red→yellow→green)
            if percentage < 40:
                color = f"rgba(255, {int(255 * percentage / 40)}, 0, 0.8)"  # Red to Yellow
            else:
                color = f"rgba({int(255 * (1 - (percentage - 40) / 60))}, 255, 0, 0.8)"  # Yellow to Green
            
            # Display score as a large number
            st.markdown(f"""
            <div style="text-align: center;">
                <h1 style="font-size: 48px; color: {color};">{percentage:.1f}%</h1>
                <p>Security Maturity Score</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Create custom progress bar with full-width gradient
            st.markdown(f"""
            <div style="margin: 20px 0;">
                <div style="
                    background-image: linear-gradient(to right, red, yellow, green);
                    border-radius: 10px;
                    height: 30px;
                    width: 100%;
                    position: relative;">
                    <!-- Score indicator -->
                    <div style="
                        position: absolute;
                        width: 4px;
                        height: 40px;
                        background-color: #333;
                        left: calc({percentage}% - 2px);
                        top: -5px;">
                    </div>
                    <!-- Score marker -->
                    <div style="
                        position: absolute;
                        width: 16px;
                        height: 16px;
                        background-color: white;
                        border: 3px solid #333;
                        border-radius: 50%;
                        left: calc({percentage}% - 8px);
                        top: 7px;">
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Risk level indicator
            if percentage < 25:
                risk_level = "Critical Risk"
                level_color = "red"
            elif percentage < 50:
                risk_level = "High Risk"
                level_color = "red"
            elif percentage < 75:
                risk_level = "Moderate Risk" 
                level_color = "orange"
            else:
                risk_level = "Low Risk"
                level_color = "darkgreen"
                
            st.markdown(f"""
            <div style="text-align: center; margin-top: 10px;">
                <h2 style="color: {level_color};">{risk_level}</h2>
                <p style="color: #666;">Based on your responses to {len(st.session_state.answers)} risk factors</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Show numeric details
            st.markdown("### Score Details")
            st.write(f"Weighted Score: {weighted_score:.1f}/{max_weighted_score:.1f}")
            st.write(f"Questions: {len(st.session_state.answers)}")
            # severity_level = "High" if percentage < 50 else "Medium" if percentage < 75 else "Low"
            # st.write(f"Overall Severity: {severity_level}")
        
        # Detailed breakdown by risk (expandable)
        with st.expander("Detailed Risk Analysis"):
            # Create list of risks with their scores for sorting
            risk_items = []
            for question_title, answer_value in st.session_state.answers.items():
                # Find the risk to get its weight
                for risk in risks.all_risks:
                    if risk['title'] == question_title:
                        weight = risk.get('weight', 1)
                        # Store tuple of (title, value, weight, risk object)
                        risk_items.append((question_title, answer_value, weight, risk))
                        break
            
            # Sort risks by score (ascending) then by weight (descending)
            # This puts the most critical risks (low score, high weight) first
            risk_items.sort(key=lambda x: (x[1], -x[2]))
            
            # Display sorted risks
            for question_title, answer_value, weight, risk in risk_items:
                # Assign risk level and color based on score
                if answer_value == 0:
                    risk_level = "Critical Security Gap"
                    risk_color = "#ff0000"  # Dark red
                elif answer_value == 1:
                    risk_level = "Significant Vulnerability"
                    risk_color = "#800000"  # Red
                elif answer_value == 2:
                    risk_level = "Moderate Risk Exposure"
                    risk_color = "#ffa500"  # Orange/yellow
                elif answer_value == 3:
                    risk_level = "Basic Compliance"
                    risk_color = "#90ee90"  # Light green
                else:  # answer_value == 4
                    risk_level = "Security Best Practice"
                    risk_color = "#008000"  # Green
                
                weighted_item_score = answer_value * weight
                max_weighted_item_score = 4 * weight
                
                # Risk header with level indicator
                st.markdown(f"#### {question_title}")
                st.markdown(f"""
                <div style="display: flex; align-items: center; margin-bottom: 10px;">
                    <div style="background-color: {risk_color}; color: white; padding: 3px 8px; border-radius: 4px; margin-right: 10px; font-weight: bold;">
                        {risk_level}
                    </div>
                    <div>
                        Score: {answer_value}/4 × Weight {weight} = {weighted_item_score}/{max_weighted_item_score}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                
                # Show appropriate advice based on score
                if answer_value < 3:
                    st.warning(f"Recommendation: {risk['advice']}")
                else:
                    st.success(f"Good practice: {risk.get('advice_good', 'Your implemented security measures in this area align with industry best practices.')}")
                
                st.divider()
    
    if st.button("Start Over"):
        st.session_state.page = "use_cases"
        st.session_state.selected_use_cases = []
        st.session_state.answers = {}
        st.rerun()

def main():
    st.set_page_config(page_title="Risk Assessment Quiz", layout="wide")
    
    # Initialize session state
    if "selected_use_cases" not in st.session_state:
        st.session_state.selected_use_cases = []
    
    if "page" not in st.session_state:
        st.session_state.page = "use_cases"
        
    if "answers" not in st.session_state:
        st.session_state.answers = {}
    
    if "current_question_index" not in st.session_state:
        st.session_state.current_question_index = 0
    
    if "questions" not in st.session_state:
        st.session_state.questions = []
    
    st.title("Risk Assessment Quiz")
    
    # Display the appropriate page based on the current state
    if st.session_state.page == "use_cases":
        display_use_cases_selection()
    elif st.session_state.page == "risk_assessment":
        display_risk_assessment()
    elif st.session_state.page == "results":
        display_results()

if __name__ == "__main__":
    main()