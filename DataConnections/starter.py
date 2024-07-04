import streamlit as st
import pandas as pd
import requests

#Function to make a GET request

@st.cache_data(show_spinner="Searching ...")
def search_gutenberg(author, title):
    #Define your base url
    BASE_URL = "https://gutendex.com/books/?search="
    
    #Replace whitespace with 20% as per the documentation
    #For the search parameters
    author = author.replace(" ", "%20")
    title = title.replace(" ", "%20")
    
    #Make a url from the search parameters
    params_url = f"{author}%20{title}"
    
    #Make the final search url
    search_url = f"{BASE_URL}{params_url}"
    
    try:
        #Make a get request
        res = requests.get(search_url)
        
        #Get the JSON response
        json_res = res.json()
        
        # If your JSON has no results, return False
        # Else, return the JSON response
        if json_res['count'] == 0:
            return False
        else:
            return json_res  
        
    except:
        return False
    

#Function to format the JSON response as a DataFrame
@st.cache_data
def format_json_res(json_res):
    cols = ['Id', 'Author', 'Title', 'Language', 'Link']
    
    rows = []
    
    try:
        #For loop to access all data in the response
        for result in json_res["results"]:

            id = result["id"]
            author = result["authors"][0]["name"]
            title = result["title"]
            language = result["languages"][0]
            link = f"https://www.gutenberg.org/ebooks/{id}"

            rows.append([id, author, title, language, link])

        df = pd.DataFrame(rows, columns=cols)

        return df
    except:
        st.error("Error while parsing data")


if __name__ == "__main__":
    st.title("📚 Search Project Gutenberg")
    with st.form("search-form"):
        col1, col2 = st.columns(2)
        
        with col1:
            author = st.text_input("Author")
        with col2:
            title = st.text_input("Title")
        
        search = st.form_submit_button("Search", type="primary")
        
        if search:
            json_res = search_gutenberg(author, title)
            
            if json_res:
                df = format_json_res(json_res)
                st.subheader("Results")
                st.table(df)
            else:
                st.error("No results found")
    
        
    
    

