# Action plan for redoing the way we construct the time schedule table

- [Action plan for redoing the way we construct the time schedule table](#action-plan-for-redoing-the-way-we-construct-the-time-schedule-table)
  - [1](#1)
  - [2 - New data Strategy](#2---new-data-strategy)
  - [3 - Clean up](#3---clean-up)
  - [4](#4)
  - [5](#5)


## 1

Look at the similarities between the new query's return and how the original table looks. Was there anything amiss? 

Missing data, missing columns, new columns? What are the differences

## 2 - New data Strategy

If everything from 1 looks good. Then it's time to move onto the plan on how to procede:  
1. Extract all records from `dm_fact_Protal_Tog_Litra` where `KoereDoegn_BKEY` value starts from 60 days before and up to 90 days ahead the current day
2. Merge it with all relevant dimension tables and define the columns as we needthem on our side 
   - Some columns are not computed immediately (e.g. ``FirstExecutedHourInterval``).
     They will be computed at a later stage.
3. Copy the records from BI server over to our ``dsbapp0104`` in a service table (we truncate the table first) like ``DSB_Trains_TrainTimeSchedule-Temp``.
To do this, assuming we have defined a query to do the previous points:
    - Generate a temporary csv file path. Example:

    ```python
    temporary_file_path = pkg_resources.resource_filename(
        'TrainDemandPredictions',
        'data/temp/',    
        )
        
    random_id = helpers.random_id_generator(size=6)

    time_schedule_temp_filename = 'time_schedule_' + random_id + '.csv'
    time_schedule_temp_filepath = os.path.join(temporary_file_path, time_schedule_temp_filename)
    ```

    - Use the function ``get_dataset_from_db()`` (from datawarehouse.py) to store the results in the temporary ``csv`` file.We store the results in a csv file so that we can take advantage of the "pagination" that is defined in ``get_dataset_from_db()`` for that case.
    - Use the function ``store_csv()`` (from datawarehouse.py) to store the temporary csv   file in the desired table.
4. Create stored procedure that:
   - Complete service table with missing computed columns (``FirstExecutedHourInterval``)
   - Compares the records between ``DSB_Trains_TrainTimeSchedule`` and ``DSB_Trains_TrainTimeSchedule-Temp``, and insert/update/deletes records as necessary. Records that have not changed should not be modified.
  
## 3 - Clean up

Now that we have done all of the above, we run into the problem that we have to clean up a lot of tables becasue they become unused do to this new strategy

Currently we speculate that the following tables become unused:


## 4

## 5