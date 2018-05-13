"""" This program will print three form letters asking for votes in the upcoming election"""
firstletter= ('Hildegard','Hilary Clinton','Hilary Clinton','Brunhilda')
secondletter=('Cheech','Donald Trump','Donald Trump','Chong')
thirdletter=('Moe','Bernie Sanders','Bernie Sanders','Jack')
letter="Dear, %s \n I would like to vote for %s \n because I think %s is best for \n this country. \n Sincerely, \n %s"
tupleList =[firstletter,secondletter,thirdletter]
for x in tupleList:
    print(letter % x)

"""Dear, Hildegard
 I would like to vote for Hilary Clinton
 because I think Hilary Clinton is best for
 this country.
 Sincerely,
 Brunhilda
Dear, Cheech
 I would like to vote for Donald Trump
 because I think Donald Trump is best for
 this country.
 Sincerely,
 Chong
Dear, Moe
 I would like to vote for Bernie Sanders
 because I think Bernie Sanders is best for
 this country.
 Sincerely
Jack """

