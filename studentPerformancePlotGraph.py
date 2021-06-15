import pandas as pd
import plotly.express as px

def scatterPlotGraph():
    df = pd.read_csv("studentLevelData.csv")
    calculatedMean = df.groupby(["Student-Id", "Level"], as_index = False)["Attempt"].mean()

    figure = px.scatter(calculatedMean, x = "Student-Id", y = "Level", size = "Attempt", color = "Attempt")
    figure.show()         

def main():
    print("Student Performance Scatter Plot Graph will be shown on Local Host !")
    scatterPlotGraph() 

if __name__ == "__main__":
    main()