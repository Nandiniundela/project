# Bus_Details
## Stage-1 APIS using DRF           
## App Views---->(Function names)
### apis--> v1/views
###### 1.all_buses
###### 2.add_bus
###### 3.edit_bus
###### 4.put_bus
###### 5.delete_bus
###### 6.one_busdetails

## App serializer
### apis-->v1/serializer
### bus_serializer--->Class name
### Meta--->Class name

| Attributes    | Models Fields | 
| ------------- |:-------------:|
| model         | CharField     |
| fileds        | TextField     | 

## App Urls ---->Function name
### apis-->v1/urls


|   Route                  |   Views Name            |   
| ----------------------   |:-----------------------:|
| 'get_bus'                | views.all_buses         | 
| 'add_bus'                | views.add_bus           |  
| 'edit_bus'               | views.edit_bus          |    
| 'put_bus'                | views.put_bus           |  
| 'delete_bus'             | views.delete_bus        |  
| 'one_busdetail/<int:num>'| views.one_busdetail     | 

### Main Urls----> App path
|   Route             |   App Name                    |
| --------------------|:-----------------------------:|
| 'apis/v1/'          | include('apis.v1.urls')       |              




## Stage-2 Database(Models)
## App Models
### bus_details--->Class name

| Attributes         | Models Fields | Constraints    |
| -------------      |:-------------:|---------------:|
| bus_name           | CharField     | max_length=50  |
| bus_number         | IntegerField  |                |
| bus_rotues         | CharField     | max_length=50  |
| bus_start_timmings | DateTimeField | blank=True     |
| bus_end_timmings   | DateTimeField | blank=True     |
| bus_fare           | IntegerField  |                |





