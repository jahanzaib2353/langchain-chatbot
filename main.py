import streamlit as st
import langchain_helper as lch

def main():
    st.title("Search a book")

    input_name = st.text_input("Enter the book name")

    if st.button("Search"):
        if input_name:
            book_description = lch.generate_book_desc(input_name)

            if book_description:
                st.subheader(f"Book Description for '{input_name}':")
                st.write(book_description)
            else:
                st.warning(f"No information found for '{input_name}'.")

if __name__ == "__main__":
    main()
