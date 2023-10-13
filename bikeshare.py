import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#define a list of months to use for input and and getting the number of the month
months = ['january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please enter a city name, chicago, new york city or washington: ')
    city = city.lower()
    
    while city not in CITY_DATA:
        city = input('Please enter a valid city name i.e chicago, new york city or washington: ')
        city = city.lower()
   
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Enter a month from january to june or all: ') 
    month = month.lower() 
    while True:
        if month in months or month == 'all':
            break
       
        else:
            month = input('Please enter a valid month (i.e january, february, march..june or all): ')
            month = month.lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Enter a day ( e.g sunday, monday, tuesday... saturday): ')
    day = day.title()
    
    while True:  
        if day == 'All' or day in ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
            break  # Exit the loop if a valid day or 'all' is entered.
        else:
            day = input('Please enter a valid day of the week( e.g sunday, monday, tuesday... saturday): ')
            day = day.title()
                                                  
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # uses the index of the months list to get the corresponding int  
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    elif month == 'all':
        pass

        
    # filter by day of week if applicable
    if day.lower() != 'all':
        # filter by day of week to create the new dataframe 
        df = df[df['day_of_week'] == day.title()]
          
         
    elif day.lower() == 'all':
        pass #explore the data for all days
        
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    
    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print('The most common month is: {}'.format(common_month))
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of week is: {}'.format(common_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_start_hour = df['hour'].mode()[0]
    print('The most common hour is: {}'.format(common_start_hour))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()
    print('The most commonly used Start Station is: {}'.format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()
    print('The most commonly used End Station is: {}'.format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station is: {}'.format(common_trip))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total time of travel is: {}'.format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is: {}'.format(mean_travel_time))
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df:
        user_types_count = df['User Type'].value_counts()
        print('Counts of user types: {}'.format(user_types_count))
    else:
        print('User Type data is not available in {}.'.format(city).tiltle())
        
    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Counts of gender types: {}'.format(gender_count))
    else:
        print('Gender data is not available in {}.'.format(city).title())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_yr_of_birth = df['Birth Year'].min()
        print('The earliest year of birth is: {}'.format(earliest_yr_of_birth))
           
        most_recent_yr_of_birth = df['Birth Year'].max()
        print('The most recent year of birth is: {}'.format(most_recent_yr_of_birth))
    
        most_common_yr_of_birth = df['Birth Year'].mode()
        print('The most common year of birth is: {}'.format(most_common_yr_of_birth))
        
    else:
       print('Birth Years data is not available in {}.'.format(city.title()))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
     # Ask the user if they want to view any raw data first
        view_raw_data = input('Do you want to view some raw data first? yes/no: ')
        if view_raw_data.lower() == 'yes':
            num_rows = 5  
            row_index = 0  

            try:
                while True:
                    print(df.iloc[row_index:row_index + num_rows])
                    row_index += num_rows

                    view_again = input('Do you want to view more? yes/no: ')
                    if view_again.lower() != 'yes' or row_index >= len(df):
                        break

            except KeyboardInterrupt: 
                pass
                
        # Execute functions in this order
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
