import altair as alt
import numpy as np
import pandas as pd
import streamlit as st


from pii_process.api import PiiTextProcessor

# Create the object, defining the language to use and the policy
# Further customization is possible by providing a config
proc = PiiTextProcessor(lang="fr", default_policy="label")



def main():
	""" NLP Based App with Streamlit """

	# Title
	st.title("Anonyx")
	st.subheader("Anonymise les données personnelles dans vos documents et fichiers.")
	# st.markdown("""
    # 	#### Description
    # 	+ 
    # 	""")
	

	st.subheader("Anonymise  Text")

	message = st.text_area("Entrez du texte", placeholder="Tapez ici...")
	# if st.button("Analyze"):
		# nlp_result = text_analyzer(message)
		# st.json(nlp_result)

	if st.button("Analyzer"):
		# Process a text buffer and get the transformed buffer
		outbuf = proc(message)
		st.write(outbuf)
			
			# nlp_result = text_analyzer(message)
			# st.json(nlp_result)

	
    
if __name__ == '__main__':
	main()