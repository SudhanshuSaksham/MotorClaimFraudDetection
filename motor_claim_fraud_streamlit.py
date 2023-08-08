import streamlit as st
import json
from single_record_prediction import predict_single_json_record
import pandas as pd
import plotly.express as px


def plotly_barplot_for_causality(causality_dict):
    new_dic = causality_dict['fraud_reported_n'] | causality_dict["fraud_reported_y"]
    df = pd.DataFrame(list(new_dic.items()), columns=['features', 'shap_value'])
    df['fraud_reported'] = ['fraud_reported_y' if float(x) < 0 else 'fraud_reported_n' for x in df['shap_value']]
    df.sort_values(by='shap_value', ascending=False, inplace=True)
    fig = px.bar(df, y=df['features'], x=df['shap_value'], orientation='h', color=df['fraud_reported'],
                 labels=df['fraud_reported'])
    fig.update_layout(showlegend=True)
    return fig


def app():
    streamlit_dict = {}
    json_file = st.file_uploader('INPUT JSON FILE!!', type=["json"])

    fraud_file = None
    if json_file is not None:
        json_file.seek(0)
        fraud_file = json.load(json_file)

        st.json(fraud_file)

    if fraud_file:
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])

        with col1:
            policy_annual_premium = st.number_input("Annual Policy Premium", min_value=400.00, max_value=2500.00,
                                                    value=fraud_file['policy_annual_premium'], format="%.2f")
            streamlit_dict['policy_annual_premium'] = policy_annual_premium

            #############################################################################
            capital_loss = st.number_input("Capital Loss", min_value=-111100, max_value=0,
                                           value=fraud_file['capital-loss'])
            streamlit_dict['capital-loss'] = capital_loss

            #############################################################################
            bodily_injuries = st.number_input("Number of People Injured", min_value=0, max_value=3,
                                              value=fraud_file['bodily_injuries'])
            streamlit_dict["bodily_injuries"] = bodily_injuries

            #############################################################################
            vehicle_claim = st.number_input("Vehicle Claim", min_value=70, max_value=79560,
                                            value=fraud_file['vehicle_claim'])
            streamlit_dict["vehicle_claim"] = vehicle_claim

            #############################################################################
            occupation_values = ["adm-clerical", "armed-forces", "craft-repair",
                                 "exec-managerial", "farming-fishing",
                                 "handlers-cleaners", "machine-op-inspct",
                                 "other-service", "priv-house-serv",
                                 "prof-specialty",
                                 "protective-serv", "sales", "tech-support",
                                 "transport-moving"]
            insured_occupation = st.selectbox("Insured Occupation", occupation_values,
                                              index=occupation_values.index(fraud_file['insured_occupation']))
            streamlit_dict["insured_occupation"] = insured_occupation

            ##############################################################################
            collision_values = ["Front Collision", "Rear Collision", "Side Collision", "UNKNOWN"]
            collision_type = st.selectbox("Collision Type", collision_values,
                                          index=collision_values.index(fraud_file['collision_type']))
            streamlit_dict["collision_type"] = collision_type

            ##############################################################################
            property_damage_value = ["YES", "NO", "UNKNOWN"]
            property_damage = st.selectbox("Property Damage", property_damage_value,
                                           index=property_damage_value.index(fraud_file['property_damage']))
            streamlit_dict["property_damage"] = property_damage
            ##############################################################################
            age = st.number_input("Age", min_value=19, max_value=64, step=1, value=fraud_file['age'])
            streamlit_dict["age"] = age

        with col2:
            umbrella_limit = st.number_input("Umbrella Limit", min_value=0, max_value=10000000, step=1000000,
                                             value=fraud_file['umbrella_limit'])
            streamlit_dict["umbrella_limit"] = umbrella_limit
            ##############################################################################

            incident_severity_values = ['Trivial Damage', 'Minor Damage', 'Major Damage', 'Total Loss']
            incident_severity = st.selectbox("Incident Severity", incident_severity_values,
                                             index=incident_severity_values.index(fraud_file['incident_severity']))
            streamlit_dict["incident_severity"] = incident_severity

            ##############################################################################

            witnesses = st.number_input("Witnesses", min_value=0, max_value=3, value=fraud_file['witnesses'])
            streamlit_dict["witnesses"] = witnesses
            ##############################################################################

            auto_make_values = ["Accura", "Audi", "BMW", "Chevrolet", "Dodge", "Ford", "Honda", "Jeep",
                                "Mercedes", "Nissan", "Saab", "Suburu", "Toyota", "Volkswagen"]
            auto_make = st.selectbox("Automobile Model", auto_make_values,
                                     index=auto_make_values.index(fraud_file['auto_make']))
            streamlit_dict["auto_make"] = auto_make
            ###############################################################################
            insured_hobbies_values = ["base-jumping", "basketball", "board-games",
                                      "bungie-jumping", "camping", "chess", "cross-fit",
                                      "dancing", "exercise", "golf", "hiking", "kayaking",
                                      "movies", "paintball", "polo", "reading", "skydiving",
                                      "sleeping", "video-games", "yachting"]

            insured_hobbies = st.selectbox("Insured Hobbies", insured_hobbies_values,
                                           index=insured_hobbies_values.index(fraud_file['insured_hobbies']))
            streamlit_dict["insured_hobbies"] = insured_hobbies
            ##############################################################################

            authorities_contacted_values = ["Ambulance", "Fire", "None", "Other", "Police"]
            authorities_contacted = st.selectbox("Authorities Contacted", authorities_contacted_values,
                                                 index=authorities_contacted_values.index(
                                                     fraud_file['authorities_contacted']))
            streamlit_dict["authorities_contacted"] = authorities_contacted
            ##############################################################################

            police_report_available_values = ["YES", "NO", "UNKNOWN"]
            police_report_available = st.selectbox("Police Report Available", police_report_available_values,
                                                   index=police_report_available_values.index(
                                                       fraud_file['police_report_available']))
            streamlit_dict["police_report_available"] = police_report_available
            ##############################################################################
            policy_deductable_values = ["500", "1000", "2000"]
            policy_deductable = st.selectbox("Policy Deductable", policy_deductable_values,
                                             index=policy_deductable_values.index(fraud_file['policy_deductable']))
            streamlit_dict["policy_deductable"] = policy_deductable

        with col3:
            insured_education_level_values = ["High School", "College", "Associate", "JD", "MD", "Masters", "PhD"]
            insured_education_level = st.selectbox("Education level", insured_education_level_values,
                                                   index=insured_education_level_values.index(
                                                       fraud_file['insured_education_level']))
            streamlit_dict["insured_education_level"] = insured_education_level

            incident_hour_of_the_day = st.number_input("Hour of the day", min_value=0, max_value=24, step=1,
                                                       value=fraud_file['incident_hour_of_the_day'])
            streamlit_dict["incident_hour_of_the_day"] = incident_hour_of_the_day

            injury_claim = st.number_input("Injury Claim", min_value=0, max_value=21450, step=1,
                                           value=fraud_file['injury_claim'])
            streamlit_dict["injury_claim"] = injury_claim

            policy_state_values = ["IL", "IN", "OH"]
            policy_state = st.selectbox("Policy State", policy_state_values,
                                        index=policy_state_values.index(fraud_file['policy_state']))
            streamlit_dict["policy_state"] = policy_state

            insured_relationship_values = ["husband", "not-in-family", "other-relative",
                                           "own-child", "unmarried", "wife"]
            insured_relationship = st.selectbox("Insured Relationship", insured_relationship_values,
                                                index=insured_relationship_values.index(
                                                    fraud_file['insured_relationship']))
            streamlit_dict["insured_relationship"] = insured_relationship

            incident_city_values = ["Arlington", "Columbus", "Hillsdale",
                                    "Northbend", "Northbrook", "Riverwood", "Springfield"]
            incident_city = st.selectbox("Incident City", incident_city_values,
                                         index=incident_city_values.index(fraud_file['incident_city']))
            streamlit_dict["incident_city"] = incident_city

            auto_year_values = ["1995", "1996", "1997", "1998", "1999", "2000", "2001",
                                "2002", "2003", "2004", "2005", "2006", "2007", "2008",
                                "2009", "2010", "2011", "2012", "2013", "2014", "2015"]
            auto_year = st.selectbox("Auto Make Year", auto_year_values,
                                     index=auto_year_values.index(fraud_file['auto_year']))
            streamlit_dict["auto_year"] = auto_year

        with col4:
            capital_gains = st.number_input("Capital Gains", min_value=0, max_value=105000,
                                            value=fraud_file['capital-gains'])
            streamlit_dict["capital-gains"] = capital_gains

            number_of_vehicles_involved = st.number_input("Number of Vehicles", min_value=1, max_value=4,
                                                          value=fraud_file['number_of_vehicles_involved'])
            streamlit_dict["number_of_vehicles_involved"] = number_of_vehicles_involved

            property_claim = st.number_input("Property Claim", min_value=0, max_value=23670, step=1,
                                             value=fraud_file['property_claim'])
            streamlit_dict["property_claim"] = property_claim

            policy_csl_values = ["100/300", "250/500", "500/1000"]
            policy_csl = st.selectbox("Policy CSL", policy_csl_values,
                                      index=policy_csl_values.index(fraud_file['policy_csl']))
            streamlit_dict["policy_csl"] = policy_csl

            incident_type_values = ["Multi-vehicle Collision", "Parked Car", "Single Vehicle Collision",
                                    "Vehicle Theft"]
            incident_type = st.selectbox("Incident Type", incident_type_values,
                                         index=incident_type_values.index(fraud_file['incident_type']))
            streamlit_dict["incident_type"] = incident_type

            incident_state_values = ["NC", "NY", "OH", "PA", "SC", "VA", "WV"]
            incident_state = st.selectbox("Incident State", incident_state_values,
                                          index=incident_state_values.index(fraud_file['incident_state']))
            streamlit_dict["incident_state"] = incident_state

            months_as_customer = st.number_input("Months As Customer", min_value=0, max_value=479, step=1,
                                                 value=fraud_file['months_as_customer'])
            streamlit_dict["months_as_customer"] = months_as_customer

        predict_button = st.sidebar.button(label="PREDICT")

        print(streamlit_dict == fraud_file)
        if predict_button:
            response = predict_single_json_record(fraud_file)  # response = predict_single_json_record(streamlit_dict)
            st.text_area(label="Fraud Score", value=response['fraudScore'], height=10)
            st.text_area(label="Fraud Status", value=response['fraudStatus'], height=10)
            st.json(response['causality'])

            fig = plotly_barplot_for_causality(response['causality'])
            st.write(fig)

            fraud_explanation_response = list(">\t" + i for i in response['explanation']['fraud_explanation'])
            fraud_explanation_response = "\n".join(fraud_explanation_response)
            st.text_area(label="Fraud Explanation", value=fraud_explanation_response, height=175,
                         key="Fraud Explanation")

            non_fraud_explanation_response = list(">\t" + i for i in response['explanation']['non_fraud_explanation'])
            non_fraud_explanation_response = "\n".join(non_fraud_explanation_response)
            st.text_area(label="Non Fraud Explanation", value=non_fraud_explanation_response,
                         height=150)


if __name__ == '__main__':
    app()
