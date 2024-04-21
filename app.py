import streamlit as st
from prime import is_prime

def main():
    st.title("Find Prime")
    number = st.number_input("Enter number: ", min_value=0)

    if st.button("Find"):
        prime = [x for x in range(1, number+1) if is_prime(x)]
        st.write(f'List prime:\n {prime}')
        st.balloons()
if __name__ == "__main__":
    main()

