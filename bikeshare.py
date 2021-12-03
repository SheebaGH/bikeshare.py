import time
import pandas as pd
import numpy as np
CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}
def check_input(input_str,input_type):
 while True:
     input_read=input(input_str)
     try: 
       if input_read.lower() in ['chicago','new york city','washington'] and input_type == 1:
            break
       elif input_read.lower() in ['january','february','march','april','may','june','all'] and input_type == 2:
            break
       elif input_read.lower() in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type == 3:
            break
       else:
         if input_type == 1:
            print("Please enter a valid city name")
         if input_type == 2:
            print("please enter a valid month")
         if input_type == 3:
            print("please enter a valid day")
     except ValueError:
         print("Sorry, your input is wrong")
 return input_read
 
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    city = check_input.lower()("Would you like to see the data for chicago, new york city or washington?",1)
    month = check_input.lower()("Which Month (all, january, ... june)?", 2)
    day = check_input.lower()("Which day? (all, monday, tuesday, ... sunday)", 3)
    print('-'*40)
    return city, month, day

raw = {'chicago': 'chicago.csv','new york city': 'new_york_city.csv','washington': 'washington.csv'}.lower()
def get_from_files(city, month, day):
    df = pd.read_csv(raw[city])
    
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    
     Args:
        (str) city - name of the city to analyze .lower()
	(str) month - name of the month to filter by, or "all" to apply no month filter .lower()
        (str) day - name of the day of week to filter by, or "all" to apply no day filter .lower()
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df
    
def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    most_common_month = df['month'].mode()[0]
    print('Most Popular Month:', most_common_month)
    
    most_common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:',  most_common_day_of_week)
    
    most_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_common_start_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print('Most Common Start Hour:',  most_common_start_hour)
    
def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
  
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_start_station)

    popular_end_station = df['End Station'].mode()[0]
    print('Most End Station:', popular_end_station)

    group_field=df.groupby(['Start Station','End Station'])
    popular_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', popular_combination_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df,city):
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        print('Gender Stats:')
        print(df['Gender'].value_counts())
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:',earliest_year)
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
