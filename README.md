# Investigate-Hotel-Business-using-Data-Visualization
Mini project about Investigate Hotel Business using Data Visualization <br>
<br>

## Investigate Business Hotel Using Data Visualization : Project Overview <br>
<br>
### -	It is very important for a company to always analysis their business performance. In this project, we focusing business performance in Hospitality sector. Our focus is to find about customers behave when placing an order hotel and its relationship to the rate of cancellation of hotel bookings. Results and insights that we find, we will present it in the form of visualization data to make it easier to understand and more persuasive.<br>
### -	The process using python program.<br>
### - In this dataset, there are two hotels. We compare each other.<br>
<br>

## The Process<br>
### 1.	Input data.<br>
### 2.	Check duplicate data on this dataset and found as may as 3324 data. Then, drop duplicate.<br>
### 3.	Take a look for blank data in this dataset. As the result, found four columns, namely children, city, agent, and company. So that the empty data is filled with the number 0 for children, agent, and company columns. Whereas for city, filled is unknown.<br>
### 4.	Change data type for children, agent, and company column from float to integer.<br>
### 5.	Change undefined to no meal from meal column because there is same meaning.<br>
### 6.	Searching for data that have zero guest and zero night.<br>
### 7.	Drop the data that not having guest and night.<br>
### Form that step, the result of data use is 85378 data.<br>
<br>

## The Results<br>
### -	Monthly Hotel Booking Analysis Based on Hotel Type<br>
<br>

![ALT]https://github.com/inggridpris/Investigate-Hotel-Business-using-Data-Visualization/blob/main/fig/average%20number.jpeg "Monthly hotel booking")

<br>
### From this picture, that we know there are two hotel, namely City Hotel and Resort Hotel. When it is in holiday season, both of them get more number of booking, but in November, both of this hotel have a more less booking. In September. City Hotel decreased. In other hand, Resort Hotel increase. Both of them, have a low booking in January until March.<br>

<br>
### -	Impact Analysis of stay Duration on Hotels Booking Cancellation Rates<br>
<br>
![ALT](https://github.com/inggridpris/Investigate-Hotel-Business-using-Data-Visualization/blob/main/fig/percent%20canceled.jpeg "Cancelled")
<br>
### In this picture above, can tell about the relationship of percentage cancelled with stay duration in two hotels. In the City Hotel, the longer you stay is the highest you got cancelled. In the other hand, Resort Hotel not so. For 5 days of stay, both hotel have the same percent cancelled. The trend of Resort Hotel tends to be flat while Trend City Hotel tends to rise.<br>
<br>

### -	Impact Analysis of Lead Time on Hotel Bookings Cancellation Rate<br>
<br>
![ALT](https://github.com/inggridpris/Investigate-Hotel-Business-using-Data-Visualization/blob/main/fig/lead%20time.jpeg "Lead Time")
<br>
### In this graph, there are relationship lead time duration with percentage of cancelled in City hotel and Resort Hotel. With the first month, both of them have the lowest cancelled. In 11-12 months period, City Hotel have reach the highest percentage cancelled. It is different from Resort Hotel, Resort Hotel get the low percentage cancelled in the end of 12 months. City Hotel tends to rise until 12 months but then went down in the next periods. Resort Hotel have a volatile graph for the Lead Time Duration.<br>
<br>

## Summary <br>
<br>
### For monthly hotel booking, both of them have a nice tracking. Their have a increase booking at high peak season, but decrease if it is not in holiday season. Both of them, can make some improvement for month that is not in holiday season, so the impact not be a great. City hotel need to looking about their service for the customers, because more night, the customers do not appreciate about it. Resort Hotel need to know about the trends hotel these days, so they can keep up their reputation. In this condition, Resort City can get increase for customers bookings. The more lead time the more that hotel get cancelled. Almost 60% City Hotel get cancelled for lead time more than 11 months. Customers do not cancelled the booking of both hotel if their can get the booking not more than 30 days. <br>
<br>

#### For more detail, you can visit the link below:<br>
#### https://github.com/inggridpris/Investigate-Hotel-Business-using-Data-Visualization <br>
#### https://drive.google.com/file/d/1Ne0Pblvb3pTz1nGhX-MmootjCLD5odnd/view?usp=sharing <br>
<br>
#### or you can connect with me with linkedin <br>
#### https://www.linkedin.com/in/inggriani-priscilia-69779b179/ <br>
