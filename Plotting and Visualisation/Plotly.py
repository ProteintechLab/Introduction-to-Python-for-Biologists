import plotly.express as px

# Interactive scatter plot of protein expression across proteins and genotypes
fig = px.scatter(df, x="MouseID", y="DYRK1A_N", color="Genotype",  # Using DYRK1A_N for illustration
                 title="Interactive Protein Expression Plot")
fig.write_html("interactive_expression_plot.html")  # Save as HTML
fig.show()
