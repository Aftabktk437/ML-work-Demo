import streamlit as st
import joblib

# Load the trained Random Forest model
random_forest_model = joblib.load('random_forest_model.h5')

# Function to predict house price


def predict_price(size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage, driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log):
    input_features = [[size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage,
                       driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log]]
    predicted_price = random_forest_model.predict(input_features)
    return predicted_price[0]

# Streamlit UI


def main():
    st.title("House Price Prediction")
    st.write("Please enter the details of the house to predict its price.")

    # Input fields
    col1, col2 = st.columns(2)
    with col1:
        size = st.slider("Size (sqft)", min_value=0, max_value=10000, step=10)
        property_age = st.slider(
            "Property Age", min_value=0, max_value=100, step=1)
        bedrooms = st.number_input(
            "Bedrooms", min_value=0, max_value=10, step=1)
        bathrooms = st.number_input(
            "Bathrooms", min_value=0, max_value=10, step=1)
        livingrooms = st.number_input(
            "Living Rooms", min_value=0, max_value=10, step=1)
        kitchen = st.number_input(
            "Kitchens", min_value=0, max_value=10, step=1)
        garage = st.number_input("Garages", min_value=0, max_value=10, step=1)
    with col2:
        driver_room = st.number_input(
            "Driver Rooms", min_value=0, max_value=10, step=1)
        maid_room = st.number_input(
            "Maid Rooms", min_value=0, max_value=10, step=1)
        furnished = st.selectbox("Furnished", ["0", "1"])
        ac = st.selectbox("Air Conditioning", ["0", "1"])
        roof = st.selectbox("Roof", ["0", "1"])
        pool = st.selectbox("Pool", ["0", "1"])
        frontyard = st.selectbox("Frontyard", ["0", "1"])
        basement = st.selectbox("Basement", ["0", "1"])
        duplex = st.selectbox("Duplex", ["0", "1"])
        stairs = st.selectbox("Stairs", ["0", "1"])
        elevator = st.selectbox("Elevator", ["0", "1"])
        fireplace = st.selectbox("Fireplace", ["0", "1"])
        price_log = st.number_input("Price Log", min_value=0.0, step=0.01)

    if st.button("Predict", key="predict_button"):
        # Predict house price
        predicted_price = predict_price(size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage,
                                        driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log)
        st.success(
            f"The predicted price of the house is ${predicted_price:.2f}")


if __name__ == "__main__":
    main()


# # Load the trained Random Forest model
# random_forest_model = joblib.load('random_forest_model.h5')

# # Function to predict house price


# def predict_price(size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage, driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log):
#     input_features = [[size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage,
#                        driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log]]
#     predicted_price = random_forest_model.predict(input_features)
#     return predicted_price[0]

# # Streamlit UI


# def main():
#     st.title("House Price Prediction")
#     st.write("Please enter the details of the house to predict its price.")

#     # Input fields
#     col1, col2 = st.columns(2)
#     with col1:
#         size = st.slider("Size (sqft)", min_value=0, max_value=10000, step=10)
#         property_age = st.slider(
#             "Property Age", min_value=0, max_value=100, step=1)
#         bedrooms = st.number_input(
#             "Bedrooms", min_value=0, max_value=10, step=1)
#         bathrooms = st.number_input(
#             "Bathrooms", min_value=0, max_value=10, step=1)
#         livingrooms = st.number_input(
#             "Living Rooms", min_value=0, max_value=10, step=1)
#         kitchen = st.number_input(
#             "Kitchens", min_value=0, max_value=10, step=1)
#         garage = st.number_input("Garages", min_value=0, max_value=10, step=1)
#     with col2:
#         driver_room = st.number_input(
#             "Driver Rooms", min_value=0, max_value=10, step=1)
#         maid_room = st.number_input(
#             "Maid Rooms", min_value=0, max_value=10, step=1)
#         furnished = st.selectbox("Furnished", ["0", "1"])
#         ac = st.selectbox("Air Conditioning", ["0", "1"])
#         roof = st.selectbox("Roof", ["0", "1"])
#         pool = st.selectbox("Pool", ["0", "1"])
#         frontyard = st.selectbox("Frontyard", ["0", "1"])
#         basement = st.selectbox("Basement", ["0", "1"])
#         duplex = st.selectbox("Duplex", ["0", "1"])
#         stairs = st.selectbox("Stairs", ["0", "1"])
#         elevator = st.selectbox("Elevator", ["0", "1"])
#         fireplace = st.selectbox("Fireplace", ["0", "1"])
#         price_log = st.number_input("Price Log", min_value=0.0, step=0.01)

#     if st.button("Predict", key="predict_button"):
#         # Predict house price
#         predicted_price = predict_price(size, property_age, bedrooms, bathrooms, livingrooms, kitchen, garage,
#                                         driver_room, maid_room, furnished, ac, roof, pool, frontyard, basement, duplex, stairs, elevator, fireplace, price_log)
#         st.success(
#             f"The predicted price of the house is ${predicted_price:.2f}")

#     # Logout button
#     # Logout button
#     if st.button("Logout"):
#         st.session_state.pop("authenticated", None)
#         # Redirect to signup page
#         params = {"page": "signup"}
#         st.experimental_set_query_params(**params)

#     # if st.button("Logout"):
#     #     st.session_state.pop("authenticated", None)
#     #     st.write("Logged out successfully.")
