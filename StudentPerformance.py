import pandas as pd
import statistics
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
df = pd.read_csv('StudentsPerformance.csv')
readingList = df['reading score'].tolist()

mean = statistics.mean(readingList)
mode = statistics.mode(readingList)
median = statistics.median(readingList)
standardDeviation = statistics.stdev(readingList)

print (mean, mode, median, standardDeviation)

readingListfsds, readingListfsde = mean - standardDeviation, mean + standardDeviation
readingListssds, readingListssde = mean - (2*standardDeviation), mean + (2*standardDeviation)
readingListtsds, readingListtsde = mean - (3*standardDeviation), mean + (3*standardDeviation)
fig = ff.create_distplot([readingList], ['readingscores'], show_hist = False)
fig.add_trace(go.Scatter(x = [mean, mean], y = [0,0.17], mode = 'lines', name = 'mean'))
fig.add_trace(go.Scatter(x = [readingListfsds, readingListfsds], y = [0,0.17], mode = 'lines', name = 'standardDeviation1'))
fig.add_trace(go.Scatter(x = [readingListfsde, readingListfsde], y = [0,0.17], mode = 'lines', name = 'standardDeviation1'))
fig.add_trace(go.Scatter(x = [readingListssds, readingListssds], y = [0,0.17], mode = 'lines', name = 'standardDeviation2'))
fig.add_trace(go.Scatter(x = [readingListssde, readingListssde], y = [0,0.17], mode = 'lines', name = 'standardDeviation2'))
fig.add_trace(go.Scatter(x = [readingListtsds, readingListtsds], y = [0,0.17], mode = 'lines', name = 'standardDeviation3'))
fig.add_trace(go.Scatter(x = [readingListtsde, readingListtsde], y = [0,0.17], mode = 'lines', name = 'standardDeviation3'))

readingList_of_data_within_fsd = [result for result in readingList if result > readingListfsds and result < readingListfsde]
readingList_of_data_within_ssd = [result for result in readingList if result > readingListssds and result < readingListssde]
readingList_of_data_within_tsd = [result for result in readingList if result > readingListtsds and result < readingListtsde]

print ('{}% of data for reading lies within 1standardDeviation'.format(len(readingList_of_data_within_fsd)*100/len(readingList)))
print ('{}% of data for reading lies within 2standardDeviation'.format(len(readingList_of_data_within_ssd)*100/len(readingList)))
print ('{}% of data for reading lies within 3standardDeviation'.format(len(readingList_of_data_within_tsd)*100/len(readingList)))
