#########################################################################
#Title: PYTHON Project Scenario - Data Analysis
#Description: This program allows user to analyse.......
#Name: <Valentin>
#Group Name: <Coders>
#Class: <PN2004Y>
#Date: <16 July 2021>
#Version: <...>
#########################################################################

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################
#import pandas and matplotlib for data analysis
import pandas as pd
import matplotlib.pyplot as plt

#########################################################################
#IMPORT Pandas Library for Data Analysis
#########################################################################


#########################################################################
#CLASS Branch - Data Analysis
#load excel data (CSV format) to dataframe
#########################################################################
class DataAnalysis:
    def __init__(self):

        #load excel data (CSV format) to dataframe - 'df'
        dataframe = pd.read_csv('MonthlyVisitors.csv')
        #show specific country dataframe
        sortCountry(dataframe)


#########################################################################
#CLASS Branch: End of Code
#########################################################################


#########################################################################
#FUNCTION Branch - sortCountry
#parses data and displays sorted result(s)
#########################################################################
def sortCountry(df):

    #print number of rows in dataframe
    print("There are " + str(len(df)) + " data rows read. \n")

    #display dataframe (rows and columns)
    print("The following dataframe are read as follows: \n")
    print(df)

    #Replacing the Value of na to 0
    df = df.replace(to_replace=[" na ", "na"], value ="0")

    #display European countries
    Eur = df.columns[20] + df.columns[21] + df.columns[22] + df.columns[23] + df.columns[24] + df.columns[25] + df.columns[26] + df.columns[27] + df.columns[28] + df.columns[29] + df.columns[30]
    print("\nThese are the countries in Europe:" + Eur + ". The Europe region from 1997 to 2007 was selected as shown below.\n")
    
 #display a sorted dataframe based on Europe
    SortedEur = (df[[
        'Year', 'Month', ' United Kingdom ', ' Germany ', ' France ',
        ' Italy ', ' Netherlands ', ' Greece ', ' Belgium & Luxembourg ', ' Switzerland ',' Austria ', ' Scandinavia ', ' CIS & Eastern Europe '
    ]][228:360])

    print(SortedEur)

  #remove year & month from dataframe
    NewEur = SortedEur.drop(columns=["Year", "Month"])

  #convert the contents into int
    NewEur = NewEur.astype(str).astype(int)
  
  #Total visitors for each country
    TotalEur = NewEur.sum()

  #Sort in order
    NewSortedEur = TotalEur.sort_values(ascending = False)

  #back to object
    NewSortedEur = NewSortedEur.reset_index()

  #adding columns
    NewSortedEur.columns = ['Countries', 'Visitors']

   #display top 3 countries in europe
    print("\nThe top 3 countries in Europe that visited Singapore are ranked below.\n")
    Top3 = (NewSortedEur.head(3))
    print(Top3)

#Plotting Pie Chart
    visitorss = [4752232, 1735040, 945953]
    Countries = [' United Kingdom ',' Germany ',' Scandinavia ']
    plt.pie(visitorss, labels = Countries , autopct = '%1.1f%%')
    plt.title('Insert Title')
    plt.axis('equal')
    plt.legend(loc="lower right")
    plt.show()

    

    return


#########################################################################
#FUNCTION Branch: End of Code
#########################################################################

#########################################################################
#Main Branch
#########################################################################
if __name__ == '__main__':

    #Project Title
    print('######################################')
    print('# Data Analysis App - PYTHON Project #')
    print('######################################')

    #perform data analysis on specific excel (CSV) file
    DataAnalysis()

#########################################################################
#Main Branch: End of Code
#########################################################################
